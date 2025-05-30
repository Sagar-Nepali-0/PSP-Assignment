'''
Finds common letters between two words.
'''

def word_intersection():
    """
    Finds and displays common letters between two words.
    """
    word1 = input("Enter first word: ").lower()
    word2 = input("Enter second word: ").lower()
    
    common_letters = set(word1) & set(word2)
    
    if common_letters:
        print("Common letters:", ', '.join(sorted(common_letters)))
    else:
        print("No common letters")

word_intersection()