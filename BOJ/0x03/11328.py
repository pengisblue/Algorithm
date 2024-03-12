def Strfry(in_text1, in_text2):
    alpha = [0]*26
    possible = True
    if len(in_text1) != len(in_text2):
        return 'Impossible'
    for chr in in_text1:
        index = ord(chr) - 97
        alpha[index] += 1
    for chr in in_text2:
        index = ord(chr) - 97
        alpha[index] -= 1
        if alpha[index] < 0:
            possible = False
            break
    if possible:
        return 'Possible'
    else:
        return 'Impossible'


N = int(input())
for i in range(N):
    text1, text2 = input().split()
    print(Strfry(text1, text2))