a = list(map(int, input().split()))
# 어처피 두 수를 비교하는 거니까 굳이 리스트 사용할 이유 없었음
# a, b = map(int, input().split())으로 2개의 변수에 숫자 비교했으면 됐음

if a[0] > a[1]:
    print(">")
elif a[0] < a[1]:
    print("<")
else:
    print("==")
