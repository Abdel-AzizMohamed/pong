"""Define a collision module"""
###### Python Packages ######
import pygame
from pygame.mouse import get_pos as mouse_pos

###### My Packages ######


def mouse_collision(rect: pygame.Rect) -> bool:
    """
    Check if the given rect collision with mouse cursor

    Arguments:
        rect: rect to check collision with mouse cursor
    """
    if rect.collidepoint(mouse_pos()):
        return True
    return False


def object_collision(rect: pygame.Rect, other: object) -> bool:
    """
    Check if the given rect collision another rect

    Arguments:
        rect: rect to check collision with
        other: other rect to check collision with
    """
    if other is None:
        return False

    if rect.colliderect(other.rect):
        return True
    return False
