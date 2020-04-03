def selection_sort(list):
  for i in range(len(list)):
    min = i
    for j in range(i + 1, len(list)):
      if list[min] > list[j]:
        min = j
    list[i], list[min] = list[min], list[i]
  return list

list = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
print(selection_sort(list))