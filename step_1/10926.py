def exclamation(joona):
    print(f"{joona}??!")


joona = input().replace(" ", "")
exclamation(joona)

# split()은 공백을 뺴주는 게 아님
# 공백을 기준으로 쪼개서 리스트를 생성
# ['j', 'oon']이런식으로
