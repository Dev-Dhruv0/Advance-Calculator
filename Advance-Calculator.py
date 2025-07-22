import customtkinter as ctk
import ast
import operator

# =======================
# Configuration
# =======================
# Set appearance and theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Main window config
app = ctk.CTk() #Tk() - Creates the main app window
app.title("Calculator") #Creates the title
app.geometry("320x500") #Window resolution

# Global Variable
current_expression = ""

# =======================
# Utility Functions
# =======================
# - Safe evaluation
def safe_eval(expr):
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }
    def _eval(node):    # Helper Function
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.BinOp):
            return allowed_ops[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Constant): # For Python 3.8+
            return node.value
        else:
            raise ValueError("Invalid Input!")
    parsed_node = ast.parse(expr, mode='eval')
    return _eval(parsed_node.body)

# =======================
# Button Functionality
# =======================
def handle_button_press (text):
    global current_expression

    if text == "=":
        try:
            current_expression = str(safe_eval(current_expression))
        except (ValueError, ZeroDivisionError, SyntaxError) as e:
            print(f"[Error] {type(e).__name__}: {e}")
            current_expression = "Error"
    elif text == "C":
            current_expression = current_expression[:-1]
    elif text == "AC":
            current_expression = ""
    # Prevent double operators
    elif text in "+-*/" and current_expression[-1:] in "+-*/":
        current_expression = current_expression[:-1] + text
    elif text == "%":
        try:
            value = float(current_expression)
            current_expression = str(value/100)
        except (ValueError, ZeroDivisionError, SyntaxError) as e:
            print(f"[Error] {type(e). __name__}: {e}")
            current_expression = "Error"
    elif text == "x":
        current_expression += "*"
    elif text == "÷" or text == "/":
        current_expression += "/"
    else:
        current_expression += text
    # Update Display
    entry.delete(0, "end") #Clear current text in entry

    # Display back to "0" when empty
    if current_expression == "":
        entry.insert(0, "0")
    else:
        entry.insert(0, current_expression) #Insert the updated expression

# =======================
# Keyboard Support
# =======================
def on_key_press(event):
    key = event.char
    special_key = event.keysym

    if key in "0123456789.+-*/":
        handle_button_press(key)
    elif key == "\r": # Enter key
        handle_button_press("=")
    elif special_key == "BackSpace":
        handle_button_press("C")
    elif special_key == "Escape":
        handle_button_press("AC")

# Bind keyboard support
app.bind("<Key>", on_key_press)


# =======================
# GUI Layout
# =======================
# Window row and column configure
app.rowconfigure(0, weight=0)
app.rowconfigure(1, weight=1)
app.columnconfigure(0, weight=1)

# Create a frame/ Container for a top display portion of calculator
top_frame = ctk.CTkFrame(app, corner_radius=10)
top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

# Entry widget (Display)
entry = ctk.CTkEntry(
    top_frame,
    justify="right",
    height=60,
    corner_radius=10,
    placeholder_text="0",
    border_width=0
)
entry.pack(fill="both", expand=True)

# Create bottom frame for buttons
bottom_frame = ctk.CTkFrame(app, corner_radius=10)
bottom_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

# =======================
# Button Design
# =======================
# Apple style colors for button
gray = "#A5A5A5"
dark_gray = "#333333"
orange = "#FF9500"

# Font style for buttons
button_font = ("SF Pro", 22)

# Font row of buttons: AC, C, %, /
buttons = [
    [("AC", gray), ("C", gray), ("%", gray), ("/", orange)],
    [("7", dark_gray), ("8", dark_gray), ("9", dark_gray), ("x", orange)],
    [("4", dark_gray), ("5", dark_gray), ("6", dark_gray), ("-", orange)],
    [("1", dark_gray), ("2", dark_gray), ("3", dark_gray), ("+", orange)],
    [("0", dark_gray), (".", dark_gray), ("=", dark_gray)]
]

# Configure grid for 4 columns in bottom_frame
for c in range(4):
    bottom_frame.columnconfigure(c, weight=1)
for r in range(len(buttons)):
    bottom_frame.rowconfigure(r, weight=1)

# Create and place each button
for row_index, row in enumerate(buttons):
    col_index = 0
    for text, color in row:
        # Determine if the button is "0" and needs to span 2 columns
        if text == "0":
            button = ctk.CTkButton(
                bottom_frame,
                text=text,
                font=button_font,
                fg_color=color,
                hover_color="white",
                corner_radius=30,
                height=20,
                command=lambda t=text: handle_button_press(t))
            button.grid(row=row_index, column=col_index, columnspan=2, padx=5, pady=5, sticky="nsew")
            col_index += 2 # Skip a column
        else:
            if text == "AC":
                ac_button = ctk.CTkButton(
                    bottom_frame,
                    text=text,
                    font=button_font,
                    fg_color=color,
                    hover_color="white",
                    corner_radius=30,
                    height=20,
                    command=lambda t=text: handle_button_press(t)
                )
                ac_button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
                col_index += 1
            else:
                button = ctk.CTkButton(
                    bottom_frame,
                    text=text,
                    font=button_font,
                    fg_color=color,
                    hover_color="white",
                    corner_radius=30,
                    height=20,
                    command=lambda t=text: handle_button_press(t))
                button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
                col_index += 1
app.mainloop() # Runs the GUI until closed