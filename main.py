# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
def shift_string(message, shift_value):
def shift_string(message: str, shift_value: int) -> str:
    """Return a new string with each ASCII letter shifted by `shift_value`.

    Non-letter characters are left unchanged. Letter wrapping preserves case.
    """
    shifted_message = []
    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted_char = (ord(char) - ord('A') + shift_value) % 26 + ord('A')
            else:
                shifted_char = (ord(char) - ord('a') + shift_value) % 26 + ord('a')
            shifted_message.append(chr(shifted_char))
        else:
            shifted_message.append(char)
    return ''.join(shifted_message)


if __name__ == "__main__":
    input_message = input("Enter a message to shift: ")
    try:
        input_shift = int(input("Enter the shift value (number of positions to shift): "))
    except ValueError:
        print("Invalid shift value; please enter an integer.")
    else:
        print(shift_string(input_message, input_shift))
