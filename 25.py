# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement
S,k=map(str,input().split())
for i in list(combinations_with_replacement(sorted(S),int(k))):
    ans=""
    for j in i:
        ans=ans+j
    print(ans)