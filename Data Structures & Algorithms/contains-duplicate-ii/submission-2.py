class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        indexes = {}
        l = 0
        for i in range(0, len(nums)):
            if i - l > k:
                indexes.pop(nums[l])
                l += 1
            if nums[i] in indexes:
                return True
            indexes[nums[i]] = i
        return False