while True:
    push = input()
    if push == '0 0':
        break
    else:
        A, B = map(int, push.split())
        if A % B == 0:
            print('multiple')
        elif B % A == 0:
            print('factor')
        else:
            print('neither')
