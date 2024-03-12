import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def is_palindrome(s, idx, cnt):
    # 재귀 횟수가 문자열 길이의 절반을 넘어가면 palindrome
    if cnt > (N//2):
        return 1, cnt
    # 문자가 서로 다르면 종료
    if s[idx] != s[N-1-idx]:
        return 0, cnt
    # 문자가 서로 같으면 다음 문자 탐색
    else:
        return is_palindrome(s, idx+1, cnt+1)


T = int(input())
for tc in range(T):
    S = input().rstrip()
    N = len(S)
    print(*is_palindrome(S, 0, 1))
