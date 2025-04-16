import qrcode

data = 'QR code  using  make() function'
img =  qrcode.make(data)

img.save('qr code  project 7.png')
