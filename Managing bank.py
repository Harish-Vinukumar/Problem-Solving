def main():
    num = int(input())
    lists = [int(x) for x in input().split()][:num]

    print(len(set(lists)), end='')


main()