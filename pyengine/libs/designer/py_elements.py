"""Contains all the basic ui elements"""
###### Python Packages ######
###### My Packages ######
from pyengine.libs.designer.py_attributes import Rectangle, Text
from pyengine.libs.eventer.eventer import Eventer

# pylint: disable=R0903


class PyBase:
    """Define a base class for basic shapes"""

    def __init__(self, attributes: dict) -> None:
        """
        init base data to elements

        Attributes:
            attributes: contains all the base data
        """
        self.name = attributes.get("name")
        self.group = attributes.get("group")
        self.type = attributes.get("class")


class PyRect(PyBase, Rectangle, Text):
    """Define a basic rect shape"""

    def __init__(self, attributes: dict) -> None:
        """
        init a new Rect object

        Attributes:
            attributes: contains all the rect data
        """
        PyBase.__init__(self, attributes.get("base_data"))
        Rectangle.__init__(self, attributes.get("rect_data"))
        Text.__init__(self, attributes.get("text_data"), self.rect)

        obj_data = attributes.get("obj_data")

        self.color = obj_data.get("color")


class PyCircle(PyBase, Rectangle, Text):
    """Define a basic circle shape"""

    def __init__(self, attributes: dict) -> None:
        """
        init a new Circle object

        Attributes:
            attributes: contains all the circle data
        """
        PyBase.__init__(self, attributes.get("base_data"))
        Rectangle.__init__(self, attributes.get("rect_data"))
        Text.__init__(self, attributes.get("text_data"), self.rect)

        obj_data = attributes.get("obj_data")

        self.radius = obj_data.get("radius")
        self.rect.size = (self.radius * 2, self.radius * 2)

        self.color = obj_data.get("color")


class PyButton(PyBase, Rectangle, Text):
    """Define a basic button object"""

    def __init__(self, attributes: dict) -> None:
        """
        init a new Button object

        Attributes:
            attributes: contains all the button data
        """
        PyBase.__init__(self, attributes.get("base_data"))
        Rectangle.__init__(self, attributes.get("rect_data"))
        Text.__init__(self, attributes.get("text_data"), self.rect)

        obj_data = attributes.get("obj_data")

        self.active = obj_data.get("active")
        self.disabled = obj_data.get("disabled")

        self.active_color = self.base_color = obj_data.get("base_color")
        self.hover_color = obj_data.get("hover_color")
        self.select_color = obj_data.get("select_color")
        self.disabled_color = obj_data.get("disabled_color")

        Eventer.add_object_event(
            self,
            {
                "pyengine.libs.eventer.ui_events:ButtonEvents.button_hover": {
                    "event": "mousein",
                    "args": [],
                }
            },
        )
        Eventer.add_object_event(
            self,
            {
                "pyengine.libs.eventer.ui_events:ButtonEvents.button_hover": {
                    "event": "mouseout",
                    "args": [False],
                }
            },
        )
        Eventer.add_object_event(
            self,
            {
                "pyengine.libs.eventer.ui_events:ButtonEvents.button_select": {
                    "event": "leftclick",
                    "args": [],
                }
            },
        )
