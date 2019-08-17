import os

from twilio.twiml.voice_response import VoiceResponse


def lambda_handler(event, context):
    phone_number = os.environ["PHONE_NUMBER"]
    company_name = os.environ["COMPANY_NAME"]

    response = VoiceResponse()
    response.say(
        f"Thanks for calling {company_name}. Please wait while I am connecting.", voice="woman", language="en-US"
    )
    response.dial(phone_number, action="/dev/dial-call-status", timeout=11)
    return response.to_xml()
