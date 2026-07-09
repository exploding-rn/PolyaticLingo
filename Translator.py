from pygal import Bar

#Uncomment the one you want to use (delete the first hashtag and make sure only one langauge is uncommented)

#usercodechoice = ' zxcvbnmlkjhgfdsaqwertyuiop.,/?!@#$%^&*()1234567890 ' #1
#usercodechoice = ' asdfghjklqwertyuiopzxcvbnm.,/?!@#$%^&*()1234567890 ' #2
#usercodechoice = ' qwertyuiopzxcvbnmasdfghjkl.,/?!@#$%^&*()1234567890 ' #3
#usercodechoice = ' abcdefghijklmnopqrstuvwxyz.,/?!@#$%^&*()1234567890 ' #4
#usercodechoice = ' qazwsxedcrfvtgbyhnujmikolp.,/?!@#$%^&*()1234567890 ' #5
#usercodechoice = ' polikmujnyhbtgvrfcedxwszqa.,/?!@#$%^&*()1234567890 ' #6
usercodechoice = ' zxcvbnmlkjhgfdsaqwertyuiop ' #OG (declans)
backwards = usercodechoice[::-1]
code = {usercodechoice[i]: backwards[i] for i in range(len(usercodechoice))}
def repeatencode():
    usertexttoencode = input('what text to encode')

    def atbash(text):
        text = text.lower()
        output = ''
    
        for letter in text:
            if letter in code:
                output += code[letter]
    
        return output
        drawtextoutputofencodedecode = output
    print(atbash(usertexttoencode))
repeatencode()


    
