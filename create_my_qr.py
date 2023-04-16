import qrcode

qr_img=qrcode.make("https://github.com/AndzejK")
qr_img.save("qr_my_github.png")