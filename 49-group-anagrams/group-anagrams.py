class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  #initially[0,0,....0] i.e a-z
            for ch in s:
                count[ord(ch) - ord("a")] += 1  #sub from a so that 0-25 
            res[tuple(count)].append(s)
        return list(res.values())