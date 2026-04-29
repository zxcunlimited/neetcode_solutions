class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def bin_search(arr, val):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        res = []
        while nums:
            temp = nums.pop()
            idx = bin_search(res, temp)
            res.insert(idx, temp)
        return res