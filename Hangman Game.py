import csv
print('Welcome to hangman')
print('Try to guess the word')

HANGMAN=['''
         +---+
         |   |
             |
             |
             | ''',
            ''' 
            +---+
            |   |
            0   |
                |
                |'''
            ,''' 
            +---+
            |   |
            0   |
            |   |
                |
                '''
            ,'''
            +---+
            |   |
            0   |
            |   |
            |   |'''
            ,'''
            +---+
            |   |
            0   |
            |/  |
            |   |
                     '''
            ,'''
            +---+
            |   |
            0   |
           \|/  |
            |   |'''
            ,''' 
            +---+
            |   |
            0   |
           \|/  |
            |\  |''',
            ''' 
            +---+
            |   |
            0   |
           \|/  |
           /|\  |'''
                       ]

maxwrong=len(HANGMAN)-1

def word():
    with open('words.csv','w',newline='') as file:
       i=input('enter word:')
       writerobj=csv.writer(file)
       writerobj.writerow([i.upper()])
       
def read():   
    with open('words.csv',newline='') as file:
        readerobj=csv.reader(file)
        
        for i in readerobj:
           
            for word in i:
                print('----------BEGIN-----------')
            
            #main loop
            wrong_guess=0
            currentguess='-'*len(word)

            while wrong_guess<maxwrong and currentguess!=word:
                print(HANGMAN[wrong_guess])
        
                print('So far the word is',currentguess)
                guessletter=input('enter your letter:')
                if guessletter.upper() in word:
                    print('You have guessed correctly!!')
                    newguess=''
                    for letter in range(len(word)):
                        if guessletter.upper()==word[letter]:
                            newguess+=guessletter.upper()
                        else:
                            newguess+=currentguess[letter]
                    currentguess=newguess
                else:
                    print('Wrong!Try Again')
                    wrong_guess+=1
            if wrong_guess==maxwrong:
                    print(HANGMAN[wrong_guess])
                    print('You Lost')
                    print('The correct word is:',word)
            else:
                    print('You Have Won!')
                    
        
    
word()
read()
    
     


        
        
        
        
        