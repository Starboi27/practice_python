s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

for char in alpha:
    # char in alpha는 alpha에 있는 값을 순서대로 호출
    print(s.find(char), end=" ")
    """
    s에서 찾는 다 뭘? char를
    char이 뭔데? a~z까지 알파벳
    end = " "은 출력 결과가 띄어쓰기 한 칸을
    수행 하는 게 아니라 오른쪽 나란히 붙게 된다
    """
