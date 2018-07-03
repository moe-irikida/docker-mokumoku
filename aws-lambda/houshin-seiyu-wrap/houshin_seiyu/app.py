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
			charas = jsondata["houshin"]
			for i, chara in enumerate(charas):
				voice_strip = chara["voice"].replace(" ", "").replace("　", "")
				charas[i]['url'] = "https://ja.wikipedia.org/wiki/" + voice_strip

	else:
		title = 'non title'

	return {
        "statusCode": 200,
        "body": json.dumps({
            'title': title,
            'data': charas
        }, ensure_ascii=False)
	}
