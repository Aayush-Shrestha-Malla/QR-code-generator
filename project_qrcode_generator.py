import qrcode

# Data to encode
data = "The message you want to show....or URL"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code: 1 is the smallest, 40 is the largest
    # error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR code
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="red", back_color="green")
# Save the image to a file
img.save("qr.png")
