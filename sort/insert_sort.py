def insert_sort(arr):
  for i in range(1, len(arr)):
    j = i - 1
    print(j)
    ele = arr[i]
    while arr[j] > ele and j >= 0:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = ele
  return arr

lst = [9981, 3333, 5123, 1243, 7412]
print(insert_sort(lst))