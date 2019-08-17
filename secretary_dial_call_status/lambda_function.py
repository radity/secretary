from twilio.twiml.voice_response import VoiceResponse


def lambda_handler(event, context):
    print("Event")
    print("======")
    print(event)

    print("Context")
    print("=======")
    print(context)

    response = VoiceResponse()
    status = "completed"
    if status in ["busy", "no-answer"]:
        response.say(
            "Sorry, our team could not answer your call. Please stay on the line to leave a message."
        )
        response.record(timeout=10, transcribe=True)
    return response.to_xml()
