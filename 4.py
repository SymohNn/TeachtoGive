"""Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string."""
def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result
