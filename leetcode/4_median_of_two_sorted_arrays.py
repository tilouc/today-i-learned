class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged_array = sorted(nums1 + nums2)

        left_index = int((len(merged_array) / 2) - 1)

        right_index = int(len(merged_array) / 2)

        if len(merged_array) % 2 == 0:
            return (merged_array[left_index] + merged_array[right_index]) / 2

        elif len(merged_array) % 2 != 0:
            return merged_array[int((len(merged_array) / 2) - 0.5)]