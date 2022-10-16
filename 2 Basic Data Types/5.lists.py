if __name__ == '__main__':

    # sample inputs
    input_insert = 'insert'
    input_print = 'print'
    input_remove = 'remove'
    input_append = 'append'
    input_sort = 'sort'
    input_pop = 'pop'
    input_reverse = 'reverse'

    # lists
    my_list = []
    command_list = []

    # functions
    def function_insert():
        my_list.insert(int(command_list[1]), int(command_list[2]))

    def function_print():
        print(my_list)

    def function_remove():
        my_list.remove(int(command_list[1]))

    def function_append():
        my_list.append(int(command_list[1]))

    def function_sort():
        my_list.sort()

    def function_pop():
        if my_list:
            my_list.pop()

    def function_reverse():
        my_list.reverse()

    N = int(input())

    for _ in range(0, N):
        command_list = str(input()).split(' ')
        command_list = [command_list[0]] + list(map(int, command_list[1:]))
        command = str(command_list[0])
        if command == input_insert:
            function_insert()
        elif command == input_print:
            function_print()
        elif command == input_remove:
            function_remove()
        elif command == input_append:
            function_append()
        elif command == input_sort:
            function_sort()
        elif command == input_pop:
            function_pop()
        elif command == input_reverse:
            function_reverse()
