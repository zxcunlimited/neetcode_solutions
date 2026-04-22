class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        max_el = nums[0]
        for k, v in freq.items():
            if freq.get(max_el) < v:
                max_el = k
        return max_el