def sum_of_numbers():
    number=input('Please, enter a number:')
    if number=='':
        return 0.0
    return float(number)+sum_of_numbers()

def main():
    count=sum_of_numbers()
    print(count)

if __name__='__main__':
    main()