def selectionSort(array):
    for i in range(len(array)):
        sm = i
        # 这地方多比较了一次
        for j in range(i, len(array)):
            sm = j if array[j] < array[sm] else sm
        array[sm], array[i] = array[i], array[sm]
    return array
