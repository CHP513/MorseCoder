from tkinter import *
from playsound import playsound

# Sounds for Morse code
DOT_SOUND = "C:/Users/chpb5/PycharmProjects/MorseCoder/dot.wav"
DASH_SOUND = "C:/Users/chpb5/PycharmProjects/MorseCoder/dash.wav"
BLANK_SOUND = "C:/Users/chpb5/PycharmProjects/MorseCoder/blank.wav"


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

    # Convert list to String (Seperate each list item by space)
    morse = " ".join(list_morse)

    # Convert blank label to morse
    label_morse.config(text=morse)

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
            playsound(BLANK_SOUND, False)


# Build tkinter window
window= Tk()
window.title("Morse Coder")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

# Create intro label
label_intro = Label(text="Type what you want converted into morse code:", font=("Arial", 10))
label_intro.grid(row=0, column=1)

# Create input text
inputtxt = Entry(width=20)
inputtxt.grid(row=1, column=1)

# Create label for morse code
label_morse = Label(text="", font=("Arial", 20))
label_morse.grid(row=2, column=1)

# Create button to convert text

convert_button = Button(text="Convert", command=convert_to_morse)
convert_button.grid(row=1, column=2)

# Create button to play sound
# sound_image = PhotoImage(file="sound.jpg")
play_button = Button(text="Play", command=play_morse)
play_button.grid(row=3, column=1)
# Keep window open
window.mainloop()

# # Prompt User for String to convert
# string_to_morse = input("Input String to translate into Morse: ")

# # Print Morse Code
# print(f"{string_to_morse} in morse code is {morse}")
