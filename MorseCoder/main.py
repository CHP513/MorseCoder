# Charles (Chip) Brady
# June 2026
# This project is able to read an input on a string and not only outputs the string
# into Morse code, but also immediately reads the dot's and dashes to produce the corresponding sound.

import tkinter as tk
import os
from tkinter import END

import pygame

pygame.mixer.init()

# Setup for Sound Paths
BASE_DIR = os.path.dirname(__file__)
DOT_SOUND = os.path.join(BASE_DIR, "dot.wav")
DASH_SOUND = os.path.join(BASE_DIR, "dash.wav")

DOT = pygame.mixer.Sound(DOT_SOUND)
DASH = pygame.mixer.Sound(DASH_SOUND)

DOT_LENGTH = 100
DASH_LENGTH = 300
LETTER_SPACE = 200
WORD_SPACE = 700

# Error check for dot.wav and dash.wav sound file
if not os.path.exists(DOT_SOUND):
    raise FileNotFoundError(f"Missing file: {DOT_SOUND}")

if not os.path.exists(DOT_SOUND):
    raise FileNotFoundError(f"Missing file: {DASH_SOUND}")

# Prevent Multiple Playbacks with is_playing check
is_playing = False

# Dictionary of Morse Code
MORSE_CODE = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    "!":"-.-.--",
    "?":"..--..",
    ".":".-.-.-",
    ",":"--..--",
    ":":"---...",
    " ": " "
}

# Converts string in inputtxt to morse code and outputs into morse label
def convert_to_morse():
    # Get String from input box and upper case string
    text = inputtxt.get().upper()

    # Output list for morse code
    morse_output = []

    for char in text:
        if char == " ":
            morse_output.append("/") # word seperator
        else:
            morse_output.append(MORSE_CODE.get(char, ""))

    morse = " ".join(morse_output).strip()

    label_morse.config(text=morse)

    if morse:
        window.after(100, play_morse)

# Plays sound of morse code in morse label
def play_morse():

    # Do not play if sound is already playing
    global is_playing

    if is_playing:
        return

    is_playing = True

    # get text from label
    morse = label_morse.cget("text")

    try:
        # Play sound depending on symbol
        for symbol in morse:
            if symbol == ".":
                DOT.play()
                pygame.time.wait(DOT_LENGTH)

            elif symbol == "-":
                DASH.play()
                pygame.time.wait(DASH_LENGTH)

            elif symbol == "/":
                # pause between words
                pygame.time.wait(WORD_SPACE)

            else:
                # space between letters
                pygame.time.wait(LETTER_SPACE)

    finally:
        is_playing = False

def clear_text():
    inputtxt.delete(0, END)
    label_morse.config(text="")

# Build tkinter window
window = tk.Tk()
window.title("Morse Coder")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20, background="black")

# Create and place intro label
label_intro = tk.Label(text="Type what you want converted into morse code:", font=("Arial", 10), bg="black", fg="green")
# label_intro.place(x=100, y=50)
label_intro.grid(row=0, column=0, columnspan=2, pady=10)

# Create and place input text
inputtxt = tk.Entry(width=20, bg="green", fg="black")
# inputtxt.place(x=160, y=80)
inputtxt.grid(row=1, column=0)

# Create and place label for morse code.
label_morse = tk.Label(text="", font=("Arial", 20), bg="black", fg="green")
# label_morse.place(relx=.5, rely=.5, anchor="center")
label_morse.grid(row=2, column=0, columnspan=2, pady=20)

# Create and place button to convert text
convert_button = tk.Button(text="Convert", command=convert_to_morse, bg="green", fg="black")
# convert_button.place(x=300, y=80)
convert_button.grid(row=1, column=1)

# Create and place button to clear text in input textbox
clear_button = tk.Button(text="Clear", command=clear_text, bg="green", fg="black")
clear_button.grid(row=1, column=2)

# Press Enter to Convert Text
inputtxt.bind("<Return>", lambda event: convert_to_morse())

# Keep window open
window.mainloop()

# # Command line code:
# # Prompt User for String to convert
# string_to_morse = input("Input String to translate into Morse: ")

# # Print Morse Code
# print(f"{string_to_morse} in morse code is {morse}")
