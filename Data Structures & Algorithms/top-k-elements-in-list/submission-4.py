class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # самое примитивное решение, сложность O(NlogN)
        # chars = {}
        # for i in nums:
        #     if i in chars:
        #         chars[i] += 1
        #     else:
        #         chars.update({i: 1})
        # chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
        # res = []
        # for i in range(k):
        #     res.append(chars[i][0])
        # return res

        # решение покруче, через bucket sort (используется внутри множество так как сложность O(1) у операций с ним)
        n = len(nums)
        bucket = {i:set() for i in range(n + 1)}
        chars = {}
        for i in nums:
            if i in chars:
                bucket[chars[i]].remove(i)
                chars[i] += 1
                bucket[chars[i]].add(i)
            else:
                chars.update({i: 1})
                bucket[chars[i]].add(i)
        res = []
        i = n
        while k > 0:
            for j in bucket[i]:
                if k == 0:
                    break
                res.append(j)
                k -= 1
            i -= 1
        return res

        