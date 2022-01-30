
# 'String to integer (atoi)' - Problem Reflections

### 2022-01-30
This medium was pretty easy. The hardest part of this was dealing with the edge cases.

### What I did

This problem was pretty similar to the #7 Reverse Integer problem. So I followed a similar approach to that one. I iterated through each item in the string and verified it satisfied the requirements. At the end I checked it wasnt out of 32-bit integer range.

What caused me the most problems were the difference between what I read the problem as and what the problem actually asked. Some examples are
- Even if a string contains a valid number, if it starts with a non-digit character (other than + or -) the result should be 0
- If the characters '+' and '-' are next to each other, the second instance is treated as a non-digit character and it, as well as everything after it, are ignored

I also had a couple issues with my 'min max' constraint testing, but that was mostly just minor bugs involving things I forgot.

The problem really wasnt too bad, but special attention needs to be taken care of for the edge cases and unique strings. I did make extra test cases out of these examples, so if anyone is revisiting this problem the tests are great to have! Tests in general are pretty great things to verify your solution. Its great to write down those edge cases so you can be sure your code cover's them. Its part of the reason all the problems here have tests!

### What I would change

I think my code ended up too complex and hard to read. There also may be inefficiencies with it, nothing that will change its 'Big O' time complexity, but there are things that could be improved. So If I were to change things, I'd refactor the code to make it easier to read and understand what's going on at each step. I'd also try and improve some of those inefficiencies. I also used pythons built-in int converter to convert from string to int after I cleaned up the string. I don't know if thats in the 'spirit' of the problem, so I might also make a more 'in the spirit' way of converting from string to int

### Take-Away's

Read the problem carefully and consider the edge cases!

