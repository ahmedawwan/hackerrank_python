def swap_case(string):
    new_string = ''
    for element in string:
        if element.isupper():
            new_string += element.lower()
        elif element.islower():
            new_string += element.upper()
        else:
            new_string += element
    return new_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
