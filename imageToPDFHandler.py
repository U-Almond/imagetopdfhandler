from PIL import Image
from pathlib import Path

# Open the image file
image_file = Image.open("/Users/spacegirl/Desktop/image.png")

# Create a PDF file
pdf_file = Path("/Users/spacegirl/Desktop/output.pdf")

# Convert the image to PDF
image_file.save(pdf_file, "PDF", resolution=100.0)