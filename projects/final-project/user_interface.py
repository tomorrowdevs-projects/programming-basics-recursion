from data import home
from manage_data import (find_room, check_object_in_data, check_for_category, display_object, delete_object,
                         display_type_of_category, update_object, add_object)


def user_interface() -> str:
    """
    This function represents the user interface for navigating home environments.
    Users can search for specific items, manage objects in their environment, and explore various rooms.

    return: an information string once asked to close the program
    """

    print("Welcome home!!!")

    using_the_app = input("\nPress Enter if you want to use the app. Otherwise press 'q' to exit: ")
    while using_the_app != "" and using_the_app.lower() != "q":
        using_the_app = input("\nPress Enter if you want to use the app. Otherwise press 'q' to exit: ")

    while using_the_app == "":

        checking_object = input("Are you looking for a specific item?\nPress Enter to write its name and search for it,"
                                " otherwise press 'q' to explore the various environments:\n")
        while checking_object != "" and checking_object.lower() != "q":
            checking_object = input("Are you looking for a specific item?\nPress Enter to write its name and search "
                                    "for it, otherwise press 'q' to explore the various environments:\n")

        if checking_object == "":
            object_to_find = input("Enter the name of the object: ").lower()
            room = find_room(object_to_find)

            if room:
                print(f"Your object is in the {room}")
                print(check_object_in_data(object_to_find, home[room]))

            else:
                print(f"{object_to_find} not found!")
                print("Would you prefer searching by categories?")
                checking_categories = input(
                    "Press Enter if you want to find it by categories, or press 'q' to explore your environment: ")

                while checking_categories != "" and checking_categories.lower() != "q":
                    checking_categories = input(
                        "Press Enter if you want to find it by categories, or press 'q' to explore your environment: ")

                if checking_categories == "":
                    print("Here are the currently updated categories: ")
                    categories = display_type_of_category()

                    for i in categories:
                        print(str(i))
                    category = input("Choose one of the following categories:").lower()

                    if category not in categories:
                        print(f"{category} not found!")

                    else:

                        for i in home:
                            print(check_for_category(category, home[i]))

        print("Explore one of your environments:\n")

        for key in home:
            print(key)

        user_room = input("Type here the name of your environment: ").lower()
        while user_room not in home:
            print(f"{user_room} not found!")
            user_room = input("Type here the name of your environment: ").lower()

        user_choice = input("\nPress Enter if you want to display your items,\n"
                            "press 'a' to add an item to your environment,\n"
                            "press m to manage your object,\n"
                            "press r to delete your object,\n"
                            "press q to quit: ")
        while (user_choice.lower() != "" and user_choice.lower() != "a" and user_choice.lower() != "m"
               and user_choice.lower() != "r" and user_choice.lower() != "q"):
            user_choice = input("\nPress Enter if you want to display your items,\n"
                                "press 'a' to add an item to your environment,\n"
                                "press m to manage your object,\n"
                                "press r to delete your object,\n"
                                "press q to quit: ")

        if user_choice == "":
            display = display_object(home[user_room])

            if display:
                print(display_object(home[user_room]))

            else:
                print("Empty environment!")

        if user_choice.lower() == "a":
            name = input("Enter the name of the object: ").lower()
            check_name = check_object_in_data(name, home[user_room])

            if not check_name:
                category = input("Enter the type of category of the object: ").lower()
                position = input("Enter where your object is located: ").lower()
                print(add_object(home[user_room], name, category, position))

            else:
                print(f"{name} already in the environment!")

        if user_choice.lower() == "m":
            object_to_update = input("Enter the name of the object to update: ").lower()

            if check_object_in_data(object_to_update, home[user_room]):
                name = input("Enter the new object name: ").lower()
                print(update_object("name", object_to_update, home[user_room], name))
                category = input("Enter the type of category of the object: ").lower()
                print(update_object("category", name, home[user_room], category))
                position = input("Enter where your object is located: ").lower()
                print(update_object("position", name, home[user_room], position))

            else:
                print(f"{object_to_update} not found!")

        if user_choice.lower() == "r":
            object_to_delete = input("Enter the name of the object to delete: ").lower()

            if check_object_in_data(object_to_delete, home[user_room]):
                print(delete_object(object_to_delete, home[user_room]))

            else:
                print(f"{object_to_delete} not found!")

        if user_choice.lower() == "q":
            break

        using_the_app = input("\nPress Enter if you want to use the app. Otherwise press 'q' to exit: ")
        while using_the_app != "" and using_the_app.lower() != "q":
            using_the_app = input("\nPress Enter if you want to use the app. Otherwise press 'q' to exit: ")

    return "Closing the app"
