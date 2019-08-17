import logging
import os

from twilio.twiml.voice_response import VoiceResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"EVENTS: {event}")
    logger.info(f"ENVIRONMENT VARIABLES: {os.environ}")

    phone_number = os.environ["PHONE_NUMBER"]
    company_name = os.environ["COMPANY_NAME"]

    response = VoiceResponse()
    response.say(
        f"Thanks for calling {company_name}. Please wait while I am connecting.", voice="woman", language="en-US"
    )
    response.dial(phone_number, action="/dev/dial-call-status", timeout=11)
    return response.to_xml()
