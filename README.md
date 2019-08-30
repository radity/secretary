**Secretary** is a Twilio app working over Amazon Lambda.

# Tech Stack

- AWS Lambda
- API Gateway
- Twilio

You may want to take a look at this document before starting to implement:
https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python-amazon-lambda

# Requirements

- virtualenv
- python3.7
- zip

# Development

Create a virtual environment folder named `venv-aws` and activate it. Then install the required packages:

```
pip install -r requirements.txt
```

# Deployment

In the project root folder:

```
./create_archives.sh
```

Then, you can upload this zip file using the AWS console. Or if you have aws command-line application, try this command, **secretary_dial** is a function name:

```
aws lambda update-function-code --function-name secretary_dial --zip-file fileb://function.zip
```

The last step in AWS-side is configuring API endpoint for the dial. After you configured the endpoint, you will use this URL in Twilio.

**Required environment variables:**

- **ENV:** `dial`, `dial_call_status`. To get API urls looking at the environment. It can be **prod** or **dev**, or what you decided in API Gateway.
- **PHONE_NUMBER:** `dial`. To redirect the caller if the contact doesn't answer the call.
- **COMPANY_NAME:** `dial`. Used in welcome message.
- **AWS_REGION_NAME:** `dial_call_status`. A region for amazon SES.
- **AWS_ACCESS_KEY:** `dial_call_status`. For using Amazon SES service.
- **AWS_SECRET_KEY:** `dial_call_status`.
- **AWS_EMAIL_ADDRESS:** `dial_call_status`. From email.
- **MANAGER_EMAIL_ADDRESSES:** `dial_call_status`. To email.
