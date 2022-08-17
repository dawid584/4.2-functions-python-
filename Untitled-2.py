word = input("enter your word:  ")
word = word.lower()
# wprowadzanie wyrazu
def palindome(word):
    if (word == word[::-1]):
        return True
    else:
        return False
        """"
        Funkcja sprawdzająca czy dany wyraz to palndrom
        """

    
    