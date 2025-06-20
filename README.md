# 📄🔊 PDF to Speech 

A simple Python utility that reads text from a PDF file and converts it into spoken audio using Text-to-Speech (TTS) technology. This is useful for visually impaired users, productivity enhancement, or listening to PDFs on the go.

---

## 📌 Features

- 🗂️ Select and load any valid `.pdf` file
- 📃 Reads each page using `PyPDF2`
- 🔊 Converts PDF text to speech using `pyttsx3`
- 🔁 Gracefully handles errors and invalid file selections
- 🧠 Simple and interactive command-line interface with file dialog

---

## ⚙️ Tech Stack

| **Technology** | **Purpose**                          |
|----------------|--------------------------------------|
| Python         | Core programming language            |
| PyPDF2         | PDF parsing and text extraction      |
| pyttsx3        | Offline text-to-speech conversion    |
| tkinter.filedialog | GUI-based file selection dialog |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KaisoX24/PDF-To-Speech.git
cd PDF-To-Speech
```
### 2. Install Dependencies
It's recommended to use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate # For MAC: source venv/bin/activate
```
- Install the required packages:

  ```bash
  pip install -r requirements.txt

### 3. Run the Script

```bash
python main.py
```
---
## 🧑‍💻 Author
Developed by Pramit Acharjya
---
## 🪪 License
MIT License — free to use, modify, and distribute.
