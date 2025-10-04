# Facebook Page Poster

A Python tool for posting text, photos, and videos to a Facebook Page using the Graph API.

---

## 🚀 Features

- Post text messages or messages from a file  
- Upload photos or videos with captions  
- Simple command-line interface  

---

## ⚙️ Requirements

- **Python 3.7+**
- Facebook **User Token** with the following permissions:
  - `pages_manage_posts`
  - `pages_read_engagement`
  - `pages_show_list`
- Your **Page ID**

---

## 🧩 Installation

```bash
git clone https://github.com/mayaanit/PostRQST.git
cd facebook-page-poster
pip install -r requirements.txt
```

---
## 🧠 UsageUsage

```bash
python main.py <mode> <value> [--caption <text>] [--captionfile <file>]


Arguments
Argument	    Description
mode	        Type of post: text, textfromfile, pic, video
value	        Message text, filename, or media file
--caption	    Caption text for photo or video
--captionfile	File containing caption text
```

🧾 Examples
Post a simple text message
```bash
python main.py text "Hello, Facebook world!"
```

Post Text fro file
```bash
python main.py textfromfile message.txt
```

Upload a photo with a caption
```bash
python main.py pic myphoto.jpg --caption "Good morning from our office 🌞"
```

