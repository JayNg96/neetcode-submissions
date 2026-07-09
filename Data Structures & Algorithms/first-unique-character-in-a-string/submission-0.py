class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)

        for string in s:
            freq[string] += 1

        if 1 not in freq.values():
            return -1

        for idx, string in enumerate(s):
            if freq[string] == 1:
                return idx
        
        return -1