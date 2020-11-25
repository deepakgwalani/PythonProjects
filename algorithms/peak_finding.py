def peak_finding(arr, l, r, n):
    if l == r:
        # array of length 1
        return arr[l]
    mid = (l + r) // 2
    if (mid == 0 or arr[mid] >= arr[mid + 1]) and (mid == n-1 or arr[mid] >= arr[mid - 1]):
        return arr[mid]
    elif arr[mid] < arr[mid - 1]:
        return peak_finding(arr, l, mid - 1, n)
    else:
        return peak_finding(arr, mid + 1, r, n)


def main():
    arr = [10, 14, 15, 22, 23, 90, 67]
    n = len(arr)
    print(peak_finding(arr, 0, n-1, n))


main()
