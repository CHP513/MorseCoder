# Morse Coder

This Python project provides a simple GUI tool that converts text into **Morse code** and plays the corresponding **dot and dash sounds**. It uses `tkinter` for the interface and `playsound` for audio playback.  

It can also be run from the **command line** to translate text without the GUI.

---

## ✨ Features
- Convert any input text (A–Z, 0–9, space) into Morse code.
- Displays the translated Morse code in real-time.
- Plays the Morse code as audio (`.wav` sounds for dots and dashes).
- Simple GUI built with **Tkinter**.
- Optional command-line usage for quick translations.

---

## 📦 Requirements
- Python 3.7+
- Libraries:
  - `tkinter` (bundled with Python)
  - [`playsound`](https://pypi.org/project/playsound/)

Install dependencies with:
```bash
pip install playsound
```

---

## ▶️ GUI Usage
1. Clone or download this repository.
2. Update the paths to the `dot.wav` and `dash.wav` files inside **`main.py`**:
   ```python
   DOT_SOUND = "path/to/dot.wav"
   DASH_SOUND = "path/to/dash.wav"
   ```
3. Run the program:
   ```bash
   python main.py
   ```
4. In the GUI:
   - Enter text in the input box.
   - Click **Convert**.
   - See the Morse code displayed.
   - Hear the Morse code played as sound.

---

## 💻 Command-Line Usage
The script also contains commented-out code for running in **command-line mode**.  

1. Uncomment this section in `main.py`:
   ```python
   # # Command line code:
   # string_to_morse = input("Input String to translate into Morse: ")
   # print(f"{string_to_morse} in morse code is {morse}")
   ```
2. Run the program from the terminal:
   ```bash
   python main.py
   ```
3. Enter text when prompted:
   ```
   Input String to translate into Morse: HELLO
   ```
4. Output:
   ```
   HELLO in morse code is .... . .-.. .-.. ---
   ```

---

## 🔈 Audio
- Provide your own **dot.wav** and **dash.wav** sound files.
- Place them anywhere on your system and update the file paths in `main.py`.

---

## 📚 Example
Input:
```
HELLO
```
Output:
```
.... . .-.. .-.. ---
```
Audio playback: dot and dash sounds for each symbol.

---

## 📜 License
This project is open-source and available under the MIT License.
