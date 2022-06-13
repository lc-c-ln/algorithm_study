from itertools import combinations
def solution(N,K):
    #  K개의 1로 이루어진 N 자릿수로 이루어진 이진수 중 3의 배수의 개수
    li = [1,2] * ((N // 2) +1)
    combi = list(combinations([i for i in range(N)],K))
    for i in combi :
        sum = 0
        for j in i :
            sum += li[j]
    print(combi)
solution(10,6)
