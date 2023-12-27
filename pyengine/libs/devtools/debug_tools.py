"""Define a debugging tools module"""
###### Python Packages ######
import pygame

###### My Packages ######
from pyengine.window import win_obj
from pyengine.libs.designer.py_attributes import Text
from pyengine.libs.designer.designer import Designer


class Debugger:
    """Define debugging tools"""

    grid_color = None

    fps_font = None
    fps_antialias = None
    fps_color = None
    fps_align = None

    object_rect_color = None
    object_rect_size = None

    @staticmethod
    def display_grid() -> None:
        """Display game gird according to x_ceil, y_ceil in window object"""
        for row in range(win_obj.x_ceil):
            offset = row * (win_obj.screen_height / win_obj.x_ceil)
            pygame.draw.aaline(
                win_obj.screen,
                Debugger.grid_color,
                (0, offset),
                (win_obj.screen_width, offset),
            )

        for column in range(win_obj.y_ceil):
            offset = column * (win_obj.screen_width / win_obj.y_ceil)
            pygame.draw.aaline(
                win_obj.screen,
                Debugger.grid_color,
                (offset, 0),
                (offset, win_obj.screen_height),
            )

    @staticmethod
    def display_fps() -> None:
        """Display game current fps"""
        fps_text = str(round(win_obj.clock.get_fps()))
        render_font = Text.fonts[Debugger.fps_font].render(
            fps_text, Debugger.fps_antialias, Debugger.fps_color
        )

        font_width = render_font.get_rect().size[0]
        font_height = render_font.get_rect().size[1]
        half_font_width = render_font.get_rect().size[0] // 2
        half_font_height = render_font.get_rect().size[1] // 2

        window_width = win_obj.screen_width
        window_height = win_obj.screen_height
        half_window_width = win_obj.screen_width // 2
        half_window_height = win_obj.screen_height // 2

        offset = 25

        if Debugger.fps_align == "top":
            x_pos = abs(half_window_width - half_font_width)
            y_pos = offset
        elif Debugger.fps_align == "topleft":
            x_pos = offset
            y_pos = offset
        elif Debugger.fps_align == "topright":
            x_pos = abs(window_width - font_width - offset)
            y_pos = 25
        elif Debugger.fps_align == "center":
            x_pos = abs(half_window_width - half_font_width)
            y_pos = abs(half_window_height - half_font_height)
        elif Debugger.fps_align == "midleft":
            x_pos = offset
            y_pos = abs(half_window_height - half_font_height)
        elif Debugger.fps_align == "midright":
            x_pos = abs(window_width - font_width - offset)
            y_pos = abs(half_window_height - half_font_height)
        elif Debugger.fps_align == "bottom":
            x_pos = abs(half_window_width - half_font_width)
            y_pos = abs(window_height - font_height - offset)
        elif Debugger.fps_align == "bottomleft":
            x_pos = offset
            y_pos = abs(window_height - font_height - offset)
        else:
            x_pos = abs(window_width - font_width - offset)
            y_pos = abs(window_height - font_height - offset)

        win_obj.screen.blit(render_font, (x_pos, y_pos))

    @staticmethod
    def display_object_rect() -> None:
        """Display all game objects rect"""
        elements = [
            item for group in Designer.game_elements.values() for item in group.values()
        ]

        for element in elements:
            pygame.draw.rect(
                win_obj.screen,
                Debugger.object_rect_color,
                element.rect,
                Debugger.object_rect_size,
            )

    @staticmethod
    def load_debugger_config(config: dict) -> None:
        """Load config data

        Arguments:
            config: dict contains config data {grid_color, fps_font, fps_antialias, fps_color, ...}
        """
        Debugger.grid_color = config.get("grid_color")

        Debugger.fps_font = config.get("fps_font")
        Debugger.fps_antialias = config.get("fps_antialias")
        Debugger.fps_color = config.get("fps_color")
        Debugger.fps_align = config.get("fps_align")

        Debugger.object_rect_color = config.get("object_rect_color")
        Debugger.object_rect_size = config.get("object_rect_size")
