from time import sleep
import random

# Get user input for the sentence
word = input("Enter the sentence you want to unfuck: ")

# Define a fixed interval
t = 0.05  # Adjust the interval as needed

# Define character sets
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
random_shite = "1234567890+x÷=/_<>[]!@#*%^&*()-*:;,?`~\\{}€£¥$°•○•□■♡☆<>i¿.."

# Create a list of all possible characters
list_abc = list(abc + ABC + random_shite)

# Initialize the "unfucked" string
unfucked_word = ""

# Process each letter in the input word
for letter in word:
    if letter == " ":  # Handle spaces directly
        unfucked_word += " "
        continue

    while True:
        # Select a random character from the list
        I = list_abc[random.randint(0, len(list_abc) - 1)]
        
        # Print the current state of the unfucked word plus the random character
        print(unfucked_word + I)
        
        # Pause for the specified interval
        sleep(t)
        
        # If the random character matches the correct letter, append it to the unfucked word
        if I == letter:
            unfucked_word += I
            break

# Print the final unfucked word
print(unfucked_word)
