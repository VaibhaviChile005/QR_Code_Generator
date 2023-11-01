#basic qr code generation
import segno
qrcode = segno.make_qr("Vaibhavi")
qrcode.save("basic_qrcode.png")

# adding features to the qr code like border, color etc
import segno
featured_qrcode = segno.make_qr("https://github.com/VaibhaviChile005")
featured_qrcode.save('updated_qrcode.png', scale=5, light="lightblue", dark="darkblue",data_dark="black", data_light="white",)

