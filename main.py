def count_positives_sum_negatives(arr):
    if arr == [] or arr is None:
        return []

    positive_count = 0
    negative_sum = 0

    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_sum += i

    return [positive_count, negative_sum]
arr = [4 , 84 , 741 ,15 , 0]
