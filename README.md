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

- `PHONE_NUMBER`
- `COMPANY_NAME`
