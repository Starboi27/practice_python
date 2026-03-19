def trans_year(buddhist_era):
    anno_domini = buddhist_era - 543
    print(anno_domini)

buddhist_era = int(input())
trans_year(buddhist_era)

#map함수는 객채로 결과를 반환함 그래서 한번 변환
#map은 각 글자에 함수를 적용
#,는 안에 있는 값을 꺼낼 때 쓰는 파이썬 문법
#split은 공백이 있으면 공백 기준 "12 34" → ["12", "34"],
#공백이 없으면 "1234" → ["1234"] 일단은 리스트로 반환해 준다로 이해
