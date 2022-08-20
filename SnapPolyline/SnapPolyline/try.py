import base64
base6="rgwhtejrkhga"
img=base64.b64decode(base6)
from PIL import Image
print(type(img))
midleimg=open("SnapPolyline/SnapPointsAPI/stat/middleimg.png","wb")
midleimg.write(base64.b64decode(base6))
midleimg.close()