import qrcode

Data = 'This is First QR code Experience.'

qr = qrcode.QRCode(version=10,box_size=40,border=50)

qr.add_data(Data)
qr.make(fit=True)

img = qr.make_image(fill_color='Blue',back_color='aqua')

img.save('D:/Coding World/Qr_code/Qr1.png')