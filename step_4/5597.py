arr = list(range(1, 31))

arr_2 = []
for x in range(28):
    arr_2.append(int(input()))

total_arr = sorted(set(arr) - set(arr_2))
"""
sort 함수는 in-place연산을 하여 total_arr.sort()를 하고
다시 total_arr를 출력해야 정렬된 arr이가 출력되는 반면
sorted() 함수는 out-of-place연산을 하여 원본 데이터를 다시
출력할 필요 없이 바로 출력 가능
"""
"""
첫 시도에는 list-list를 시도 했음
list로 연산이 불가능 하다는 걸 깨닫고 집합으로 변환 후 연산 시도
"""
print(total_arr[0])
print(total_arr[1])
