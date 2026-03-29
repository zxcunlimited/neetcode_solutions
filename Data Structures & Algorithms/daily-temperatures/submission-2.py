class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # плохое решение через O(N^2)
        # l, r = 0, 1
        # res = []
        # n = len(temperatures)
        # while l < n:
        #     now = temperatures[l]
        #     if r == n:
        #         l += 1
        #         r = l + 1
        #         res.append(0)
        #     elif temperatures[r] > now:
        #         res.append(r - l)
        #         l += 1
        #         r = l + 1
        #     else:
        #         r += 1
        # return res
        

        # хорошее решение через стэк
        stack = [0]
        n = len(temperatures)
        res = [0 for i in range(n)]
        for i in range(1, n):
            while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res