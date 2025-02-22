"""
Projek1.py: první projekt do Engeto Online Python Akademie

author: Martin Rexa
email: martinrexa@seznam.cz
"""
# texty
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
# registrovaní uživatelé
usernames = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# přihlašovací proces
username = input("username:")
password = input("password:")
if username in usernames and usernames[username] == password:
    print("-" * 30)
    print("Welcome to the app,", username, ".")
    print("We have 3 texts to be analyzed.")
    print("-" * 30)
else:
    print("Unregistered user. Terminating the program..")

# nachystané proměnné pro analýzu jednotlivých textů
text1 = list(TEXTS[0].split())
text1_stripped = list()
for word in text1:
        text1_stripped.append(word.strip("!#$%&\'()*+,-./:;=>?@[\\]^_`{|}~"))
text1_title = 0
text1_upper = 0
text1_lower = 0
text1_decimal= 0
text1_sum_of_numbers = 0
text1_lengths = list()

text2 = list(TEXTS[1].split())
text2_stripped = list()
for word in text2:
        text2_stripped.append(word.strip("!#$%&\'()*+,-./:;=>?@[\\]^_`{|}~"))
text2_title = 0
text2_upper = 0
text2_lower = 0
text2_decimal= 0
text2_sum_of_numbers = 0
text2_lengths = list()

text3 = list(TEXTS[2].split())
text3_stripped = list()
for word in text3:
        text3_stripped.append(word.strip("!#$%&\'()*+,-./:;=>?@[\\]^_`{|}~"))
text3_title = 0
text3_upper = 0
text3_lower = 0
text3_decimal= 0
text3_sum_of_numbers = 0
text3_lengths = list()

# výběr textu
selected_text = int(input("Enter a number btw. 1 and 3 to select:"))

# analýza textů
# text 1
if selected_text == 1:
    #počet slov = délka (počet prvků) listu
    print("There are", len(text1_stripped), "words in the selected text.")
    # počet slov začínajících velkým písmenem
    for word in text1_stripped:
        if word.istitle() or word.isupper():
            text1_title = text1_title + 1
        else: continue
    print("There are", text1_title, "titlecase words.")
    # počet slov psaných velkými písmeny
    for word in text1_stripped:
        if word.isupper() and word.isalpha():
            text1_upper = text1_upper + 1
        else: continue
    print("There are", text1_upper, "uppercase words.")
    # počet slov psaných malými písmeny
    for word in text1_stripped:
        if word.islower():
            text1_lower = text1_lower + 1
        else: continue
    print("There are", text1_lower, "lowercase words.")
    # počet čísel (ne cifer)
    for word in text1_stripped:
        if word.isdecimal():
            text1_decimal = text1_decimal + 1
        else: continue
    print("There are", text1_decimal, "numeric strings.")
    # suma všech čísel (ne cifer)
    for word in text1_stripped:
        if word.isdecimal():
            text1_sum_of_numbers = text1_sum_of_numbers + int(word)
        else: continue
    print("The sum of all the numbers", text1_sum_of_numbers)
    print("-" * 30)
    print("LEN| OCCURENCES |NR.")
    print("-" * 30)
    # sloupcový graf četnosti délek slov v textu
    for word in text1_stripped:
        text1_lengths.append(len(word))
    print("1|", "*" * text1_lengths.count(1), text1_lengths.count(1))
    print("2|", "*" * text1_lengths.count(2), text1_lengths.count(2))
    print("3|", "*" * text1_lengths.count(3), text1_lengths.count(3))
    print("4|", "*" * text1_lengths.count(4), text1_lengths.count(4))
    print("5|", "*" * text1_lengths.count(5), text1_lengths.count(5))
    print("6|", "*" * text1_lengths.count(6), text1_lengths.count(6))
    print("7|", "*" * text1_lengths.count(7), text1_lengths.count(7))
    print("8|", "*" * text1_lengths.count(8), text1_lengths.count(8))
    print("9|", "*" * text1_lengths.count(9), text1_lengths.count(9))
    print("10|", "*" * text1_lengths.count(10), text1_lengths.count(10))
    print("11|", "*" * text1_lengths.count(11), text1_lengths.count(11))
    print("12|", "*" * text1_lengths.count(12), text1_lengths.count(12))
    print("13|", "*" * text1_lengths.count(13), text1_lengths.count(13))

# text 2
elif selected_text == 2:
    #počet slov = délka (počet prvků) listu
    print("There are", len(text2_stripped), "words in the selected text.")
    # počet slov začínajících velkým písmenem
    for word in text2_stripped:
        if word.istitle() or word.isupper():
            text2_title = text2_title + 1
        else: continue
    print("There are", text2_title, "titlecase words.")
    # počet slov psaných velkými písmeny
    for word in text2_stripped:
        if word.isupper() and word.isalpha():
            text2_upper = text2_upper + 1
        else: continue
    print("There are", text2_upper, "uppercase words.")
    # počet slov psaných malými písmeny
    for word in text2_stripped:
        if word.islower():
            text2_lower = text2_lower + 1
        else: continue
    print("There are", text2_lower, "lowercase words.")
    # počet čísel (ne cifer)
    for word in text2_stripped:
        if word.isdecimal():
            text2_decimal = text2_decimal + 1
        else: continue
    print("There are", text2_decimal, "numeric strings.")
    # suma všech čísel (ne cifer)
    for word in text2_stripped:
        if word.isdecimal():
            text2_sum_of_numbers = text2_sum_of_numbers + int(word)
        else: continue
    print("The sum of all the numbers", text2_sum_of_numbers)
    print("-" * 30)
    print("LEN| OCCURENCES |NR.")
    print("-" * 30)
    # sloupcový graf četnosti délek slov v textu
    for word in text2_stripped:
        text2_lengths.append(len(word))
    print("1|", "*" * text2_lengths.count(1), text2_lengths.count(1))
    print("2|", "*" * text2_lengths.count(2), text2_lengths.count(2))
    print("3|", "*" * text2_lengths.count(3), text2_lengths.count(3))
    print("4|", "*" * text2_lengths.count(4), text2_lengths.count(4))
    print("5|", "*" * text2_lengths.count(5), text2_lengths.count(5))
    print("6|", "*" * text2_lengths.count(6), text2_lengths.count(6))
    print("7|", "*" * text2_lengths.count(7), text2_lengths.count(7))
    print("8|", "*" * text2_lengths.count(8), text2_lengths.count(8))
    print("9|", "*" * text2_lengths.count(9), text2_lengths.count(9))
    print("10|", "*" * text2_lengths.count(10), text2_lengths.count(10))
    print("11|", "*" * text2_lengths.count(11), text2_lengths.count(11))
    print("12|", "*" * text2_lengths.count(12), text2_lengths.count(12))
    print("13|", "*" * text2_lengths.count(13), text2_lengths.count(13))

# text 3
elif selected_text == 3:
    #počet slov = délka (počet prvků) listu
    print("There are", len(text3_stripped), "words in the selected text.")
    # počet slov začínajících velkým písmenem
    for word in text3_stripped:
        if word.istitle() or word.isupper():
            text3_title = text3_title + 1
        else: continue
    print("There are", text3_title, "titlecase words.")
    # počet slov psaných velkými písmeny
    for word in text3_stripped:
        if word.isupper() and word.isalpha():
            text3_upper = text3_upper + 1
        else: continue
    print("There are", text3_upper, "uppercase words.")
    # počet slov psaných malými písmeny
    for word in text3_stripped:
        if word.islower():
            text3_lower = text3_lower + 1
        else: continue
    print("There are", text3_lower, "lowercase words.")
    # počet čísel (ne cifer)
    for word in text3_stripped:
        if word.isdecimal():
            text3_decimal = text3_decimal + 1
        else: continue
    print("There are", text3_decimal, "numeric strings.")
    # suma všech čísel (ne cifer)
    for word in text3_stripped:
        if word.isdecimal():
            text3_sum_of_numbers = text3_sum_of_numbers + int(word)
        else: continue
    print("The sum of all the numbers", text3_sum_of_numbers)
    print("-" * 30)
    print("LEN| OCCURENCES |NR.")
    print("-" * 30)
    # sloupcový graf četnosti délek slov v textu
    for word in text3_stripped:
        text3_lengths.append(len(word))
    print("1|", "*" * text3_lengths.count(1), text3_lengths.count(1))
    print("2|", "*" * text3_lengths.count(2), text3_lengths.count(2))
    print("3|", "*" * text3_lengths.count(3), text3_lengths.count(3))
    print("4|", "*" * text3_lengths.count(4), text3_lengths.count(4))
    print("5|", "*" * text3_lengths.count(5), text3_lengths.count(5))
    print("6|", "*" * text3_lengths.count(6), text3_lengths.count(6))
    print("7|", "*" * text3_lengths.count(7), text3_lengths.count(7))
    print("8|", "*" * text3_lengths.count(8), text3_lengths.count(8))
    print("9|", "*" * text3_lengths.count(9), text3_lengths.count(9))
    print("10|", "*" * text3_lengths.count(10), text3_lengths.count(10))
    print("11|", "*" * text3_lengths.count(11), text3_lengths.count(11))
    print("12|", "*" * text3_lengths.count(12), text3_lengths.count(12))
    print("13|", "*" * text3_lengths.count(13), text3_lengths.count(13))

else:
    print("You didn´t write valid input.")

