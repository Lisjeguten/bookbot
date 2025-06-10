def sort_on(d):
    l = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
    for k, v in l.items():
        m = k + ":"
        print(m,v)
    
    
        
    


def words_in_book(t):
    w = t.split()
    words = len(w)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

def number_of_chars(n):
    number = {}
    letters = n.lower()

    for letter in letters:
        if letter in number:
            number[letter] += 1
        else:
            if letter.isalpha():
                number[letter] = 1
    
    print("--------- Character Count -------")
    sort_on(number)
    print("============= END ===============")