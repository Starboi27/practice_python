n = int(input())
count = 0

for _ in range(n):
    string = set()
    prev = ""
    is_group = True
    char = input()
    for x in char:
        if x != prev:
            if x in string:
                is_group = False
                # 이전 문자와 달라졌는데, 이미 나온 적 있는 문자일 때
            string.add(x)
        prev = x
    if is_group:
        count += 1

print(count)