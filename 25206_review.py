grade_point = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0,
}

total_credit = 0
total_score = 0

for _ in range(20):
    class_name, credit, grade = input().split()
    if grade == "P":
        continue
        """ 
        continue는 if문에 조건에 부합하고 continue가
        실행됐을 때 밑에 코드로 가는 걸 막고 다시 위 코드
        를 실행한다
        """
    total_credit += float(credit)
    total_score += float(credit) * grade_point[grade]
    # 딕셔너리에 있는 값을 grade_point[grade] 추출 할 수 있다

print(f"{total_score / total_credit:.6f}")
# f-string 으로 : 형식 지정하고 .소수점 2f 번재 까지 출력
"""
GAP(Grade Average Point) : 총평점 / 총학점으로 구할 수 있다
"""
