def longestPalindrome(s: str) -> str:
    maxLength = 1
    l = len(s)
    low = 0
    high = 0
    res = s[0]
    for i in range(1, l):
        low = i - 1
        high = i
        while low >= 0 and high < l and s[low] == s[high]:
            if (high - low + 1) > maxLength:
                res = s[low:high + 1]
                maxLength = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < l and s[low] == s[high]:
            if (high - low + 1) > maxLength:
                res = s[low:high + 1]
                maxLength = high - low + 1
            low -= 1
            high += 1
    return res


if __name__ == '__main__':
    print(longestPalindrome('babad'))
