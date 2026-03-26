# Intermediate Quiz

1. What does the `is` operator check?  
   **Answer: Same object in memory (identity)**
2. Difference between `==` and `is`?  
   **Answer: `==` checks value, `is` checks identity**
3. Tuples are mutable? (True/False)  
   **Answer: False**
4. Output of `"python"[::-1]`?  
   **Answer: "nohtyp" (reverse slicing)**
5. What is short-circuiting in `and`/`or`?
     **Answer: Python stops evaluating as soon as result is known**
6. What does continue do inside a loop?   a) exits the loop   b) skips to next iteration   c) does nothing   d) raises error   **Ans : skips to next iteration**

7. When does the else block of a for loop execute?
   a) always   b) only if break was never called   c) only if break was called   d) never
   **Ans : only if break was never called**
8. Which of these will not cause an infinite loop?
   a) while True: pass
   b) while 1: print(1)
   c) i=5; while i>0: i+=1
   d) for i in range(10): pass
   **Ans : for loop with range(10) finishes normally**

9. Can you have multiple elif clauses?
   a) yes   b) no   c) only two   d) only one
   **Ans : yes (as many as needed)**

**Answer Key with Explanation**:

- Q1 & Q2: `is` uses `id()`, `==` uses `__eq__`.
- Q3: Tuples are immutable (cannot `.append()`).
- Q4: `[::-1]` is Pythonic way to reverse.
- Q5: Saves time (e.g., `False and expensive()` never calls function).