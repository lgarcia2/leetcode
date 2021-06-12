
# 'Median Of Two Sorted Arrays' - Problem Reflections

### 2021-05-16
The difficulty with this problem surrounds the time complexity constraint. It isn't particularly difficult to sort two sorted arrays and it isn't difficult to get the median of the sorted array. Doing it all while under the time constraint can be tough. 

I started in a couple ways. I decomposed the problem into those two concepts: merging the arrays and finding the median. I'll leave the optimization for later. With that in mind, I didn't completely forget about the time constraint. 

The problem mentioned that the time complexity should be O(log(m+n)) where m is the length of the first array and n is the length of the second. Any time I see a 'log' in a time complexity I think about the problem getting smaller as it goes on. A lot of time that leads me to look into recursive functions so thats how I designed my merge arrays function.

I decided to tackle this problem in two sessions. I've been doing one of these problems per weekend while I sip my coffee and I still want to have time for other things. So I left off after I implemented the recursive merge of arrays and after I found the median of the merged arrays. I haven't tested it against the leetcode tester, but I did write my own test script to verify it does in fact satisfy all their examples. I'm fairly certain that it won't meet their time complexity requirements so I'll work on those requirements when I come back later. I broke down the problem into those two ideas: merging the arrays then finding the median. However, I think to satisfy the time complexity, I may have to find the median while merging the arrays.


## Update 2021-06-12
The solution I wrote last time passed all the provided examples, however when I went to submit the code it failed! There was one test that it didnt pass, where the inputs were [1, 3] and [2, 7]. This was an interesting one example because the merging of these arrays did not fit into the model I had in my mind. That is, I kind of thought, based on the examples, that the ordered lists would themselves be ordered. I hadn't considered whether the lists order could be intertwined with each other. With that in mind I restructured my algorighm to accommodate. Maybe it was just the idea of coming at this with a new set of eyes, but I wrote and tested the function with relative ease. 
Back in my undergrad, I remembered my Algorigthms professor explaining this same kind of merge to us. He had two piles (I'm using the word 'pile' here to avoid using the word 'stack' which has data structure implications) of index cards. He started by taking one card off each pile and asking us which was smaller. He then put the smaller one in a new pile. After that he grabbed a new index card from the pile corresponding to the card he just moved. This went on and on until there were no cards left in one of the piles. At that point, he put the remaining cards in the new pile and all the index cards were sorted.
This was the concept I was trying to emulate in my function `merge_sorted_arrays()`. And since the problem got smaller as it went on, the time complexity seemed okay for now. So I submitted to leetcode and it all passed. I definately prefer this algorithm to the one before since its a smaller code footprint and easier to understand (if you know the story!).
Lastly, I had already written a test file which was good, but I wanted to make it more solid so I added pytest into the mix. I didnt start with test driven development, but having it at the end made rewriting my algorithm much quicker.


### What I did

As I mentioned earlier, I initially broke down the problem into two components. I merged the arrays and I found the median. I designed the merge function to be recursive in preparation to meet the time constraints and to conform to the idea I had in my head. 

### What I would change

I would have preferred more examples, specifically the one that made me rethink the algorithm. I suppose I would change my testing assumptions. I'd try and come up with more scenarios, other than the examples, that I could encounter.

### Take-Away's

- Python 3.9 definitely has some interesting differences than earlier versions of Python. I ran into some list type hint issues while doing this. I'm running Python 3.9 on my computer so in order to test my code I had to update the type hints in the Leetcode stub from `List` to `list`. If I were to run this code in an earlier version of Python, I could keep the original stub and do a `from typing import List` instead. So thats something to keep in the back of my mind when working with Python 3.9 and also with Leetcode in general. Now I know Leetcode does not use Python 3.9

- Like other programming languages, I had assumed integer division would yield an integer as the return type. That is, int / int = int. I found this not to be the case though when I was using math to find the index of an array. There is a specific Python operator for doing the integer division I was used to. That operator is `//` which does the integer math that sets the result to the floor of the divided number. e.g. 3/2 = 1.5, 3//2 = 1

