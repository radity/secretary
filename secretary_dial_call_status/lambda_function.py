import logging

from twilio.twiml.voice_response import VoiceResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"EVENTS: {event}")

    response = VoiceResponse()
    status = event.get("DialCallStatus") or "completed"
    if status in ["busy", "no-answer"]:
        response.say(
            "Sorry, our team could not answer your call. Please stay on the line to leave a message.",
            voice="woman",
            language="en-US",
        )
        response.record(timeout=10, transcribe=True)
    return response.to_xml()
