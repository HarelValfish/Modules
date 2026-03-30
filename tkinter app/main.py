import tkinter as tk

def handle_click():
    name = user_input.get() # Get text from the entry box
    result_label.config(text=f"Result: Hi {name}")

# Main window object
app = tk.Tk()
app.title("My First App")
app.geometry("400x300") # Width x Height

tk.Label(app, text="Enter Name:").grid(row=0, column=0, padx=10, pady=10) # Static text

user_input = tk.Entry(app) # The input box
user_input.grid(row=0, column=1)

submit_btn = tk.Button(app, text="Run", command=handle_click) # The button
submit_btn.grid(row=0, column=2, columnspan=1, pady=10)

result_label = tk.Label(app, text="") # Empty label to show results later
result_label.grid(row=2, column=0, padx=0, pady=0)

# Run the main loop.
app.mainloop()