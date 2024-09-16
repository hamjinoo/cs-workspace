def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 예시
arr = [5, 3, 7, 1, 9, 4]
target = 7
result = linear_search(arr, target)
if result != -1:
    print(f"{target}을(를) {result}번째 위치에서 찾았습니다.")
else:
    print(f"{target}을(를) 찾지 못했습니다.")
    