import random
from PIL import ImageDraw, ImageFont
from PIL.Image import Image


class MemeEngine:
    def __init__(self, output_path):
        """Create instance of class"""
        self.output_path = output_path

    def make_meme(self, path, text, author, width=500):
        """Create meme with given text and author"""
        global img, img_font, height
        try:
            img = Image.open(path)
        except Exception as ex:
            print(f'Exception: {ex}')

        if width:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            size = (width, height)
            img = img.resize(size, Image.NEAREST)

        if text:
            img_draw = ImageDraw.Draw(img)
            img_font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', int(height / 10))

        # calculate x axis range for the text
        x_min = (img.size[0] / 10)
        x_max = (img.size[0] / 2)
        range_x = random.randint(x_min, x_max)

        lines_to_draw = [text, "- " + author]

        # Calculate y axis for text display
        y_min = (img.size[1] / 20)
        y_max = img.size[1]
        range_y = random.randint(y_min, y_max)

        range_x_y = (range_x, range_y)
        # draw text
        for line in lines_to_draw:
            img_draw.text(range_x_y, line, img_font, "left")

        out_path = f'{self.output_path}/{random.randint(0, 1000000)}.jpeg'
        img.save(out_path)
        return out_path
