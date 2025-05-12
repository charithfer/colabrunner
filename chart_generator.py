# chart_generator.py

from PIL import Image, ImageDraw

# Create a dummy image
img = Image.new("RGB", (400, 300), color=(73, 109, 137))
draw = ImageDraw.Draw(img)
draw.text((10, 150), "Dummy Candlestick Chart", fill=(255, 255, 0))

# Save it
img.save("chart.png")

print("Dummy chart created.")
