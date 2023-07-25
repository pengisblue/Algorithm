def anagram(in_text1, in_text2):
    alpha = [0] * 26
    for chr in in_text1:
        index = ord(chr) - 97
        alpha[index] += 1
    for chr in in_text2:
        index = ord(chr) - 97
        alpha[index] -= 1
    delete = sum(list(map(abs,alpha)))
    return delete

text1 = input()
text2 = input()
print(anagram(text1, text2))