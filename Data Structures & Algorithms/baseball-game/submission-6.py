class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreList = []
        for i in operations:
            if i.lstrip("-").isdigit():
                scoreList.append(int(i))
            elif i == "+":
                scoreList.append(scoreList[-1] + scoreList[-2])
            elif i == "C":
                scoreList.pop()
            elif i == "D":
                scoreList.append(scoreList[-1] * 2)

        return sum(scoreList)