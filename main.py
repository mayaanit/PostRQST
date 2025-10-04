import os
from dotenv import load_dotenv
import requests
import argparse
from post import PostMessage, PostMessageFromFile, PostPhotoWithCaptionFile, PostPhoto

def get_access_token(user_token):
    url = f"https://graph.facebook.com/v20.0/me/accounts?access_token={user_token}"
    response = requests.get(url)
    print(response.json())
    
    access_token = response.json()["data"][0]["access_token"]
    print(access_token)
    return access_token

def is_file_exist(filename):
    if not os.path.exists(filename):
        return False
    return True

def main():    
    # Load variables from .env
    load_dotenv()
    access_token = get_access_token(os.getenv("USER_TOKEN"))   

    # Read them in Python
    
    #access_token = os.getenv("ACCESS_TOKEN")
    page_id = os.getenv("PAGE_ID")

    parser = argparse.ArgumentParser(description="Post content to Facebook Page")
    parser.add_argument("mode", choices=["text", "textfromfile", "pic", "video"],
                        help="Type of post: text | textfromfile | pic | video")
    parser.add_argument("value", help="Message text OR filename OR media file")
    parser.add_argument("--caption", help="Caption text for photo")
    parser.add_argument("--captionfile", help="File containes the captions text")
    
    
    #parser.add_argument("extra", nargs="?", help="Optional: message for pic/video")

    args = parser.parse_args()
    if args.mode == "text":
        # value = message
        post = PostMessage(access_token, page_id, args.value)
    elif args.mode == "textfromfile":
        if is_file_exist(args.value) == False:
            print("The file 'args.value' doesn't exist \n:", args.value)        
            return
        post = PostMessageFromFile(access_token, page_id,args.value)
    elif args.mode == "pic":
        if is_file_exist(args.value) == False:
            print("The file  doesn't exist \n:", args.value)        
            return
        if args.captionfile:
            if is_file_exist(args.captionfile) == False:
                print("The file  doesn't exist \n:", args.captionfile)        
                return
            post = PostPhotoWithCaptionFile(access_token, page_id, args.value, args.captionfile )
        else: 
            caption  = ""
            if args.caption:
                caption = args.caption
            post = PostPhoto(access_token, page_id, args.value, caption )

    else:
        raise ValueError("Unsupported mode!  ")
    post.send()   


if __name__ == "__main__":
    main()