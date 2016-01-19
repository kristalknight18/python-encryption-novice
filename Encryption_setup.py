#Deployment program for encryption/decryption script.
import random
# strings from string module


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
punctuation = "!@#$%^&*()_-><.,"
printable = digits + ascii_letters + punctuation

string_list = [] # make a list for the characters.
string_list = list(printable) #populate the list with characters from string mod.
list_len = len(string_list)# counter for looping purposes.
n = 0 # handy dandy counter.
encrypt = {} #encryption dictionary, keys are characters and values n.
decrypt ={} #decryption dictionary, keys are n and values characters.

while n < list_len:
    popped = random.choice(string_list)
    encrypt[popped] = (n);
    decrypt[n] = (popped);
    string_list.remove(popped)
    n = n + 1

encrypt_module = ("""#/usr/bin/env python3
###This is  an encryption module.                                               ###
###The module takes a password, splits the characters and converts them         ###
###to different values one by one. The end result is a HEX and remainder        ###
###per character converted.  The system uses random generated pins, in order    ###
###to encode the passwords. This Means that the pin is crucial for decoding the ###
###the password.                                                                ###
###################################################################################
###################################################################################
###################################################################################
import random
#function to print and write code
def msg(): 
    pass_txt = open('encrypted.py', 'w')
    pass_txt.write('import decryption')
    pass_txt.write('\\n')
    pass_txt.write("#copy this and paste in the file with encrypted password")
    pass_txt.write("\\n")
    pass_txt.write('hex_encr = ' + str(hex_encr))
    pass_txt.write('\\n')
    pass_txt.write('pin = ' + str(pin_joined))
    pass_txt.write('\\n#pw will be the password.\\n')
    pass_txt.write('pw = decryption.decrypting(hex_encr, pin)')
    pass_txt.write('\\n#make sure to add pw = 0 at the end of your file')
    pass_txt.close()
    print('the dictionary value is: ')
    print('hex_encr = ' + str(hex_encr))
    print('The PIN is: ' + str(pin_joined))
    print('This information has been written in encrypted.txt')

#Generate Pin, can't be 0 or 1
def PIN(pin):   
    n = 0 #general counter
    while n < 4:
        pin.append(random.randrange(2,10,1))
        n = n + 1
    return pin
pin = []
PIN(pin)
pin_3 = pin[2]
pin_joined = (''.join(str(x) for x in pin))


#Have Password split into list where each character is a list item
password = input('Type the password you wish to encrypt: ')
pass_list = list(password)
pass_len = len(password)

#random dictionary list
\nencrypt = """ + str(encrypt) +
"""

n = 0 #general counter
semi_enc = []
while n < pass_len:  #assigns the numbers for the list item
    semi_enc.append(encrypt[pass_list[n]])
    n = n + 1


#Encoding formula. Values will be converted into a dict containing dict[n] = (HEX,remainder);
n = 0 #counter reset
hex_encr = {}
while n < len(semi_enc):
    pass_thru = [] # need to make a list that will reset per cycle
    y = ((((semi_enc[n])**pin_3)*int(pin_joined)) // 432)
    z = ((((semi_enc[n])**pin_3)*int(pin_joined)) % 432)
    pass_thru.append(hex(y))
    pass_thru.append(z)
    hex_encr[n] = pass_thru ;
    n = n + 1
msg()
#reset values so they won't be recalled from shell
n=0
while n < 42: #resets value 42 times before ending
    pin = []
    password = ''
    pass_list = []
    pass_len = 0
    hex_encr = {}
    semi_enc = []
    pin_joined = 0
    pass_thru = []
    pin_3 = 0
    break
""")

decrypt_module = ("""#!/usr/bin/env python3

#Decription module, would need to be imported from program with password
#the reset values need to be typed in program with encrypted password
#to erase decrypted password from memory
#need pin and dictionary


#randomly generated dictionary

\ndecrypt =""" + str(decrypt) + """

#password is imported from other files

def decrypting(hex_encr, pin):
    pin_list = list(str(pin)) # can't conver ints to lists without converting to str first

    pin_3 = pin_list[2]

    pass_len = len(hex_encr.values()) #how many passes on the decoding process

    #need to separate the elements in the dictionary and reverse the encoding formula

    n = 0 #handy dandy counter
    password = []
    while n < pass_len:
        y = int(hex_encr[n][0], 16) #hex to dec
        x = (((( y * 432) + int(hex_encr[n][1]))/pin)**(1/int(pin_3))) # reverse to value for finding key
        x = int(x)
        password.append(x)
        n = n + 1

    #indexing is stored in password, now retrieve the value
    pass_decryp = [] # make list to store values
    n = 0
    while n < pass_len:
        pass_decryp.append(decrypt[password[n]])
        n = n + 1

    pass_fin = ''.join(pass_decryp)
    return pass_fin""")
    
### write modules###
encryption_file = open('encryption.py','w')
encryption_file.write(encrypt_module)
encryption_file.close()

encryption_file = open('decryption.py','w')
encryption_file.write(decrypt_module)
encryption_file.close()

print("""
import decryption

### This is the code inserted in the file in which you want your password
### Copy and paste encrypted.txt under here



###
pw = decryption.decrypt(hex_encr, pin)

""")
