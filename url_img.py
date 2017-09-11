import requests
VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]
url = 'https://dgplug.org/assets/img/header.png'
def if_img(url, extension_list=VALID_IMAGE_EXTENSIONS):
    #return any([url.endswith(e) for e in extension_list])
    if (url.endswith(e) for e in extension_list):
        img = requests.get(url)
        with open('filename', 'wb') as image:
            image.write(img.content)

if_img(url)
