import logging
import os

import boto

from twilio.twiml.voice_response import VoiceResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
AWS_EMAIL_ADDRESS = os.environ["AWS_EMAIL_ADDRESS"]
AWS_REGION_NAME = os.environ["AWS_REGION_NAME"]
AWS_SECRET_KEY = os.environ["AWS_SECRET_KEY"]
MANAGER_EMAIL_ADDRESSES = map(lambda email: email.strip(), os.environ["MANAGER_EMAIL_ADDRESSES"].split(","))


class Email(object):
    def __init__(self, context_data):
        self.context_data = context_data

    def get_subject(self):
        caller = self.context_data.get("From") or "an unknown number"
        subject = f"You have a missed call from {caller}"
        return subject

    def get_body(self):
        body = ["Here you can find all the details about the call:", "", *[f"{k}: {v}" for k, v in self.context_data]]
        return "\n".join(body)

    def send(self):
        connection = boto.ses.connect_to_region(
            AWS_REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY
        )
        response = connection.send_email(
            source=AWS_EMAIL_ADDRESS,
            subject=self.get_subject(),
            body=self.get_body(),
            to_addresses=MANAGER_EMAIL_ADDRESSES,
            format="text",
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
