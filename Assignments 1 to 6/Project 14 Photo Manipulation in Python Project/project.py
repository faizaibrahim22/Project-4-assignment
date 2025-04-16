from PIL import Image, ImageFilter, ImageDraw, ImageFont

# Load your image (make sure this image is present in your folder)

img = Image.open("your_image.jpg")

# Resize image
resized = img.resize((300, 300))

# Grayscale image
gray = img.convert("L")

# Apply blur filter
blurred = img.filter(ImageFilter.BLUR)

# Rotate image
rotated = img.rotate(45)

# Save modified images
resized.save("resized_image.jpg")
gray.save("grayscale_image.jpg")
blurred.save("blurred_image.jpg")
rotated.save("rotated_image.jpg")

# Add text on image
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((10, 10), "Code by Faiza", fill="red", font=font)

img.save("image_with_text.jpg")

print("✅ ALL IMAGE MANIPULATIONS DONE AND SAVED!")
