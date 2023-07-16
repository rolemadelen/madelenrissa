# Stack Linked List

Stack is a linear data structure that follows a particular order (Last-In, Last-Out; LIFO) in which operations are performed.

<a href="https://www.programiz.com/dsa/stack"><img src="https://cdn.programiz.com/sites/tutorial2program/files/stack.png" title="programiz.com" alt="Stack Operations" /></a>

|      | push | pop  | top  | empty |
| :--: | :--: | :--: | :--: | :---: |
| Time | O(1) | O(1) | O(1) | O(1)  |

## Pseudocode for Basic Operations

### push

```text
push(top, value) -> void
    Pre: top represents the top node in the stack.
         value is the value we're going to push it to the stack.
    Post: new data is pushed to the stack

    n      = new Node(value)
    n.next = top
    top    = n
END
```

### pop

```text
pop(top) -> Node | null
    Pre: top represents the top node in the stack.
    Post: removes the top node from the stack; returns NULL if failed.

    n   = top
    IF (top)
        top = top.next
    END IF

    return n
END
```

### top

```text
top(topNode) -> Node | NULL
    Pre: topNode is the top node in the stack.
    Post: returns the top node on the stack; returns NULL if stack is empty.

    IF (top)
        return top.value
    END IF

    return NULL
END
```

### empty

```text
empty(top) -> boolean
    Pre: top represents the top node in the stack.
    Post: returns true if stack is empty; otherwise false.

    return top == NULL
END
```

## Problems

Stack related problems selected from [Leetcode](https://leetcode.com/tag/stack/).

|       #       | Problem                                              | Difficulty |
| :-----------: | :--------------------------------------------------- | :--------- |
|   [20][i20]   | Valid Parentheses                                    | Easy       |
|  [232][i232]  | Implement Queue using Stacks                         | Easy       |
|  [234][i234]  | Palindrome Linked List                               | Easy       |
| [1021][i1021] | Remove Outermost Parentheses                         | Easy       |
| [1047][i1047] | Remove All Adjacent Duplicates In String             | Easy       |
| [1614][i1614] | Maximum Nesting Depth of the Parentheses             | Easy       |
|  [173][i173]  | Binary Search Tree Iterator                          | Medium     |
|  [654][i654]  | Maximum Binary Tree                                  | Medium     |
|  [946][i946]  | Validate Stack Sequences                             | Medium     |
| [1008][i1008] | Construct Binary Search Tree from Preorder Traversal | Medium     |
| [1381][i1381] | Design a Stack With Increment Operation              | Medium     |
| [1441][i1441] | Build an Array With Stack Operations                 | Medium     |
| [1472][i1472] | Design Browser History                               | Medium     |
| [2130][i2130] | Maximum Twin Sum of a Linked List                    | Medium     |
|  [726][i726]  | Number of Atoms                                      | Hard       |
|  [736][i736]  | Parse Lisp Expression                                | Hard       |
|  [895][i895]  | Maximum Frequency Stack                              | Hard       |
| [1944][i1944] | Number of Visible People in a Queue                  | Hard       |

[i20]: https://leetcode.com/problems/valid-parentheses/
[i232]: https://leetcode.com/problems/implement-queue-using-stacks/
[i234]: https://leetcode.com/problems/palindrome-linked-list/
[i1021]: https://leetcode.com/problems/remove-outermost-parentheses/
[i1047]: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
[i1614]: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
[i173]: https://leetcode.com/problems/binary-search-tree-iterator/
[i654]: https://leetcode.com/problems/maximum-binary-tree/
[i946]: https://leetcode.com/problems/validate-stack-sequences/
[i1008]: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
[i1381]: https://leetcode.com/problems/design-a-stack-with-increment-operation/
[i1441]: https://leetcode.com/problems/build-an-array-with-stack-operations/
[i1472]: https://leetcode.com/problems/design-browser-history/
[i2130]: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
[i726]: https://leetcode.com/problems/number-of-atoms/
[i736]: https://leetcode.com/problems/parse-lisp-expression/
[i895]: https://leetcode.com/problems/maximum-frequency-stack/
[i1944]: https://leetcode.com/problems/number-of-visible-people-in-a-queue/
