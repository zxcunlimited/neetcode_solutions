class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        groups = [[] for _ in  range(int(len(hand) / groupSize))]
        for elem in hand:
            for group in groups:
                if group == []:
                    group.append(elem)
                    break
                else:
                    if group[-1] == elem - 1 and len(group) < groupSize:
                        group.append(elem)
                        break
            else:
                return False

        return True