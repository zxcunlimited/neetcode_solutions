class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        def sub_dict(d, sub_d) -> bool:
            for k, v in sub_d.items():
                if not(d.get(k, 0) >= v):
                    return False
            return True

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        min_len = float("inf")
        min_str = ""
        temp_s = ""
        l = 0
        temp_s_dict  = {}
        for r in s:
            temp_s_dict[r] = temp_s_dict.get(r, 0) + 1
            temp_s += r
            while sub_dict(temp_s_dict, t_dict):
                if len(temp_s) < min_len:
                    min_len = len(temp_s)
                    min_str = temp_s
                temp_s = temp_s[1:]
                temp_s_dict[s[l]] -= 1
                l += 1
        return "".join(min_str)