print("Loading function")


def lambda_handler(event, context):
    response_data = {
        "message": "Thanks for calling! Please select one of the following options",
        "options": ["Call Ricky", "Join the conference line", "Get jiggy with it"],
    }
    return response_data
