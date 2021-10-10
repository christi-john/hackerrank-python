# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
  
    ans=""
    for i in line:
        if(i!=" "):ans=ans+i
        else:ans=ans+"-"
    return ans
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)