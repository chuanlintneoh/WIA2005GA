# WIA2005 Algorithm Analysis and Design

## Group Assignment: The Adventure of Algo Jones

### Group Members:

| **NAME**           | **MATRIC NUMBER** |
| ------------------ | ----------------- |
| TNEOH CHUAN LIN    | 22004808          |
| LEE ING ZHEN       | 22055760          |
| LEE WENG HONG      | 22004797          |
| JAMES WONG YI NGIE | 22004837          |
| NG KHAI HON        | 22004741          |
| CHONG BOON PING    | 22004846          |

### Part 1: Finding the Golden Statue of Bastet

**Problem Description:**

Algo Jones is an archaeologist, who goes around the world looking for missing treasures. His latest project brought him to Egypt, to look for the Golden Statue of Bastet, said to be hidden in a chest in one of the chambers in the Pyramid of Khufu. The pyramid contains many chambers and the floor plan (marked with grid numbers), look like the following (Figure 1). Entrance is located in chamber 1.

![Part 1](https://github.com/chuanlintneoh/WIA2005GA/blob/main/assets/)

**Problem:**
How to search all the chambers without missing any areas?

### Part 2: Cracking the Chest Lock Code

**Problem Description:**

Algo Jones finally found the chest in chamber marked 14 in the floor plan. The chest contains a lock that requires a 3-digit number combination (Figure 2).

![Part 2](https://github.com/chuanlintneoh/WIA2005GA/blob/main/assets/)

**Problem:**
What are the possible number combination for the lock?

### Part 3: Choosing the Treasures

**Problem Description:**

Algo Jones have 120 possible 3-digit lock combination to try, but fortunately, he manages to open the lock on his 20th try. He found several treasure items in the chest and a couple of letters. He was carrying a bag but he knows he could not fit all of the treasures in his bag which can only carry up to 10kg, but he must choose the most precious one first and come back for the rest later. After evaluating all the items, he came out with an assessment list for all the items (Table 1).

| Items                                | Description                                                                                                                                                                                                                                                       | Value        | Weight |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------ |
| Sceptre of Eternal Power             | A jewelled sceptre adorned with rare gems, said to grant its wielder unimaginable power and authority over life and death. Legends claim it was used by the ancient pharaohs to command the forces of nature and control the destiny of nations.                  | Priceless    | 5kg    |
| The Eye of Horus Pendant             | A golden pendant in the shape of the Eye of Horus, crafted with intricate hieroglyphics and encrusted with precious stones. It is rumoured to possess protective powers, granting its wearer visions of the future and safeguarding them from harm.               | $2 Million   | 0.5kg  |
| The Ankh of Immortality              | A shimmering ankh symbol made of pure silver, believed to hold the secret to eternal life. According to myth, those who possess it can defy death itself and enjoy everlasting youth and vitality.                                                                | $5 Million   | 1.5kg  |
| The Scarab Amulet of Fortune         | An ancient scarab amulet carved from jade, with iridescent wings and inscribed with ancient symbols. Legend has it that it brings incredible luck to its owner, ensuring prosperity, success, and protection from evil spirits.                                   | $1.5 Million | 0.2kg  |
| The Golden Mask of Osiris            | A magnificent mask crafted from solid gold, depicting the god Osiris with eyes encrusted with sparkling gemstones. It is said to hold the wisdom of the gods and bestow unparalleled insight and enlightenment upon those who wear it.                            | $10 Million  | 2kg    |
| The Crown of the Pharaohs            | A majestic crown adorned with rare jewels and precious metals, symbolizing the divine authority of the pharaohs. It is said to confer upon its wearer the wisdom of the gods and the right to rule over the lands of Egypt with absolute power and sovereignty.   | $15 Million  | 3kg    |
| The Emerald Scarab of Transformation | A large emerald scarab beetle statue with wings outstretched, believed to hold the power of metamorphosis. According to legend, it can grant its possessor the ability to shape-shift into any creature they desire, transcending the limitations of mortal form. | $3 Million   | 2kg    |

Table 1: List of items in the chest including the weight and value

**Problem:**
Which items should he carry out in his bag first?

### Part 4: The Love Letter

**Problem Description:**

Once he have put all of the selected items in his bag, he went to look at the two letters in the chest. He picked up the letters (Figure 3) and there it was written:

![Part 4](https://github.com/chuanlintneoh/WIA2005GA/blob/main/assets/Part%204.png)

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

### Part 5: The Secret Message

**Problem Description:**

The different words found in one of the letter sounded like an ancient book title that Algo Jones have seen in the library back in Harvard University. He straight away plan his travel to visit the library. Once there he found the book and straight away open to read them. At first glance, nothing seems out of the ordinary apart from the usual writings on ancient civilisation, but at the end of the book, Algo Jones found a string of strange characters (Figure 4).

![Part 5](https://github.com/chuanlintneoh/WIA2005GA/blob/main/assets/)

**Problem:**
What is the secret message from the book?

### Part 6: The Final Search of the Golden Statue of Bastet

**Problem Description:**

The message forces Algo Jones to find a ship so that he can travel to Cluster Island. The island is made of 5 separate islands with different land condition and wild animals. The condition are as follows (Table 2):

| Island location | Land condition                               | Wild animals                |
| --------------- | -------------------------------------------- | --------------------------- |
| North           | Swamp area                                   | Full of wild animals        |
| South           | Mountains and caves                          | Some wild animals           |
| East            | Thick woods and a lake                       | Full of wild animals        |
| West            | Sandy flat land                              | Small but poisonous animals |
| Middle          | Inhabited with villages and agriculture area | No wild animals             |

Table 2: The 5 islands of Cluster Island’s land condition and wild animals

As much as Algo Jones wanted to find the Golden Statue of Bastet, he must consider where to look for it safely. He needs to determine which island he should search without endangering himself.

**Problem:**
Which island(s) should he search?

### Part 7:

**Problem Description:**
Decide how the story ends.
