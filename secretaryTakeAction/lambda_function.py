import urllib

print("Loading function")


def parse_query(query_str):
    query = {}
    for key_value in query_str.split("&"):
        key, *value = key_value.split("=")
        query[urllib.parse.unquote(key)] = urllib.parse.unquote("".join(value))
    return query


def lambda_handler(event, context):
    options = [
        "<Dial>+1-555-555-5555</Dial>",
        "<Dial><Conference>IVR Party</Conference></Dial>",
        "<Play>http://demo.rickyrobinett.com/jiggy.mp3</Play>",
    ]
    query = parse_query(event["reqbody"])
    digit = query["Digits"]
    selected_option = options[int(digit) - 1 if digit.isdigit() else 0]
    return selected_option
