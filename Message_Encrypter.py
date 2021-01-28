# Johnny Geng, johnnyge@usc.edu

# Description:
# This program uses a shifted alphabet to encrypt a message.
# This program can also automatically decrypt the encrypted message.

def main():

    # set-up:
    message = input("Enter a message: ")
    o_alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = input("Enter a number to shift by (0-25): ")
    number = int(shift)

    # encrypt the message:
    c_alphabet = o_alphabet[number:] + o_alphabet[:number]
    alphaList = list(c_alphabet)
    x = 0
    encryped = ""
    for i in message:
        if i.isalpha():
            x = o_alphabet.find(i)
            i = alphaList[x]
        encryped += i
    print("Encrypting message....")
    print("     Encrypted message: " + encryped)

    # decrypt the message:
    shift_back = c_alphabet[26-number:] + c_alphabet[:26-number]
    y = 0
    decrypted = ""
    for a in encryped:
        if a.isalpha():
            y = shift_back.find(a)
            a = o_alphabet[y-number]
        decrypted += a
    print("Decrypting message....")
    print("     Decrypted message: " + decrypted)

    # print the original message for comparison:
    print("     Oringinal message: " + message)

main()