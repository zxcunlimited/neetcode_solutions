class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_order = {}
        i = 0
        for char in order:
            idx_order[char] = i
            i += 1
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for char1, char2 in zip(w1, w2):
                if idx_order[char1] < idx_order[char2]:
                    break
                elif idx_order[char1] == idx_order[char2]:
                    continue
                else:
                    return False
            else:
                if len(w1) > len(w2):
                    return False
        return True