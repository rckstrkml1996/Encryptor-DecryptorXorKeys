
logo = '''
_________________________$$$$$$$________________
________________________$$$$$$$$$$______________
________________________$$$$$$$$$$$_____________
_____rockstarkamel_______$$$$$$$$$$$$$$_________
__________________________$$$$$$$$$$$___________
_____________________________$$$$$$$$$$$$$______
___________________________$$$$$$$$$$___________
_________________________$$$$$$$$$$$$$$$________
________________$$$______$$$$$$$$$$$$$$_________
______________$$$$$$$$_____$$$$$$__$$$$$________
_____________$$$$$$$$$$_____$$$$____$$$$$_______
___________$$$$$$_$$$$$$$$__$$$$______$$$$______
__________$$$$$_____$$$$$$$$_$$$$_______$$$_____
________$$$$$_________$$$$$$$$$$$$_______$$$____
_______$$$_____________$$$$$$$$$$$________$$$___
_____$$$________________$$$$$$$$$$________$$$$$$
__$$$$$$__________________$$$$$$$_______________
██████╗░░█████╗░██╗░░██╗░██████╗████████╗██████╗░██╗░░██╗███╗░░░███╗██╗░░░░░
██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔══██╗██║░██╔╝████╗░████║██║░░░░░
██████╔╝██║░░╚═╝█████═╝░╚█████╗░░░░██║░░░██████╔╝█████═╝░██╔████╔██║██║░░░░░
██╔══██╗██║░░██╗██╔═██╗░░╚═══██╗░░░██║░░░██╔══██╗██╔═██╗░██║╚██╔╝██║██║░░░░░
██║░░██║╚█████╔╝██║░╚██╗██████╔╝░░░██║░░░██║░░██║██║░╚██╗██║░╚═╝░██║███████╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
TG: @rckstrkml
GitHub: https://github.com/rckstrkml1996/Encryptor-DecryptorXorKeys/commits?author=rckstrkml1996


'''
print(logo)
kal = input("Enter choice: [1]Encrypt; [2]Decrypt:")

if kal == "1":
    mytext = input("Write Text:")
    key = input("Write Key:")

    def xor_encrypt(mytext, key):
        xored = "".join(
            chr(ord(x) ^ ord(y))
            for x, y in zip(
                mytext, key * (len(mytext) // len(key)) + key[: len(mytext) % len(key)]
            )
        )
        return xored

    encrypted_text = xor_encrypt(mytext, key)
    print(f"Encrypted text: {encrypted_text}")
    print(f"Key: {key}")

elif kal == "2":
    mytextfordec = input("Write Text:")
    keyfordec = input("Write Key:")

    def xor_decrypt(mytextfordec, keyfordec):
        return "".join(
            chr(ord(x) ^ ord(y))
            for x, y in zip(
                mytextfordec,
                keyfordec * (len(mytextfordec) // len(keyfordec))
                + keyfordec[: len(mytextfordec) % len(keyfordec)],
            )
        )

    decrypted_text = xor_decrypt(mytextfordec, keyfordec)
    print(f"Decrypted text: {decrypted_text}")

else:
    print("Incorrect choice. Please enter 1 or 2.")



