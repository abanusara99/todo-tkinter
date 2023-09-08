import tkinter as tk
from tkinter import *


# Function to handle saving the task
def saveTask():
    task_text = task_entry.get()  # Get the task from the Entry widget
    if task_text:
        with open("listtask.txt", "a") as file:
            file.write(task_text + "\n")  # Save the task to the file
        task_entry.delete(0, "end")  # Clear the Entry widget
        displayTasks()  # Refresh the task list


# Function to display tasks
def displayTasks():
    listbox.delete(0, "end")  # Clear the task list Listbox widget
    try:
        with open("listtask.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert("end", task)  # Display tasks in the Listbox widget
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist

def deleteTask():
    selected_task = listbox.get("active")  # Get the currently selected task
    listbox.delete("active")  # Remove it from the list
    with open("listtask.txt", "r") as file:
        lines = file.readlines()
    with open("listtask.txt", "w") as file:
        for line in lines:
            if line.strip() != selected_task.strip():
                file.write(line)  # Write all tasks back to the file except the deleted one

# Create the main window
root = tk.Tk()
root.geometry("400x650+400+100")
root.resizable(False,False)

#icon
Image_icon = PhotoImage(file="img/task.png")
root.iconphoto(False, Image_icon)

# Color top
TopImage = PhotoImage(file="img/topbar.png")
tk.Label(root, image=TopImage).pack()

# Option image
dockImage = PhotoImage(file="img/dock.png")
tk.Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

# Page title
heading = tk.Label(root, text="TASK LIST", font="arial 25 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Frame box to type the task
frame = Frame(root, width=400, height=90, bg="white")
frame.place(x=0, y=180)

# Entry box of todo list
task = StringVar()
task_entry = Entry(frame, textvariable=task, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)

# Button to submit the task
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=saveTask)
button.place(x=300, y=0)

# Frame1 box to display the already given task
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

# Display the tasks in order
listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side="left", fill="both", padx=2)

# Load and display tasks
displayTasks()

# Up scrollbar and down scrollbar
scrollbar = Scrollbar(frame1)
scrollbar.pack(side="right", fill="y")

# Merged list box and scrollbar box
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a button to delete tasks
delete_icon = PhotoImage(file="img/delete.png")

# Frame to hold the delete button
delete_frame = Frame(root)
delete_frame.pack()

delete_button = Button(delete_frame, image=delete_icon, bd=0, command=deleteTask)
delete_button.pack(pady=10)


# Run the main loop
root.mainloop()
