'''
An atbash cipher usually simply reverses the order of entire range of alphabets.
abc becomes cba
'''
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = intab[::-1] #this will reverse whatever is in intab

def get_crypt():
    input_user = input("Please enter the string you believe is Atbash Crypted > ")
    input_user = input_user.lower()
    print("You entered : " + input_user)
    return input_user

def get_translated(string_input):
    print(string_input.translate({ord(x): y for (x, y) in zip(intab, outtab)}))

if __name__ == "__main__":
    message = get_crypt()
    print("\nHere's what i got:\n")
    get_translated(message)