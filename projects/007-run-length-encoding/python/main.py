def run_length_encoding(list_to_code):

    if not list_to_code:
        return list_to_code
    elif len(list_to_code) == 1:
        return list_to_code + [1]
    else:
        number = 1
        letter = list_to_code[0]
        count = 1

        while letter == list_to_code[count]:
            number += 1
            count += 1
    return [letter] + [number] + run_length_encoding(list_to_code[count:len(list_to_code)])
