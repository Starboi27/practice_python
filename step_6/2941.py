croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

n = input()
count = 0

for char in croatia:
    n = n.replace(char, "*")
    """
    문자열 객체에 속한 메서드이다
    str.replace(old, new, count)
    old : 찾을 문자열, 필수
    new : 대체할 문자열, 필수
        - new에 문자열의 길이에 따리 묶어서 비교함
    count : 교체할 최대, 횟수 선택
    """

print(len(n))
