# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations
S,k=map(str,input().split())

for i in range(1,int(k)+1):
    for j in (list(combinations(sorted(S), int(i)))):
        ans=""
        for k in j: ans=ans+k
        print(ans)