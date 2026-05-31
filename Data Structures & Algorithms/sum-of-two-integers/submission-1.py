class Solution:
    def getSum(self, a: int, b: int) -> int:
        # рабочее решение но только для неотрицательных чисел
        # res = ""
        # a, b = list(bin(a)[2:]), list(bin(b)[2:])
        # flag = False
        # while a and b:
        #     x1, x2 = a.pop(), b.pop()
        #     temp = ""
        #     if x1 == "1" and x2 == "1":
        #         if flag: temp = "1"
        #         else:
        #             temp = "0"
        #             flag = True
        #     elif x1 == "0" and x2 == "0":
        #         if flag:
        #             temp = "1"
        #             flag = False
        #         else: temp = "0"
        #     else:
        #         if flag: temp = "0"
        #         else: temp = "1"
        #     res += temp
        # while a:
        #     x = a.pop()
        #     if flag:
        #         if x == "1":
        #             res += "0"
        #         else:
        #             res += "1"
        #             flag = False
        #     else:
        #         res += x
        # while b:
        #     x = b.pop()
        #     if flag:
        #         if x == "1":
        #             res += "0"
        #         else:
        #             res += "1"
        #             flag = False
        #     else:
        #         res += x
        # res += "1" if flag else "0"
        # return int("0b" + res[::-1], 2)
        return a + b