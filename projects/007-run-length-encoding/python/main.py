def textCompression(text,compressedText=None):
    if compressedText==None:
        compressedText=[]

    if len(text)>0:
        if type(text)==list:
            currentElem=text.pop(0)
        else:
            currentElem=text[0]
            text=text[1:]
        if not currentElem in compressedText:
            compressedText.append(currentElem)
            compressedText.append(1)
        else:
            charIndex=compressedText.index(currentElem)
            compressedText[charIndex+1]+=1
        return textCompression(text,compressedText)
    else:
        return compressedText

def main():
    text=input('Please, enter a text to be compressed:')
    compressedText=textCompression(text)
    print('Text: {}\nCompressed text: {}'.format(text,compressedText))

if __name__=='__main__':
    main()