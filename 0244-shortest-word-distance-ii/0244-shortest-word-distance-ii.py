class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordlist = wordsDict

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

        word1_loc = []
        word2_loc = []

        for i in range(len(self.wordlist)):
            if self.wordlist[i] == word1:
                word1_loc.append(i)
            elif self.wordlist[i] == word2:
                word2_loc.append(i)
            else:
                continue
        
        min_diff = float('inf')
        p1 = 0
        p2 = 0
        l1 = len(word1_loc)
        l2 = len(word2_loc)
        while p1 < l1 and p2 < l2:
            min_diff = min(min_diff, abs(word1_loc[p1]-word2_loc[p2]))

            if word1_loc[p1] < word2_loc[p2]:
                p1+=1
            else:
                p2+=1
        return min_diff

            




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)