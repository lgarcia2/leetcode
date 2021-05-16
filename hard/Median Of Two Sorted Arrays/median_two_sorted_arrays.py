class Solution:
    # I'm using python 3.9, for earlier versions (and the version on Leetcode), 
    # this should be the signature (NOTE: make sure to 'from typing import List')
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        # The time complexity of this is probably incorrect
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

    # recursive function
    def merge_sorted_arrays(self, nums1: list[int], nums2: list[int]):
        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1

        sortedList = []
        leftOffOnIndex = 0
        # iterate through nums1 to find out where nums2[0] fits
        for i in range(0, len(nums1)):
            num1 = nums1[i]
            num2 = nums2[0]
            leftOffOnIndex = i

            if num2 < num1:
                sortedList.append(num2)
                sortedList.append(num1)
                break
            if num1 == num2:
                sortedList.append(num2)
                sortedList.append(num1)
                break
            if num2 > num1: 
                # add num1 to the sorted final list and continue
                sortedList.append(num1)
            if(i == (len(nums1)-1)):
                # both lists already sorted, early exist
                print(f"Both lists already sorted {nums1}, {nums2}, early exit")
                nums1.extend(nums2)
                return nums1

        print(f"temp sorted: {sortedList}")
        # guard against out of bounds
        nextNums1 = []                 
        if len(nums1) > 1:
            nextNums1 = nums1[leftOffOnIndex:-1]

        nextNums2 = []
        if len(nums1) > 1:
            nextNums2 = nums2[1:-1]

        # Recursion!
        print(f"Recursing with {nextNums1} and {nextNums2}")
        nextSorted = self.merge_sorted_arrays(nextNums1, nextNums2)
        sortedList.extend(nextSorted)
        return sortedList


            