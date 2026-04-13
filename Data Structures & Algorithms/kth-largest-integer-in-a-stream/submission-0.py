class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        # сначала попробуем сделать линейный поиск, потом мб бинарный
        for i in range(len(self.sorted_nums)):
            if val <= self.sorted_nums[i]:
                self.sorted_nums.insert(i, val)
                break
        else:
            self.sorted_nums.append(val)
        return self.sorted_nums[-(self.k)]
