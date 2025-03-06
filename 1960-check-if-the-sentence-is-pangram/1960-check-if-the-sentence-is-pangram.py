class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        track = defaultdict(int)
        for letter in sentence:
            track[letter] +=1
        
        if len(track) == 26:
            return True
        else:
            return False