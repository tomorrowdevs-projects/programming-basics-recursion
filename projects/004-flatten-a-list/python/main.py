def flatten_a_list(unflattened_list):

    if not unflattened_list:
        return unflattened_list

    else:

        if isinstance(unflattened_list[0], list):
            l1 = flatten_a_list(unflattened_list[0])
            l2 = flatten_a_list(unflattened_list[1:])

            return l1 + l2

        else:
            l1 = [unflattened_list[0]]
            l2 = flatten_a_list(unflattened_list[1:])

            return l1 + l2
