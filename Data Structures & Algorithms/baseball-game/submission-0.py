class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for oper in operations:
            if oper == "C":
                records.pop()
            elif oper == "D":
                records.append(records[-1] * 2)
            elif oper == "+":
                records.append(records[-1] + records[-2])
            else:
                num = int(oper)
                records.append(num)
        return sum(records)