"""Main app runner"""
###### Python Packages ######
###### My Packages ######
from pyengine.engine import PyEngine
from pyengine.libs.designer.designer import Designer
from pyengine.libs.mixer import Music


game_data = {
    "vs_player": 0,
    "vs_bot": 0,
    "left_score": 0,
    "right_score": 0,
    "x_ball_speed": 4.0,
    "y_ball_speed": 4.0,
    "pad_speed": 10,
    "left_move": "none",
    "right_move": "none",
}


if __name__ == "__main__":
    PyEngine.load_data()
    Designer.create_from_file("ui_data/main_menu.json")
    Designer.create_from_file("ui_data/gameplay.json")

    Designer.toggle_exclude("gameplay")
    Designer.get_element("rightpad").rect.width -= 20
    Designer.get_element("rightpad").rect.x += 20
    Designer.get_element("leftpad").rect.width -= 20

    # Music.play_music("bgm")

    PyEngine.mainloop(debug=True)
