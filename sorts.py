
def selection_sort(seq):
    selection_comparisons = 0
    length = len(seq)
    for bottom in range(length-1):
        min_ind = bottom
        for el_1 in range(bottom + 1, length):
            selection_comparisons += 1
            if seq[el_1] < seq[min_ind]:
                min_ind = el_1
        seq[bottom], seq[min_ind] = seq[min_ind], seq[bottom]
    return seq, selection_comparisons

def insertion_sort(seq):
    insertion_comparisons = 0
    for i in range(1, len(seq)):
        j = i - 1
        key = seq[i]
        flag = True
        while (seq[j] > key) and (j >= 0):
            seq[j+1] = seq[j]
            j -= 1
            insertion_comparisons += 1
            flag = False
        seq[j+1] = key
        if flag:
            insertion_comparisons += 1
    return seq, insertion_comparisons


merge_comparisons = 0
def merge(left, right):
    left_ind, right_ind = 0, 0
    result = []
    while left_ind < len(left) and right_ind < len(right):
        global merge_comparisons
        merge_comparisons += 1
        if left[left_ind] < right[right_ind]:
            result.append(left[left_ind])
            left_ind += 1
        else:
            result.append(right[right_ind])
            right_ind += 1 

    result += left[left_ind:]
    result += right[right_ind:]
    return result

def merge_sort(seq):
    length = len(seq)
    if length in (0, 1):
        return seq
    mid = length // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def shell_sort(seq):
    shell_comparisons = 0
    part = len(seq) // 2
    while part > 0:
        for i in range(part, len(seq)):
            curr = seq[i]
            j = i

            while j - part >= 0 and j>=0 and seq[j - part] > curr:
                shell_comparisons += 1
                seq[j] = seq[j - part]
                j -= part

            seq[j] = curr
            if j - part >= 0:
                shell_comparisons+=1
        part = part // 2
    return seq, shell_comparisons
    