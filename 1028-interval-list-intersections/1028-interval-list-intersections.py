class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        l1 = len(firstList)
        l2 = len(secondList)
        res =[]

        while p1 < l1 and p2 < l2:
            
            sa, ea = firstList[p1][0], firstList[p1][1]
            sb, eb = secondList[p2][0], secondList[p2][1]

            if sa <= eb and sb <= ea:
                res.append([max(sa, sb), min(ea, eb)])
            
            if ea <= eb:
                p1+=1
            else:
                p2+=1
        return res
                