class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        def o1spaceSol():
            for i, j in zip(sentence1, sentence2):
                if [i,j] in similarPairs or [j,i] in similarPairs or i == j:
                    continue
                return False

            return True

        def o1timeSol():
            similar_pair_dict = defaultdict(set)
            for w1, w2 in similarPairs:
                similar_pair_dict[w1].add(w2)
                similar_pair_dict[w2].add(w1)

            print(similar_pair_dict)

            for w1, w2 in zip(sentence1, sentence2):
                if w1 == w2 or w2 in similar_pair_dict[w1]:
                    continue
                return False
            return True
        return o1timeSol()