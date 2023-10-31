"""
Assignment 8: "Linguistic Analysis"

Author: Kirti Subramanian
CWID: 20531478
Date: 11/19/2022

Program Description: This program prompts the user for the name of a file and reports the
frequency of each letter of the alphabet in the file, regardless of the case.
"""

from assignment7 import find_file


def compute_frequencies(f):
    """
    Computes the number of occurrences of each letter in the input file.
    :param f: input file
    :return: total number of letters in the file and a dictionary containing
    the letters and their number of occurrences
    """
    letter_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                    "m": 0,
                    "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
                    "z": 0}
    total_letters = 0
    for line in f.readlines():
        line = line.lower()
        for letter in line:
            if letter in letter_count:
                total_letters += 1
                letter_count[letter] += 1
    return total_letters, letter_count


def print_frequencies(total_letters, letter_count):
    """
    Prints the frequency of each letter as a percentage.
    :param total_letters: the total number of letters
    :param letter_count: dictionary containing the letters and their number of occurrences
    :return: none
    """
    print("The frequency of each letter in your file:")
    for letter in letter_count:
        print(letter + ": " + '{0:.3g}'.format((letter_count[letter] / total_letters) * 100) + "%")


def main():
    # open the file
    f = find_file()
    # compute the frequencies
    total_letters, letter_count = compute_frequencies(f)
    # print the frequencies
    print_frequencies(total_letters, letter_count)


if __name__ == "__main__":
    main()

# test
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment8.py
What is the name of the file you would like to process? data.txt
The frequency of each letter in your file:
a: 7.42%
b: 1.02%
c: 2.69%
d: 2.62%
e: 13.2%
f: 4.15%
g: 1.75%
h: 5.02%
i: 6.4%
j: 0.146%
k: 0.364%
l: 4.95%
m: 2.18%
n: 5.53%
o: 7.13%
p: 2.77%
q: 0.437%
r: 7.21%
s: 6.19%
t: 11.6%
u: 3.93%
v: 0.291%
w: 0.946%
x: 0.146%
y: 1.82%
z: 0.0728%

Process finished with exit code 0
"""