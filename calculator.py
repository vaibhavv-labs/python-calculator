import tkinter as tk
from tkinter import font as tkfont


#  CALCULATOR LOGIC


class Calculator:
    def __init__(self):
        self.current = "0"
        self.previous = ""
        self.operator = None
        self.reset_next = False
        self.history = []

    def input_number(self, value):
        if self.reset_next:
            self.current = str(value)
            self.reset_next = False
        else:
            if self.current == "0":
                self.current = str(value)
            elif len(self.current) < 15:
                self.current += str(value)

    def input_decimal(self):
        if self.reset_next:
            self.current = "0."
            self.reset_next = False
        elif "." not in self.current:
            self.current += "."

    def input_operator(self, op):
        if self.operator and not self.reset_next:
            self.calculate()
        self.previous = self.current
        self.operator = op
        self.reset_next = True

    def calculate(self):
        if not self.operator or not self.previous:
            return
        a = float(self.previous)
        b = float(self.current)
        result = 0

        if self.operator == "+":
            result = a + b
        elif self.operator == "-":
            result = a - b
        elif self.operator == "×":
            result = a * b
        elif self.operator == "÷":
            if b == 0:
                self.current = "Error"
                self.operator = None
                self.reset_next = True
                return
            result = a / b

      
        if result == int(result) and abs(result) < 1e12:
            result_str = str(int(result))
        else:
            result_str = f"{result:.10g}"

   
        op_symbol = self.operator
        entry = f"{self.format_num(a)} {op_symbol} {self.format_num(b)} = {result_str}"
        self.history.insert(0, entry)
        if len(self.history) > 5:
            self.history.pop()

        self.current = result_str
        self.previous = ""
        self.operator = None
        self.reset_next = True

    def toggle_sign(self):
        if self.current not in ("0", "Error"):
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current

    def percentage(self):
        try:
            self.current = str(float(self.current) / 100)
            if float(self.current) == int(float(self.current)):
                self.current = str(int(float(self.current)))
        except:
            pass

    def clear(self):
        self.current = "0"
        self.previous = ""
        self.operator = None
        self.reset_next = False

    def backspace(self):
        if self.current not in ("0", "Error"):
            self.current = self.current[:-1] or "0"

    def format_num(self, n):
        if n == int(n):
            return str(int(n))
        return f"{n:.6g}"


──

class CalculatorApp:
 
    BG_DARK       = "#0d1117"
    BG_DISPLAY    = "#161b22"
    BG_CARD       = "#1c2128"
    BTN_NUM       = "#21262d"
    BTN_NUM_HOV   = "#30363d"
    BTN_OP        = "#1f2d4a"
    BTN_OP_HOV    = "#2d4070"
    BTN_EQ        = "#3b5bdb"
    BTN_EQ_HOV    = "#4c6ef5"
    BTN_CLR       = "#3a1a1a"
    BTN_CLR_HOV   = "#5a2020"
    BTN_FN        = "#1c2128"
    BTN_FN_HOV    = "#2d333b"

    TEXT_WHITE    = "#e6edf3"
    TEXT_MUTED    = "#7d8590"
    TEXT_OP       = "#79c0ff"
    TEXT_CLR      = "#ff7b7b"
    TEXT_FN       = "#a8b1ba"
    TEXT_EQ       = "#ffffff"
    BORDER        = "#30363d"
    ACCENT        = "#3b5bdb"

    def __init__(self, root):
        self.root = root
        self.calc = Calculator()
        self.setup_window()
        self.build_ui()
        self.bind_keyboard()

    def setup_window(self):
        self.root.title("Calculator")
        self.root.geometry("380x650")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG_DARK)
 
        self.root.eval('tk::PlaceWindow . center')

    def build_ui(self):
    
        self.font_result  = tkfont.Font(family="Courier New", size=42, weight="bold")
        self.font_expr    = tkfont.Font(family="Courier New", size=13)
        self.font_btn     = tkfont.Font(family="Segoe UI", size=18, weight="bold")
        self.font_btn_sm  = tkfont.Font(family="Segoe UI", size=14)
        self.font_hist    = tkfont.Font(family="Courier New", size=10)

       
        display_frame = tk.Frame(self.root, bg=self.BG_DISPLAY,
                                 highlightbackground=self.BORDER,
                                 highlightthickness=1)
        display_frame.pack(fill="x", padx=12, pady=(16, 0))

)
        self.expr_label = tk.Label(display_frame, text="", font=self.font_expr,
                                   bg=self.BG_DISPLAY, fg=self.TEXT_MUTED,
                                   anchor="e", padx=16, pady=12)
        self.expr_label.pack(fill="x", pady=(12, 0))

      
        self.result_label = tk.Label(display_frame, text="0", font=self.font_result,
                                     bg=self.BG_DISPLAY, fg=self.TEXT_WHITE,
                                     anchor="e", padx=16, pady=4)
        self.result_label.pack(fill="x")

   
        self.history_frame = tk.Frame(display_frame, bg=self.BG_DISPLAY)
        self.history_frame.pack(fill="x", padx=16, pady=(4, 12))

  ──────
        btn_frame = tk.Frame(self.root, bg=self.BG_DARK)
        btn_frame.pack(fill="both", expand=True, padx=12, pady=12)

        layout = [
     )
            [("AC", "clear",  1, "clr"), ("+/−", "sign",    1, "fn"),
             ("%",  "pct",    1, "fn"),  ("÷",   "÷",       1, "op")],
            [("7",  "7",      1, "num"), ("8",   "8",       1, "num"),
             ("9",  "9",      1, "num"), ("×",   "×",       1, "op")],
            [("4",  "4",      1, "num"), ("5",   "5",       1, "num"),
             ("6",  "6",      1, "num"), ("−",   "-",       1, "op")],
            [("1",  "1",      1, "num"), ("2",   "2",       1, "num"),
             ("3",  "3",      1, "num"), ("+",   "+",       1, "op")],
            [("0",  "0",      2, "num"), (".",   ".",       1, "num"),
             ("=",  "=",      1, "eq")],
        ]

        colors = {
            "num": (self.BTN_NUM,  self.BTN_NUM_HOV,  self.TEXT_WHITE),
            "op":  (self.BTN_OP,   self.BTN_OP_HOV,   self.TEXT_OP),
            "eq":  (self.BTN_EQ,   self.BTN_EQ_HOV,   self.TEXT_EQ),
            "clr": (self.BTN_CLR,  self.BTN_CLR_HOV,  self.TEXT_CLR),
            "fn":  (self.BTN_FN,   self.BTN_FN_HOV,   self.TEXT_FN),
        }

        for row_idx, row in enumerate(layout):
            col_idx = 0
            for (label, action, colspan, style) in row:
                bg, hov, fg = colors[style]
                f = self.font_btn if len(label) <= 2 else self.font_btn_sm
                btn = tk.Button(
                    btn_frame, text=label, font=f,
                    bg=bg, fg=fg, activebackground=hov, activeforeground=fg,
                    relief="flat", bd=0, cursor="hand2",
                    highlightthickness=1, highlightbackground=self.BORDER,
                    command=lambda a=action: self.on_press(a)
                )
                btn.grid(row=row_idx, column=col_idx, columnspan=colspan,
                         padx=5, pady=5, sticky="nsew", ipady=14)
                # Hover effect
                btn.bind("<Enter>", lambda e, b=btn, c=hov: b.config(bg=c))
                btn.bind("<Leave>", lambda e, b=btn, c=bg:  b.config(bg=c))
                col_idx += colspan

  
        for c in range(4):
            btn_frame.columnconfigure(c, weight=1)
        for r in range(5):
            btn_frame.rowconfigure(r, weight=1)

    def on_press(self, action):
        c = self.calc
        if action == "clear":
            c.clear()
        elif action == "sign":
            c.toggle_sign()
        elif action == "pct":
            c.percentage()
        elif action in ("÷", "×", "+", "-"):
         
            op_map = {"÷": "÷", "×": "×", "+": "+", "-": "-"}
            c.input_operator(op_map[action])
        elif action == "=":
            c.calculate()
        elif action == ".":
            c.input_decimal()
        elif action == "back":
            c.backspace()
        else:
            c.input_number(action)
        self.refresh()

    def refresh(self):
        c = self.calc

        txt = c.current
        size = 42 if len(txt) <= 10 else (30 if len(txt) <= 14 else 22)
        self.result_label.config(text=txt,
                                 font=tkfont.Font(family="Courier New", size=size, weight="bold"))

      
        op_show = {"÷": "÷", "×": "×", "+": "+", "-": "−", None: ""}
        if c.operator and c.previous:
            self.expr_label.config(text=f"{c.previous}  {op_show.get(c.operator,'')}")
        else:
            self.expr_label.config(text="")

  
        for w in self.history_frame.winfo_children():
            w.destroy()
        for entry in c.history[:3]:
            lbl = tk.Label(self.history_frame, text=entry, font=self.font_hist,
                           bg=self.BG_DISPLAY, fg=self.TEXT_MUTED, anchor="e")
            lbl.pack(fill="x")

    def bind_keyboard(self):
        self.root.bind("<Key>", self.on_key)
        self.root.focus_set()

    def on_key(self, event):
        k = event.keysym
        c = event.char
        if c in "0123456789":
            self.on_press(c)
        elif c == ".":
            self.on_press(".")
        elif c == "+":
            self.on_press("+")
        elif c in ("-", "minus"):
            self.on_press("-")
        elif c == "*":
            self.on_press("×")
        elif c == "/":
            self.on_press("÷")
        elif c in ("=", "\r"):
            self.on_press("=")
        elif k == "Escape":
            self.on_press("clear")
        elif k == "BackSpace":
            self.on_press("back")
        elif c == "%":
            self.on_press("pct")



if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
