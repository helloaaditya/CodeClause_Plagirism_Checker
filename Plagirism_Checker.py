import tkinter as tk
from difflib import SequenceMatcher
import os

def check_plagiarism():
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()

    if os.path.isfile(file1_path) and os.path.isfile(file2_path):
        with open(file1_path) as first_file, open(file2_path) as second_file:
            file1 = first_file.read()
            file2 = second_file.read()

            ab = SequenceMatcher(None, file1, file2).ratio()

            result = int(ab*100)
            result_label.config(text=f"{result}% Plagiarized Content")
    else:
        result_label.config(text="Invalid file path(s)")

root = tk.Tk()
root.title("Plagiarism Checker")
root.geometry("500x300")

# create label for file 1
file1_label = tk.Label(root, text="File 1")
file1_label.place(x=20, y=20)

# create entry for file 1
file1_entry = tk.Entry(root, width=50)
file1_entry.place(x=80, y=20)

# create label for file 2
file2_label = tk.Label(root, text="File 2")
file2_label.place(x=20, y=60)

# create entry for file 2
file2_entry = tk.Entry(root, width=50)
file2_entry.place(x=80, y=60)

# create button to check plagiarism
check_button = tk.Button(root, text="Check Plagiarism", command=check_plagiarism)
check_button.place(x=200, y=100)

# create label to display result
result_label = tk.Label(root, text="")
result_label.place(x=200, y=150)

root.mainloop()
