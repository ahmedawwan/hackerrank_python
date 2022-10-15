if __name__ == '__main__':
    list_scores = []
    nested_list = []
    list_names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
        list_scores.append(score)

    list_scores = list(dict.fromkeys(sorted(list_scores)))
    for x, y in nested_list:
        if list_scores[1] == y:
            list_names.append(x)

    list_names.sort()
    for i in list_names:
        print(i)

