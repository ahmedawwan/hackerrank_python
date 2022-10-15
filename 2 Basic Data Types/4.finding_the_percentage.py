if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        names, *line = input().split()
        scores = list(map(float, line))
        student_marks[names] = scores
    query_name = input()
    scores_sum = 0.0
    for student_name in student_marks:
        if student_name == query_name:
            for i in student_marks[student_name]:
                scores_sum += i
    print("%.2f" % round(scores_sum / 3, 2))
