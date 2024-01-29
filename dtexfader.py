import os
import sys 
from PIL import Image, ImageDraw

rows = 4
cols = 1
gradient_divider = 2

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_image(file):
    return os.path.splitext(file)[1] in img

def main():
    # Check if file path is image
    if(not is_image(sys.argv[1])):
        print("Invalid file.")
        return -1
    
    # Get img and it's palette
    img = Image.open(sys.argv[1])
    img = img.convert('RGBA')
    img_w, img_h = img.size

    # Set up grid
    grid = Image.new('RGBA', size=(img_w, rows * img_h))
    grid_w, grid_h = grid.size

    # Paste img into grid
    for i in range(rows):
        offset = (0, grid_h - (img_h * (i + 1)))
        grid.paste(img, offset)

    # Create gradient
    start_y = (grid_h // gradient_divider) + (grid_h % gradient_divider)
    gradient = Image.new("RGBA", (grid_w, grid_h - start_y))
    draw = ImageDraw.Draw(gradient)
    for i in range(gradient.height):
        alpha = int(255 * (i / gradient.height))
        draw.line([(0, i), (gradient.width, i)], fill=(247, 247, 247, alpha))

    # Combine grid and gradient
    grid.paste(gradient, (0, start_y), gradient)
    grid.show()

if __name__ == '__main__':
    main()