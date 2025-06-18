#cách 1: Sử dụng vòng lặp để tìm độ dài của chuỗi số có dấu hiệu luân phiên
def max_alternating_sign_length(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] * arr[i - 1] < 0:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1

    return max_len

# Ví dụ sử dụng:
arr = [1, -2, 3, -4, 5, 6, -1]
print("Cách 1:", max_alternating_sign_length(arr))
# Cách 2: Sử dụng hàm pairwise để nhóm các số có dấu hiệu luân phiên và tìm nhóm dài nhất
from itertools import pairwise
def max_alternating_sign_length_pairwise(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for a, b in pairwise(arr):
        if a * b < 0:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len
# Ví dụ sử dụng:
print("Cách 2:", max_alternating_sign_length_pairwise(arr))
