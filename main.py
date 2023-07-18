import tkinter as tk
from tkinter import messagebox
from main import button_labels

# Define the button press handler
def button_press_handler(button_label):
    if button_label == 'enter':
        # Get the content from the text box
        content = text_box.get("1.0", tk.END).strip()
        
        try:
            # Evaluate the content as an expression and get the result
            result = eval(content)
            
            # Clear the text box and display the result
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f"{content} = {result}\n")
        except Exception as e:
            # Display an error message if the evaluation fails
            messagebox.showerror("Error", str(e))
    else:
        # Clear the text box if it contains a result
        if "Result: " in text_box.get("1.0", tk.END):
            text_box.delete("1.0", tk.END)
        
        # Display the button label in the text box
        text_box.insert(tk.END, button_label)

# Create the GUI window
window = tk.Tk()
window.title('Calculator')

# Create a header frame
header_frame = tk.Frame(window)
header_frame.grid(row=0, column=0, columnspan=4, pady=10)

# Create a text box in the header frame
text_box = tk.Text(header_frame, height=2, width=20)
text_box.pack()

# Create buttons for each label
for i, label in enumerate(button_labels):
    row = (i + 4) // 4
    col = i % 4
    button = tk.Button(window, text=label, width=5, height=2, command=lambda label=label: button_press_handler(label))
    button.grid(row=row, column=col)

# Handle the window close event
def close_window():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close_window)

# Start the GUI main loop
window.mainloop()
