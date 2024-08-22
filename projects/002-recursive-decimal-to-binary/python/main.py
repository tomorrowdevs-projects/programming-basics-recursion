def dec_to_bin(number):
    if number==0:
        return '0'
    elif number==1:
        return '1'
    else:
        return dec_to_bin(number//2)+str(number%2)
    
def main():
    number=input('Please, enter the decimal number to be converted in binary system:')
    while not number.isdigit():
        number=input('Only decimal numebes:')
    number=int(number)
    binary_str=dec_to_bin(number)
    print('The decimal number {} corresponds to {} in binary system.'.format(number,binary_str))

if __name__=='__main__':
    main()