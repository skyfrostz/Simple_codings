import qrcode
# data to be encoded
data = "Hello World"
# generating QR code
img = qrcode.make(data)
# saving QR code as an image
img.save("qrcode.png")
print("QR code generated successfully!")