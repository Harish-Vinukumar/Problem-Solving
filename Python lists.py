def main():
    num = int(input())
    input_list = [input().split() for x in range(num)]
    res_list = list()
    final_res =list()
    for x in input_list:
        var = list()
        if int(x[0]) == 1 and len(x) > 1:
            res_list.append(x[1])
        elif int(x[0]) == 2:
            var = res_list.copy()
            final_res.append(var)
    for i in range(len(final_res)):
        if i == len(final_res)-1:
            print(final_res[i], end='')
        else:
            print(final_res[i])
main()