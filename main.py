# mergeSort
# python
def mergeSort(List):
  def merge(List_a, List_b):
    'merge two Lists have sorted'
    if len(List_a) == 0 or len(List_b) == 0:
      return List_a+List_b
    elif List_a[0] < List_b[0]:
      return List_a[0:1] + merge(List_a[1:], List_b)
    else:
      return List_b[0:1] + merge(List_a, List_b[1:])
  
  # baseline conditions
  if len(List) == 1:
    return List
  mid = int(len(List)/2)
  List_a = List[0:mid]
  List_b = List[mid:]
  List_a = mergeSort(List_a)
  List_b = mergeSort(List_b)
  return merge(List_a, List_b)
