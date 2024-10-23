consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k' , 'l', 'm' , 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w']

while 1:
    word = input()

    if word == 'quit!':
        break
  
    if len(word) > 4:
        if word[-3] in consonants and word[-2] == 'o' and word[-1] == 'r':
            word = word[:-2] + 'our'
    
    print(word)