import pyttsx3 as pt
import PyPDF2 as pd
from PyPDF2.errors import PdfReadError
from tkinter.filedialog import *

# Keep asking for a valid PDF file
while True:
    try:
        pdf = askopenfilename(title='Select a PDF file', filetypes=[('PDF Files', '*.pdf')])
        if not pdf:
            print("No file selected. Please select a PDF file.")
            continue

        pdfreader = pd.PdfReader(pdf)
        pages = len(pdfreader.pages)
        break  # Exit loop if everything's okay

    except FileNotFoundError:
        print("File not found. Please select a valid PDF file.")
    except PdfReadError:
        print("Error reading the PDF. The file may be corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Initialize TTS engine
player = pt.init()

# Read and speak the content
for i in range(pages):
    page = pdfreader.pages[i]
    text = page.extract_text()
    if text:
        player.say(text)

player.runAndWait()
