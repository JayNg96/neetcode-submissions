class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        for i, j in zip(sentence1, sentence2):
            if [i,j] in similarPairs or [j,i] in similarPairs or i == j:
                continue
            return False

        return True