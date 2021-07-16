###
#-------------------------------------------------------------------------------
# readability.py
#-------------------------------------------------------------------------------
#
# determine the reading level of a particular text
#
# Gemaakt door: Susanne Becker
#
###

from cs50 import get_string

def main():    
    # Get input from the user
    s = get_string("Text: ");

    letters = 0;
    words = 1;
    sentences = 0;
    counter = 0;
    
    for i in s:
        counter += 1
    
    # Determine number of words, sentences and letters
    for i in range(counter):

        if (ord(s[i]) >= 65 and ord(s[i]) <= 90 or ord(s[i]) >= 97 and ord(s[i]) <= 122):
            letters += 1

        elif (ord(s[i]) == 32):
            words += 1

        elif (ord(s[i]) == 33 or ord(s[i]) == 46 or ord(s[i]) == 63):
            sentences += 1


    # Calculate the index
    L = (letters / words) * 100.0;
    S = (sentences / words) * 100.0;
    index = (0.0588 * L) - (0.296 * S) - 15.8;
    grade = round(index);
    
    # Determine the reading level
    if (grade < 1):
        print("Before Grade 1")

    elif (grade >= 16):
        print("Grade 16+")

    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
