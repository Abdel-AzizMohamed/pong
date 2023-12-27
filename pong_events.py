"""Define pong game functions events"""
###### Python Packages ######
import sys
import pygame

# pylint: disable=E1101
###### My Packages ######
from pyengine.window import win_obj
from pyengine.libs.designer.designer import Designer
from main import game_data


def exit_game(_):
    """Exit game"""
    pygame.quit()
    sys.exit()


def back_to_menu(_):
    """Return to main menu"""
    Designer.toggle_exclude("gameplay")
    Designer.toggle_exclude("mainmenu")
    game_data["vs_player"] = 0
    game_data["vs_bot"] = 0


def start_game(_, game_type: str):
    """Starts game"""
    Designer.toggle_exclude("gameplay")
    Designer.toggle_exclude("mainmenu")

    if game_type == "player":
        game_data["vs_player"] = 1
    else:
        game_data["vs_bot"] = 1


def ball_movement(ball):
    """
    Handle the ball movement and speed increment

    Arguments:
        ball: wanted ball to move
    """
    if game_data.get("vs_player") == 0 and game_data.get("vs_bot") == 0:
        return

    ball = Designer.get_element(ball)
    ball.rect.x += game_data.get("x_ball_speed")
    ball.rect.y += game_data.get("y_ball_speed")

    if ball.rect.left <= 0 or ball.rect.right >= win_obj.screen_width:
        game_data["x_ball_speed"] *= -1
    if ball.rect.top <= 0 or ball.rect.bottom >= win_obj.screen_height:
        game_data["y_ball_speed"] *= -1


def left_ball_collision(_):
    """Reflect speed if the ball collied with pad"""
    game_data["x_ball_speed"] *= -1
    game_data["y_ball_speed"] *= -1


def right_ball_collision(_):
    """Reflect speed if the ball collied with pad"""
    print("test")
    game_data["x_ball_speed"] *= -1
    game_data["y_ball_speed"] *= -1


def hold_pad_up(pad):
    """Move the pad up"""
    if game_data.get("vs_bot") == 1 and pad.name == "leftpad":
        return
    if pad.name == "leftpad":
        game_data["left_move"] = "up"
    if pad.name == "rightpad":
        game_data["right_move"] = "up"


def release_pad_up(pad):
    """Move the pad up"""
    if game_data.get("vs_bot") == 1 and pad.name == "leftpad":
        return
    if pad.name == "leftpad":
        game_data["left_move"] = "none"
    if pad.name == "rightpad":
        game_data["right_move"] = "none"


def hold_pad_down(pad):
    """Move the pad down"""
    if game_data.get("vs_bot") == 1 and pad.name == "leftpad":
        return
    if pad.name == "leftpad":
        game_data["left_move"] = "down"
    if pad.name == "rightpad":
        game_data["right_move"] = "down"


def release_pad_down(pad):
    """Move the pad down"""
    if game_data.get("vs_bot") == 1 and pad.name == "leftpad":
        return
    if pad.name == "leftpad":
        game_data["left_move"] = "none"
    if pad.name == "rightpad":
        game_data["right_move"] = "none"


def player_movement():
    """
    Handle the Player movement
    """
    left_pad = Designer.get_element("leftpad")
    right_pad = Designer.get_element("rightpad")

    if game_data.get("left_move") == "up":
        left_pad.rect.y -= game_data.get("pad_speed")
    if game_data.get("left_move") == "down":
        left_pad.rect.y += game_data.get("pad_speed")
    if game_data.get("right_move") == "up":
        right_pad.rect.y -= game_data.get("pad_speed")
    if game_data.get("right_move") == "down":
        right_pad.rect.y += game_data.get("pad_speed")

    if left_pad.rect.top <= 0:
        left_pad.rect.top = 0
    if right_pad.rect.top <= 0:
        right_pad.rect.top = 0

    if left_pad.rect.bottom >= win_obj.screen_height:
        left_pad.rect.bottom = win_obj.screen_height
    if right_pad.rect.bottom >= win_obj.screen_height:
        right_pad.rect.bottom = win_obj.screen_height
