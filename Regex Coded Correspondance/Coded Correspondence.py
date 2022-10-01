# Casual Coded Corrspondence

# In this project, you will be working to code and decode various messages between you and your fictional cryptography enthusiast pen pal.
# Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar Cipher.
# Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset.
# For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet).
# So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"!
# Now I can send you my message and the offset and you can decode it.
# The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool!
# Okay, now I'm going to send you a longer coded message that you have to decode yourself!


message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"


# Decoding the message

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
translated_message = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)


# Sending a Coded Reply

message_for_pal = "hey pal! This is a super cool cipher, thanks for showing me! What else you got?"
translated_reply = ""
for letter in message_for_pal:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_reply += alphabet[(letter_value - 10) % 26]
    else:
        translated_reply += letter
print(translated_reply)


# Reply Messages from Pal

message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
    
def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

print(decoder(message_one, 10))
print(decoder(message_two, 14))



# Vigenere Decoder (Multiple Caeser Cipher, without knowing the shift spaces)

def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))



