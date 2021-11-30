# Isakov V.E.

# since python does not have built-in array classes I'm gonna use numpy arrays
import numpy as np

alphabet = {
    'а' : 1,
    'б' : 2,
    'в' : 22,
    'г' : 8,
    'ґ' : 7,
    'д' : 4,
    'е' : 5,
    'ж' : 34, # zh
    'з' : 26,
    'и' : 25,
    'і' : 9,
    'к' : 11,
    'л' : 12,
    'м' : 13,
    'н' : 14,
    'о' : 15,
    'п' : 16,
    'р' : 18,
    'с' : 19,
    'т' : 20,
    'у' : 21,
    'ф' : 6,
    'х' : 19, # kh
    'ц' : 39, # ts
    'ч' : 11, # ch
    'ш' : 27, # sh
    'щ' : 38, # shch
    "'" : 0,
    'ь' : 0
}

def vectorizer(file_name):
    with open(file_name, encoding='utf8') as f:
        text = f.read()

        sum = 0
        row = [] # list for current sentence
        matrix = [] # two dimensional list for whole text
        previous = ' ' # variable for some letters

        for letter in text.lower():
            if(letter.isalpha()):
                if(letter == 'є'): # some letters in the beginning of the word and other position have different transliteration
                    if(previous == ' '):
                        sum += 30 # ye
                    else:
                        sum += 14 # ie
                elif(letter == 'ї'):
                    if(previous == ' '):
                        sum += 34 # yi
                    else:
                        sum += 9 # i
                elif(letter == 'й'):
                    if(previous == ' '):
                        sum += 25 # y
                    else:
                        sum += 9 # i
                elif(letter == 'ю'):
                    if(previous == ' '):
                        sum += 46 # yu
                    else:
                        sum += 30 # iu
                elif(letter == 'я'):
                    if(previous == ' '):
                        sum += 26 # ya
                    else:
                        sum += 10 # ia
                else:
                    sum += alphabet[letter]
            elif(letter == ' '): # end of word
                if(sum):
                    row.append(sum)
                    sum = 0
            elif(letter == '.' or letter == '\n'): # end of sentence
                matrix.append(row)
                row = []
                sum = 0
            previous = letter

        # if there was a single sentence without point mark
        if(not matrix and row):
            matrix.append(row)

        # make rows length equal to convert into the matrix
        if(matrix):
            max_len = len(max(matrix, key=len))
            temp = [row + [0] * (max_len - len(row)) for row in matrix]
            return(np.array(temp))
        # if text file is empty
        return(-1)

print(vectorizer("text.txt"))