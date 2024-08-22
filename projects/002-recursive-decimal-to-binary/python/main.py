def dec_to_bin(number):     
    if number<2:
        digit_str=str(number)
    return dec_to_bin(number//2)+str(number%2)

def main():
    number=input('Please, enter a decimal number to convert in binary system:')
    while not number.isdigit():
        number=input('Only numerical input:')
    number=int(number)
    print(dec_to_bin(number))

if __name__=='__main__':
    main()