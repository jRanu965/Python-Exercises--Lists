# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
def shift_string(message, shift_value):
# Create an empty list to store the shifted characters  
    shifted_message = []
# Loop through each character in the string:
    for char in message:
#    If the character is a letter (A-Z or a-z):
        if char.isalpha():
#        Shift the letter by adding the shift value to its ASCII code (use the ord function)
            if char.isupper():
                shifted_char = (ord(char) - ord('A') + shift_value) % 26 + ord('A')
            else:
                shifted_char = (ord(char) - ord('a') + shift_value) % 26 + ord('a')
#        Convert the new ASCII code back to a character (use the chr function)
            shifted_message.append(chr(shifted_char))
        else:
#    If the character is not a letter:
            shifted_message.append(char)
# After the loop, join the list into a string and return it  
    return ''.join(shifted_message)
#        Convert the new ASCII code back to a character (use the chr function)
#        Add the shifted character to the list
#    If the character is not a letter:
#        Add the character unchanged to the list
# After the loop, join the list into a string and return it  
# Get user input for the message and shift value  
# Call the function with the inputs and display the result