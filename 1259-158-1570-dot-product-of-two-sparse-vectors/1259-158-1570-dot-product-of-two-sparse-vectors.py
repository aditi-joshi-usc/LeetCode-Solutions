class SparseVector:
    def __init__(self, nums: List[int]):
        self.pos =[]
        for i, num in enumerate(nums):
            self.pos.append((i,num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vec1 = self.pos
        vec2 = vec.pos


        p1 =0 
        p2 =0
        res =0 
        while p1< len(vec1) and p2< len(vec2):

            if vec1[p1][0] == vec2[p2][0]:
                res+= vec1[p1][1] * vec2[p2][1]
                p1+=1
                p2+=1
            elif vec1[p1][0] < vec2[p2][0]:
                p1+=1
            else:
                p2+=1
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)