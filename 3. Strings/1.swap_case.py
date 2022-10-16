def swap_case(string):
    newString = ''
    for element in string:
        if element.isupper():
            newString += element.lower()
        elif element.islower():
            newString += element.upper()
        else:
            newString += element
    return newString


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
