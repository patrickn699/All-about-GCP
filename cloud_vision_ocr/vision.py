
from google.cloud import vision
import io

'''
you need to create a service account key in google cloud console
and download the json file to the same directory as this file
and create environment variable with the name of the json file
else you need to pass the key through code itself.

export GOOGLE_APPLICATION_CREDENTIALS="vision-key.json"

''' 

def detect_text(path):
    """Detects text in the file."""
   
    #client = vision.ImageAnnotatorClient.from_service_account_json('vision-key.json')
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    v = []


    for text in texts:
        print('\n"{}"'.format(text.description))
        v.append(text.description)

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    print(v)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



detect_text("h20.jpg")
