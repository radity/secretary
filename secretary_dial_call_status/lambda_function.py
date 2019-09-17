import logging
import os
from urllib.parse import unquote

import boto3
from twilio.twiml.voice_response import VoiceResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

AWS_REGION = os.environ["AWS_REGION"]
AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
SYSTEM_EMAIL_ADDRESS = os.environ["SYSTEM_EMAIL_ADDRESS"]
MANAGER_EMAIL_ADDRESSES = list(map(lambda email: email.strip(), os.environ["MANAGER_EMAIL_ADDRESSES"].split(",")))
CHARSET = "UTF-8"


class Email(object):
    def __init__(self, context_data):
        self.context_data = context_data

    def get_subject(self):
        caller = self.context_data.get("From") or "an unknown number"
        subject = f"You have a missed call from {unquote(caller)}"
        return subject

    def get_body(self):
        body = [
            "Here you can find all the details about the call:",
            "",
            *[f"{unquote(k)}: {unquote(v)}" for k, v in self.context_data.items()],
        ]
        return "\n".join(body)

    def send(self):
        subject = self.get_subject()
        body = self.get_body()
        client = boto3.client("ses")
        response = client.send_email(
            Source=SYSTEM_EMAIL_ADDRESS,
            Destination={"ToAddresses": MANAGER_EMAIL_ADDRESSES},
            Message={
                "Body": {
                    "Text": {"Charset": CHARSET, "Data": body},
                    "Html": {"Charset": CHARSET, "Data": body.replace("\n", "<br/>")},
                },
                "Subject": {"Charset": CHARSET, "Data": subject},
            },
        )
        return response


def lambda_handler(event, context):
    logger.info("EVENTS: %s", event)

    response = VoiceResponse()
    status = event.get("DialCallStatus") or "completed"
    if status in ["busy", "no-answer"]:
        response.say(
            "Sorry, our team could not answer your call. Please stay on the line to leave a message.",
            voice="woman",
            language="en-US",
        )
        response.record(timeout=10, transcribe=True, max_length=300)
        email = Email(context_data=event)
        email_response = email.send()

        logger.info("EMAIL RESPONSE: %s", email_response)

    return response.to_xml()
