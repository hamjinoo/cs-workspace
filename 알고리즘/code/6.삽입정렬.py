def insertion_sort(arr):
  for i in range(1, len(arr)): # 두 번째 요소부터 시작
    key = arr[i] # 현재 삽입될 요소
    j = i - 1 # 비교를 시작할 위치
    while j >= 0 and key < arr[j]: # 적절한 위치를 찾을 때까지
      arr[j + 1] = arr[j] # 요소를 오른쪽으로 이동
      j -= 1
    arr[j + 1] = key # 삽입 위치에 key를 저장
  return arr


# 예시
arr = [12, 11, 13, 5, 6]
print("정렬 전:", arr)
sorted_arr = insertion_sort(arr)
print("정렬 후:", sorted_arr)