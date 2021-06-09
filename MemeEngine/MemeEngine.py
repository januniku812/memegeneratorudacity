import random
from PIL import ImageDraw, ImageFont
import PIL.Image


class MemeEngine:
    def __init__(self, output_path):
        """Create instance of class"""
        self.output_path = output_path

    def make_meme(self, path, text, author, width=500):
        print("make meme reached")
        """Create meme with given text and author"""
        global img, img_font, height, img_draw
        try:
            img = PIL.Image.open(path)
        except Exception as ex:
            print(f'Exception: {ex}')

        if width:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            size = (width, height)
            img = img.resize(size, PIL.Image.NEAREST)

        line_to_draw = f'{text}\n- {author}'

        if text:
            img_draw = ImageDraw.Draw(img)
            fnt_size = int(height/(len(line_to_draw.strip(" ")))) * 2
            fnt_path = './fonts/LilitaOne-Regular.ttf'
            img_font = ImageFont.truetype(fnt_path, int(height/11))

        # Calculate y axis for text display
        y_min = (img.size[1] / 20)
        y_max = img.size[1]
        range_y = random.randint(y_min, y_max)

        # draw text
        img_draw.multiline_text((0, range_y), line_to_draw, 'white', img_font)

        out_path = f'{self.output_path}/{random.randint(0, 1000000)}.jpeg'
        img.save(out_path)
        print(f"meme saved to {self.output_path}")
        return out_path
