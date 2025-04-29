class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        nums1.extend(nums2)
        final_arr = nums1
        if not final_arr:
            return 0
        final_arr.sort()
        len_final = len(final_arr)
        if len_final %2 == 0:
            return (final_arr[(len_final -1)//2] + final_arr[(len_final)//2] )/2
        else:
            return final_arr[len_final//2]