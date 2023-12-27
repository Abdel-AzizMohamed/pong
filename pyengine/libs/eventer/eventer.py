"""Define game events handler"""
#### Python Packages ####
from importlib import import_module
import pygame

# pylint: disable=E1101
#### My Packages ####
from pyengine.utils.collision_handler import mouse_collision


class Eventer:
    """Define main event class"""

    keyboard_keys = {
        "right": 1073741903,
        "left": 1073741904,
        "down": 1073741905,
        "up": 1073741906,
    }

    elements_events = {}
    global_events = []
    exclude_groups = {}

    @staticmethod
    def add_object_event(element: object, event_data: dict) -> None:
        """
        Add event to given element

        Arguments:
            element: element the preform the event
            event_data: dict contains event_data {event, args}
        """
        if not event_data:
            return

        if not Eventer.elements_events.get(element.group):
            Eventer.elements_events[element.group] = []
            Eventer.exclude_groups[element.group] = 1

        for import_data, data in event_data.items():
            module_path, function_path = import_data.split(":")

            if function_path.find(".") != -1:
                str_class, str_func = function_path.split(".")
                module_class = getattr(import_module(module_path), str_class)
                module_function = getattr(module_class, str_func)
            else:
                module_function = getattr(import_module(module_path), function_path)

            Eventer.elements_events[element.group].append(
                (module_function, data, element)
            )

    @staticmethod
    def load_global_events(events: dict, element_grabber: object) -> list:
        """
        Load global events from config file

        Arguments:
            event_data: dict contains event_data {event, args}
        """
        non_events = []

        if not events:
            return

        for import_data, data in events.items():
            module_path, function_path = import_data.split(":")

            if function_path.find(".") != -1:
                str_class, str_func = function_path.split(".")
                module_class = getattr(import_module(module_path), str_class)
                module_function = getattr(module_class, str_func)
            else:
                module_function = getattr(import_module(module_path), function_path)

            if data.get("event") == "none":
                non_events.append((module_function, data))
            elif data.get("event") == "rectin":
                data["args"][0] = element_grabber(data["args"][0])
                data["args"][1] = element_grabber(data["args"][1])
                non_events.append((module_function, data))
            else:
                Eventer.global_events.append((module_function, data))

        return non_events

    @staticmethod
    def trigger_events(event: pygame.event) -> None:
        """
        Trigger all global/elements events

        Arguments:
            event: event object from pygame to check for events
        """
        elements = [
            element
            for (name, group) in Eventer.elements_events.items()
            for element in group
            if Eventer.exclude_groups.get(name)
        ]

        for element in elements:
            function = element[0]
            event_type = element[1].get("event")

            args = element[1].get("args").copy()
            args.insert(0, element[2])

            params = element[1].get("params")
            rect = element[2].rect

            if not mouse_collision(rect) and event_type == "mouseout":
                function(*args)
            if mouse_collision(rect) and event_type == "mousein":
                function(*args)
            if Eventer.check_mouse_event(event, event_type) and mouse_collision(rect):
                function(*args)
            if Eventer.check_keyboard_event(event, event_type):
                function(*args)

        for global_event in Eventer.global_events:
            function = global_event[0]
            event_type = global_event[1].get("event")
            args = global_event[1].get("args").copy()

            if Eventer.check_mouse_event(event, event_type):
                function(*args)
            if Eventer.check_keyboard_event(event, event_type):
                function(*args)

    @staticmethod
    def check_mouse_event(event: pygame.event, event_type: str) -> bool:
        """
        Check for mouse event

        Arguments:
            event: event object from pygame to check for events
            event_type: event type (leftclick, rightclick)
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event_type == "click":
                return True
            if event.button == 1 and event_type == "leftclick":
                return True
            if event.button == 2 and event_type == "middleclick":
                return True
            if event.button == 3 and event_type == "rightclick":
                return True
        return False

    @staticmethod
    def check_keyboard_event(event: pygame.event, event_type: str) -> bool:
        """
        Check for keyboard event

        Arguments:
            event: event object from pygame to check for events
            event_type: event type (leftclick, rightclick)
        """
        if event_type.find("_") == -1:
            return False

        key_action, key = event_type.split("_")

        if event.type == pygame.KEYDOWN and key_action == "down":
            if len(key) == 1 and event.key == ord(key):
                return True
            if event.key == Eventer.keyboard_keys.get(key):
                return True
        if event.type == pygame.KEYUP and key_action == "up":
            if len(key) == 1 and event.key == ord(key):
                return True
            if event.key == Eventer.keyboard_keys.get(key):
                return True

        return False
