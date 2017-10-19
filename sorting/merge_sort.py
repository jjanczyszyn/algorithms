def merge_sort(arr):
	helper = [None] * len(arr)
	_merge_sort(arr, helper, 0, len(arr) - 1)


def _merge_sort(arr, helper, low, high):
	if low < high:
		middle = (low + high) // 2

		_merge_sort(arr, helper, low, middle)
		_merge_sort(arr, helper, middle + 1, high)
		_merge(arr, helper, low, middle, high)


def _merge(arr, helper, low, middle, high):
	for i in range(low, high + 1):
		helper[i] = arr[i]

	current = low
	left_index = low
	right_index = middle + 1
	
	while left_index <= middle and right_index <= high:
		if helper[left_index] <= helper[right_index]:
			arr[current] = helper[left_index]
			left_index += 1

		else:
			arr[current] = helper[right_index]
			right_index += 1

		current +=1

	while left_index <= middle: 
		arr[current] = helper[left_index]
		left_index += 1
		current +=1
