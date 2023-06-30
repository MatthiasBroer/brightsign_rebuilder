# Import library
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
 
def init_window(window_title):
    # Create window Tkinter
    window = tk.Tk()
    # Name our Tkinter application title
    window.title(window_title)
    # Set the window size
    window.state('zoomed')
    return window
    
# Function to update the label text for first button click in Tkinter
def on_click_btn1(label):
    label["text"] = "You clicked first button"
     
# Function to update the label text for second button click in Tkinter
def on_click_btn2(label):
    label["text"] = "You clicked second button"

def display_text(label, entry):
    label["text"] = "You entered: " + entry.get()

def browse_file(label):
    filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a File", filetypes = (("brightsign presentation", "*.bpf*"), ("all files", "*.*")))
    label.configure(text="File Opened: "+filename)

def main():
    window = init_window("Brightsign Zone Controller")

    #  Create a File Explorer label
    label_file_explorer = ttk.Label(window, text = "Select a Brigtsign file to rebuild the zones", font = ("Calibri 15 bold"))
    button_explore = ttk.Button(window, text = "Browse Files", command = lambda:browse_file(label_file_explorer))
    label_file_explorer.pack(pady=20)
    button_explore.pack(pady=20)

    # Create a label widget in Tkinter
    label = tk.Label(window, text="Click the Button to update this Text", font=('Calibri 15 bold'))
    label.pack(pady=20)

    # Create 1st button to update the label widget
    btn1 = tk.Button(window, text="Button1", command=lambda:on_click_btn1(label))
    btn1.pack(pady=20)
    
    # Create 2nd button to update the label widget
    btn2 = tk.Button(window, text="Button2", command=lambda:on_click_btn2(label))
    btn2.pack(pady=40)

    # Initialize a label to display the user input
    label2 = tk.Label(window, text="", font=('Calibri 15 bold'))
    label2.pack()

    # Create a entry widget to accept user input
    entry = tk.Entry(window, width=40)
    entry.focus_set()
    entry.pack()

    # Create a button to validate entry widget
    ttk.Button(window, text="Okay", width=20, command=lambda:display_text(label2, entry)).pack(pady=20)
    
    
    # Run main loop
    window.mainloop()

if __name__ == "__main__":
    main()