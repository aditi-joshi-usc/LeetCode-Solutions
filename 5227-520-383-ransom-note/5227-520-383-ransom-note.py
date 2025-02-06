class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # mag_dict = {}

        # for m in magazine:
        #     if m in mag_dict:
        #         mag_dict[m] +=1
        #     else: 
        #         mag_dict[m] = 1
        

        # for r in ransomNote:
        #     if r not in mag_dict:
        #         return False
        #     else:
        #         if mag_dict[r] < 1:
        #             return False
        #         else:
        #             mag_dict[r] -= 1
        # return True
        
        for r in ransomNote:
            if r not in magazine:
                return False
            else:
                magazine = magazine.replace(r, "", 1)
        return True