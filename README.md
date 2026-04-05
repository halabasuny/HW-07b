# HW 07b — Testing a Legacy System

---

## 1. Assignment Description

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program. In this assignment you will start with an existing implementation of the classify triangle program that will be given to you. You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.

These are the two files: Triangle.py and TestTriangle.py.
- Triangle.py is a starter implementation of the triangle classification program.
- TestTriangle.py contains a starter set of unittest test cases to test the classifyTriangle() function in Triangle.py.

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program. You should run the complete set of tests against the original triangle program to see how correct the triangle program is. Based on the results, you will then update the classify triangle program to fix all of the logic bugs you found. Continue to run the test cases as you fix defects until all of the defects have been fixed.

---

## 2. Author

**Hala Basyouni**

---

## 3. Summary

### Results Summary

The original `Triangle.py` contained **5 bugs**. Running the 31-test suite against the buggy implementation produced **22 failures and 1 error** — only 8 tests passed, all in the `InvalidInput` category. The root cause was a typo (`b <= b` instead of `b <= 0`) that caused the function to return `InvalidInput` for virtually every call before any other logic could execute. After fixing all 5 bugs, all 31 tests passed with zero failures.

### Reflection

The most important lesson from this assignment was how a single small typo can completely mask all other bugs in a program. Because `b <= b` is always `True`, the function returned `InvalidInput` immediately for almost every input — making it impossible to even reach the triangle inequality check, the equilateral check, or the right-triangle formula. This meant bugs B-02 through B-05 were invisible until B-01 was fixed first.

Writing tests before fixing code was essential. Without tests, it would be tempting to just look at the logic and assume it works. The tests made each failure undeniable and gave a clear target for each fix.

What worked well: equivalence partitioning across all 6 output categories, combined with boundary values (e.g., sides of 200, degenerate triangles where a+b=c). What was harder: the right-triangle bug (B-04) required knowing that `*2` vs `**2` produces very different results — code inspection caught it, but the test output confirmed it.

---

## 4. Honor Pledge

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment.

---

## 5. Detailed Results

### 5a. Techniques Used

Test cases were designed using two standard black-box testing techniques:

**Equivalence Partitioning** — the input space was divided into 6 classes matching the 6 possible return values: `Right`, `Equilateral`, `Isoceles`, `Scalene`, `NotATriangle`, and `InvalidInput`. At least one test was written for each class.

**Boundary Value Analysis** — for each class, edge cases were tested: the maximum valid side length (200), the minimum valid side length (1), degenerate triangles (a+b = c), all three positions of the hypotenuse for right triangles, and all three positions of the equal pair for isosceles triangles.

The strategy for determining test sufficiency: testing was considered complete when every output class had at least 3 tests, every boundary condition was covered, and no new failures were being discovered by adding more tests of the same type.

### 5b. Assumptions and Constraints

- Inputs must be integers in the range [1, 200]; floats and strings are treated as `InvalidInput`.
- A degenerate case where the sum of two sides exactly equals the third (e.g., 3+5=8) is classified as `NotATriangle`.
- The `Right` classification takes priority over `Isoceles`.
- The original code was not rewritten from scratch — only the 5 identified bugs were corrected.

### 5c. Data Inputs Used

31 test cases across 6 categories:

| Category | Test IDs | Count |
|----------|----------|-------|
| Right triangle | RT-01 to RT-06 | 6 |
| Equilateral | EQ-01 to EQ-03 | 3 |
| Isosceles | IS-01 to IS-04 | 4 |
| Scalene | SC-01 to SC-03 | 3 |
| NotATriangle | NT-01 to NT-04 | 4 |
| InvalidInput | II-01 to II-09 | 9 |
| Edge cases | ED-01 to ED-02 | 2 |
| **Total** | | **31** |

### 5d. Defects Found & Fixed

| Bug # | Location in Code | Description | Fix Applied |
|-------|-----------------|-------------|-------------|
| B-01 | `if a<=0 or b<=b or c<=0` | `b <= b` is always True — causes every valid call to return `InvalidInput` | Changed `b<=b` to `b<=0` |
| B-02 | Triangle inequality check | Logic `a>=(b-c)` etc. is wrong; never correctly identifies `NotATriangle` | Replaced with `(a+b)<=c or (a+c)<=b or (b+c)<=a` |
| B-03 | `if a==b and b==a` | Equilateral check omits `c`; `b==a` just repeats `a==b` | Changed second condition to `b==c` |
| B-04 | `(a*2)+(b*2)==(c*2)` | Uses multiplication (`*2`) instead of squaring (`**2`); only checks one side order | Changed to `a**2+b**2==c**2` checking all 3 permutations |
| B-05 | `(a!=b) and (b!=c) and (a!=b)` | Scalene check has `a!=b` duplicated; never checks `a!=c` | Changed last condition to `a!=c` |

---

## 6. Test Run 1 — Buggy Implementation (Part 1)

Test set executed against the **original unmodified Triangle.py**.

| Test ID | Input (a,b,c) | Expected Result | Actual Result | Pass or Fail |
|---------|--------------|-----------------|---------------|--------------|
| RT-01 | (3,4,5) | Right | InvalidInput | Fail |
| RT-02 | (5,3,4) | Right | InvalidInput | Fail |
| RT-03 | (4,3,5) | Right | InvalidInput | Fail |
| RT-04 | (5,12,13) | Right | InvalidInput | Fail |
| RT-05 | (8,15,17) | Right | InvalidInput | Fail |
| RT-06 | (6,8,10) | Right | InvalidInput | Fail |
| EQ-01 | (1,1,1) | Equilateral | InvalidInput | Fail |
| EQ-02 | (10,10,10) | Equilateral | InvalidInput | Fail |
| EQ-03 | (100,100,100) | Equilateral | InvalidInput | Fail |
| IS-01 | (2,2,3) | Isoceles | InvalidInput | Fail |
| IS-02 | (5,5,8) | Isoceles | InvalidInput | Fail |
| IS-03 | (3,5,5) | Isoceles | InvalidInput | Fail |
| IS-04 | (5,3,5) | Isoceles | InvalidInput | Fail |
| SC-01 | (3,4,6) | Scalene | InvalidInput | Fail |
| SC-02 | (7,10,12) | Scalene | InvalidInput | Fail |
| SC-03 | (5,7,9) | Scalene | InvalidInput | Fail |
| NT-01 | (1,2,3) | NotATriangle | InvalidInput | Fail |
| NT-02 | (1,1,3) | NotATriangle | InvalidInput | Fail |
| NT-03 | (10,1,1) | NotATriangle | InvalidInput | Fail |
| NT-04 | (5,1,2) | NotATriangle | InvalidInput | Fail |
| II-01 | (0,1,1) | InvalidInput | InvalidInput | Pass |
| II-02 | (-1,4,5) | InvalidInput | InvalidInput | Pass |
| II-03 | (1,0,1) | InvalidInput | InvalidInput | Pass |
| II-04 | (1,1,0) | InvalidInput | InvalidInput | Pass |
| II-05 | (201,1,1) | InvalidInput | InvalidInput | Pass |
| II-06 | (1,201,1) | InvalidInput | InvalidInput | Pass |
| II-07 | (1,1,201) | InvalidInput | InvalidInput | Pass |
| II-08 | (1.5,2,3) | InvalidInput | InvalidInput | Pass |
| II-09 | ('a',2,3) | InvalidInput | ERROR (crash) | Fail |
| ED-01 | (200,200,200) | Equilateral | InvalidInput | Fail |
| ED-02 | (3,5,8) | NotATriangle | InvalidInput | Fail |

**Run 1 Result: 8 Passed, 22 Failed, 1 Error — out of 31 tests**

---

## 7. Test Run 2 — Fixed Implementation (Part 2)

Same test set executed against the **corrected Triangle.py** after all 5 bugs were fixed.

| Test ID | Input (a,b,c) | Expected Result | Actual Result | Pass or Fail |
|---------|--------------|-----------------|---------------|--------------|
| RT-01 | (3,4,5) | Right | Right | Pass |
| RT-02 | (5,3,4) | Right | Right | Pass |
| RT-03 | (4,3,5) | Right | Right | Pass |
| RT-04 | (5,12,13) | Right | Right | Pass |
| RT-05 | (8,15,17) | Right | Right | Pass |
| RT-06 | (6,8,10) | Right | Right | Pass |
| EQ-01 | (1,1,1) | Equilateral | Equilateral | Pass |
| EQ-02 | (10,10,10) | Equilateral | Equilateral | Pass |
| EQ-03 | (100,100,100) | Equilateral | Equilateral | Pass |
| IS-01 | (2,2,3) | Isoceles | Isoceles | Pass |
| IS-02 | (5,5,8) | Isoceles | Isoceles | Pass |
| IS-03 | (3,5,5) | Isoceles | Isoceles | Pass |
| IS-04 | (5,3,5) | Isoceles | Isoceles | Pass |
| SC-01 | (3,4,6) | Scalene | Scalene | Pass |
| SC-02 | (7,10,12) | Scalene | Scalene | Pass |
| SC-03 | (5,7,9) | Scalene | Scalene | Pass |
| NT-01 | (1,2,3) | NotATriangle | NotATriangle | Pass |
| NT-02 | (1,1,3) | NotATriangle | NotATriangle | Pass |
| NT-03 | (10,1,1) | NotATriangle | NotATriangle | Pass |
| NT-04 | (5,1,2) | NotATriangle | NotATriangle | Pass |
| II-01 | (0,1,1) | InvalidInput | InvalidInput | Pass |
| II-02 | (-1,4,5) | InvalidInput | InvalidInput | Pass |
| II-03 | (1,0,1) | InvalidInput | InvalidInput | Pass |
| II-04 | (1,1,0) | InvalidInput | InvalidInput | Pass |
| II-05 | (201,1,1) | InvalidInput | InvalidInput | Pass |
| II-06 | (1,201,1) | InvalidInput | InvalidInput | Pass |
| II-07 | (1,1,201) | InvalidInput | InvalidInput | Pass |
| II-08 | (1.5,2,3) | InvalidInput | InvalidInput | Pass |
| II-09 | ('a',2,3) | InvalidInput | InvalidInput | Pass |
| ED-01 | (200,200,200) | Equilateral | Equilateral | Pass |
| ED-02 | (3,5,8) | NotATriangle | NotATriangle | Pass |

**Run 2 Result: 31 Passed, 0 Failed — out of 31 tests**

---

## 8. Summary Results Matrix

| Metric | Test Run 1 (Buggy) | Test Run 2 (Fixed) |
|--------|:-----------------:|:-----------------:|
| Tests Planned | 31 | 31 |
| Tests Executed | 31 | 31 |
| Tests Passed | 8 | **31** |
| Tests Failed | 22 | **0** |
| Errors (crash) | 1 | 0 |
| Defects Found | 5 | — |
| Defects Fixed | 0 | 5 |

**Test sufficiency strategy:** Testing was considered complete when (1) every output equivalence class had at least 3 test cases, (2) all boundary conditions were exercised, (3) all 3 argument positions were covered for symmetric cases, and (4) all invalid input types were represented. No new failure categories were being discovered, indicating adequate coverage.