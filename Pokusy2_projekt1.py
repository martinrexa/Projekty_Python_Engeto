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
    exit()

select_text = int(input("Enter a number btw. 1 and 3 to select:"))
if select_text == 1 or select_text == 2 or select_text == 3:
    # nachystané proměnné pro analýzu vybraného textu
    selected_text = TEXTS[select_text - 1]
    selected_text_splitted = list(selected_text.split())
    selected_text_stripped = list()
    for word in selected_text_splitted:
        selected_text_stripped.append(word.strip("!#$%&\'()*+,-./:;=>?@[\\]^_`{|}~"))
    selected_text_title = 0
    selected_text_upper = 0
    selected_text_lower = 0
    selected_text_decimal= 0
    selected_text_sum_of_numbers = 0
    selected_text_lengths = list()

    #počet slov = délka (počet prvků) listu
    print("There are", len(selected_text_stripped), "words in the selected text.")
    # počet slov začínajících velkým písmenem
    for word in selected_text_stripped:
        if word.istitle() or word.isupper():
            selected_text_title = selected_text_title + 1
        else: continue
    print("There are", selected_text_title, "titlecase words.")
    # počet slov psaných velkými písmeny
    for word in selected_text_stripped:
        if word.isupper() and word.isalpha():
            selected_text_upper = selected_text_upper + 1
        else: continue
    print("There are", selected_text_upper, "uppercase words.")
    # počet slov psaných malými písmeny
    for word in selected_text_stripped:
        if word.islower():
            selected_text_lower = selected_text_lower + 1
        else: continue
    print("There are", selected_text_lower, "lowercase words.")
    # počet čísel (ne cifer)
    for word in selected_text_stripped:
        if word.isdecimal():
            selected_text_decimal = selected_text_decimal + 1
        else: continue
    print("There are", selected_text_decimal, "numeric strings.")
    # suma všech čísel (ne cifer)
    for word in selected_text_stripped:
        if word.isdecimal():
            selected_text_sum_of_numbers = selected_text_sum_of_numbers + int(word)
        else: continue
    print("The sum of all the numbers", selected_text_sum_of_numbers)
    print("-" * 30)
    print("LEN| OCCURENCES |NR.")
    print("-" * 30)
    # sloupcový graf četnosti délek slov v textu
    for word in selected_text_stripped:
        selected_text_lengths.append(len(word))
    for cislo in range(1, 20):
        if selected_text_lengths.count(cislo) != 0:
            print(cislo, "| ", "*" * selected_text_lengths.count(cislo), selected_text_lengths.count(cislo))
        else:
            continue
else:
    print("You didn´t write valid input.")
    exit()
