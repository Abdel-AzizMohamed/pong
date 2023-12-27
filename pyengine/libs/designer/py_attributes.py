"""Define elements attributes"""
###### Python Packages ######
import pygame

###### My Packages ######
from pyengine.window import win_obj

# pylint: disable=R0903
# pylint: disable=R0902
# pylint: disable=R0913


class Rectangle:
    """Define a pygame Rectangle"""

    def __init__(self, rect_data: dict) -> None:
        """
        Init new pygame rect object

        Arguments:
            rect_data: dict contains rect data {x_pos, y_pos, x_size, y_size}
        """
        self.rect = Rectangle.create_rect(rect_data)

    @staticmethod
    def create_rect(rect_data: dict) -> pygame.Rect:
        """
        creates a new pygame rect object from dict

        Arguments:
            rect_data: dict contains rect data {x_pos, y_pos, x_size, y_size}
        """

        x_pos = rect_data.get("x_pos")
        y_pos = rect_data.get("y_pos")

        x_size = rect_data.get("x_size")
        y_size = rect_data.get("y_size")

        x_pos = round(x_pos * (win_obj.screen_width / win_obj.y_ceil))
        y_pos = round(y_pos * (win_obj.screen_height / win_obj.x_ceil))

        if x_size is None or y_size is None:
            x_size = y_size = 0
        else:
            x_size = round(x_size * (win_obj.screen_width / win_obj.y_ceil))
            y_size = round(y_size * (win_obj.screen_height / win_obj.x_ceil))

        return pygame.Rect((x_pos, y_pos), (x_size, y_size))


class Text:
    """Define a pygame Text"""

    fonts = {}

    def __init__(self, text_data: dict, rect: object) -> None:
        """
        Init new pygame text object

        Arguments:
            text_data: dict contains text data {font, text, antialias, color, align}
        """
        self._font = None
        self._text = None
        self._antialias = None
        self._color = None
        self._align = None

        self._font_size = None
        self._rect_size = rect.size

        self.align_x = 0
        self.align_y = 0
        self.font_render = None

        self.set_text(text_data)

    def update_text(
        self,
        font: str = None,
        text: str = None,
        antialias: bool = None,
        color: str = None,
        align: str = None,
    ) -> None:
        """
        Update font properties

        Arguments:
            font: font name
            text: font text
            antialias: font antialias
            color: font color
            align: font alignment according to its object
        """
        self._font = self._font if font is None else self.fonts.get(font)
        self._text = self._text if text is None else text
        self._antialias = self._antialias if antialias is None else antialias
        self._color = self._color if color is None else color
        self._align = self._align if align is None else align

        self.font_render = self._font.render(self._text, self._antialias, self._color)
        self._font_size = self.font_render.get_rect().size

        self.set_align(self._align)

    def set_text(self, text_data: dict) -> None:
        """
        creates a new pygame text object

        Arguments:
            text_data: dict contains text data {font, text, antialias, color, align}
        """

        self._font = self.fonts.get(text_data.get("font"))
        self._text = text_data.get("text")
        self._antialias = text_data.get("antialias")
        self._color = text_data.get("color")
        self._align = text_data.get("align")

        self.font_render = self._font.render(self._text, self._antialias, self._color)
        self._font_size = self.font_render.get_rect().size

        self.set_align(self._align)

    def set_align(self, align: str) -> None:
        """
        Calculate the text alignment offset

        Arguments:
            align: text alignment (left, right, ...)
        """
        self._align = align

        x_text_size = self._font_size[0]
        y_text_size = self._font_size[1]
        half_x_text_size = self._font_size[0] // 2
        half_y_text_size = self._font_size[1] // 2

        x_rect_size = self._rect_size[0]
        y_rect_size = self._rect_size[1]
        half_x_rect_size = self._rect_size[0] // 2
        half_y_rect_size = self._rect_size[1] // 2

        if align == "top":
            self.align_x = abs(half_x_text_size - half_x_rect_size)
            self.align_y = 0
        if align == "topleft":
            self.align_x = 0
            self.align_y = 0
        if align == "topright":
            self.align_x = abs(x_rect_size - x_text_size)
            self.align_y = 0

        if align == "bottom":
            self.align_x = abs(half_x_text_size - half_x_rect_size)
            self.align_y = abs(y_text_size - y_rect_size)
        if align == "bottomleft":
            self.align_x = 0
            self.align_y = abs(y_text_size - y_rect_size)
        if align == "bottomright":
            self.align_x = abs(x_text_size - x_rect_size)
            self.align_y = abs(y_text_size - y_rect_size)

        if align == "center":
            self.align_x = abs(half_x_text_size - half_x_rect_size)
            self.align_y = abs(half_y_text_size - half_y_rect_size)
        if align == "midleft":
            self.align_x = 0
            self.align_y = abs(half_y_text_size - half_y_rect_size)
        if align == "midright":
            self.align_x = abs(x_text_size - x_rect_size)
            self.align_y = abs(half_y_text_size - half_y_rect_size)

    @staticmethod
    def load_fonts(fonts: dict) -> None:
        """
        Load all fonts from config file

        Arguments:
            fonts: dict contains fonts {font_path, font_size}
        """

        for name, font in fonts.items():
            font_path = font.get("font_path")
            font_size = font.get("font_size")

            py_font = pygame.font.Font(font_path, font_size)
            Text.fonts[name] = py_font
