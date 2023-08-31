import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
pocket_dic = {}
num_dic = {}
for i in range(1, N+1):
    pocketmon = input().rstrip()
    pocket_dic[pocketmon] = i
    num_dic[i] = pocketmon

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(num_dic[int(question)])
    else:
        print(pocket_dic[question])
