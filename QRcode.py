import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,
                   border=2)

qr.add_data("https://linktr.ee/rehteel")
qr.make(fit=True)

img = qr.make_image(fill_color="brown", back_color="pink")
img.save("RehteelQrcode.png")

