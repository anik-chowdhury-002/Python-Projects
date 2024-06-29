import qrcode as qr
img= qr.make("https://www.youtube.com/watch?v=9TUPVMWhpvk")

img.save("RCB_Anthem_QR.png")
