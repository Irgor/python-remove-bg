from rembg import remove
from PIL import Image

print("started")

input_image = "input.png"
output_image = "output.png"

input_object = Image.open(input_image)
print("image loaded")

output = remove(input_object)
print("background removed")

output.save(output_image)
print("new image saved")