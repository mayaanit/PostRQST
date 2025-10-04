import requests

class PostBase:
    def __init__(self, token, id, message):
        self.token =  token
        self.id = id
        self.msg = message
        self.url = ""
       

    def results(self, response):
        if response.status_code == 200:
            print("✅ Post created successfully:", response.json())
        else:
            print("❌ Error:", response.json())

    

class PostMessage(PostBase):

    def __init__(self, token, id, message):
        super().__init__(token, id, message)
        self.url = f"https://graph.facebook.com/{id}/feed"        

    def send(self):
        # Facebook Graph API endpoint        
        payload = {
            "message": self.msg,
            "access_token": self.token
        }
        
        print("paylod \n", payload)
        response = requests.post( self.url, data=payload)
        super().results(response)        


class PostMessageFromFile(PostMessage):
    def __init__(self,token, id, fname):
        with open(fname, 'r') as file:
            msg = file.read()
        super().__init__(token, id, msg)

class PostFile(PostBase):
    def __init__(self,token, id, file, msg):
        super().__init__(token, id, msg)
        self.file = file

    def send(self):
       
        payload = {
            "caption": self.msg,
            "access_token": self.token
        }
        files = {
            "source": open(self.file, "rb")
        }
        print("url photo", self.url, payload)
        response = requests.post(self.url, data=payload, files=files)
        files["source"].close()
        super().results(response) 

class  PostPhoto(PostFile):
    def __init__(self, token, id, photo_file, caption):
        super().__init__(token, id, photo_file, caption)
        self.url = f"https://graph.facebook.com/{id}/photos"
            
class  PostPhotoWithCaptionFile(PostPhoto):
    def __init__(self, token, id, photo_file, caption_file):
        with open(caption_file, 'r') as file:
            caption = file.read()
        super().__init__(token, id, photo_file, caption)
        
            


        
        