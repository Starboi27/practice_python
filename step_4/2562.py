a = []
for x in range(9):
    a.append(int(input()))
    # 첫 시도 때 for문에 a = list(map(...))을 썼음
    # 이유는 입력 받을 때 마다 변수가 덮어질지 몰랐음
    # 1줄씩 변수를 입력 받을 땐 append함수 쓰기

print(max(a))
print(a.index(max(a)) + 1)
# count는 list에 value값이 총 몇 개 있는지 반환
# index는 list에 value값이 어느 위치에 값 반환
# 슬라이스 기능을 통해 입력받은 9개 까지만 입력 가능 [:9]
