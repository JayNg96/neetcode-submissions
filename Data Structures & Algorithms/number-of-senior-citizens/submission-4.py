class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        
        for d in details:
            age = int(d[-4] + d[-3])
            if age > 60:
                count += 1

        return count