def run_length_decoding(undecoded_list):

    if not undecoded_list:
        return undecoded_list

    else:
        letter = undecoded_list[0]
        number = undecoded_list[1]

        return [letter] * number + run_length_decoding(undecoded_list[2:len(undecoded_list)])
