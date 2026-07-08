class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        
        for i in range(n):
            for j in range(len(words[i])):
                if j >= n:
                    return False

                if i >= len(words[j]):
                    return False
                
                if words[j][i] != words[i][j]:
                    return False

        return True