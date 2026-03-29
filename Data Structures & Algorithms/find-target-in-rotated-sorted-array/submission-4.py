class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # проверка на повернутость
            if nums[l] <= nums[mid]:
                rotated_part = True
            else:
                rotated_part = False
            # повернутая часть
            if rotated_part:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # не повернутая часть
            elif not (rotated_part):
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1