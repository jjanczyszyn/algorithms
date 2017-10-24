def quick_sort(arr):
  _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, first, last):
  if first < last:
      splitpoint = _partition(arr, first, last)
      _quick_sort(arr, first, splitpoint - 1)
      _quick_sort(arr, splitpoint + 1, last)


def _partition(arr, first, last):
  pivot_value = arr[first]
  left = first + 1
  right = last

  done = False
  while not done:
      while right >= left and arr[left] <= pivot_value:
          left += 1
      while right >= left and arr[right] >= pivot_value:
          right -= 1

      if right < left:
          done = True
      else:
          swap(arr, left, right)

  swap(arr, first, right)

  return right


def swap(arr, left, right):
  arr[left], arr[right] = arr[right], arr[left]
