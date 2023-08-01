A, B, V = map(int,input().split())

if A == V:
    day = 1
else:
    up = (V - A)//(A - B)
    if  