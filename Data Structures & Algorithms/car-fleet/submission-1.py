class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        race = [tuple([0, 0]) for i in range(target + 1)]
        for i in range(len(position)):
            race[position[i]] = tuple([position[i], speed[i]])
        for i in range(target, -1, -1):
            if race[i] == (0, 0):
                continue
            if stack != []:
                t1 = (target - race[i][0]) / race[i][1]
                t2 = (target - stack[0][0]) / stack[0][1]
                if t1 > t2:
                    while stack != []:
                        stack.pop()
                    res += 1
                stack.append(race[i])
            else:
                stack.append(race[i])
        return res + 1
