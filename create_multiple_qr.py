import qrcode
import re
with open('urls.txt','r') as file:
    links=file.readlines() # gettling a list with the links 

# Set up
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#img = qrcode.make("https://github.com/AndzejK")
img = qr.make_image(back_color=(0, 0, 0), fill_color=(255, 255, 255))
img.save("qr_v3.png")
pattern=re.compile("[a-z]+")
for link in links:
    link.strip()
    qr_img=qrcode.make(link)
    name=pattern.findall(link[8:])
    print(name[0])
    qr_img.save(f"qr-{name[0]}.png")