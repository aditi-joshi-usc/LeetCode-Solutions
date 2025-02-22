class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        res = ['/']
        for i in path:
            if i== '' or i == '.':
                continue
            elif i == '...' or i == '....':
                res.append(i)
                res.append('/')
            elif i=='..':
                if len(res) > 1:
                    res = res[:-2]
                
            else:
                res.append(i)
                res.append('/')
        
        if len(res) > 1 and res[-1] == '/':
            return ''.join(res[:-1])
        else:
            return ''.join(res)
            