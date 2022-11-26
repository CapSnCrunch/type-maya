from PIL import Image
from blocks import blocks

image1 = Image.open('./glyphs/n/na-2.png')
image2 = Image.open('./glyphs/l/la-1.png')
image3 = Image.open('./glyphs/n/na-1.png')

images = [image1, image2, image3]

scale = 5

# determine block shape
block_shape = ''
for i, image in enumerate(images):
    width = image.size[0]
    height = image.size[1]
    aspect_ratio = width / height

    if abs(1 - aspect_ratio) < 0.1:
        block_shape += 'square'
    elif aspect_ratio < 1:
        block_shape += 'vertical'
    else:
        block_shape += 'horizontal'

    if i < len(images)-1:
        block_shape += '-'

# combine glyphs
background = Image.new("RGB", (100*scale, 100*scale), (255, 255, 255))
block = blocks[block_shape]
for i, image in enumerate(images):
    x = int(block[i]['origin'][0]*(scale))
    y = int(block[i]['origin'][1]*(scale))
    width = int(block[i]['width']*(scale))
    height = int(block[i]['height']*(scale))

    resized_image = image.resize((width, height))

    background.paste(resized_image, (x,y), resized_image)

background.show()