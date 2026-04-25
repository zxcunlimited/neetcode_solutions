class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def not_positive(x):
            return x < 0
        stack = [asteroids[0]]
        for aster in asteroids[1:]:
            coll = False
            if not_positive(aster):
                while stack and not(not_positive(stack[-1])):
                    if stack[-1] > abs(aster):
                        break
                    elif stack[-1] == abs(aster):
                        stack.pop()
                        coll = True
                        break
                    else:
                        stack.pop()
                        continue
                if (stack == [] or not_positive(stack[-1])) and not(coll):
                    stack.append(aster)
            else:
                stack.append(aster)
        return stack