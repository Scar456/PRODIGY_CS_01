# A Python Program that can encrypt and decrypt text using the Caesar Cipher Algorithm
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            #the isalpha() is a string method that checks if all characters in a string  are alphabetic characters (either lowercase / uppercase)

            #shift character within 'A '- 'Z' or 'a' -'z' range
            base = ord('A') if char.isupper() else ord('a')

            if mode == 'encrypt':
                new_char = chr((ord(char) - base + shift) % 26 + base)

            elif mode =='decrypt':
                new_char = chr((ord(char) - base - shift) % 26 + base)  

            result += new_char
        else:
            result += char #Non-alphabet characters remain unchanged 

    return result 

def main():
    print( "Welcome to the Caeser Cipher Program!")

    while True:
        choice = input("Enter 'E' for encryption, 'D' for decryption, or 'Q' to quit:").upper()

        if choice == 'E':
            plaintext = input("Enter the message to encrypt:")
            shift = int(input("Enter the shift value (integer):"))
            encrypted_text = caesar_cipher(plaintext, shift,  mode='encrypt')
            print(f"Encrypted message: {encrypted_text}")

        elif choice == 'D':
             encrypted_text =  input("Enter the message to decrypt:")
             shift = int(input("Enter the shift value used for encryption (integer): "))
             decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
             print(f"Decrypted message: {decrypted_text}")

        elif choice == 'Q':
            print("Exiting program..")
            break

        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

if __name__=="__main__":
    main()
    