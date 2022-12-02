import openai
import urllib.request
import cv2
from PIL import Image
import sys

openai.organization = "org-7GHrzPrQec6Q9QGVWpfDG3yC"
openai.api_key = "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"
openai.Model.list()


nbIteration = 1
folderPath = "C:/Users/crhon/Desktop/buffer";

response = openai.Image.create(
    prompt=sys.argv[1],
    n=nbIteration,
    size="256x256"
)
for i in range(nbIteration):
    fileInput = folderPath + "/image" + str(i) + ".png"
    fileOutput = folderPath + "/image" + str(i) + str(nbIteration) + ".png"
    url = (response['data'][i]['url'])
    urllib.request.urlretrieve(url, fileInput)
    open(fileOutput, 'wb').write(rembg.remove(open(fileInput, 'rb').read()))


    sys.stdout.flush()


