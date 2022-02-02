
# 'Add Two Numbers' - Problem Reflections

### 2021-04-25
I think the difficulty, 'Medium' describes this problem well. In my mind, it was straight forward what to do. There were no 'gotchas', but it did require an understanding of data structures and how they can interact with each other. After reflecting on the problem, there may be other ways to solve it too.

### What I did

In my code, I went through each linked list and converted it to an int so I could add the numbers. I added the values to a stack so I could quickly reverse the values. I did have to lookup the syntax for a 'stack' in python. Stacks are my favorite data structure but its not too often that I actually use them. After converting the Linked Lists to integers and adding them, I had to to the process in reverse. I converted the int to a Linked List and that was it. I created a couple methods to help me with repetitive tasks, I think they make the code look a little cleaner.

With all this in mind, my solution has the following time complexities.
- O(n), for my `getNumber()` function. I have to iterate through the linked list and iterate through the stack. This is O(2n) but simplifies to O(n)
- O(n), for my `intToReversedLinkedList()` function. I have to iterate through the digits of a number and add to a Linked List

Since I'm not calling any of these functions _within_ each other my overall time complexity should be O(n)


### What I would change

While in the middle of writing my `intToReversedLinkedList()` function, I had a thought for a different way to approach the problem. Since both the input Linked Lists are reversed and you're just adding numbers up, you could probably do both the addition of the values while iterating through the linked list. You might also be able to 

### Take-Away's

I still have a lot of habits of C# coding. I often make my variables camelCase or UpperCamelCase instead of snake_case which is what you're supposed to do in python. 

I learned that stacks seem to be implemented with Python's default list behavior which is kind of cool and I learned the syntax for that.

I also had to double check how to iterate through a string's characters in Python. My assumptions beforehand about iterating through it were mostly correct, but now I know the syntax. I'll also have to be aware of Python's behavior because iterating through a string the way I did it results in strings for the individual characters rather than 'chars' which I would have expected.