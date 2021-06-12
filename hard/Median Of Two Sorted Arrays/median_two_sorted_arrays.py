from typing import List

class Solution:
    # if using python 3.9, signatures look like this:
    # def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

    # for earlier versions (and the version on Leetcode), 
    # this should be the signature (NOTE: make sure to 'from typing import List')
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = self.merge_sorted_arrays(nums1, nums2)
        print(f"Merged List: {mergedList}")
        print(f"Looking for median first at index {len(mergedList)//2}")
        median = float(mergedList[(len(mergedList)//2)])
        if len(mergedList) % 2 == 0:
            medianlow = float(mergedList[(len(mergedList)//2)-1])
            medianhigh = float(mergedList[(len(mergedList)//2)])
            median = float((medianlow + medianhigh) / 2)

        print(f"Median: {median}")

        return median


    def merge_sorted_arrays(self, nums1: List[int], nums2: List[int]):
        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1

        merged_nums = []
        if nums1[0] < nums2[0]:
            merged_nums.append(nums1[0])
            next_nums1 = nums1[1:]
            merged_nums.extend(self.merge_sorted_arrays(next_nums1, nums2))
        else:
            merged_nums.append(nums2[0])
            next_nums2 = nums2[1:]
            merged_nums.extend(self.merge_sorted_arrays(nums1, next_nums2))

        return merged_nums
