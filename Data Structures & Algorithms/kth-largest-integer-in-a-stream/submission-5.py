class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        # сначала попробуем сделать линейный поиск, потом мб бинарный
        # for i in range(len(self.sorted_nums)):
        #     if val <= self.sorted_nums[i]:
        #         self.sorted_nums.insert(i, val)
        #         break
        # else:
        #     self.sorted_nums.append(val)
        # return self.sorted_nums[-(self.k)]

        l, r = 0, len(self.sorted_nums)
        while l < r:
            mid = (l + r) // 2
            try:
                if self.sorted_nums[mid - 1] <= val <= self.sorted_nums[mid]:
                    self.sorted_nums.insert(mid, val)
                    return self.sorted_nums[-(self.k)]
            except IndexError:
                if val < self.sorted_nums[mid]:
                    self.sorted_nums.insert(0, val)
                else:
                    self.sorted_nums.insert(1, val)
                return self.sorted_nums[-(self.k)]
            if self.sorted_nums[mid] < val:
                l = mid + 1
            else:
                r = mid - 1
        self.sorted_nums.insert(((abs(l) + abs(r)) // 2), val)
        return self.sorted_nums[-(self.k)]
        