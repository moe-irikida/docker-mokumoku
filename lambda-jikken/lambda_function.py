def lambda_handler(event, context):
    for i in event["houshin"]:
        print (i["character"])
        print("<a href='https://ja.wikipedia.org/wiki/" + i["voice"] + "'>")
        print(i["voice"])
        print("</a>¥n")
    return 0

def get_seiyu_json():
