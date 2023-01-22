import tkinter as tk

class Calculator:
    """
    Calculator app class
    Contains methods needed for building and running the calculator
    """

    def __init__(self):
        """
        Initialize important variables
        Initialize Tkinter window and create calculator
        Begin running the application
        """
        # calc vars
        self.prev = None
        self.display = None
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.configure(bg="black")
        self.calc = tk.Frame(self.window, bg="black")
        self.prev_contents = ""
        self.display_contents = ""
        self.holder = 0
        # window setup
        self.window.minsize(340, 460)
        self.window.maxsize(340, 460)
        # self.window.geometry("300x450")
        self.calc.columnconfigure(4)
        self.calc.rowconfigure(8)
        self.calc.pack()
        self.make_calc(self.calc)
        self.window.mainloop()

    def update(self):
        """
        Updates calculator display
        """
        if self.display is not None and self.prev is not None:
            self.display.configure(text=self.display_contents)
            self.prev.configure(text=self.prev_contents)

    def dot(self):
        """
        Adds decimal when button is pressed if one is not already in the entry
        """
        if "." not in self.display_contents:
            self.display_contents = self.display_contents + "."
            self.update()

    def numeric(self, z):
        """
        Adds the entered number if the number is not over 13 characters long
        :param z: the number being entered
        """
        if len(self.display_contents) < 13:
            self.display_contents = self.display_contents + str(z)
            self.update()

    def back_space(self):
        """
        Remove the ending character to the current entry
        """
        if self.display_contents != "":
            if len(self.display_contents) == 1:
                self.display_contents = ""
            elif len(self.display_contents) == 2 and "-" in self.display_contents:
                self.display_contents = ""
            else:
                self.display_contents = self.display_contents[:len(self.display_contents) - 1]
            self.update()

    def equals(self):
        if self.prev_contents != "" and self.display_contents != "":
            y = float(self.holder)
            z = float(self.display_contents)
            o = self.prev_contents[len(self.prev_contents) - 1]
            if o == '+':
                self.display_contents = str(float(y + z))
            if o == '-':
                self.display_contents = str(float(y - z))
            if o == '*':
                self.display_contents = str(float(y * z))
            if o == '/':
                self.display_contents = str(float(y / z))
            self.holder = None
            self.prev_contents = ""
            self.update()
        if self.prev_contents != "" and self.display_contents == "":
            self.prev_contents = ""
            self.display_contents = str(self.holder)
            self.holder = None
            self.update()

    def operation(self, o):
        """
        Handles inputs of arithmetic operation buttons
        :param o: character representing which operation to perform
        """
        if self.display_contents != "":
            if self.prev_contents == "":
                self.holder = float(self.display_contents)
                self.prev_contents = str(self.holder) + str(o)
                self.display_contents = ""
                self.update()
            else:
                if o == '+':
                    self.holder += float(self.display_contents)
                if o == '-':
                    self.holder -= float(self.display_contents)
                if o == '*':
                    self.holder *= float(self.display_contents)
                if o == '/':
                    self.holder /= float(self.display_contents)
                self.prev_contents = str(self.holder) + str(o)
                self.display_contents = ""
                self.update()
        else:
            if self.prev_contents != "":
                self.prev_contents = self.prev_contents[:len(self.prev_contents) - 1] + str(o)
                self.update()

    def inputs(self, arg):
        """
        Calls various functions based on which calculator button was clicked
        :param arg: character denoting which button was clicked on calculator
        """
        if arg == '.':          # decimal input
            self.dot()
            return
        if arg.isnumeric():     # number input
            self.numeric(arg)
            return
        if arg == 'c':          # clear all, C, input
            self.display_contents = ""
            self.prev_contents = ""
            self.holder = None
            self.update()
            return
        if arg == 'e':          # clear current entry, CE, input
            self.display_contents = ""
            self.update()
            return
        if arg == '<':          # backspace input
            self.back_space()
            return
        if arg == '=':          # equals input
            self.equals()
            return
        if arg == '+' or arg == '-' or arg == '*' or arg == '/':     # operation inputs
            self.operation(arg)
        if arg == '#':  # negation input
            if len(self.display_contents) >= 1 and self.display_contents != ".":
                if "." in self.display_contents:
                    self.display_contents = str(float(self.display_contents) * -1)
                else:
                    self.display_contents = str(int(self.display_contents) * -1)
                self.update()
                return

    def make_calc(self, w):
        """
        Create buttons and labels, layout calculator widgets
        :param w: Tkinter window
        """
        button1 = tk.Button(w, text="1", width=10, command=lambda: self.inputs('1'), height=4, relief="raised")
        button2 = tk.Button(w, text="2", width=10, command=lambda: self.inputs('2'), height=4, relief="raised")
        button3 = tk.Button(w, text="3", width=10, command=lambda: self.inputs('3'), height=4, relief="raised")
        button4 = tk.Button(w, text="4", width=10, command=lambda: self.inputs('4'), height=4, relief="raised")
        button5 = tk.Button(w, text="5", width=10, command=lambda: self.inputs('5'), height=4, relief="raised")
        button6 = tk.Button(w, text="6", width=10, command=lambda: self.inputs('6'), height=4, relief="raised")
        button7 = tk.Button(w, text="7", width=10, command=lambda: self.inputs('7'), height=4, relief="raised")
        button8 = tk.Button(w, text="8", width=10, command=lambda: self.inputs('8'), height=4, relief="raised")
        button9 = tk.Button(w, text="9", width=10, command=lambda: self.inputs('9'), height=4, relief="raised")
        button0 = tk.Button(w, text="0", width=10, command=lambda: self.inputs('0'), height=4, relief="raised")
        button_negate = tk.Button(w, text="+/-", width=10, command=lambda: self.inputs('#'), height=4, relief="raised")
        button_dot = tk.Button(w, text=".", width=10, command=lambda: self.inputs('.'), height=4, relief="raised")
        button_add = tk.Button(w, text="+", width=10, command=lambda: self.inputs('+'), height=4, relief="raised")
        button_sub = tk.Button(w, text="-", width=10, command=lambda: self.inputs('-'), height=4, relief="raised")
        button_mul = tk.Button(w, text="*", width=10, command=lambda: self.inputs('*'), height=4, relief="raised")
        button_div = tk.Button(w, text="/", width=10, command=lambda: self.inputs('/'), height=4, relief="raised")
        button_enter = tk.Button(w, text="=", width=10, command=lambda: self.inputs('='), height=4, relief="raised")
        button_del = tk.Button(w, text="<<", width=10, command=lambda: self.inputs('<'), height=4, relief="raised")
        button_ca = tk.Button(w, text="CE", width=10, command=lambda: self.inputs('e'), height=4, relief="raised")
        button_c = tk.Button(w, text="C", width=10, command=lambda: self.inputs('c'), height=4, relief="raised")
        display = tk.Label(w, text="Welcome", width=35, height=5, bg="light grey", font=("Arial", 13),
                           borderwidth=1, relief="solid")
        prev = tk.Label(w, width=15, bg="light grey", font=("Arial", 10))
        button1.grid(row=6, column=0)
        button2.grid(row=6, column=1)
        button3.grid(row=6, column=2)
        button_add.grid(row=6, column=3)
        button4.grid(row=5, column=0)
        button5.grid(row=5, column=1)
        button6.grid(row=5, column=2)
        button_sub.grid(row=5, column=3)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=4, column=2)
        button_mul.grid(row=4, column=3)
        button0.grid(row=7, column=1)
        button_negate.grid(row=7, column=0)
        button_dot.grid(row=7, column=2)
        display.grid(row=0, column=0, rowspan=3, columnspan=4)
        prev.grid(row=0, column=2, columnspan=2)
        button_enter.grid(row=7, column=3)
        button_div.grid(row=3, column=3)
        button_ca.grid(row=3, column=0)
        button_c.grid(row=3, column=1)
        button_del.grid(row=3, column=2)
        self.display = display
        self.prev = prev

x = Calculator()    # create calculator instance to run
