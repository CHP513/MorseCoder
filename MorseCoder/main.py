from tkinter import *
from playsound import playsound
import time

# Sounds for Morse code
# Need full file path in order to work correctly
DOT_SOUND = "FILE_PATH/dot.wav"
DASH_SOUND = "FILE_PATH/dash.wav"

#Dictionary of Morse Code
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
    "10":"-----",
    " ": " "
}

# Converts string in input txt to morse code and outputs into morse label
def convert_to_morse():
    # Get String from input box
    string_to_morse = inputtxt.get()

    # Make each letter in String Capital so it can be read by dictionary
    upper_string_to_morse = string_to_morse.upper()

    # Read each char in String and put into a list
    list_string = list(upper_string_to_morse)

    # Convert each char to Morse Code
    list_morse = []
    for char in list_string:
        list_morse.append(MORSE_CODE[char])

    # Convert list to String (Separate each list item by space)
    morse = " ".join(list_morse)

    # Convert blank label to morse
    label_morse.config(text=morse)

    # Play morse in sound, window after is needed to display text and make sound simultaneously
    window.after(100,play_morse)

#Plays sound of morse code in morse label
def play_morse():
    # get text from label
    morse = label_morse.cget("text")
    for note in morse:
        if note == ".":
            playsound(DOT_SOUND, True)
        if note == "-":
            playsound(DASH_SOUND, True)
        if note == " ":
            time.sleep(1)


# Build tkinter window
window = Tk()
window.title("Morse Coder")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20, background="black")

# Create intro label
label_intro = Label(text="Type what you want converted into morse code:", font=("Arial", 10), bg="black", fg="green")
label_intro.place(x=100, y=50)

# Create input text
inputtxt = Entry(width=20, bg="green", fg="black")
inputtxt.place(x=160, y=80)

# Create label for morse code. Relative is to center.
label_morse = Label(text="", font=("Arial", 20), bg="black", fg="green")
label_morse.place(relx=.5, rely=.5, anchor="center")

# Create button to convert text
convert_button = Button(text="Convert", command=convert_to_morse, bg="green", fg="black")
convert_button.place(x=300, y=80)

# Keep window open
window.mainloop()

# # Command line code:
# # Prompt User for String to convert
# string_to_morse = input("Input String to translate into Morse: ")

# # Print Morse Code
# print(f"{string_to_morse} in morse code is {morse}")
