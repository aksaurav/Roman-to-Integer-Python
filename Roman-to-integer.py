roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

# def romanToInt(S: str) -> int:
#     ans = 0
#     for i in range(len(S)-1,-1,-1):
#         num = roman[S[i]]
#         if 4 * num < ans: ans -= num
#         else: ans += num
#     return ans

# if __name__ == '__main__':
#     s = 'CMXCVIII'
#     print(romanToInt(s))


def romatoInt(s):
    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res

if __name__ == '__main__':
    s = 'IV'
    print(romatoInt(s))