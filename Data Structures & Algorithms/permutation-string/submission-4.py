class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # решение более менее, логика чуть верная но можно подправить некоторые моменты:
        
        if s1 == s2 or s1 in s2:
            return True
        l, r = 0, 0 # окно можно сделать размером len(s2), потому что мы ищем именно такого длины подстроку
        res = dict()
        for char in s1:
            res[char] = res.get(char, 0) + 1
        temp = dict()
        temp.update({s2[0]: 1})
        while r != len(s2) - 1:
            r += 1
            if res.get(s2[r], 0) != 0:
                while temp.get(s2[r], 0) >= res.get(s2[r], 0) and l < r:
                    temp[s2[l]] = temp.get(s2[l], 0) -  1
                    l += 1
                temp[s2[r]] = temp.get(s2[r], 0) + 1
                if temp == res:
                    return True
            else:
                while l != r:
                    if temp == res:
                        return True
                    temp[s2[l]] -= 1
                    if temp[s2[l]] == 0:
                        temp.pop(s2[l])
                    l += 1
                temp[s2[r]] = temp.get(s2[r], 0) + 1
        return False
        