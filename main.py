from PIL import Image


image = Image.open(r"(<directory to image>)")

def resize_image(size1, size2):

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save(f"Resized_input{size1}x{size2}.jpg")

size1 = int(input("Desired width: "))
size2 = int(input("Desired Height: "))

resize_image(size1, size2)