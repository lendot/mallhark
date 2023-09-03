import json
import numpy as np
from wand.image import Image
from wand.drawing import Drawing
from wand.font import Font
from wand.color import Color

FONT_FILE = "fonts/Caudex-Regular.ttf"

TEMPLATE_DIR = "templates"

TEMPLATE_CONFIG = "templates.json"


class PlotImage:
    """ Renders a movie plot to an image """

    def __init__(self):
        pass

    def _get_template(self,template_name):
        with open(f'{TEMPLATE_DIR}/{TEMPLATE_CONFIG}') as file:
            json_data = file.read()
        templates = json.loads(json_data)
        return templates[template_name]

    def render(self, plot, template="default"):
        template_settings = self._get_template(template) 
        # todo: handle template not found

        template_image = f"{TEMPLATE_DIR}/{template_settings['template']}"
        
        with Image(filename = template_image) as canvas:

            with Drawing() as context:
                font = Font(FONT_FILE, color = Color('#a00000'))
                context(canvas)
                canvas.caption(
                        plot, 
                        left = template_settings['left'], 
                        top = template_settings['top'],
                        width = template_settings['width'],
                        height = template_settings['height'],
                        font=font, 
                        gravity='north_west'
                )

            img_array = np.array(canvas)

        return img_array
