import pytest
from zigzag_conversion import Solution as Solution

def test_example_1():
    ### Example 1:
    ##Input: 
    s = "PAYPALISHIRING"
    numRows = 3
    ##Output: 
    output_1 = "PAHNAPLSIIGYIR"

    # Act
    sol = Solution()
    converted_str = sol.convert(s, numRows)

    # Assert
    print(f"**Testing Solution, Example 1: {converted_str} should be {output_1}** \r\n")
    assert(converted_str == output_1)


def test_example_2():
    ### Example 1:
    ##Input: 
    s = "PAYPALISHIRING"
    numRows = 4
    ##Output: 
    output_1 = "PINALSIGYAHRPI"

    # Explaination
    # P     I    N
    # A   L S  I G
    # Y A   H R
    # P     I

    # Act
    sol = Solution()
    converted_str = sol.convert(s, numRows)

    # Assert
    print(f"**Testing Solution, Example 2: {converted_str} should be {output_1}** \r\n")
    assert(converted_str == output_1)


def test_example_3():
    ### Example 1:
    ##Input: 
    s = "A"
    numRows = 1
    ##Output: 
    output_1 = "A"

    # Act
    sol = Solution()
    converted_str = sol.convert(s, numRows)

    # Assert
    print(f"**Testing Solution, Example 3: {converted_str} should be {output_1}** \r\n")
    assert(converted_str == output_1)

def test_example_4():
    ### Example 1:
    ##Input: 
    s = "ABCD"
    numRows = 2
    ##Output: 
    output_1 = "ACBD"

    # Act
    sol = Solution()
    converted_str = sol.convert(s, numRows)

    # Assert
    print(f"**Testing Solution, Example 1: {converted_str} should be {output_1}** \r\n")
    assert(converted_str == output_1)


