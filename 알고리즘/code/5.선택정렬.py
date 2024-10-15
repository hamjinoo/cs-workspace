def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
         min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr


# 예시
arr = [64, 25, 12, 22, 11]
print("정렬 전:", arr)
sorted_arr = selection_sort(arr)
print("정렬 후:", sorted_arr)