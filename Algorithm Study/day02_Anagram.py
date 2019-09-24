

# Initial Code
def is_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    return False


print(is_anagram('silent', 'listen'))
print(is_anagram('abc', 'def'))


# function name is_anagram -> are_anagrams
# parameter names -> make it shorter
# if else -> save memory by returning the result of comparison

# Modified Code
def are_anagrams_modified(s1, s2):
    return sorted(s1) == sorted(s2)


print(are_anagrams_modified('silent', 'listen'))
print(are_anagrams_modified('abc', 'def'))