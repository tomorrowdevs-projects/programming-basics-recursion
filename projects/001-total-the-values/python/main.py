'''
Write a program that reads values from the user until a blank line is entered.   
Display the total of all the values entered by the user (or 0.0 if the first value entered is a blank line).   
Complete this task **using recursion**.  
Your program may not use any loops.

Hint: The body of your recursive function will need to read one value from the user, 
and then determine whether to make a recursive call.  
Your function does not need to take any arguments, but it will need to return a numeric result.
'''

def newvalue(uservalue, m):
    uservalue = int(input("Please input a value: "))
    n = int(uservalue)
    l = n + m
    m = l
    print(l)
    newvalue(uservalue, m)

def main():
    uservalue = 0
    m = 0
    newvalue(uservalue, m)

if __name__ == '__main__':
    main()