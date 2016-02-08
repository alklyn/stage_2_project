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

def display_paragraph(paragraph):
    """ Prints out the current paragraph """
    print "The current paragraph reads as such:\n"
    print paragraph
    print

def update_paragraph(paragraph, answer, count):
    """Update the current paragraph with the correct answer.
    count: Keeps track of the current blank.
    """
    current_blank = "__{}__".format(count)
    return  paragraph.replace(current_blank, answer)
    

def play_quizz(paragraph, current_answers, guesses):
    """Fill in the blanks game.
    The quiz will prompt a user with a sentence containing several blanks. The user 
    is then be asked to fill in each blank appropriately to complete the sentence.
    """
    for index, answer in enumerate(current_answers):
        trys_left = guesses
        
        while trys_left > 0:
            display_paragraph(paragraph)
            response = raw_input("What should go in blank number {}? ".format(index + 1))
            
            if response.lower() == answer.lower():
                print "\nCorrect!\n"
                paragraph = update_paragraph(paragraph, answer, index + 1)
                break
            else:
                trys_left -= 1
                if trys_left > 0:
                    print "That isn't the correct answer!  Let's try again; you have {} trys left!\n".format(trys_left)
                else:
                    print "You've failed too many straight guesses!  Game over!"
                    return
    display_paragraph(paragraph)
    print "You won!\n"
            


level = get_level()
current_paragraph = paragraphs[level] #get paragraph for current level
current_answers = answers[level] #Get list of answers for current level
guesses = get_number_of_guesses()    
play_quizz(current_paragraph, current_answers, guesses)    
