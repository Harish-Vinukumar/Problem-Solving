import numpy as np

list1 = [2, 4]
list2 = np.array([16, 51 , 96])

def getTotalX(a, b):
    # Write your code here
    res_list = []

    for x in a:
        res_list.append(list(b % x))

    for i in range(len(res_list)-1):
        for j in range(i+1, len(res_list)):
            if res_list[i] == res_list[j]:
                return len(res_list[i])
            elif res_list[i].count(0) == res_list[j].count(0):
                return res_list[i].count(0)

print(getTotalX(list1, list2))
