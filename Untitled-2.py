word = "ala ala"
print(f"Sprawdzanie słowa czy jest to palindrom - {word}") 
# wprowadzanie wyrazu
def palindrom(word):
    if word =="".join(reversed(word)):
     #    Funkcja sprawdzająca czy dany wyraz to palindrom   
        return True
    else:
        return False
        
if (palindrom(word) == True):
    # Wyświetlanie informacji dla sprawdzającego czy dany wyraz to palindrom

    print("this word is palindrom")
else:    
    print("this word is not palindrom")
    
    
    