"""Ask the user for a column number and direction to create a cipher key dictionary."""

number_of_columns = input("How many columns will your key have? ")
key_dictionary = dict()
for number in range(1, int(number_of_columns)+1):
    print(f"This is column #{number}")
    key_dictionary[number] = input("Please type up or down for the direction for this column:  ")

print("Here is your configuration:")
for key, value in key_dictionary.items():
    print(f"Column #{key} has direction: {value}")
