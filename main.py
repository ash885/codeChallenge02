# BigAndSmall Numbers Game Python Program
# I have a little more than 50 lines because you asked to have "verbose comments" Verbose means "expressed in more words
# than needed, so I wanted to do what you said. I hope this will be acceptable. I also ran out of time before I could
# make it so that the unused attempts don't show, but I can keep working on it if you ask me to and will accept it.
# I'm submitting the basic requirements tonight though because it is due tonight. Thank you!
# I started by importing the numpy library that helps with arrays using comprehensive mathematical functions to complete
# tasks. I then created variables. The largest and smallest have a value of none so they can change their data type to
# anything later in the program, rather than making them a certain type before we actually use them. Then I set up the
# array variable to show the max integers a user can put in for the game. The num_of_try variable keeps track of how
# times the loop has iterated so that you don't pass the 20 integer max intended. The second array is for the invalid
# attempts made by the user, like if they type a word. I limited it to 5 non number inputs. Then the clean_input clears
# out the error when there is a non number entry made, so that the program can continue as intended and not crash. It
# is initialized as true because everything is fine until the user uses a non number. Then it turns to false when it
# "sees" the exception. Then we go through the if statements where it says as long as the user hasn't typed done and
# is still entering numbers, up til 20, (I changed it to 19 because we count 0) the game goes on as usual, recording the
# inputs and organizing them to find the largest and smallest. Then I have the output portion that the player actually
# sees when they play. It shows results: largest and smallest number, invalid attempts, and all the users input entries.
# TODO 01:
import numpy as np
print(np.__version__)
# TODO 02:
largest = None
smallest = None
user_int_array = np.array(
    [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999])
num_of_try = 0
user_str_array = np.array(
    ["Invalid Attempt 1", "Invalid Attempt 2", "Invalid Attempt 3", "Invalid Attempt 4", "Last Invalid Attempt 5"])
# TODO 03:
clean_input = None
clean_input = True
# TODO 04:
print("\n\n Welcome to the Big And Small Numbers game. Enter up to 20 integers and/or enter done to")
print("   stop the game. WARNING: You will get an error if you enter anything other than a number.\n\n")
# TODO 4.1:
num = input("Enter a only numbers or the word (\"done\" to stop): ")
# TODO 4.2:
largest = num
smallest = num
num_of_try = 0
num_of_user_strs = 0
while True:
    clean_input = True
    if num == "done" or num_of_try == 19:
        break
    try:
        (isinstance(int(num), int))
    except:
        print("Invalid input")
        clean_input = False
        user_str_array[num_of_user_strs] = num
        num_of_user_strs += 1
    if clean_input:
        num = int(num)
        if int(num) > int(largest):
            largest = num
        if int(num) < int(smallest):
            smallest = num
        user_int_array[num_of_try] = int(num)
    num_of_try = num_of_try + 1
    num = input("Enter a number (\"done\" to stop): ")
print()
print("************************************************************************************************")
print("****** Thank you for playing the Big and Small Numbers game! Your results are below ************")
print("************************************************************************************************\n")
print("Largest number is ", largest)
print("Smallest number is ", smallest)
print("\nUser input was: ")
for item in user_int_array:
    print(item)
print("\n\n")
print("Invalid user input attempts: ")
for item in user_str_array:
    print(item)
print("\n\n")
