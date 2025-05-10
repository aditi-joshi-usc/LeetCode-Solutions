class Solution:
    def isValid(self, code: str) -> bool:
        if code[0] !='<' or code[-1]!='>':
            return False
        

        containsFlag = False
        stack = []

        def isValidCdata(s):
            return s.find('[CDATA[') == 0


        def isValidTagName(tag, isEndFlag):
            nonlocal containsFlag
            if not tag or len(tag) > 9:
                return False
            for c in tag:
                if not c.isupper():
                    return False
            
            if isEndFlag:
                return stack and stack.pop() == tag
            
            containsFlag = True
            stack.append(tag)
            return True





        i=0

        while i < len(code):
            if not stack and containsFlag:
                return False
            
            if code[i] == '<':
                if stack and code[i+1] == '!':
                    closeIndex = code.find(']]>', i+2)
                    if closeIndex == -1 or not isValidCdata(code[i+2: closeIndex]):
                        return False
                elif code[i+1] == '/':
                    closeIndex = code.find('>', i+2)
                    if closeIndex == -1 or not isValidTagName(code[i+2:closeIndex], True):
                        return False
                else:
                    closeIndex = code.find('>', i+2)
                    if closeIndex == -1 or not isValidTagName(code[i+1:closeIndex], False):
                        return False
                i = closeIndex
            i+=1
        
        return not stack and containsFlag
                    