class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i not in "+-*/":
                nums.append(int(i))
            else:
                n2, n1 = nums.pop(), nums.pop()
                match i:
                    case "+":
                        nums.append(n1 + n2)
                    case "-":
                        nums.append(n1 - n2)
                    case "*":
                        nums.append(n1 * n2)
                    case "/":
                        nums.append(int(n1 / n2))
        return nums[0]
                        