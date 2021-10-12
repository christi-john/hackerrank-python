# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    list1=[]
    for _ in range(N):
        command=input().split()
        if "insert" in command: list1.insert(int(command[1]),int(command[2]))
        elif "append" in command: list1.append(int(command[1]))
        elif "remove" in command: list1.remove(int(command[1]))
        if "sort" in command: list1.sort()
        if "pop" in command: list1.pop()
        if "reverse" in command: list1.reverse()
        if "print" in command: print(list1)