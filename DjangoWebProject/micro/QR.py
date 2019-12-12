import pyqrcode
from pyzbar.pyzbar import decode

def QR_GEN(img):
    big_code = pyqrcode.create(img
        , error='L', version=27, mode='binary')
    return big_code.png_as_base64_str(scale=5,module_color=[
        0, 0, 0, 255],background=[255,255,255,255],quiet_zone=4)

def QR_DEG(img):
    deg = decode(img)
    return deg
