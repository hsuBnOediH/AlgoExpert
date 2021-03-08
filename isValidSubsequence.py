# https://www.algoexpert.io/questions/Validate%20Subsequence
# 带顺序的 双指针问题
# 搞清楚 a 和 b
# 过滤目标, 最后检测也是检测目标
def isValidSubsequence(array, sequence):
    arr_len = len(array)
    seq_len = len(sequence)
    arr_idx = 0
    seq_idx = 0
    while arr_idx < arr_len and seq_idx < seq_len:
        if sequence[seq_idx] == array[arr_idx]:
            arr_idx += 1
            seq_idx += 1
        else:
            arr_idx += 1
    return seq_idx == seq_len
