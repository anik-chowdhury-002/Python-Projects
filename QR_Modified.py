import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://www.youtube.com/watch?v=p0QUmC2WJwM&t=4689s")
qr.make(fit=True)

img = qr.make_image(fill_color='green', back_color='white')
img.save("c_prog.png")
