import pytest
from string_to_int import Solution as Solution

def test_example_1():
    ### Example 1:
    ##Input: 
    input = "42"
    ##Output: 
    output = 42

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 1: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)


def test_example_2():
    ### Example 1:
    ##Input: 
    input = "   -42"
    ##Output: 
    output = -42

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 2: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)


def test_example_3():
    ### Example 1:
    ##Input: 
    input = "4193 with words"
    ##Output: 
    output = 4193

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 3: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)


def test_example_4():
    ### Example 1:
    ##Input: 
    input = "words and 987"
    ##Output: 
    output = 0

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 4: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)

def test_example_5():
    ### Example 1:
    ##Input: 
    input = "+-12"
    ##Output: 
    output = 0

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 5: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)

def test_example_6():
    ### Example 1:
    ##Input: 
    input = "2147483646"
    ##Output: 
    output = 2147483646

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 6: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)

def test_example_6():
    ### Example 1:
    ##Input: 
    input = "1095502006p8"
    ##Output: 
    output = 1095502006

    # Act
    sol = Solution()
    fnOutput = sol.myAtoi(input)

    # Assert
    print(f"**Testing Solution, Example 7: {fnOutput} should be {output}** \r\n")
    assert(fnOutput == output)