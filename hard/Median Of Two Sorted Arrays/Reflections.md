
# 'Median Of Two Sorted Arrays' - Problem Reflections

### 2021-05-16
The difficulty with this problem surrounds the time complexity constraint. It isn't particularly difficult to sort two sorted arrays and it isn't difficult to get the median of the sorted array. Doing it all while under the time constraint can be tough. 

I started in a couple ways. I decomposed the problem into those two concepts: merging the arrays and finding the median. I'll leave the optimization for later. With that in mind, I didn't completely forget about the time constraint. 

The problem mentioned that the time complexity should be O(log(m+n)) where m is the length of the first array and n is the length of the second. Any time I see a 'log' in a time complexity I think about the problem getting smaller as it goes on. A lot of time that leads me to look into recursive functions so thats how I designed my merge arrays function.

I decided to tackle this problem in two sessions. I've been doing one of these problems per weekend while I sip my coffee and I still want to have time for other things. So I left off after I implemented the recursive merge of arrays and after I found the median of the merged arrays. I haven't tested it against the leetcode tester, but I did write my own test script to verify it does in fact satisfy all their examples. I'm fairly certain that it won't meet their time complexity requirements so I'll work on those requirements when I come back later. I broke down the problem into those two ideas: merging the arrays then finding the median. However, I think to satisfy the time complexity, I may have to find the median while merging the arrays.


### What I did

As I mentioned earlier, I initially broke down the problem into two components. I merged the arrays and I found the median. I designed the merge function to be recursive in preparation to meet the time constraints. At this time though, in the worst case, all elements in both arrays are visited. Yielding a time complexity of O(m+n) not good enough for the problem. We'll see how it turns out when I come back though!

### What I would change

I think in this case I may want to rename some variables, or restructure the code in a more readable way while keeping the core logic very similar.

### Take-Away's

- Python 3.9 definitely has some interesting differences than earlier versions of Python. I ran into some list type hint issues while doing this. I'm running Python 3.9 on my computer so in order to test my code I had to update the type hints in the Leetcode stub from `List` to `list`. If I were to run this code in an earlier version of Python, I could keep the original stub and do a `from typing import List` instead. So thats something to keep in the back of my mind when working with Python 3.9 and also with Leetcode in general. Now I know Leetcode does not use Python 3.9

- Like other programming languages, I had assumed integer division would yield an integer as the return type. That is, int / int = int. I found this not to be the case though when I was using math to find the index of an array. There is a specific Python operator for doing the integer division I was used to. That operator is `//` which does the integer math that sets the result to the floor of the divided number. e.g. 3/2 = 1.5, 3//2 = 1
