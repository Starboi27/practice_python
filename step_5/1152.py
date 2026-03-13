
"""
s = input().split()

split()은 공백을 기준으로 리스트 생성
공백이 없을 땐 단일 리스트 생성

print(len(s))
"""

s = input()

if s == "":
    print(0)
else:
    print(s.count(" ")+1)
"""
count() 함수는 내가 타겟한 값을
내부적으로 반복해 찾은 후 그 값을 정수로
반환한다
"""