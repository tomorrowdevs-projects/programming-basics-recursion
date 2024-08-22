def edit_distance(str1,str2):
    if len(str1)==0 or len(str2)==0:
        dist=max(len(str1),len(str2))
        return dist
    else:
        len1=len(str1)
        len2=len(str2)
        if len1>len2:
            dist=len1-len2
            str1=str1[:len1-1-dist]
            str2=str2[:len2-1]
        elif len1<len2:
            dist=len2-len1
            str1=str1[:len1-1]
            str2=str2[:len2-1-dist]
        else:
            if str1[-1]!=str2[-1]:
                dist=1
                str1=str1[:len1-1]
                str2=str2[:len2-1]
            else:
                dist=0
                str1=str1[:len1-1]
                str2=str2[:len2-1]
        return dist+edit_distance(str1,str2)

def main():
    str1=input('Enter the first string to compare:')
    str2=input('Enter the second string to compare:')
    dist=edit_distance(str1,str2)
    print('The edit distance between the string you have input is {} characters'.format(dist))

if __name__=='__main__':
    main()