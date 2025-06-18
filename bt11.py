## Bài tập 11: Tìm chuỗi con không tăng dài nhất trong một mảng
def longest_non_increasing_subsequence(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1

    return max_len

# Ví dụ sử dụng
arr = [5, 4, 4, 3, 6, 2, 1, 1, 0]
print("Cách 1:", longest_non_increasing_subsequence(arr))
#cách 2:
from itertools import pairwise

def longest_non_increasing_subsequence_builtin(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for prev, curr in pairwise(arr):
        if curr <= prev:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len

# Ví dụ sử dụng
arr = [5, 4, 4, 3, 6, 2, 1, 1, 0]
print("Cách 2:", longest_non_increasing_subsequence_builtin(arr))

