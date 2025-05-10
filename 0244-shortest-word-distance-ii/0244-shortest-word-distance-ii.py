class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.track = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.track[word].append(i)



    def shortest(self, word1: str, word2: str) -> int:
        
        '''
        practice - 0
        coding - 3

        makes = 1, 4
        coding  = 3
        diff = 1


        makess = 1, 4, 7
        coding = 3, 6 
        diff = 1
        '''


        
        min_diff = float('inf')
        p1 = 0
        p2 = 0
        l1 = len(self.track[word1])
        l2 = len(self.track[word2])
        while p1 < l1 and p2 < l2:
            min_diff = min(min_diff, abs(self.track[word1][p1]-self.track[word2][p2]))

            if self.track[word1][p1] < self.track[word2][p2]:
                p1+=1
            else:
                p2+=1
        return min_diff

            




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)