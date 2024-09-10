# I hereby certify that this program is solely the result of my own work and is in compliance 
# with the Academic Integrity policy of the course syllabus and the academic 
# integrity policy of the CS department.

import random # Import the 'random' module
import Draw # Import the 'Draw' module 

# This function is to load words from a external file 
# and return a list of 6-letter words.  
def loadWords():     
    ans = [] # Create an empty list to store the words.
    
    fin = open("HangmanWords.txt") # Open the dictionary file
    
    # Iterate through each word in the file.
    for word in fin: 
        
        # Check if the word is a valid 6 letter word, stripping whitespaces 
        # and if it is, append it to the list.
        if len(word.strip()) == 6:
            ans.append(word.strip()) 
            
    fin.close() # Close the file.
            
    return ans # Return the list.

# This function is to choose a random word from a list of words. 
def chooseRandomWord(words):
    
    # Choose a random word from words and return it.
    targetWord = random.choice(words) 
    return targetWord 
 
# This function is to draw the hangaman board.
def drawBoard(hangmanPieces, usedLetters, guess):  
    Draw.clear() # Clear the canvas
    Draw.setColor(Draw.BLUE) # Assign the color of the elements in the board to blue.
    
    # Draw the gallows:
    
    # Draw the gallows' vertical pole.
    Draw.line(1300, 30, 1300, 650) 
    
    # Draw the gallows' horizontal pole
    Draw.line(1100, 30, 1400, 30)
    
    # Draw the gallows' base.
    Draw.line(1200, 650, 1400, 650) 
    
    # Draw a title for the game, setting the font family, font size, 
    # color and position:
    Draw.setFontFamily('Courier') 
    Draw.setColor(Draw.RED) 
    Draw.setFontSize(200) 
    x = 28 
    y = 50 
    Draw.string("HANGMAN", x, y)  
    
    # Call the function that draws the guess of the user.
    drawGuess(guess) 
    
    # Call the function that draws the used letters.
    drawLetters(usedLetters) 
    
    # Call the function that draws the figure of the hangaman.
    drawMan(hangmanPieces)
    
    Draw.show() # Show the updated drawing

# This function is to draw the current guessed letters. 
def drawGuess(guess):
    
    # Set the font size, color, exact location, width, and height for 
    # the text (or underscore, depending on the case). 
    Draw.setFontSize(150) 
    Draw.setColor(Draw.BLUE) 
    x = 100 
    y = 650 
    width =  100 
    height = 125 
    
    # Iterate through the position of each element in the 'guess' list.
    for i in range(len(guess)): 
        
        letter = guess[i] # Assign a variable for the positions in the list.
        
        # Check if the position is empty ('None'), and in case it is, draw a underscore 
        # at the correct location and move to the next underscore position.
        if letter == None: 
            Draw.line(x, y, x + width, y) 
            x += width + 30
        
        # Otherwise, draw the guessed letter at the correct location and move 
        # to the next letter position.     
        else: 
            Draw.string(letter, x, y - height) 
            x += width + 30 

# This function is to draw the letters that are not yet used.  
def drawLetters(usedLetters):
    
    # Set the font size, color, width, and exact location.
    Draw.setFontSize(75) 
    Draw.setColor(Draw.BLACK) 
    x = 30 
    y = 670 
    width = 50 
    
    # Initialize a variable that contains a string with all alphabet letters.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    
    for letter in alphabet: # Iterate through each letter in the alphabet.
        
        # Check if the letter has been used.
        if letter in usedLetters: 
            
            # If yes, draw a empty space at the correct location and move to the next letter position.
            Draw.string(" ", x, y) 
            x += width 
            
        # If the letter has not been used, draw it in the correct position, 
        # and move to the next letter position. 
        else: 
            Draw.string(letter, x, y) 
            x += width 

# This function is to draw the hangman figure based on the number of incorrect guesses.
def drawMan(hangmanPieces):
    Draw.setColor(Draw.BLACK) # Assign the color of the hangman figure to black.
    
    # If there's one incorrect guess, draw the head.
    if hangmanPieces > 0: 
        Draw.filledOval(1040, 28, 150, 150)
        
    # If there's two incorrect guesses, draw the body.   
    if hangmanPieces > 1: 
        Draw.line(1115, 140, 1115, 400)
    
    # If there's three incorrect guesses, draw the left arm.  
    if hangmanPieces > 2: 
        Draw.line(1115, 170, 1215, 350) 
        
    # If there's four incorrect guesses, draw the right arm    
    if hangmanPieces > 3: 
        Draw.line(1115, 170, 1015, 350) 
        
    # If there's five incorrect guesses, draw the left leg.  
    if hangmanPieces > 4: 
        Draw.line(1115, 400, 1210, 600) 
        
    # If there's six incorrect guesses, draw the right leg.
    if hangmanPieces > 5: 
        Draw.line(1115, 400, 1015, 600) 
        
# This function is to fill in the guessed letters in the 'guess' list.
def fillGuess(letter, guess, targetWord):
    
    # Initialize a flag to False.
    result = False 
    
    # Iterate through each position of the target word and check if the letter typed match the letter found 
    # in the target word (both uppercase). If they do, update that position in the 'guess' list and set 
    # the flag to True.
    for i in range(len(targetWord)): 
        if letter.upper() == targetWord[i].upper(): 
            guess[i] = letter 
            result = True 
    
    return result # Return the result that indicates whether the letter was a match.

# This function is to play the Hangman game.
def playGame(hangmanPieces, usedLetters, guess, targetWord):   
   
   # While the hangman is not fully drawn and the word has not yet been guessed
   # (there are empty spaces in the 'guess' list):
    while hangmanPieces < 6 and (None in guess):
        drawBoard(hangmanPieces, usedLetters, guess) # Display the current state of the board.
    
        # If the user typed a key, get it and convert it to uppercase.
        if Draw.hasNextKeyTyped(): 
            newKey = Draw.nextKeyTyped() 
            newKey = newKey.upper() 
            
            # Check if the typed key is not in the already used letters and is a valid letter.
            if newKey not in usedLetters: 
                if newKey in "ABCDEFGHIJKLMNOPQRSTUVWYZ": 
                    
                    # Remember that the letter was used, and attempt to fill in the guess.
                    usedLetters += newKey 
                    ans = fillGuess(newKey, guess, targetWord) 
                    
                     # If the guess letter was not a match: Increment the count of the incorrect guesses.
                    if ans == False:
                        hangmanPieces += 1 
                        
        drawBoard(hangmanPieces, usedLetters, guess) # Display the updated state of the board.
    
    # Check if there are no more empty positions in 'guess', and if there aren't, 
    # display a message telling the user that he won.
    if None not in guess:
        x = 200
        y = 300         
        drawBoard(hangmanPieces, usedLetters, guess)
        Draw.setFontSize(40)
        Draw.setColor(Draw.GREEN)
        Draw.string("You won! Great Job", x, y)
    
    # Otherwise, display a message telling the user that he lost and what the correct word was.
    else:
        x = 28
        y = 300         
        drawBoard(hangmanPieces, usedLetters, guess)   
        Draw.setFontSize(40)
        Draw.setColor(Draw.RED)        
        Draw.string("You lost! The correct word was: " + targetWord, x, y)
    
    Draw.show() # Show the updated drawing


# This is the Main function used to intialize the game.            
def main():
    Draw.setCanvasSize(1425, 1080) # Set the canvas size.
    
    # Assign a variable to the words loaded into a list:
    words = loadWords()
    
    # Assign a variable to the random chosen target word from words:
    word = chooseRandomWord(words)
    
    # Initialize a variable ‘hangamanPieces’ to 0, to maintain a count of 
    # the current pieces of the hangman:
    hangmanPieces = 0
    
    # Initialize an empty string ‘usedLetters’, that would contain all 
    # the letters that have been already used by the user:
    usedLetters = ""
    
    # Initialize a list of six positions called ‘guess’, 
    # with each position initialized as ‘None’:
    guess = [None, None, None, None, None, None]  
    
    # Call the function used to play the game:
    playGame(hangmanPieces, usedLetters, guess, word)
       
main() # Invoke the main function