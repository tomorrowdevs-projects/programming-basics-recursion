def total_values():
    value = input("Enter a value: ")

    if value == "":
        return 0.0

    else:
        return int(value) + int(total_values())
