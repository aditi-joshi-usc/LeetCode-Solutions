class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:


        def get_words(i):
            curr_line = []
            curr_len = 0

            while i< len(words) and curr_len + len(words[i]) <= maxWidth:
                curr_line.append(words[i])
                curr_len+= len(words[i]) + 1
                i+=1
        
            return curr_line
    

        def create_line(line, i):

            base_len = -1
            
            for word in line:
                base_len+= len(word)+1
            
            extra_space = maxWidth - base_len

            if len(line) == 1 or i == len(words):
                return ' '.join(line)+' '*extra_space 

            space_count = len(line) - 1
            space_per_word =  extra_space//  space_count
            needs_extra_space = extra_space %  space_count 
            for j in range(needs_extra_space):
                line[j]+=' '
            
            for j in range(space_count):
                line[j]+=' '*space_per_word
            return ' '.join(line)
        
        res = []

        i = 0

        while i< len(words):
            curr_line = get_words(i)
            i+= len(curr_line)
            res.append(create_line(curr_line, i))
        return res
            


