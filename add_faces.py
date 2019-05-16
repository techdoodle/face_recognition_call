import requests
import cloudinary
from cloudinary.uploader import upload
import cloudinary.api
import glob


cloudinary.config( 
  cloud_name = "pranaym", 
  api_key = "289535338647225", 
  api_secret = "ArY0_cUv32naHqRLWzq5wPbjHjM" 
)

photos = glob.glob('C:\\Users\\prana\\Desktop\\new_faces\\*')

for i in photos:
	response = upload(i, tags='test')

	url = "https://centralindia.api.cognitive.microsoft.com/face/v1.0/facelists/lsa/persistedFaces"

	querystring = {"userData": str(response['original_filename'])}
	print(querystring)
	payload = "{\"url\": \"" +str(response['url'])+"\"}"
	print(payload)
	headers = {
	    'Content-Type': "application/json",
	    'Ocp-Apim-Subscription-Key': "ceb167ef037f4135a7a55b9ef8c35f61"
	    }

	azureResponse = requests.request("POST", url, data=payload, headers=headers, params=querystring)

	print(azureResponse.text)