import json

# むずかしい！もっといい書き方あるでよ

def lambda_handler(event, context):


	import boto3
	import os.path

	BUCKET_NAME = "music-moemoe"

	s3 = boto3.resource('s3')
	bucket = s3.Buket(BUCKET_NAME)
	objects = bucet.objects.all()
	files = []

	for(object in objects):
		files.append(object.name)

	for (file in files):
		name, ext = os.path.splitext(file.name)
		if (is_image(ext)):
			music_file = name + '.mp3'
			if(music_file in files):
				id = get_rearrange_id()
				rearrange(music_file, id)
				db_push(id)


	return {
		"statusCode": 200,
		"body": json.dumps({
			'message': 'hello world',
			'location': ip.text.replace('\n', ''),
		})
	}
def get_rearrange_id():
	return '100'
def rearrange(music_filename, id)
def db_push(id):
	return true

def is_image(ext):
	if(ext == 'png'¥
	|| ext == 'jpg'¥
	|| ext == 'gif'):
		return true
	return false
