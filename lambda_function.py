import boto3

SIMILARITY_THRESHOLD = 75.0
bucket='amazon-rekognitio'
sourceFile='test.jpg'
targetFile='target.jpg'
	
def lambda_handler(event, context):
	client = boto3.client('rekognition')
	SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
	TargetImage={'S3Object':{'Bucket':bucket,'Name':targetFile}}	

	response = client.search_faces_by_image(
		CollectionId='myphotos',
		Image={
                    'S3Object': {
                        'Bucket': 'amazon-rekognitio',
                        'Name': 'test.jpg',
                        'Version': 'null'
                        }
                     },
                MaxFaces=123,
                FaceMatchThreshold = SIMILARITY_THRESHOLD
                )
	return response
