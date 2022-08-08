def printMaxOfMin(arr, x):
    maxOfMin = 1

    for i in range(len(arr) - x + 1):

        # Find minimum of current window
        minimum = arr[i]
        for j in range(x):
            if arr[i + j] < minimum:
                minimum = arr[i + j]

        # Update maxOfMin if required
        if minimum > maxOfMin:
            maxOfMin = minimum

    # Print max of min for current window size
    # print("maxOfMin")
    print(maxOfMin, end=" ")


if __name__ == '__main__':
    arr = [2,5,4,6,8]
    printMaxOfMin(arr, 3)
