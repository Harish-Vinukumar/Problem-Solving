def main():
    club1 = int(input())
    s1 = list(map(int,input().strip().split()))[:club1]
    club2 = int(input())
    s2 = list(map(int,input().strip().split()))[:club2]
    A = set(s1)
    B = set(s2)
    C = A.__or__(B)
    count = len(C)
    print(count,end='')