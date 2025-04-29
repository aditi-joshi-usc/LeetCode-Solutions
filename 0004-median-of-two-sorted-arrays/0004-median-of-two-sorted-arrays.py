class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if not nums1 and not nums2:
        #     return 0
        # nums1.extend(nums2)
        # final_arr = nums1
        # if not final_arr:
        #     return 0
        # final_arr.sort()
        # len_final = len(final_arr)
        # if len_final %2 == 0:
        #     return (final_arr[(len_final -1)//2] + final_arr[(len_final)//2] )/2
        # else:
        #     return final_arr[len_final//2]


        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        lenA, lenB = len(A), len(B) 
        total = len(A) + len(B)
        half = total // 2

        low, high = 0, len(A)

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (lenA+lenB+1)//2 - mid1

            l1 = A[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = B[mid2 - 1] if mid2 > 0 else float('-inf')

            r1 = A[mid1] if mid1 < len(A) else float('inf')
            r2 = B[mid2] if mid2 < len(B) else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
