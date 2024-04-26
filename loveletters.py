def find_differences(letter1, letter2):
    words1 = letter1.split()
    words2 = letter2.split()
    differences = []
    
    for index in range(min(len(words1), len(words2))):
        if words1[index] != words2[index]:
            differences.append((index, words1[index], words2[index]))
    
    if len(words1) > len(words2):
        for index in range(len(words2), len(words1)):
            differences.append((index, words1[index], 'No word in Letter 2'))
    elif len(words2) > len(words1):
        for index in range(len(words1), len(words2)):
            differences.append((index, 'No word in Letter 1', words2[index]))
    
    return differences

letter1 = """
To My Dearest Nefertari,
As I sit here amidst the grandeur of this
ancient pyramid, surrounded by the whispers
of the past, my thoughts turn to you, my
beloved. Though miles may separate us, know
that you are always in my heart, a beacon of
light guiding me through the darkness of the
unknown.
As I embark on this journey into the depths of
the pyramid, I am filled with a mixture of
excitement and trepidation. The allure of
uncovering ancient secrets and treasures
beckons me forward, but with each step I take,
I am reminded of the risks that accompany
such endeavors.
I cannot help but think of the life we have
built together, the moments of joy and
laughter we have shared, and the love that
binds us together across time and space. It is
your unwavering support and encouragement
that give me strength in the face of
uncertainty, and for that, I am eternally
grateful.
Though the sands of time may have long since
buried the civilization that built this
magnificent structure, I find solace in the
knowledge that our love transcends the ages, a
timeless testament to the power of the human
spirit.
Until we are reunited once more, know that
you are always with me, guiding me through
the labyrinth of life with your love and light.
With all my heart,
Your devoted.
"""
letter2 = """
To My Dearest Nefertari,
As I sit here amidst the grandeur of this
antediluvian pyramid, surrounded by the
whispers of the past, my thoughts turn to you,
my beloved. Though miles may separate us,
know that you are always in my heart, a
beacon of light guiding me through the
darkness of the unknown.
As I embark on this voyage into the depths of
the pyramid, I am filled with a mixture of
excitement and trepidation. The allure of
uncovering ancient secrets and treasures
beckons me forward, but with each step I take,
I am reminded of the risks that accompany
such endeavors.
I cannot help but think of the life we have
built together, the moments of joy and
laughter we have shared, and the love that
binds us together within time and space. It is
your unwavering support and encouragement
that give me strength in the face of
uncertainty, and for that, I am eternally
grateful.
Though the sands of time may have long since
buried the society that built this magnificent
structure, I find solace in the knowledge that
our love transcends the ages, a timeless
testament to the power of the human spirit.
Until we are reunited once more, know that
you are always with me, guiding me through
the labyrinth of life with your love and light.
With all my heart,
Your devoted.
"""

differences = find_differences(letter1, letter2)
print("Differences:", differences)