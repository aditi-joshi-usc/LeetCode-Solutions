class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wordlen = len(words[0])
        totallen = len(words) * wordlen
        res = []
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] =1

        
        for i in range(wordlen):
            left = i
            sub_count = {}
            count = 0

            for j in range(i, len(s) - wordlen+1, wordlen):
                subword = s[j:j+wordlen]
                if subword in word_count:
                    if subword in sub_count:
                        sub_count[subword]+=1
                    else:
                        sub_count[subword]=1
                    count+=1

                    while sub_count[subword] > word_count[subword]:
                        sub_count[s[left:left+wordlen]] -=1
                        count-=1
                        left += wordlen
                    if count == len(words):
                        res.append(left)
                else:
                    count =0 
                    sub_count = {}
                    left = j + wordlen 
        return res


            
