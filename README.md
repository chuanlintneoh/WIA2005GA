# WIA 2005 Algorithm Analysis and Design

### Members:

1. Tneoh Chuan Lin **(Leader)**

2. Lee Weng Hong

3. Lee Ing Zhen

4. Ng Khai Hon

5. Chong Boon Ping

6. James Wong Yi Ngie



### Part 4: The Love Letter

Problem Description:

Once he have put all of the selected items in his bag, he went to look at the two letters in the chest. He picked up the letters (Figure 3) and there it was written:

![alt text](https://github.com/chuanlintneoh/WIA2005GA/blob/main/assets/Part%204.png)

The two letters looked similar but he notices some of the words are different between the two letters.


**Problem:**
What are the different words from the two letters?



##### 1. Discuss and record possible approaches to the problem:

To solve the problem of identifying different words between two letters, we can consider the following approaches:

**Approach 1: Set-based Approach**

- **Description:** Utilise sets in Python, which automatically handle uniqueness within a collection. Convert both letters into sets of words and compute the difference between these sets.

- **Pros**: Simple and easy to implement using Python's set operations.

- **Cons**: Does not specify where the differences occur in the text. It only shows which words are different.



**Approach 2: Index-based Comparison**

- **Description**: Convert the letters into lists of words and compare each word at the same index in both lists.

- **Pros**: Identifies the position of the differing words, providing more context.

- **Cons**: More complex than the set-based approach (Approach 1). It assumes that the text structure is the same, which may not always be the case.



**Approach 3: Dictionary-based Approach**

- **Description**: Use a dictionary to count occurrences of each word in both letters. Compare frequency of each word across both dictionaries.

- **Pros**: Provides information about differing word frequencies between texts.

- **Cons**: Like the set-based approach, it lacks information on the location of differences.

##### 2. Describe the algorithm for the best approach:

**Approach 2** is chosen because this approach ensures that we are not only finding the differing words but also understand their position within the letters, which is crucial for a thorough analysis. 



###### Algorithm Steps:

1. Split both letters into lists of words

2. Iterate over both lists using indices.

3. For each index, compare the words: if they differ, record the words and their positions.

4. Return the list of differing words with the positions



###### Pseudocode:

```
Initialise list1 to split words of Letter1
Initialise list2 to split words of Letter2
Initialise differences as an empty list

For each index from 0 to the minimum length of list1 and list2:
    If word at index in list1 is not equal to word at index in list2:
        Append (index, list1[index], list2[index]) to differences

If length of list1 is not equal to length of list2:
    Append information about extra words in the longer list to differences

Return differences
```

###### Running Time Complexity:

1. Best and Average Case: $O(n)$
   
   - **Where $n$ is the length of the shorter letter in terms of words**
   
   - This complexity arises because the algorithm needs to iterate through each word in the shorter letter only once, directly comparing it to the corresponding word in the other letter if available.
   
   - This scenario assumes that both letters are of nearly similar length, thus requiring a single pass-through of the list of words in the shorter letter.

2. Worst Case: $O(m+n)$
   
   - **Where $m$ and $n$ are the lengths of the two letters respectively.**
   
   - This complexity is considered when the two letters are significantly different in length. The algorithm will need to first compare all corresponding words up to the length of the shorter letter (contributing $O(n)$), and then separately handle the remaining words in the longer letter (contributing $O(m-n)$ if $m > n$).
   
   - The computational effort increases linearly with the total count of words due to the need to check additional words and handle discrepancies in length. 

###### Advantages and Limitations:

- **Advantages**: Gives precise location and nature of difference.
- **Limitations**: Assumes both texts are similarly structured (e.g. same sentence/word order). More code needed to handle texts of different lengths.



Code refer to the `loveletters.py` .


