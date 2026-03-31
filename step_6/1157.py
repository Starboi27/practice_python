n = input().upper()
max = 0
string = ""
# 현재 단어 보관 용도

for char in set(n):
    counter = n.count(char)
    # count 함수는 요소의 갯수를 알려준느 역할을 함
    # 인덱스 넘버를 알려주는 거라고 착각함
    if counter > max:
        string = char
        max = counter
    elif counter == max:
        string = "?"

print(string)
