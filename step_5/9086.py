t = int(input())

a = []
for x in range(t):
    a.append(input())

for x in range(t):
    print(a[x][0] + a[x][len(a[x]) - 1])
    """
    a[x][len(a[x]) - 1]를 a[x][-1]로 도 가능하다
    """

