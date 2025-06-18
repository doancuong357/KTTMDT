from itertools import groupby
# viết hàm tính số lượng các số dương liên tiếp có tổng lớn nhất
def max_positive_sum_length(arr):
    max_sum = 0
    current_sum = 0
    max_len = 0
    current_len = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            current_sum += arr[i]
            current_len += 1
            if current_sum > max_sum:
                max_sum = current_sum
                max_len = current_len
            elif current_sum == max_sum and current_len > max_len:
                max_len = current_len
        else:
            current_sum = 0
            current_len = 0
    return max_len
# Ví dụ sử dụng:
arr = [1, 2, -1, 3, 4, 2, -2, 5, 6, 1]
print("Cách 1:", max_positive_sum_length(arr))
# Cách 2: Sử dụng hàm groupby để nhóm các số dương liên tiếp và tìm nhóm có tổng lớn nhất
def max_positive_sum_length_groupby(arr):
    max_len = 0
    for key, group in groupby(arr, lambda x: x > 0):
        if key:  # Chỉ xử lý nhóm các số dương
            current_group = list(group)
            current_sum = sum(current_group)
            current_len = len(current_group)
            if current_sum > max_len:
                max_len = current_len
            elif current_sum == max_len and current_len > max_len:
                max_len = current_len
    return max_len
# Ví dụ sử dụng:
print("Cách 2:", max_positive_sum_length_groupby(arr))