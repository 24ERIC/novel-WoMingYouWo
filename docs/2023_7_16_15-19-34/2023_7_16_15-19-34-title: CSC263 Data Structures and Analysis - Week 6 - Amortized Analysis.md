# title: CSC263 Data Structures and Analysis - Week 6 - Amortized Analysis

- Amortized Analysis
    - Aggregate Method -> calculate number of steps use summation
        - Find the total cost of performing a sequence of operations in the worst case.
        - Divide the total cost by the number of operations in the sequence.
    - Accounting Method -> insert save 5$, search cost 3n$, keep balance
        - amortized costs
    - Credit Invariance -> A statement about the credit of the data structure which holds for every possible sequence of operations.
        - Ex: each element in second half of array has a credit of at least 2
- Questions

    ```python
        Q1 - Top k Values, again

        Recall The problem from the week 3 practice problems: we have an unsorted list of n numbers, chosen independently and uniformly randomly from the set {1, 2, 3, …, m}, where m is much larger than n. Suppose we wish to find the k largest numbers in this list, where k < n.

        After learning about BST, Sally comes up with the following algorithm:

        1. Insert all n elements into a BST
        2. Starting at the right-most element of the tree, return k elements of the tree

        We analyzed the worst case runtime of her algorithm. In particular, we showed that the worst-case runtime of the second step of this algorithm is O(kn).

        Can we get a better bound, using the ideas we learned from this week? If so, what is the runtime of the second step of this algorithm?
    ```

    ```python
        Q1 - My Answer
        unsorted list of n numbers
        random choose from {1, 2, 3, …, m}
        find the k largest numbers

        Worst case is list is sorted, and root number is smallest number, so all number goes a straight line, root-root's right child-root's right child's right child - and so on.
        it takes n steps to get to right most of the tree, ie, the largest number in tree. and then k steps. in total, it takes n+k steps in worst case.
        I think better bound is theta(n^2), but sounds not correct.
    ```

    ```python
        Q1 - Correct Answer
        good
        very good
    ```

    ```python
        Q2 - Bogo Sort
        Consider the following sorting algorithm:
        BogoSort(A): 
        1.   while not IsSorted(A): 
        2.       Randomize(A) # randomly shuffle the elements of the array
        3.   return A

        Suppose we call BogoSort on an array of length n, consisting of m zeros and (n − m) ones. (For example, the array [1, 0, 1, 1, 0] is an array of length n = 5 with m = 2 zeros and m − n = 3 ones.) Such an array is sorted if all the zeros comes before any of the ones.

        Part (a) What is the probability that calling “Randomize(A)” sorts the array?

        Part (b) Based on your result from Part (a), How many times would you expect the “IsSorted” function to be called?

        Part (c) Explain why this algorithm is considered a Las Vegas algorithm.
    ```
    
    ```python
        Q2 - My Answer

        Part (a) - 2/5 * 1/4 * 3/3 * 2/2 * 1/1 = 1/10, first two number need to be 0, the last three number must be 1

        Part (b) - 10 times, as 1/10 * 10 = 1

        Part(c) - yes, because the only result can be return out of while loop is the condition array is sorted, if it is not sorted, while will keep looping.

        Las Vegas algorithm -> computing, a Las Vegas algorithm is a randomized algorithm that always gives correct results; that is, it always produces the correct result or it informs about the failure. However, the runtime of a Las Vegas algorithm differs depending on the input. The usual definition of a Las Vegas algorithm includes the restriction that the expected runtime be finite, where the expectation is carried out over the space of random information, or entropy, used in the algorithm. An alternative definition requires that a Las Vegas algorithm always terminates, but may output a symbol not part of the solution space to indicate failure in finding a solution. The nature of Las Vegas algorithms makes them suitable in situations where the number of possible solutions is limited, and where verifying the correctness of a candidate solution is relatively easy while finding a solution is complex.
    ```

    ```python
        Q2 - Correct Answer
        good
        very good
    ```
