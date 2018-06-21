def lambda_handler(event, context):
    import json
    f = open('seiyu.json')
    data = json.load(f)
    f.close()
    if event["title"] == "houshin":
        ret = "hakyu houshin-engi"
        for i in data["houshin"]:
            print (i["character"])
            print("<a href='https://ja.wikipedia.org/wiki/" + i["voice"] + "'>")
            print(i["voice"])
            print("</a>¥n")
    else:
        ret = "other title¥n"
    return ret
