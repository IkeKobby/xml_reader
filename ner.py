import nltk
import string
from nltk.tokenize import word_tokenize


def characterClassifier(text):
    """
    A simple character classifier. 
    Args: 
        text; takes a text, tokenize it into word, character tokens.

    Returns:
            Returns a dictionary of lists of groups each belonging to 
            "AU"--> All Upper, "IU" --> Initial Upper and "L" ---> Lower
    """
    name_class = {
                "AU": [],
                "IU": [],
                "L" : []
                }
    # popular punctuations that can be extended
    puncts = string.punctuation

    # tokenize text into word tokens
    # which would includes characters as well.
    words = word_tokenize(text)

    # loop over words and for each classify accordingly
    for word in words:
        if word.isupper():
            name_class['AU'].append(word)
        elif any([word.islower(),  word in puncts]):
            name_class['L'].append(word)
        else:
            name_class['IU'].append(word)
    return name_class


if __name__ == "__main__":
    text = 'I am isaac, I like IBM, Google and Facebook.'
    print(characterClassifier(text))