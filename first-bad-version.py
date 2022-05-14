global b
def isBadVersion(x):
    if x < b:
        return False
    return True

def firstBadVersion(n: int) -> int:
        l,r = 1, n
        while l < r:
            piv = int(r + l / 2)
            print(piv,l,r)

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