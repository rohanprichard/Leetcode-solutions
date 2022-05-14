def largestGoodInteger(self, num: str) -> str:
    
    ls = []
    temp = ''
    for i in num:
        temp.join(i)
        if len(temp) == 3:
            if temp[0] == temp[1] and temp[1] == temp[2]:
                ls.append(int(temp))
            temp = ''
    print(ls)
    return max(ls)
        