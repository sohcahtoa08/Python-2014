def count_letters(text,letter):
    '''count_letters(text,letter) -> int
    returns number of times that letter appears in text'''
    total = 0
    for i in text:
        if i == letter:
            total += 1
    return total
        

# answer the question
quote = '''It's passed on.  
This parrot is no more.  
It has ceased to be. 
It's expired and gone to meet its maker.  
This is a late parrot.  
It's a stiff.  
Bereft of life, it rests in peace.  
If you hadn't nailed it to the perch, it would be pushing up the daisies.  
It's rung down the curtain and joined the choir invisible.  
This is an ex-parrot!'''
print(count_letters(quote,'e'))
