# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def convert_to_nato_alphabet():
    """You Have to use only letters"""

    word = input("Enter a word: ").upper()
    try:
        if word == "exit".upper(): return
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        convert_to_nato_alphabet()
    else:
        print(output_list)


convert_to_nato_alphabet()
