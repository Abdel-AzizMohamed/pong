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


def object_collision(first_object: object, other_object: object) -> bool:
    """
    Check if the given rect collision another rect

    Arguments:
        first_object: first object to check collision
        other_object: other object to check collision with first
    """
    return first_object.rect.colliderect(other_object.rect)
