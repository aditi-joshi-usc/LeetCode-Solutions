class Solution:

    def __init__(self, w: List[int]):
        self.sum_list = []
        running_sum = 0

        for wt in w:
            running_sum += wt
            self.sum_list.append(running_sum)
        self.total_sum = running_sum

    def pickIndex(self) -> int:

        target = random.randint(1, self.total_sum)
        left = 0
        right = len(self.sum_list)

        while left<right:
            mid = left+ (right-left) //2
            if target > self.sum_list[mid]:
                left = mid+1
            else:
                right = mid
                
        return left
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()