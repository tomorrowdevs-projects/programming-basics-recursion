def flatten_list(ls):
    flat_ls=[]
    for elem in ls:
        if type(elem)==list:
            flat_ls=flat_ls+flatten_list(elem)
        else:
            flat_ls.append(elem)
    return flat_ls

def main():
    while True:
        try:
            ls = eval(input("Please a valid list with one or more sublists (list syntax: [elem1,elem2,elem3]):"))
            break
        except SyntaxError:
            print("Wrong syntax! Try again!")
    flat_ls=flatten_list(ls)
    print("""Original list: {}\n\nFlattened list: {}""".format(ls,flat_ls))

if __name__=='__main__':
    main()