chess_pice = [1, 1, 2, 2, 2, 8]
current_pice = list(map(int, input().split()))
# 리스트끼리 사직연산은 불가능 [1, 2] + [3, 4] = [1, 2, 3, 4]가 됨
new_pice = []
for x in range(len(chess_pice)):
    # for문 in 뒤에는 반복 가능한 객채가 위치해야 한다
    new_pice.append(chess_pice[x] - current_pice[x])
print(*(new_pice))