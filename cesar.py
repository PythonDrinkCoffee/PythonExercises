import string
# Szyfr cezara
def correct_offset(offset):
    if offset >= 0 and offset <= len(list(string.ascii_lowercase+string.punctuation)) :
        return True
    return False

def resolver(text, main_alphabet, from_alphabet):
    resolve_text = ''
    for letter in text:
        if letter != ' ':
            resolve_text += main_alphabet[ from_alphabet.index(letter) ]                 
        else:
            resolve_text += ' '
    return resolve_text

def shift(alphabet='', offset=0):
    alphabet = alphabet[:] # here must be copy of list!!!
    # working on original list and original references 
    # is dangerous and making unexpected results
    #     
    for x in range(0, offset):
        alphabet.insert(len(alphabet), alphabet.pop(0))
    return alphabet

def decrypt_cesar(text='', offset=0):
    alphabet = list(string.ascii_lowercase+string.punctuation)
    text = list(text)
    shifted_alphabet = shift(alphabet, offset)
    decoded = resolver(text, alphabet, shifted_alphabet)

    return decoded


def encrypt_cesar(text='', offset=0):            
    alphabet = list(string.ascii_lowercase+string.punctuation)
    text = list(text)
    shifted_alphabet = shift(alphabet, offset)
    encrypt = resolver(text, shifted_alphabet, alphabet)
            
    return encrypt

option = ''
while option != 'exit':
    logo = """
    ▄████▄  ▓█████   ██████  ▄▄▄       ██▀███  
    ▒██▀ ▀█  ▓█   ▀ ▒██    ▒ ▒████▄    ▓██ ▒ ██▒
    ▒▓█    ▄ ▒███   ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒
    ▒▓▓▄ ▄██▒▒▓█  ▄   ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  
    ▒ ▓███▀ ░░▒████▒▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒
    ░ ░▒ ▒  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
    ░  ▒    ░ ░  ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░
    ░           ░   ░  ░  ░    ░   ▒     ░░   ░ 
    ░ ░         ░  ░      ░        ░  ░   ░     
    ░                                           
    """
    print(u"\u001b[35;1m" + logo + u"\u001b[0m")
    print("Type 'exit' to close the application ")
    
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")     

    match option:
        case 'encode':
            # I know here and below (decode) could be handling errors but I don't have time
            # and it is just exercise
            text = input("Type your message: ").lower()
            offset_number = int(input(f"Type the offset number 0 - {len(string.ascii_lowercase+string.punctuation)}: "))
            if not correct_offset(offset_number):
                print(u"\u001b[35;1m="*50+"\u001b[0m")
                print("OFFSET NUMBER IS NOT CORRECT")
                print(u"\u001b[35;1m="*50+"\u001b[0m")
                continue
                        
            print(u"\u001b[35;1m="*50+"\u001b[0m")
            print(f"Encrypted: " + u"\u001b[32m" + f"{encrypt_cesar(text=text, offset=offset_number)}" + u"\u001b[0m" )
            print(u"\u001b[35;1m="*50+"\u001b[0m")
        case 'decode':
            text = input("Type your message: ").lower()
            offset_number = int(input(f"Type the offset number 0 - {len(string.ascii_lowercase+string.punctuation)}: "))
            if not correct_offset(offset_number):
                print(u"\u001b[35;1m="*50+"\u001b[0m")
                print("OFFSET NUMBER IS NOT CORRECT")
                print(u"\u001b[35;1m="*50+"\u001b[0m")
                continue
            
            print(u"\u001b[35;1m="*50+"\u001b[0m")
            print(f"Decoded: " + u"\u001b[32m" + f"{decrypt_cesar(text=text, offset=offset_number)}" + u"\u001b[0m" )        
            print(u"\u001b[35;1m="*50+"\u001b[0m")
        case 'exit':
            print(u"\u001b[35;1m="*50+"\u001b[0m")
            print("Good bye!")
            print(u"\u001b[35;1m="*50+"\u001b[0m")
        case _:
            print(u"\u001b[35;1m="*50+"\u001b[0m")
            print(" Wrong option please try again ")
            print(u"\u001b[35;1m="*50+"\u001b[0m")
            continue
   
