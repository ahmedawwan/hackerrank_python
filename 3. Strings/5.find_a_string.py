def count_substring(my_string, my_sub_string):
    my_counter = 0
    for i in range(len(my_string)):
        if i == my_string.find(my_sub_string, i, len(my_string)):
            my_counter += 1
    else:
        pass
    return my_counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
