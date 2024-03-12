S = input()
cnt_alpha = [0] * 26
for i in S:
    index = ord(i) - 97
    cnt_alpha[index] += 1
print(*cnt_alpha)