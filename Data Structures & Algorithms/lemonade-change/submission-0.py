class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        charges = {5:0, 10:0}
        for bill in bills:
            match bill:
                case 5:
                    charges[5] += 1
                case 10:
                    if charges[5] >= 1:
                        charges[5] -= 1
                        charges[10] += 1
                    else:
                        return False
                case 20:
                    if charges[5] >= 3:
                        charges[5] -= 3
                    elif charges[10] >= 1 and charges[5] >= 1:
                        charges[10] -= 1
                        charges[5] -= 1
                    else:
                        return False
        return True