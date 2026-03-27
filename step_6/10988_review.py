char = input()
n = len(char)
is_palindrome = 1

for x in range(n // 2):
    if char[x] != char[n - x - 1]:
        """
        앞과 뒤를 검사하기 위해 n//2 절반만 구함
        그리고 char[x] 앞에 와 char[n-x-1] 뒤 검사 시작
        """
        is_palindrome = 0
        """
        if char[x] == char[n - x - 1]:
        is_palindrome = 1
        이렇게 안 하는 이유는 처음 앞 뒤 검사는 맞을 수도 있겠지만
        두 번째 세 번째 검사에 대칭성이 깨진다면 다시 밑에 is_palindrome = 0
        을 써줘야 된다 굳이?
        그래서 검사 기준을 틀릴 때로 잡아 코드 남용 방지
        """

print(is_palindrome)
