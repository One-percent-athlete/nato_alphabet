import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

x = True
while x:
    user_input = input("What is your name?").upper()
    try:
        name_list = [nato_dict[n] for n in user_input if n != " "]
        print(name_list)
        x = False
    except KeyError:
        print("Only alphabets are accepted")
