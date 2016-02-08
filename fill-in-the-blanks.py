# IPND Stage 2 Final Project

#A dictionary to hold the paragraphs for each of the levels
paragraphs = dict()
paragraphs["easy"] = \
"""A string is a sequence of one or more __1__ surrounded by quotes. If you start
a string with a single quote you have to end it with a __2__ quote. If you start 
a string with a __3__ quote you have to end it in a double quote. Using the 
plus operator we can __4__ two or more strings together. The index of the first
character of a string is __5__."""

paragraphs["medium"] = \
"""Strings are __1__table while lists are __2__table. Immutable objects cannot be
__3__ed once they are created. As a result string objects do not support item 
__4__. It is called __5__ when there are two names that refer to the same object."""

paragraphs["hard"] = \
"""An __1__ variable is a variable that is unique to each instance of a class and
it is defined __2__ a method of the class. __3__ variables are for attributes 
shared by all instances of the class. __4__ is the transfer of characteristics
of a class to other classes that are derived from it. When a method defined in
a derived class has the same name as a method in it's base class it __5__ the 
method in the base class."""

#A dictionary containing 3 lists of answers.
answers = dict()
answers["easy"] = ["characters", "single", "double", "concatenate",  "0"]
answers["medium"] = ["immu", "mu", "chang", "assignment", "aliasing"]
answers["hard"] = ["instance", "within", "Class", "Inheritance",  "overrides"]


def verify_level(choice):
    """Check if player entered a valid difficulty level."""
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
        choice = raw_input("Possible choices include easy, medium, and hard: ")
        choice = choice.lower()
        verified = verify_level(choice)
        
    print "You've chosen {}!\n".format(choice)
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
    """Check if player provided the correct answer."""
    current_answer = answers[level][count - 1]
    if response.lower() == current_answer.lower():
        return True
    else:
        return False
    

def display_current_paragraph(level):
    """ Prints out the current paragraph """
    print "The current paragraph reads as such:\n"
    print paragraphs[level]
    print

def update_current_paragraph(level, count):
    """Update the current paragraph with the correct answer.
    count: Keeps track of the current blank/answer pair.
    """
    current_blank = "__{}__".format(count)
    current_answer = answers[level][count - 1]
    paragraphs[level] =  paragraphs[level].replace(current_blank, current_answer)
    

def play_quizz(level, guesses, blanks):
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
                    print "That isn't the correct answer!  Let's try again; you have {} trys left!\n".format(trys_left)
                else:
                    print "You've failed too many straight guesses!  Game over!"
                    return
    display_current_paragraph(level)
    print "You won!\n"
            


level = get_level()
guesses = get_number_of_guesses()
blanks = 5
    
play_quizz(level, guesses, blanks)    
