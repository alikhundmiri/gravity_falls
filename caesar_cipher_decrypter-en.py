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


# the most common basic english words.
basic_words = [
    "i","a","of","to","in","it","is","be","as","at","so","we","he","by",
    "or","on","do","if","me","my","up","an","go","no","us","am",
    "the","and","for","are","but","not","you","all","any","can","had",
    "her","was","one","our","out","day","get","has","him","his","how","man","new",
    "now","old","see","two","way","who","boy","did","its","let","put","say","she","too","use",
    "that","with","have","this","will","your","from","they","know","want","been","good","much","some","time",
]
# DO NOT CHANGE ANY ON THE BELOW LINES
intab = "abcdefghijklmnopqrstuvwxyz"
d = enchant.Dict("en_US")
translate_this = ""
decrypt_list = []
decrypt_score = []

# Step 1: get the Cryptic string.
def get_crypted():
    translate_this = input("enter the line which you believe is a Caesar Cipher : >>")
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
    shift %= 26  # optional, allows for |shift| > 26
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz' (note: for Python 3, use string.ascii_lowercase instead)
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return shifted_alphabet

# Step 3: For each Key, get the decrypted String.
def get_decrypt(str, outtab):
    word = str.translate({ord(x): y for (x, y) in zip(intab, outtab)})
    is_in_english(word)

# Check if decripted string has the common words.
# If it has common words, it moves to stage 2 check.
def is_in_english(quote):
    each_word = quote.split()
    decrypt_list.append(quote)
    level_2_check(quote)
    #
    # if any(ext in each_word for ext in basic_words):
    #     decrypt_list.append(quote)
    #     level_2_check(quote)
    # else:
    #     decrypt_list.append(quote)
    #     level_2_check(quote)


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
            print(decrypt_list[line] +" - "+ str(probability) + "%")


if __name__ == "__main__":
    crypt = get_crypted()
    get_all_26(crypt)
    print("\nThis is what I came up with :\n")
    show_final_guess(crypt)


# source of common words https://www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html
