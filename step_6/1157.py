n = input().upper()
max, count = 0, 1
result_word = ""

for char in set(n):
    # set함수는 중복된 원소를 하나의 원소로 변환
    count = n.count(char)
    """
    AAB를 검사한다 했을 때 set에 의해 AB가 char에
    하나씩 저장 되고 n변수에 count(A), count(B)를 해
    A원소가 몇 개인지, B원소가 몇 개인지 탐색한다
    n에 A가 더 많으니까 count변수에 2가 저장
    """
    if count > max:
        max = count
        # max에 2가 저장 됨
        result_word = char
    elif count == max:
        result_word = "?"

print(result_word)
