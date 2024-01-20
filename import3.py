

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

df1 = pd.DataFrame()  # Initialize an empty DataFrame

def open_excel_file1():
    global df1  # Use the global variable
    file_path1 = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx;*.xls")]) 
    df1 = pd.read_excel(file_path1)
    apply_filter()

    label_path1.config(text=f"Selected Excel file: {file_path1}")

def apply_filter():
    # Get the user input for 'Codification'
    codification_value = entry_codification.get()

    # Filter the DataFrame based on the user input
    filtered_df = df1[df1['Codification'] == codification_value]

    # Clear the previous data in the table
    clear_table()

    # Insert data into the table
    for index, row in filtered_df.iterrows():
        tree.insert("", tk.END, values=(row['UUC'], row['Certificate No']))

def clear_table():
    # Clear the previous data in the table
    for i in tree.get_children():
        tree.delete(i)

root = tk.Tk()
root.title("Certificate Generator")
root.geometry("1000x500")

label_1 = tk.Label(root, text="1. Select 0_INDEX")
label_path1 = tk.Label(root, text="Selected Excel file: None")
button_1 = tk.Button(root, text="Choose File", command=open_excel_file1)

# Entry widget for user input
label_codification = tk.Label(root, text="Enter Codification:")
entry_codification = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=apply_filter)

# Create Treeview widget for the table
columns = ("UUC", "Certificate No")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)  # Adjust width as needed

label_1.grid(row=0, column=0, padx=10, pady=5)
button_1.grid(row=0, column=1, pady=5)
label_path1.grid(row=0, column=2, padx=10, pady=5)
label_codification.grid(row=0, column=3, padx=10, pady=5)
entry_codification.grid(row=0, column=4, padx=10, pady=5)
search_button.grid(row=0, column=5, padx=10, pady=5)
tree.grid(row=1, column=0, columnspan=6, padx=10, pady=5)

root.mainloop()
