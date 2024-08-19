import qrcode
from PIL import Image, ImageDraw, ImageFont

# Data to encode
data = "You're cutee 😍"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code: 1 is the smallest, 40 is the largest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR code
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code with custom colors
qr_image = qr.make_image(fill_color="black", back_color="white")

# Convert QR code image to RGB mode (required for adding text)
qr_image = qr_image.convert("RGB")

# Create a drawing object
draw = ImageDraw.Draw(qr_image)

# Text to add on top of the QR code
text = "Scan the QR code to see the magic 😋"

# Load a font
try:
    # Load a TTF font file from system or specify a font
    font = ImageFont.truetype("cour.ttf", 14)  # Adjust the font size as needed
except IOError:
    # If the specific font is not found, load the default PIL font
    font = ImageFont.load_default()

# Calculate text width and height for centering using textbbox
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
image_width, image_height = qr_image.size
x_position = (image_width - text_width) // 2
y_position = 10  # Adjust the vertical position as needed

# Add the text to the QR code image
draw.text((x_position, y_position), text, font=font, fill="red")

# Save the image to a file
qr_image.save("qr_with_text.png")
