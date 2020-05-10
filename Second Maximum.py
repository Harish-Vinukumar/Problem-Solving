''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT


def main():
    num = int(input())
    lists = [input() for i in range(num * 2)]
    name_list, score_list = list(), list()
    for i in range(len(lists)):
        if i % 2 == 0:
            name_list.append(lists[i])
        else:
            score_list.append(int(lists[i]))

    name_dict = dict()

    for i in range(len(name_list)):
        name_dict[name_list[i]] = score_list[i]

    new_score_list = list(filter(lambda a: a != max(score_list), score_list))

    res_list = [k for k, v in name_dict.items() if v == max(new_score_list)]
    res_list = sorted(res_list)
    # [print(res_list[x].strip()) for x in range(len(res_list)-1)]
    # print(res_list[-1], end='')
    for x in range(len(res_list)):
        if x == len(res_list) - 1:
            print(res_list[x], end='')
        else:
            print(res_list[x])

main()

