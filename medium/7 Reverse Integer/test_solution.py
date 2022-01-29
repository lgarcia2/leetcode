import pytest
from reverse_integer import Solution as Solution

def test_example_1():
    ### Example 1:
    ##Input: 
    input = 123
    ##Output: 
    output = 321

    # Act
    sol = Solution()
    reversed = sol.reverse(input)

    # Assert
    print(f"**Testing Solution, Example 1: {reversed} should be {output}** \r\n")
    assert(reversed == output)


def test_example_2():
    ### Example 1:
    ##Input: 
    input = -123
    ##Output: 
    output = -321

    # Act
    sol = Solution()
    reversed = sol.reverse(input)

    # Assert
    print(f"**Testing Solution, Example 1: {reversed} should be {output}** \r\n")
    assert(reversed == output)


def test_example_3():
    ### Example 1:
    ##Input: 
    input = 120
    ##Output: 
    output = 21

    # Act
    sol = Solution()
    reversed = sol.reverse(input)

    # Assert
    print(f"**Testing Solution, Example 1: {reversed} should be {output}** \r\n")
    assert(reversed == output)

def test_example_4():
    ### Example 1:
    ##Input: 
    input = 1534236469
    ##Output: 
    output = 0

    # Act
    sol = Solution()
    reversed = sol.reverse(input)

    # Assert
    print(f"**Testing Solution, Example 1: {reversed} should be {output}** \r\n")
    assert(reversed == output)
    