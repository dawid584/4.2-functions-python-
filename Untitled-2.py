text = ""
 
def palindrom(text: str) -> bool:
 
    text = text.lower()
    if text =="".join(reversed(text)):
        
        #Funkcja sprawdzająca czy dany wyraz to palindrom  

        

           print(f" Słowo to palindrom {text}")          
           return True
    else:
           print(f" Słowo to nie palindrom {text}") 
           return False



if __name__ == "__main__":
    
        # to jest absolutne minimum, które musisz zrealizować
        assert palindrom("kot") is False
        assert palindrom("kajak") is True
        assert palindrom("Ala ma kota") is False 
        assert palindrom("Kajak") is True
