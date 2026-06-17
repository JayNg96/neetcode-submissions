class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(char for char in s if char.isalnum()).lower()

        for i in range(len(cleaned)):
            if cleaned[i] != cleaned[-(1+i)]:
                return False
        return True