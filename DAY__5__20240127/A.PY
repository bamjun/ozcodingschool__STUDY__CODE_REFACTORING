def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            row.append(sum)
        result.append(row)
    return result


# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
# 입력 데이터
arr1_lists = [[[1, 4], [3, 2], [4, 1]], [[2, 3, 2], [4, 2, 4], [3, 1, 4]]]
arr2_lists = [[[3, 3], [3, 3]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]]
expected_results = [
    [[15, 15], [15, 15], [15, 15]],
    [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
]

# 각 경우에 대해 solution 함수를 실행하고 결과를 확인
for i in range(len(arr1_lists)):
    valueSolution = solution(arr1_lists[i], arr2_lists[i])
    is_correct = valueSolution == expected_results[i]
    print(f"Case {i+1}: {is_correct}")
    print(f"V{i+1} : {valueSolution} \n\n")
