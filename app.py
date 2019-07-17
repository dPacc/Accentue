# Importing the libraries

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import fitz

# Defining the window

window = Tk()
window.title("Accentue")

window.geometry('700x300')
lbl = Label(window, text="PDF Word Highlighter")
lbl.grid(column=2, row=0)
lbl.config(width=20, height=3, font=("Times", 12, "bold italic"))

lbl2 = Label(window, text="Instructions:- ")
lbl2.grid(column=2, row=1)

lbl3 = Label(window, text="(1) Enter the word/s to highlight in single inverted commas and click the 'Add Word/s' button first")
lbl3.grid(column=2, row=2)

lbl4 = Label(window, text="(2) Click on 'Highlight' to select your PDF and save the PDF as 'output.pdf'")
lbl4.grid(column=2, row=3)

text = []

# Helper Functions
def retrieve_input():
    inputValue = textBox.get("1.0", "end-1c").split("'")
    global text
    text = inputValue

def clicked():
    FILEOPENOPTIONS = dict(defaultextension=".pdf", filetypes=[('pdf file', '*.pdf')])
    filename = askopenfilename(**FILEOPENOPTIONS)
    doc = fitz.open(filename)
    global text

    for words in text:
        # For each page in the selected document
        for page in doc:
            # Text to be highlighted
            text_instances = page.searchFor(words)
            # Highlighting
            for inst in text_instances:
                highlight = page.addHighlightAnnot(inst)

    ### Saving the output
    doc.save("output.pdf", garbage=4, deflate=True, clean=True)

# Words to be highlighter textbox
textBox = Text(window, height = 4, width = 98)
textBox.grid(column=2, row=4)

# Confirming the words button
btnCommit = Button(window, height = 1, width = 10, text = "Add word/s", command= lambda: retrieve_input())
btnCommit.grid(column=2, row=5)

# Open the PDF and saving the as "output.pdf"
btn = Button(window, text="Highlight", command=clicked)
btn.grid(column=2, row=6)

# Main window loop
window.mainloop()
