
from django.conf import settings
from requests import request

class PinataAPI():
    PINATA_API_KEY = settings.PINATA_API_KEY
    PINATA_API_SECRET = settings.PINATA_API_SECRET
    PINATA_JWT = settings.PINATA_JWT

    def authenticate(self):

        url = "https://api.pinata.cloud/data/testAuthentication"
        payload={}
        headers = { 'Authorization': f'Bearer {self.PINATA_JWT}' }
        response = request("GET", url, headers=headers, data=payload)
        return response.status_code == 200
    
    def upload_file(self, file):
        url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

        payload={'pinataOptions': '{"cidVersion": 1}',
                'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}}'}
        files=[
  ('file',('cat.JPG',open('/Users/Desktop/images/cat.JPG','rb'),'application/octet-stream'))
]
        headers = { 'Authorization': f'Bearer {self.PINATA_JWT}' }

        response = request("POST", url, headers=headers, data=payload, files=files)