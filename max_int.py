# Program finds the maximum positive integer input by user

max_int = 0
# get continuous input from the user until a negative value is entered
# as the user inputs values save it as a variable
num_int = int(input("Input a number: "))    # Do not change this line
while num_int >= 0:          # when a negative value is input stop asking for input
    if num_int > max_int:    # if the next value input is larger than the one currently saved as the max overwrite with the higher value
        max_int = num_int    
    num_int = int(input("Input a number: "))

# print the currently saved highest input and end the program
print("The maximum is", max_int)    # Do not change this line