class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # bruteforce
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        #         elif numbers[i] + numbers[j] > target:
        #             break
        # 2-pointers
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]