from typing import Any
from data import home


def add_object(room: list, name: str, category: str, position: str) -> str:
    """
    Adds a new item to the room list

    param room: the room in which there are objects
    param name: object name
    param category: object category
    param position: object position
    return: informs the user that the object has been added to the room
    """

    room.append(
        {
            "name": name,
            "category": category,
            "position": position
        }
    )
    return f"{name} added!"


def check_object_in_data(object_to_identify: str, room: list) -> list | str | Any:
    """
    Checks if there are objects with that name in that room.

    param object_to_identify: object name
    param room: the room in which there are objects
    return: an empty list if the function doesn't find the object in the room, otherwise returns the object name
    """

    if not room:
        return room

    if object_to_identify == room[0]["name"]:
        return room[0]

    else:
        return check_object_in_data(object_to_identify, room[1:])


def display_object(room: list) -> str:
    """
    Allows to display all objects in the room

    param room: the room in which there are objects
    return: the objects in that room
    """
    if not room:
        return ""
    else:
        return str(room[0]) + "\n\n" + display_object(room[1:])


def delete_object(object_to_delete: str, room: list) -> str:
    """
    Allows to remove an object in the room

    param object_to_delete: object name
    param room: the room in which there are objects
    return: informs the user that the object has been deleted to the room
    """
    if room[0]["name"] == object_to_delete:
        room[0].clear()
        room.remove({})
        return "deleted!"
    else:
        delete_object(object_to_delete, room[1:])
        room.remove({})
        return "deleted!"


def update_object(value_name: str, object_to_update: str, room: list, new_value_name: str) -> str:
    """
    Allows to update the value of an object-specific key

    param value_name: the value to replace
    param object_to_update: object name
    param room: the room in which there are objects
    param new_value_name: the value updated
    return: informs the user that the object has been updated to the room
    """

    if room[0]["name"] == object_to_update:
        room[0][value_name] = new_value_name
        return "Updated!"

    else:
        update_object(value_name, object_to_update, room[1:], new_value_name)
        return "Updated!"


def find_room(object_name: str) -> list:
    """
    Allows you to search the room in which the object is present

    param object_name: object name
    return: the room in which the object is present
    """

    for rooms in home:

        if check_object_in_data(object_name, home[rooms]):
            room = rooms
            return room


def display_type_of_category() -> set:
    """
    Allows to display all objects categories

    return: all categories of existing objects
    """

    categories = set()

    for room in home:
        n = 0

        while n < len(home[room]):
            categories.add(home[room][n]["category"])
            n += 1

    return categories


def check_for_category(category: str, room: list) -> str:
    """
    Allows you to search and return all objects by categories

    param category: object category
    param room: the room in which there are objects
    return: all objects by categories
    """

    if not room:
        return ""

    if category == room[0]["category"]:
        return str(room[0]) + "\n" + check_for_category(category, room[1:])

    else:
        return check_for_category(category, room[1:])
