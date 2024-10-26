'''
Write a recursive function that converts a non-negative decimal number to binary.

Treat 0 and 1 as base cases which return a string containing the appropriate digit. 

For all other positive integers, n, you should compute the next digit using the remainder operator and then 
make a recursive call to compute the digits of n // 2.

Finally, you should concatenate the result of the recursive call (which will be a string) 
and the next digit (which you will need to convert to a string) and return this string as the result of the function.
 
Write a main program that uses your recursive function to convert a non-negative integer 
entered by the user from decimal to binary. 
Your program should display an appropriate error message if the user enters a negative value.
'''

def conv(intuserinput, r, array):
    if intuserinput == 0 or intuserinput == 1:
        array.append(intuserinput)
        array.reverse()
        return array
    elif intuserinput < 0:
        print("ERROR: Insert non-negative number!!!")
        intuserinput = int(input("Please insert a non-negative decimal number: "))
        return conv(intuserinput, r, array)
    elif intuserinput > 0:
        r = intuserinput % 2
        intuserinput = intuserinput // 2
        array.append(r)
        return conv(intuserinput, r, array)

def main():
    userinput = input("Please insert a non-negative decimal number: ")
    intuserinput = int(userinput)
    r = 0
    array = []
    x = conv(intuserinput, r, array)
    print(x)

if __name__ == '__main__':
    main()