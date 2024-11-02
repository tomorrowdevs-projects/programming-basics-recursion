'''
Write a recursive function that implements the run-length compression technique described in Run-Lenght Decoding Exercise. 

Your function will take a list or a string as its only argu- ment. It should return the run-length compressed list as its only result. 

Include a main program that reads a string from the user, compresses it, and displays the run-length
encoded result.

Hint: You may want to include a loop inside the body of your recursive function.
'''

def compression(array):
    if len(array) == 0:
        return []

    value = array[0]
    count = 1

    while count < len(array) and array[count] == value:
        count += 1

    return [value, count] + compression(array[count:])

def main():
    array = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
    compressed = compression(array)
    print(compressed)

if __name__ == "__main__":
    main()
