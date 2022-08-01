import re

cards = ["AAA","CNCC", "MMKK"]
WORDS = ["MMNA"]
def solution(card, words):
    ans = []
    # 1. Brute Force
    for word in words :
        c = card 
        ok = [0,0,0]
        for w in word :
            print(w)
            found = 0  
            for i in range(3) : 
                if w in c[i] :  
                    ok[i] = 1
                    found = 1
                    c[i] = re.sub(w, "_", c[i],1) ########### 차이? c[i].replace(w, "_", 1) 
                    print(c[i])
            if found == 0 :
                break;
        if 0 in ok :
            continue;
        ans.append(word)
    print(ans)
    if len(ans) == 0 :
        return ["-1"]
    return ans
solution(cards,WORDS)
## What was the problem
