text = "tqjzfxfdemcplvespwlhozteezdptkpazhpctylwwzespcnldpdzmdpcgptetnlxptdlhtnzybfpcpotetdmpeepcezncplepeslyezwplcyncpletyrtdesppddpynpzqwtqpldlcfwpxpyhzccjxzcplmzfehsleespjnlyedppeslylmzfehsleespjnlytetdpldtpcezqtyoxpyhszhtwwgzwfyeppcezotpeslyezqtyoeszdphszlcphtwwtyrezpyofcpaltyhtesaletpynp"

deciphered = ''

def find_key(val):
    for key,value in alphabet.items():
        if val == value:
            return key
        
    return "Key Doesn't Exist"


alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 
            'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}


for i in range(1,26):
    for j in range(0,len(text)):
        letter_num = alphabet[text[j]]

        if letter_num+i > 26:
            left_over = (letter_num+i)-26
            letter = find_key(left_over)
        else:
            letter = find_key(letter_num+i)

        deciphered += letter

    print(f"[{i}]: ")
    print(deciphered)
    deciphered = ''
    print("\n")



