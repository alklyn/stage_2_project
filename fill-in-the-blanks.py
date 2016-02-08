# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a player with a paragraph containing several blanks.
# The player should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept player input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/



def verify_level(choice):
    """This function tests if a valid difficulty level is provided.
        choice: the level chosen by the player
        The return value is True if the chosen level is valid otherwise
        False is returned
    """
    levels = ["easy", "medium", "hard"]
    for level in levels:
        if level == choice:
            return True
    print "That's not an option!"
    return False
 
def get_level():
    """Get difficulty level from player"""
    verified = False
    while not verified:
        print "Please select a game difficulty by typing it in!"
        print "Possible choices include easy, medium, and hard."
        choice = raw_input()
        choice = choice.lower()
        verified = verify_level(choice)
        
    print "You've chosen {}!".format(choice)
    print
    return choice


def get_number_of_guesses():
    """Get the number of guesses the player would like."""
    verified = False
    while not verified:
        print "How many guesses would you like per problem?"
        guesses = raw_input("Please enter a positive integer number: ")      
        
        try:
            guesses = int(guesses)
            if guesses > 0:  
                verified = True
            else:
                print"You need at least one guess!"
        except ValueError:
            print "That isn't an integer!"
    print 
    
    return guesses

def validate_response(level, response, count):
    """Checks if player provided the correct answer
    Returns True is player has entered the correct answer.
    Otherwise it returns False"""
    
    if response == answers[level][count - 1]:
        return True
    else:
        return False
    

def display_current_paragraph(level):
    print "The current paragraph reads as such:\n"
    print paragraph[level]
    print

def update_current_paragraph(level, count):
    """Updates the current paragraph with the correct answer """
    current_blank = "__{}__".format(count)
    current_answer = answers[level][count - 1]
    paragraph[level] =  paragraph[level].replace(current_blank, current_answer)
    

def quizz(level, guesses, blanks):
    """Fill in the blanks game."""
    for count in range(1, blanks + 1):
        trys_left = guesses
        
        while trys_left > 0:
            display_current_paragraph(level)
            response = raw_input("What should go in blank number {}? ".format(count))
            if validate_response(level, response, count):
                print "\nCorrect!\n"
                update_current_paragraph(level, count)
                break
            else:
                trys_left -= 1
                if trys_left > 0:
                    print "That isn't the correct answer!  Let's try again; you have {} trys left!".format(trys_left)
                else:
                    print "You've failed too many straight guesses!  Game over!"
                    return
    display_current_paragraph(level)
    print "You won!\n"
            

paragraph = dict()
paragraph["easy"] = \
"""A string is a sequence of one or more __1__ surrounded by quotes. If you start
a string with a single quote you have to end it with a __2__ quote. If you start 
a string with a __3__ quote you have to end it in a double quote. Using the 
plus operator we can __4__ two or more strings together. The index of the first
character of a string is __5__."""

paragraph["medium"] = \
"""Strings are __1__table while lists are __2__table. Immutable objects cannot be
__2__ed once they are created. As a result string objects do not support item 
__3__. It is called __4__ when there are two names that refer to the same object
and this only occurs in __5__table objects."""

paragraph["hard"] = \
"""An __1__ variable is a variable that is unique to each instance of a class and
it is defined __2__ a method of the class. __3__ variables are for attributes 
shared by all instances of the class. __4__ is the transfer of characteristics
of a class to other classes that are derived from it. When a method defined in
a derived class has the same name as a method in it's base class it __5__ the 
method in the base class."""

answers = dict()
answers["easy"] = ["characters", "single", "double", "concatenate",  "0"]
answers["medium"] = ["immu", "mu", "assignment", "aliasing",  "mu"]
answers["hard"] = ["instance", "within", "class", "inheritance",  "overrides"]


level = get_level()
guesses = get_number_of_guesses()
blanks = 5
    
quizz(level, guesses, blanks)    
