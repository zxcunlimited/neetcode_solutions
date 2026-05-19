class MedianFinder:

    def __init__(self):
        self.arr = []
        self.mid = -0.5
    def addNum(self, num: int) -> None:
        self.mid += 0.5
        if len(self.arr) == 0:
            self.arr.append(num)
        else:
            l, r = 0, len(self.arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if self.arr[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            self.arr.insert((l + r) // 2 + 1, num)
    def findMedian(self) -> float:
        print(self.arr, int(self.mid), int(self.mid + 0.5))
        return (self.arr[int(self.mid)] + self.arr[int(self.mid + 0.5)]) / 2
        