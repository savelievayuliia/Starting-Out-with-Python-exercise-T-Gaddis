import csv


def letters_to_symbols_transcription():
    with open("letters_to_symbols.csv", newline='') as file:
        codes = csv.reader(file, delimiter=";")
        symbols_dictionary = {}
        for number in codes:
            symbols_dictionary[number[0]] = number[1]
        symbols_dictionary["\n"] = "\n"
        symbols_dictionary["\t"] = "\t"
        return symbols_dictionary


def encoding_text_file_to_symbols():
    file = input("Enter file name in .txt format."
                 " We will encode that file to symbols: ")
    with open(file, "r") as text_file:
        temporary_file = text_file.readline()
        transcription = letters_to_symbols_transcription()
        with open("encoded_file.csv", "w") as encoded_text_file:
            for i in temporary_file:
                encoded_symbol = transcription[i] + "~"
                encoded_text_file.write(encoded_symbol)
            return "encoded_file.csv"


def symbols_to_letters_transcription():
    encoded_file = encoding_text_file_to_symbols()
    print("Now we will return the encoded text again"
          "and print it here: ")
    symbols_dictionary = letters_to_symbols_transcription()
    dict_reversed = dict(zip(symbols_dictionary.values(), symbols_dictionary.keys()))
    with open(encoded_file) as file:
        words = csv.reader(file, delimiter="~")
        for word in words:
            for letter in word:
                try:
                    reversed_word = dict_reversed[letter]
                    print(reversed_word, end="")
                except KeyError:
                    print("A certain key is missing")


symbols_to_letters_transcription()
