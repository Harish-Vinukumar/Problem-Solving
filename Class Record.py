''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    num = int(input())
    string1 = [x for x in input().split()]
    string2 = [x for x in input().split()]
    list1 = [int(x) for x in string1[1:]]
    list2 = [int(x) for x in string2[1:]]
    res_list = ['{:.2f}'.format(((a + b) / 2)) for a, b in zip(list1, list2)]

    for i in range(len(res_list)):
        if i == len(res_list) - 1:
            print(res_list[i], end='')
        else:
            print(res_list[i], end=' ')


# Write code here

main()

