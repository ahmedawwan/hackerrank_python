if __name__ == '__main__':
    my_string = input()
    is_alpha_num = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False

    for element in my_string:
        if element.isalnum():
            is_alpha_num = True
        if element.isalpha():
            is_alpha = True
        if element.isdigit():
            is_digit = True
        if element.islower():
            is_lower = True
        if element.isupper():
            is_upper = True

    print(is_alpha_num)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)
