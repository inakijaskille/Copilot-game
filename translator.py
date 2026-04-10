"""
Alien communication translator module.
Provides functions to encode and decode alien messages.
"""


def alien_translator(text):
    """
    Replace all vowels in text with asterisks to create alien-encoded text.
    
    This function takes any input string and replaces each vowel (both
    lowercase and uppercase) with an asterisk (*), creating an encoded
    "alien" version of the message.
    
    Args:
        text (str): The text to translate
        
    Returns:
        str: The translated text with vowels replaced by asterisks
    """
    vowels = "aeiouAEIOU"
    translated = ""
    
    # Loop through each character in the text
    for char in text:
        if char in vowels:
            translated += "*"
        else:
            translated += char
    
    return translated


def decode_message(text):
    """
    Attempt to reverse an alien translation (simple approach).
    
    This function replaces asterisks with the most common vowel 'e'
    as a reasonable approximation for decoding. This is not perfect
    but demonstrates the reverse operation.
    
    Args:
        text (str): The alien-encoded text
        
    Returns:
        str: The decoded message with asterisks replaced by 'e'
    """
    # Simple decoding: replace asterisks with 'e' (most common vowel)
    return text.replace("*", "e")


# Test the translator with example outputs
if __name__ == "__main__":
    # Example 1
    original_message_1 = "Hello from Earth"
    encoded_1 = alien_translator(original_message_1)
    decoded_1 = decode_message(encoded_1)
    print(f"Original: {original_message_1}")
    print(f"Encoded:  {encoded_1}")
    print(f"Decoded:  {decoded_1}\n")
    
    # Example 2
    original_message_2 = "Welcome to the space station"
    encoded_2 = alien_translator(original_message_2)
    decoded_2 = decode_message(encoded_2)
    print(f"Original: {original_message_2}")
    print(f"Encoded:  {encoded_2}")
    print(f"Decoded:  {decoded_2}")
