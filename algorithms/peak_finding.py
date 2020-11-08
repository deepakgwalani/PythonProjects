def peak_finding(arr, l, r):
    if l == r:
        # array of length 1
        return arr[l]
    mid = (l + r) // 2
    if (mid == l and arr[mid] >= arr[mid + 1]) or (mid == r and arr[mid] >= arr[mid - 1]):
        return arr[mid]
    elif arr[mid] < arr[mid - 1]:
        return peak_finding(arr, l, mid - 1)
    else:
        return peak_finding(arr, mid + 1, r)


def main():
    arr = [5, 10]
    print(peak_finding(arr, 0, len(arr) - 1))


main()
