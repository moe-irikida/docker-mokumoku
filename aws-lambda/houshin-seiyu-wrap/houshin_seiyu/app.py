import json

def lambda_handler(event, context):

	f = open('./seiyu.json')
	jsondata = json.load(f)
	f.close()

	charas = ""

	if (event.get("queryStringParameters") is not None \
		and event["queryStringParameters"].get('title') is not None):
		title = event["queryStringParameters"]['title']

		if (title == 'houshin'):
			for chara in jsondata["houshin"]:
				chara['url'] = "https://ja.wikipedia.org/wiki/" + chara["voice"]
				charas.append(chara)

	else:
		title = 'non title'

	return {
        "statusCode": 200,
        "body": json.dumps({
            'title': title,
            'data': charas
        })
    }
