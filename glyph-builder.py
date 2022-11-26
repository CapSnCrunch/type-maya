import cv2
import numpy as np
from PIL import Image
from blocks import blocks

image1 = Image.open('./glyphs/pure/a-4.png')
image2 = Image.open('./glyphs/l/la-1.png')
image3 = Image.open('./glyphs/n/na-1.png')

images = [np.asarray(image1), np.asarray(image2), np.array(image3)]

scale = 5
glyph = np.zeros((100*scale, 100*scale, 4))


# determine block shape
block_shape = ''
for i, image in enumerate(images):
    width = image.shape[0]
    height = image.shape[1]
    aspect_ratio = width / height

    if abs(1 - aspect_ratio) < 0.1:
        block_shape += 'square'
    elif aspect_ratio < 1:
        block_shape += 'horizontal'
    else:
        block_shape += 'vertical'

    if i < len(images)-1:
        block_shape += '-'
print(block_shape)

# combine glyphs
block = blocks[block_shape]
for i, image in enumerate(images):
    
    adjustment = 0
    if i == 0:
        adjustment = 0.05

    x = int(block[i]['origin'][0]*(scale + adjustment))
    y = int(block[i]['origin'][1]*(scale + adjustment))
    width = int(block[i]['width']*(scale + adjustment))
    height = int(block[i]['height']*(scale + adjustment))

    scaled_image = cv2.resize(image, dsize=(width,height), interpolation=cv2.INTER_CUBIC)

    glyph[y:y+height, x:x+width, :] = scaled_image

while(True):
    # cv2.imshow('Glyph 1', alignedImages[0])
    # cv2.imshow('Glyph 2', alignedImages[1])
    # cv2.imshow('Glyph 3', alignedImages[2])

    cv2.imshow('Glyph', glyph)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break