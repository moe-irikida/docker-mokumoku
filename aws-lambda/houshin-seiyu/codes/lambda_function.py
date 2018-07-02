def lambda_handler(event, context):
	import json
	f = open('seiyu.json')
	data = json.load(f)
	f.close()

	if (event.get('title') is not None):
		if (event['title'] == 'houshin'):
			for chara in data["houshin"]:
				print("<a href='https://ja.wikipedia.org/wiki/" + chara["voice"] + "'>" + chara["character"] + "/" + chara["voice"] + "</a>")
			ret = "hakyu houshin-engi"
		else:
			ret = "other title"
	else:
		ret = 'non title'

	return ret
