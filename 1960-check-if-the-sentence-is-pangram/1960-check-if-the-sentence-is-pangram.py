class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # if len(sentence) < 26:
        #     return False
        # track = defaultdict(int)
        # for letter in sentence:
        #     track[letter] +=1
        
        # if len(track) == 26:
        #     return True
        # else:
        #     return False

        seen = 0

        for letter in sentence:
            index = ord(letter) - ord('a')
            curr_bit = 1 << index
            seen |= curr_bit
        
        return seen+1 == 1 << 26