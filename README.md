# LeetCode Solutions
This repository contains some of my solutions to a select number of [LeetCode](https://leetcode.com/) problems. From time to time I like to run through some LeetCode questions to keep my skills sharp I also want to hone my Python skills since at the time of writing this (2021-04-23) I've only been _extensively_ using Python since Spring 2021. 

# Requirements
- Python 3.9 [LeetCode requirement](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-)

# Running the Code
1. Initialize venv to create a virtual environment
```
$ python -m venv env
```

2. Use venv to activate the environment
**Windows**
```
$ env/Scripts/activate
```
**Linux**
```
$ source env/bin/activate
```

3. Install Requirements
```
$ pip install -r requirements.txt
```

4. Run Pytest
Pytest can be run at the root level to run all the problems.
```
$ pytest
```

For a specific problem you'll want to run pytest in the problem directory.
**Example**
```
$ pytest '.\hard\Median Of Two Sorted Arrays\'
```

NOTE: At this time not all leetcode problems I've written have unit tests

5. Deactivate the virtual environment
```
$ deactivate
```
