import pytest
from median_two_sorted_arrays import Solution as Solution

def test_example_1():
    ### Example 1:
    ##Input: 
    nums1 = [1,3]
    nums2 = [2]
    ##Output: 
    output = 2.00000
    ##Explanation: merged array = [1,2,3] and median is 2.

    # Act
    sol = Solution()
    median1 = sol.findMedianSortedArrays(nums1, nums2)

    # Assert
    print(f"**Testing Solution, Example 1: {median1} should be {output}** \r\n")
    assert(median1 == output)


def test_example_2():
    ### Example 2:
    ##Input: 
    nums1 = [1,2]
    nums2 = [3,4]
    ##Output: 2.50000
    output = 2.50000
    ##Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

    # Act
    sol = Solution()
    median2 = sol.findMedianSortedArrays(nums1, nums2)

    # Assert
    print(f"**Testing Solution, Example 2: {median2} should be {output}** \r\n")
    assert(median2 == output)

def test_example_3():
    ### Example 3:
    #
    #Input: 
    nums1 = [0,0]
    nums2 = [0,0]
    #Output: 0.00000
    output = 0.00000

    # Act
    sol = Solution()
    median3 = sol.findMedianSortedArrays(nums1, nums2)

    # Assert
    print(f"**Testing Solution, Example 3: {median3} should be {output}** \r\n")
    assert(median3 == output)


def test_example_4():
    ### Example 4:
    #
    #Input: 
    nums1 = []
    nums2 = [1]
    #Output: 1.00000
    output = 1.00000

    # Act
    sol = Solution()
    median4 = sol.findMedianSortedArrays(nums1, nums2)

    # Assert
    print(f"**Testing Solution, Example 4: {median4} should be {output}** \r\n")
    assert(median4 == output)


def test_example_5():
    ### Example 5:
    #
    #Input: 
    nums1 = [2]
    nums2 = []
    #Output: 2.00000
    output = 2.00000

    # Act
    sol = Solution()
    median5 = sol.findMedianSortedArrays(nums1, nums2)

    # Assert
    print(f"**Testing Solution, Example 5: {median5} should be {output}** \r\n")
    assert(median5 == output)


def test_example_6():

    # Setup
    nums1 = [1,3]
    nums2 = [2,7]

    output = 2.50000

    # Act
    sol = Solution()
    median2 = sol.findMedianSortedArrays(nums1, nums2)

    # Assert
    print(f"**Testing Solution, Example 2: {median2} should be {output}** \r\n")
    assert(median2 == output)

