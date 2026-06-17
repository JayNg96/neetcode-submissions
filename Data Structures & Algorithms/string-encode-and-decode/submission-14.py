class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NOSTRING0101"
        to_string = ""
        for i in range(len(strs)):
            to_string += strs[i]
            if i != len(strs) - 1:
                to_string += '#@!'
        return to_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return ['']
        if "NOSTRING0101" in s:
            return []
        return s.split('#@!')