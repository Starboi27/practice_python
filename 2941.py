croatia = ["c=", "dz=", "d-", "lj", "nj", "s=", "z="]

n = input()

for char in croatia:
    n = n.replace(char, "*")
    # replace 함수의 old자리에는 배열이 올 수 없음
    """
    n을 각 반복마다 갱신해야 누적 적용 됨
    sum += 1 과 같은 로직
    """

print(len(n))
