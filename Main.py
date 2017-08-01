# Jumble Game function module

# We're going to create a word jumble game with various modules


import shelve #importing the shelve function
import time #For use on time
import pickle #used when storing scores and time
import random #used to randomise words

#


# --------------------------------------------------------------------------
# Preloaded one word group and shelved them ==================================================

txt_file = open("merry_words.txt", "r")
open_merry = txt_file.read()
merry = open_merry.replace(" ","").replace("\n", "").split(',') #formating
txt_file.close()

# Shelving the preloaded words

shelf = shelve.open("wordgroups.dat")
shelf["merry"] = merry
shelf.sync()
shelf.close()



# ====================================================================================================

# Adding words functioning ==================================================

def addwords():

    try:#Looking to add some sort of error system here if file already

        nameset = input('Please name the set of words you want to added:')
        file_name = input('Please input full file name, Ensure you include the right extension:')
        txt_file = open(file_name, "r")
        open_file = txt_file.read()
        word_set = open_file.replace(" ","").replace("\n", "").split(',')
        txt_file.close()
        shelf = shelve.open("wordgroups.dat")
        shelf[nameset] = word_set
        shelf.sync()
        shelf.close()
        # once succesful print
        print("Successfully added {} as new word set".format(nameset))
        exitfunction = input("Type Enter to go back to main menu")
    except FileNotFoundError:
        print('FILE NOT FOUND! PLEASE ENSURE THE FILE EXISTS IN THE FOLDER!')
        exitfunction = input("Press Enter to restart")
#--------------------------------------------------------------------------------------------

#Browsing words functioning ==================================================

def browseoptions():

    option_number = 1
    options_list = [] #list

    try:
        r = shelve.open("wordgroups.dat")
        for key in r:
            print("{} -- {}".format(option_number, key)) #alternatively we could use print( "%s -- %s" %(option_number, key))
            options_list.append(key)
            option_number += 1
        r.close()
        chosen_option = int(input('Please Select the words you would like to browse:'))
        browse(options_list[chosen_option - 1])
    except IndexError:

        print("Please select from the options above")

def browse(wordset):
# Below the system would print out the word set requested
    print('''
                  +--------------------------------+
                  |                                |
                  |     %s                         |
                  +--------------------------------+
        ''' % (wordset))
    r = shelve.open("wordgroups.dat")
    print (', '. join(r[wordset]))
    r.close()

#=====Eng of browsing======================================================================================



# Delete function listed below

def deleteoptions():
    option_number = 1
    options_list = []
    r = shelve.open("wordgroups.dat")
    for key in r:
        print("{} -- {}".format(option_number, key)) # Check with coral before I submit as this formating is different
        options_list.append(key)
        option_number += 1
    r.close()
    chosen_option = int(input('Please Select:'))
    delete(options_list[chosen_option - 1])
def delete(wordset):
    r = shelve.open("wordgroups.dat")
    del r[wordset]
    print("===============")
    print("{} DELETED!".format(wordset))
    print(" ===========")
    r.close()

#-----------------------------------------------------------------------------------------------

# The jumble game===========================================================

def game():

    shelf = shelve.open("wordgroups.dat")
    groupname = list(shelf.keys())
    #shelf.close()

    a = 1

    for i in groupname:
        print("%s---%s"% (groupname.index(i)+1, i)) #Linking keys from the wordlists
        # or print("{}---{}".format(groupname.index(i)+1, i)) learnt from Codeacademy
    while a==1:

        try:
            chosen_opt= int(input("Please select a word group to begin the game: "))
            word_set = (groupname[chosen_opt - 1])
            wordgroup = shelf[word_set]

            for i in range(10): #limit it to ten attempts

                score_count = 0
                word = random.choice(wordgroup)
                theWord = word
                jumble = "" #Let us jumble the word

                # This code  is referenced from Corals handbook

                while (len(word) > 0):

                    position = random.randrange(len(word))
                    jumble += word[position]
                    word = word[:position] + word[position + 1:]
                print("The jumble word is: {}".format(jumble))

                guess = input("Please enter your Guess: ").lowe()
                #guess.lower() #Not working
                #If the guess is correct congratulate the player!!
                if (guess == theWord):
                    print("Congratulations! You guessed Correct!")
                    score_count += 1
                else:
                    print("Thats Incorrect!!, The right word is {}".format(theWord))
            break # Once the range of 10 has been reached break back to main menu
        except ValueError:
            print("Please select using numbers") # If the user doesnt enter a number
        except IndexError:
            print("PLEASE SELECT FROM THE AVAILABLE OPTIONS!!") #If option chosen isnt available




    #Inform them of their score
    print("You scored %s out of 10" %(score_count)) #Converting the score count into a string
    #put spaces because of commenting
    scores = str(score_count) #Same as above we ensure the the score is turned into a string

    times = time.ctime() #We collect a time stamp on with this function

    time_score = '%s    %s'%(scores, times) ## put them together we have time scored

    print(time_score) #So the user can see time and score

    f = open("myscores.dat", "wb")
    pickle.dump(time_score, f)
    f.close()


def scores(): #Presenting previous dated scores to the user.
    f = open('myscores.dat', 'rb')
    scores = []
    while True:
        try:
            scores.append(pickle.load(f))
        except EOFError:
            break
        #f.close()
    d = scores

    sort_score = []

    for i in range(len(d) - 1, -1, -1):
            sort_score.append(d[i])
            print('+------------------------------+')
            print('|Score        Time             |')
            print('+------------------------------+')
    for a in sort_score:
            print(a)
            print('--------------------------------')








