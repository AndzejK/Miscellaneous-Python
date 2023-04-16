import qrcode

# qr_img=qrcode.make("https://github.com/AndzejK")
# qr_img.save("qr_my_github.png")

# Set up
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
img = qrcode.make("https://github.com/AndzejK")
img = qr.make_image(back_color=(255, 255, 204), fill_color=(204, 0, 76))
img.save("qr_v3.png")