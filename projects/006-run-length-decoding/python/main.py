def decode_compressed_list(comp_ls):
    if len(comp_ls)>0:
        elem=comp_ls[0]
        comp_ls.remove(comp_ls[0])
        num=comp_ls[0]
        comp_ls.remove(comp_ls[0])
        return [elem]*num+decode_compressed_list(comp_ls)
    else:
        return []

def main():
    StructureIsWrong=True
    while StructureIsWrong:
        SyntaxIsWrong=True
        while SyntaxIsWrong:
            try:
                comp_ls=eval(input('Please, enter a string of this type [string,integer,string,integer...]: '))
                SyntaxIsWrong=False
            except SyntaxError:
                print("Wrong list syntax, retry!")
        
        StructureIsWrong=False
        if len(comp_ls)%2>0:
            StructureIsWrong=True
        else:
            strings=comp_ls[0:2:]
            ints=comp_ls[1:2:]
            for i,j in zip(strings,ints):
                if not (type(i)==str and type(j)==int):
                    StructureIsWrong=True

    ls=comp_ls.copy()
    decomp_list=decode_compressed_list(ls)
    print('Compressed list: {}\n\nDecompressed list: {}'.format(comp_ls,decomp_list))

if __name__=='__main__':
    main()