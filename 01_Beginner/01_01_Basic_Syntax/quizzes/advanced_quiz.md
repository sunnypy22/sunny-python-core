# Advanced Quiz

1. What does the walrus operator `:=` do?  
   **Answer: Assigns value inside expression**
2. Can you use `in` operator on a dictionary?     
    **Answer: Yes** (checks keys only)
3. Name two dunder methods for `+` and `*`.     
    **Answer: `__add__` and `__mul__`**
4. Difference between list and tuple in terms of hashability?  
   **Answer: List is unhashable, tuple is hashable**
5. What happens when you do `a += [4]` on a list?  
   **Answer: Modifies in place (no new list created)**
6. In which situation is the else clause on a while loop most useful?
   a) when the loop runs at least once   b) when no break occurred   c) always   d) never
   **Ans : when no break occurred**
7. What is the output of this code?
   for i in range(3):
      if i == 1:
        continue
      print(i, end=" ")
   else:
      print("done")
   
   a) 0 1 2 done
   b) 0 2 done
   c) 0 1 done
   d) 0 2
   **Ans : 0 2 done**

8. Which statement is not allowed directly inside a loop (without being in a block)?
   a) break   b) continue   c) return   d) pass
   **Ans : return (return can only be used inside functions)**
9. Can you use break and continue in the same loop?
   a) yes   b) no
   **Ans : yes**

**Answer Key with Explanation**:

- Q1: Introduced in Python 3.8.
- Q2: `if "name" in my_dict:` works.
- Q3: Used in operator overloading.
- Q4: Only immutable types can be dict keys.
- Q5: Augmented assignment calls `__iadd__` for mutable types.
