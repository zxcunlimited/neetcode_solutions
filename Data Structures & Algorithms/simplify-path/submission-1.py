class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        res = []
        for elem in path:
            if elem == "" or elem == ".":
                continue
            elif elem == "..":
                try:
                    res.pop()
                except IndexError:
                    continue
            else:
                res.append(elem)
        return f'/{"/".join(res)}'