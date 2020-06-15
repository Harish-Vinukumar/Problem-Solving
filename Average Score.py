def main():
    num = int(input())
    lists = [input().strip().split() for i in range(num)]
    player = input()

    name_list = [x[0] for x in lists]
    score_list = [x[1:] for x in lists]
    new_score_list = list()
    for x in score_list:
        temp_list = list()
        for y in x:
            temp_list.append(int(y))
        new_score_list.append(temp_list)
    score_dict = {}

    for i in range(len(name_list)):
        score_dict[name_list[i]] = new_score_list[i]

    print("{:.2f}".format(sum(score_dict[player])/3))

main()