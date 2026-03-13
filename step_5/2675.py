t = int(input())

for x in range(t):
    r, s = map(str, input().split())
    for char in s:
        print(char*int(r),end="",)
    print()
    """
    print("\n")을 하면 \n줄바꿈 print()줄바꿈
    총 2번의 줄바꿈이 일어난다
    의도적으로 줄바꿈을 1번 하고 싶다면 print()만
    사용하자
    """ 
