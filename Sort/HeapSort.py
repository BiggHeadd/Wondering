def shift_left(elems, e, begin, end):
    i, j = begin, begin * 2 + 1
    while j < end:
        if j + 1 < end and not elems[j] < elems[j + 1]:
            j += 1
        if e < elems[j]:
            break
        elems[i] = elems[j]
        i = j
        j = j * 2 + 1
    elems[i] = e


def heap_sort(elems):
    end = len(elems)
    for i in range(end // 2 + 1, -1, -1):
        shift_left(elems, elems[i], i, end)
    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        shift_left(elems, e, 0, i)
    return elems


if __name__ == '__main__':
    a_list = [5, 6, 8, 1, 2, 4, 9]
    a_list_sorted = heap_sort(a_list)
    print(a_list_sorted)

    import heapq
    heapq.heapify(a_list)
    for i in range(len(a_list)):
        print(heapq.heappop(a_list))