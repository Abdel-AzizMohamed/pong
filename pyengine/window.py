"""Define game window that contains windows setting"""
###### Python Packages ######
import time
import os
import pygame

###### My Packages ######
from pyengine.utils.json_handler import read_json
from pyengine.utils.path_handler import alternate_path

# pylint: disable=E1101
# pylint: disable=R0903
#### Pygame Init ####
pygame.init()
pygame.mixer.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
# os.environ["SDL_VIDEO_WINDOW_POS"] = "1000,500"


class Resolution:
    """Define the game resolution"""

    def __init__(self, size: list, grid_div: int) -> None:
        """init a new resolution object"""
        self.screen_width = 1
        self.screen_height = 1
        self.width_ratio = 1.0
        self.height_ratio = 1.0
        self.x_ceil = 1
        self.y_ceil = 1

        self.set_resolution(size)
        self.set_ratio()
        self.set_grid(grid_div)

    def set_resolution(self, size: list) -> None:
        """Set the game window size"""
        screen_info = pygame.display.Info()
        monitor_width = screen_info.current_w
        monitor_height = screen_info.current_h

        if size[0] <= 0 or size[1] <= 0:
            self.screen_width = monitor_width
            self.screen_height = monitor_height
        else:
            self.screen_width = size[0]
            self.screen_height = size[1]

    def set_ratio(self) -> None:
        """Set the window ration according to 1920x1080 and the current screen size"""
        self.width_ratio = self.screen_width / 1920
        self.height_ratio = self.screen_height / 1080

    def set_grid(self, grid_div: int) -> None:
        """Set the game grid"""
        self.x_ceil = grid_div * 9
        self.y_ceil = grid_div * 16


class FrameRate:
    """Define the game main clock"""

    def __init__(self, fps: int) -> None:
        """Init a new clock object"""
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.delta_time = 1.0
        self.previous_time = time.time()

    def set_delta(self) -> None:
        """
        Sets the game delta-time

        this function will be called every game loop to calc the delta-time value
        """
        self.delta_time = time.time() - self.previous_time
        self.previous_time = time.time()


class Window(Resolution, FrameRate):
    """Game window object that contains all the window setting"""

    def __init__(self, window_data: dict) -> None:
        """
        Init a new window object

        Arguments:
            window_data: dict contains window data {window_size, grid_precision_level, fps, window_title}
        """

        window_size = window_data.get("window_size")
        grid_precision_level = window_data.get("grid_precision_level")
        fps = window_data.get("fps")
        window_title = window_data.get("window_title")

        Resolution.__init__(self, window_size, grid_precision_level)
        FrameRate.__init__(self, fps)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(window_title)


DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "default_config.json")
CONFIG_PATH = alternate_path("config.json", DEFAULT_CONFIG_PATH)
win_obj = Window(read_json(CONFIG_PATH).get("window_data"))
