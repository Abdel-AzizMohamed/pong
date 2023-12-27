"""Define start point for Devtools Package"""
###### Python Packages ######
###### My Packages ######
from pyengine.libs.devtools.debug_tools import Debugger

# pylint: disable=R0903


class DevTools:
    """Define main developer tools class"""

    show_grid = True
    show_fps = True
    show_object_rect = True

    @staticmethod
    def display_tools() -> None:
        """Display developer tools if active"""
        if DevTools.show_grid:
            Debugger.display_grid()
        if DevTools.show_fps:
            Debugger.display_fps()
        if DevTools.show_object_rect:
            Debugger.display_object_rect()
