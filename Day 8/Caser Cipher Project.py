
def caeser(text , shift , direction):
    caeser_text = []
    for ch in text:
        if ch in alphabet:
            index = alphabet.index(ch)
            if direction == 'encode':
                new_index = index + shift
            elif direction == 'decode':
                new_index = index - shift
            caeser_text.append(alphabet[new_index])
        else:
            caeser_text.append(ch)
    
    if direction == 'encode':
        print(f"Your Encrypted Text is: {''.join(caeser_text)}")
    elif direction == 'decode':
        print(f"Your Decrypted Text is: {''.join(caeser_text)}")

    





ask = ''
while ask != 'no':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caeser(text , shift , direction)
    ask_user = input("Type YEs to restart and no to stop")
    
    if ask_user == 'yes':
        continue
    else:
        ask = 'no'