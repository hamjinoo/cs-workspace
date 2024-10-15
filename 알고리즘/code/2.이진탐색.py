

def binary_search(arr, target):
    low = 0 # 인덱스 0으로 초기화한다.
    high = len(arr) - 1 # 배열의 마지막 인덱스
    
    while low <= high: # 탐색 범위를 좁혀가는 과정입니다.
        mid = (low + high) // 2 # 배열의 중간 인덱스를 구합니다.
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
        
        
        

# 예시 (정렬된 리스트)
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"{target}을(를) {result}번째 위치에서 찾았습니다.")
else:
    print(f"{target}을(를) 찾지 못했습니다.")
    
    
    
# 1. low = 0 / height 5
# 2. 5 / / 2 = 2
# 3. arr[2] = 5가 되고 타겟(7)보다 작으니까 low = mid(2) + 1 = 3
# 4. 이제 low = 3, height = 5가 된다.
# 5. mid = 3 + 5 = 8 // 2 = 4
# 6. arr[4] = 9
# ... 이런 식으로 작업