#pip install qrcode pillow
import qrcode

code=qrcode.make("https://www.linkedin.com/in/eralpertan/")
code.save("vol1.png")

code=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=2
)


code.add_data("https://www.linkedin.com/in/eralpertan/")
code.make(fit=True)

image=code.make_image(fill_color="red",back_color="black")
image.save("vol2.png")