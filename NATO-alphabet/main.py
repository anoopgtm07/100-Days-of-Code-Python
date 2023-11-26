student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(value)
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    # print(row.student)
    pass

# Keyword Method with iterrows()
# var = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
# print(var)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dataf = pandas.DataFrame(data)

new_dict = {row.letter: row.code for (index, row) in dataf.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter a name: ").upper()
output = [new_dict[letter] for letter in name]
print(output)