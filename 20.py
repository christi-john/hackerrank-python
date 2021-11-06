# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    list1=[]
    ans=0
    for _ in range(len(string)): list1.append(string[_:_+len(sub_string)])
    for i in list1: 
        if(i==sub_string): ans+=1
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)