# Import library
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import zone_swapper as zs

# global variables
file_directory = ""
zone1, zone2 = 0, 0
output_file = ""
zone_name_dict = []
zone_id_dict = []
zone_label_dict = []
image_path = "Logo1.png"
 
def init_window(window_title):
    '''Initializes the Tkinter window'''
    # Create window Tkinter
    window = tk.Tk()
    # Name our Tkinter application title
    window.title(window_title)
    # Set the window size
    window.state('zoomed')
    return window
    
def browse_file(label, window, changed_file=False):
    '''Opens a file explorer window and stores the file directory in a global variable'''
    global file_directory, zone_name_dict, zone_id_dict, zone_label_dict, output_file
    if changed_file:
        zone_name_dict, zone_id_dict = zs.find_zone_names(zs.get_root(output_file), True)
        print_zone_names(window, True)
        return
    # Destroy all zone labels if they exist
    for zone_label in zone_label_dict: zone_label.destroy()
    # Open a file explorer window
    file_directory = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a File", filetypes = (("brightsign presentation", "*.bpf*"), ("all files", "*.*")))
    label.configure(text="File Opened: "+file_directory)
    # Find the zone names and zone id's
    zone_name_dict, zone_id_dict = zs.find_zone_names(zs.get_root(file_directory), True)
    # Print the zone names and zone id's to the console
    print("Zone Names: ", zone_name_dict)
    print("Zone Id: ", zone_id_dict)
    print_zone_names(window)

def print_zone_names(window, changed_file=False):
    '''Prints the zone names to the tkinter window'''
    global zone_name_dict, zone_id_dict, zone_label_dict
    if changed_file:
        iterebol = 0
        zone_label = tk.Label(window, text="Changes Zones:", font=('Calibri 15 bold'))	
        zone_label.place(x=25, y=325)
        for zone_id in zone_id_dict:
            label = tk.Label(window, text="Zone: " + zone_id + " "+ zone_name_dict[iterebol], font=('Calibri 15 bold'))
            label.place(x=25, y=iterebol*30+355)
            iterebol += 1
            zone_label_dict.append(label)
        return
    iterebol = 0
    zone_label = tk.Label(window, text="Found Zones:", font=('Calibri 15 bold'))	
    zone_label.place(x=25, y=25)
    for zone_id in zone_id_dict:
        label = tk.Label(window, text="Zone: " + zone_id + " "+ zone_name_dict[iterebol], font=('Calibri 15 bold'))
        label.place(x=25, y=iterebol*30+55)
        iterebol += 1
        zone_label_dict.append(label)

def get_user_input(label_file_explorer, window, output_file_entry, zone1_entry, zone2_entry):
    '''Gets the user input from the tkinter window'''
    global file_directory, output_file, zone1, zone2
    #  check if the file directory is empty
    if file_directory == "":
        # If so, display a warning label with the color red
        label_file_explorer.configure(text="Please select a file")
        return
    output_file = output_file_entry.get() + ".bpf"
    zone1 = zone1_entry.get()
    zone2 = zone2_entry.get()
    #  Check if all the fields are filled out
    if output_file == "" or zone1 == "" or zone2 == "" or output_file == "":
        # If not, display a warning label with the color red
        label_file_explorer.configure(text="Please fill out all fields")
        return
    # Create the output file
    create_outputfile(label_file_explorer, window)

def create_outputfile(label_file_explorer, window):
    '''Creates the output file'''
    global output_file, zone1, zone2, file_directory
    # remove all waring labels if they exist
    label_file_explorer.configure(text=file_directory)
    # Check if the zone id's are valid
    if zone1 not in zone_id_dict or zone2 not in zone_id_dict:
        label_file_explorer.configure(text="Invalid Zone ID's")
        return
    # Create the output file
    zs.create_output_file(file_directory, output_file, zone1, zone2)
    browse_file(label_file_explorer, window, True)

def debug():
    '''Debugging function'''
    print("Debugging")
    print("Output File: ", output_file)
    print("Input File: ", file_directory)

def main():
    '''Main function to run the program'''
    window = init_window("Brightsign Zone Controller")

    #  Create a File Explorer label
    label_file_explorer = ttk.Label(window, text = "Select a Brigtsign file to rebuild the zones", font = ("Calibri 15 bold"))
    button_explore = ttk.Button(window, text = "Browse Files", command = lambda:browse_file(label_file_explorer, window))
    label_file_explorer.pack(pady=20)
    button_explore.pack(pady=20)

    # The label for output_file
    ttk.Label(window, text="Output file", font=('Calibri 15 bold')).place(x=1920/2, y=200)
    #  The label for zone1
    ttk.Label(window, text="Zone 1", font=('Calibri 15 bold')).place(x=1920/2, y=240)
    #  The label for zone2
    ttk.Label(window, text="Zone 2", font=('Calibri 15 bold')).place(x=1920/2, y=280)
    # The text entry box for user_name
    output_file_entry = tk.Entry(window, width=20)
    output_file_entry.focus_set()
    output_file_entry.place(x=1920/2+100, y=200)
    # The text entry box for user_password
    zone1_entry = tk.Entry(window, width=20)
    zone1_entry.focus_set()
    zone1_entry.place(x=1920/2+100, y=240)
    # The text entry box for user_password
    zone2_entry = tk.Entry(window, width=20)
    zone2_entry.focus_set()
    zone2_entry.place(x=1920/2+100, y=280)
    #  The submit button
    ttk.Button(window, text="Submit", command=lambda:get_user_input(label_file_explorer, window, output_file_entry, zone1_entry, zone2_entry)).place(x=1920/2, y=320)
    
    # Display the image on the button left corner of the window
    img = ImageTk.PhotoImage(Image.open(image_path).resize((269, 86)))
    # resize the image
    # img = img.resize((537.2, 171.2), Image.ANTIALIAS)
    image_label = tk.Label(window, image = img)
    image_label.place(relx=0.0, rely=1.0, anchor='sw')

    # Run main loop
    window.mainloop()

if __name__ == "__main__":
    main()