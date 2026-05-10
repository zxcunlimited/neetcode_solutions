class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        for person in trust:
            if person[0] in trusts: trusts[person[0]].add(person[1])
            else: 
                trusts[person[0]] = set()
                trusts[person[0]].add(person[1])
        
        judge = trusts[trust[0][0]]
        for k, v in trusts.items():
            judge.intersection_update(v)
        if judge == set():
            return -1
        return judge.pop()