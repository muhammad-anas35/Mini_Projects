from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('D:/Coding World/Qr_code/Qr1.png')

result = decode(img)

print(result)