class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1 версия - интуиция, сортировать строку и если совпадают то добавлять
        # res = defaultdict(list) # из модуля collections, особенность в том что не кидает ошибку при остутствии ключа а создает
        # for word in strs:
        #     temp = "".join(sorted(word))
        #     res[temp].append(word)
        # return list(res.values())

        # 2 версия - почти то же самое но группировка по хеш таблице
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word) # tuple - преобразование в кортеж так как списки не могут быт ключами
        return list(res.values())