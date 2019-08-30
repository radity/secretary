import logging
import os

from twilio.twiml.voice_response import VoiceResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ENV = os.environ["ENV"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
COMPANY_NAME = os.environ["COMPANY_NAME"]


def lambda_handler(event, context):
    logger.info("EVENTS: %s", event)
    logger.info("ENVIRONMENT VARIABLES: %s", os.environ)

    response = VoiceResponse()
    response.say(
        f"Thanks for calling {COMPANY_NAME}. Please wait while I am connecting.", voice="woman", language="en-US"
    )
    response.dial(PHONE_NUMBER, action=f"/{ENV}/dial-call-status", timeout=11)
    return response.to_xml()
