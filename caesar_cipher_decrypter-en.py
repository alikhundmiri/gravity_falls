import os
import string

# pip install pyenchant
# this library is used to check if the words in decrypted message are actually english.
import enchant

'''
in a Caesar Cipher, the numbers are rotated clock wise or anti clock wise, it could be any of 26 possibilities.
simple example:
abc-bca
abc-cab
'''

# DO NOT CHANGE ANY ON THE BELOW LINES
intab = "abcdefghijklmnopqrstuvwxyz"
d = enchant.Dict("en_US")
translate_this = ""
decrypt_list = []
decrypt_score = []

# Step 1: get the Cryptic string.
def get_crypted():
    translate_this = input("enter the line which you believe is a Caesar Cipher : >> ")
    translate_this = translate_this.lower()
    print("you entered : " + translate_this)
    return translate_this

# Step 2: get all 26 possible keys, for Caesar Cipher.
def get_all_26(message):
    # rotate the message 26 times
    for x in range(0, 27):
        out = get_outtab(x)
        get_decrypt(message, out)

# Step 2.5: get the single key.
def get_outtab(shift):
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return shifted_alphabet

# Step 3: For each Key, get the decrypted String.
def get_decrypt(str, outtab):
    word = str.translate({ord(x): y for (x, y) in zip(intab, outtab)})
    is_in_english(word)

# Check if decripted string has the valid english words.
# It adds the word to decrypt_list and, moves to stage 2 check.
def is_in_english(quote):
    decrypt_list.append(quote)
    level_2_check(quote)

# Level 2 check will give score.
def level_2_check(line):
    score = 0
    words = line.split()
    for word in words:
        if d.check(word):
            score += 1
        else:
            pass
    decrypt_score.append(score)

# print out the output.
def show_final_guess(input_word):
    total_words = len(input_word.split())
    for line in range(0,len(decrypt_list)):
        probability = decrypt_score[line]/total_words * 100
        if probability >= 20:
            print(decrypt_list[line] +" - "+ str(probability) + "% certain.")


if __name__ == "__main__":
    crypt = get_crypted()
    get_all_26(crypt)
    print("\nThis is what I came up with :\n")
    show_final_guess(crypt)