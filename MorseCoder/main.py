from tkinter import *

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


def convert_to_morse():
    print("button")
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

button = Button(text="Convert", command=convert_to_morse)
button.grid(row=1, column=2, sticky="w")


window.mainloop()

# # Prompt User for String to convert
# string_to_morse = input("Input String to translate into Morse: ")

# # Print Morse Code
# print(f"{string_to_morse} in morse code is {morse}")
