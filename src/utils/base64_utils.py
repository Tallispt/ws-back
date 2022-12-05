import cv2 as cv
import numpy as np
import base64

def readb64(uri):
   encoded_data = uri.split(',')[1]
   nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
   img = cv.imdecode(nparr, cv.IMREAD_COLOR)
   return img

def encode64(img):
  _, frame = cv.imencode(".jpeg", img)
  data = str(base64.b64encode(frame)).replace("b'", 'data:image/jpeg;base64,')
  return data