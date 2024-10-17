def flatten_list(origin_lst,flat_lst=None):
    if flat_lst==None:
        flat_lst=[]

    if len(origin_lst)>0:
        temp_lst=origin_lst.pop(0)
        if type(temp_lst)==list:
            flat_lst=flat_lst+flatten_list(temp_lst)
            return flatten_list(origin_lst,flat_lst)
        else:
            flat_lst.append(temp_lst)
            return flatten_list(origin_lst,flat_lst)
    else:
        return flat_lst

def main():
    while True:
        try:
            original_lst = eval(input("Please a valid list with one or more sublists (list syntax: [elem1,elem2,elem3]):"))
            break
        except SyntaxError:
            print("Wrong syntax! Try again!")
    lst=original_lst.copy()
    flat_lst=flatten_list(lst)
    print("""Original list: {}\n\nFlattened list: {}""".format(lst,flat_lst))

if __name__=='__main__':
    main()