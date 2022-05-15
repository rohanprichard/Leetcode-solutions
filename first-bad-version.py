"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

global b
def isBadVersion(x):
    if x < b:
        return False
    return True

def firstBadVersion(n: int) -> int:
        l,r = 1, n
        while l < r:
            piv = int(r + l / 2)

            if isBadVersion(piv) == True and isBadVersion(piv-1) == False:
                return piv

            if isBadVersion(piv) == True:
                r = piv
            else:
                l = piv + 1
                
        return l

b = 10
n = 30
firstBadVersion(n)
