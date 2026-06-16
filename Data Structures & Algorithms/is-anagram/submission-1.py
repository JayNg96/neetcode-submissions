class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_str = {}
        
        for string in s:
            if string not in check_str:
                check_str[string] = 1 
            else:
                check_str[string] += 1

        return Counter(t) == check_str
            