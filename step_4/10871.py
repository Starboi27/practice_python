a, b = map(int, input().split())
n = list(map(int, input().split()))

min_list = []
# n리스트에 있는 b보다 작은 수를 새로운 리스트에 넣고 프린트할려고 헀음
for x in range(a):
    if n[x] < b:
        # n리스트에 있는 요소로 b보다 작은 값을 구하려고 코드 짬
        min_list.append(n[x])
        # 처음엔 min_list.append(x) 했음 이랬더니 b보다 작은 값의 index 넘버가 출력 됨
        # 그래서 n[x] n리스트의 요소로 코드 변경 함
print(*min_list)
