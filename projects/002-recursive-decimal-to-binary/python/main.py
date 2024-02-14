def decimal_to_binary(decimal_number):

    if decimal_number == 0 or decimal_number == 1:
        return str(decimal_number % 2)

    elif decimal_number > 1:
        return decimal_to_binary(decimal_number // 2) + str(decimal_number % 2)

    else:
        return "Wrong value!"
