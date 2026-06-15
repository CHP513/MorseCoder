# Morse Coder

**Author:** Charles (Chip) Brady
**Date:** June 2026

## Overview

Morse Coder is a Python application built with Tkinter and Pygame that converts text into Morse code and plays the corresponding Morse code audio. Users can enter text, instantly view the Morse code translation, and hear the dots and dashes played through sound effects.

The project demonstrates the use of graphical user interfaces, dictionaries, event handling, file management, and audio playback in Python.

---

## Features

* Convert letters, numbers, and selected punctuation into Morse code
* Display Morse code translation in a graphical user interface
* Play Morse code audio using separate dot and dash sound effects
* Support for word separation using Morse code conventions
* Clear button to reset the input and output fields
* Press **Enter** to convert text without clicking the Convert button
* Prevents overlapping audio playback
* Uses relative file paths for portability

---

## Supported Characters

### Letters

A-Z

### Numbers

0-9

### Punctuation

* !
* ?
* .
* ,
* :

### Space

Spaces between words are represented by "/" in the Morse code output.

---

## Requirements

* Python 3.x
* Pygame

Install Pygame with:

```bash
pip install pygame
```

---

## Project Files

```text
MorseCoder/
│
├── morse_coder.py
├── dot.wav
├── dash.wav
└── README.md
```

### File Descriptions

* **morse_coder.py** – Main application source code
* **dot.wav** – Audio file used for Morse code dots
* **dash.wav** – Audio file used for Morse code dashes
* **README.md** – Project documentation

---

## How to Run

1. Ensure Python is installed.
2. Install Pygame:

```bash
pip install pygame
```

3. Place `dot.wav` and `dash.wav` in the same directory as the Python script.
4. Run the program:

```bash
python morse_coder.py
```

---

## How to Use

1. Launch the application.
2. Type a message into the text box.
3. Click **Convert** or press **Enter**.
4. The Morse code translation will appear on the screen.
5. The program will automatically play the Morse code audio.
6. Click **Clear** to remove the current text and translation.

---

## Concepts Demonstrated

This project demonstrates:

* Tkinter GUI development
* Event-driven programming
* Python dictionaries
* Audio playback using Pygame
* File path management with `os`
* Input validation and error handling
* Morse code encoding techniques

---

## Future Improvements

Potential enhancements include:

* Adjustable Morse code speed (Words Per Minute)
* Additional punctuation support
* Copy Morse code to clipboard
* Save translations to a text file
* Stop/Pause playback controls
* Reverse conversion (Morse code to text)
* Light and dark theme options

---

## License

This project is intended for educational and personal learning purposes.
