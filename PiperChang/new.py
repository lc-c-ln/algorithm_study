def solution(s):
    l = int(len(s) / 2) + 1
    answer = len(s)
    for i in range(1,l) : # 자르는 기준 
        string = s[:i] # i 길이의 문자열
        repeat = 1
        minlen = ''
        idx = 0
        for idx in range(i,len(s)+i,i) :
            if string == s[idx:idx+i] :
                repeat += 1
            else :
                if repeat > 1 :
                    minlen += str(repeat) + '()' + string
                else :
                    minlen += string
                string = s[idx:idx+i]
                repeat = 1
        # print(minlen)
        answer = min(answer, len(minlen)) 
    return answer
s = input()
solution(s)