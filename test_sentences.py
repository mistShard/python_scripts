from sentences import *
import random
import pytest

# List of all singular determiners
single_determiners = ["a", "one", "the"]

# List of all plural determiners
plural_determiners = ["some", "many", "the"]

# List of all singular nouns
single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

# List of all plural nouns
plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

# List of all prepositions
prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

def test_get_determiner():
    # 1. Test the single determiners.

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    #   1. Test the single nouns
    for _ in range (4):
        # Verify that the result of 'get_noun(1)'
        # is in th list single_nouns.
        assert get_noun(1) in single_nouns
    
    #  2. Test the plural nouns
    for _ in range (4):
        # Verify that the result of 'get_noun(2)'
        # is in th list plural_nouns.
        assert get_noun(2) in plural_nouns

def test_get_verb():
    #   1. Test the verbs with different parameters of
    # "past", "present", and "future"
    for _ in range(4):
        assert get_verb(1, "past") in ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        assert get_verb(1, "present") in ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        assert get_verb(2, "present") in ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        assert get_verb(1, "future") in [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

def test_get_preposition():
    # Loops to check if all four return values from the 
    # 'get_preposition' function are in the prepositions list.
    for _ in range(4):
        assert get_preposition() in prepositions

def test_get_prepositional_phrase():
    #   1. Test the return value of the get_prepositional_phrase
    # function, with "1" as argument.

    # Splits the phrase into its component strings
    # and turns it into a list.
    phrase = get_prepositional_phrase(1).split()
    for _ in range(4):
        # Confirms that the number of words in the phrase is three
        assert len(phrase) == 3
    # Verify that the string in index zero of 'phrase'
    # is in the list prepositions.
    for _ in range(4):
        assert phrase[0] in prepositions
    # Verify that the string in index one of 'phrase'
    # is in the list single_determiners.
    for _ in range(4):
        assert phrase[1] in single_determiners
    # Verify that the string in index two of 'phrase'
    # is in the list single_nouns.
    for _ in range(4):
        assert phrase[2] in single_nouns

    #   2. Test the return value of the get_prepositional_phrase
    # function, with "2" as argument.

    # Splits the phrase into its component strings
    # and turns it into a list.
    phrase = get_prepositional_phrase(2).split()
    for _ in range(4):
        # Confirms that the number of words in the phrase is three
        assert len(phrase) == 3
    # Verify that the string in index zero of 'phrase'
    # is in the list prepositions.
    for _ in range(4):
        assert phrase[0] in prepositions
    # Verify that the string in index one of 'phrase'
    # is in the list single_determiners.
    for _ in range(4):
        assert phrase[1] in plural_determiners
    # Verify that the string in index two of 'phrase'
    # is in the list plural_nouns.
    for _ in range(4):
        assert phrase[2] in plural_nouns

pytest.main(["-v", "--tb=line", "-rN", __file__])