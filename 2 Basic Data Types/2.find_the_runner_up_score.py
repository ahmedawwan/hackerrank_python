if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr, reverse=True)
    arr = list(dict.fromkeys(arr))
    print(arr[1])
