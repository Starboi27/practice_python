# N은 바구니 갯 수, M은 공을 튀길 횟 수
# 2번 째 i, j, k는 i~j 바구니 까지 k번호의 공을 넣는다
# 출력은 현재 바구니에 몇번 공이 있는지
n, m = map(int, input().split())
list = [0] * n
# 슬라이싱을 하려면 리스트에 값을 채워야 한다
for x in range(m):
    i, j, k = map(int, input().split())
    list[i - 1 : j] = [k] * (j - i + 1)
    # 슬라이싱을 하려면 우변은 리스트여야 한다
    # [k] * (j - i + 1)는 k번 공을 list에 j-i번 공을 넣은다
    # ex) i=2, j=4, k=9일 때 2, 3, 4바구니에 k를 3번 넣어야 되니까
    # j-i+1해주면 3이 나옴 그리고 list[1:4] = 1~3까지 k를 저장한다
print(*list)

# list[i - 1 : j] = [k] * (j - i + 1)이거 대신
"""
for b in range(i-1,j):
    arr[b] = k
"""
# 이렇게도 가능
