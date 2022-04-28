# Write a program that lets the user enter in some English text, then converts the text to Pig-Latin. Pig-Latin takes the first 
# letter of a word, puts it at the end, and appends "ay". The only exception is if the first letter is a vowel, in which case 
# we keep it as it is and append "hay" to the end.
# E.g. "hello" -> "ellohay", and "image" -> "immagehay"
# It will be useful to define a list or tuple at the top called VOWELS. This way, you can check if a letter x is a vowel with the 
# expression x in VOWELS.
# Ask the user to only enter words and spaces. You can convert their input from a string to a list of strings by calling split 
# on the string.
# Using this list, you can go through each word and convert it to Pig-Latin. Also, to get a word except for the first letter, 
# you can use word[1:].


VOWELS = ("A","a","E","e","I","i","O","o","U","u")

phrase = input("Enter only words and spaces:")
# We first split the phrase into an array of individual words and called it "separated_phrase"
separated_phrase = phrase.split(" ")
for word in separated_phrase:
    starts_with_vowel = False
    for x in VOWELS:
        if x == word[0]:
            # Changes the variable starts_with_vowel to TRUE, indicating the word starts with a vowel to differentiate from those that don't. This ensures the word is not 
            # analyzed again by the next if statement and instead moves on to the next word through the use of break.
            starts_with_vowel = True
            print (word + "hay")
            break
        continue
    # This if statement indicates the first letter of the word does not start with a vowel and therefore has not yet been altered to a Pig-Latin word.
    if starts_with_vowel == False: 
        # Here we saved the first letter of the word so that we can add it to the end followed by "ay".
        first_letter = word[0]
        print(word[1:] + first_letter + "ay")
        continue

