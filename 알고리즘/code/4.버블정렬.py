# 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 서로 교환
    return arr

  
  
# 예시
arr = [64, 34, 25, 12, 22, 11, 90]
print("정렬 전:", arr)
sorted_arr = bubble_sort(arr)
print("정렬 후:", sorted_arr)