import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline


sticks = input()
stack = []
cut = 0
for idx, stick in enumerate(sticks):
    if stick == '(':
        stack.append(stick)
    elif stick == ')':
        if sticks[idx-1] == '(':
            stack.pop()
            cut += len(stack)
        else:
            stack.pop()
            cut += 1

print(cut)
