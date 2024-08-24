def text_compression(text):
    comp_txt_ls=[]
    comp_txt_ls.append(text[0])
    comp_txt_ls.append(0)
    for i in range(len(text)):
        if text[i]==text[0]:
            comp_txt_ls[1]+=1
        else:
            return comp_txt_ls+text_compression(text[i:])
    
    if len(text)==1:
        return comp_txt_ls

def main():
    text=input('Please, enter a text to be compressed:')
    comp_txt_ls=text_compression(text)
    print('Text: {}\nCompressed text: {}'.format(text,comp_txt_ls))

if __name__=='__main__':
    main()