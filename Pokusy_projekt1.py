TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.'''
]
text1 = list(TEXTS[0].split())
text1_stripped = list()
for word in text1:
        text1_stripped.append(word.strip("!#$%&\'()*+,-./:;=>?@[\\]^_`{|}~"))
print(text1_stripped)
text1_lengths = list()
for word in text1_stripped:
        text1_lengths.append(len(word))
print(text1_lengths)
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