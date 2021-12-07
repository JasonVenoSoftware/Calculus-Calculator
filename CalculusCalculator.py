from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import math


# Declares f_num and math variables as ints for the BasicCalc class
f_num = 0
math_var = 0
pi = 3.1416  # Used in several Geometry classes


class Tk(tk.Tk):

    # __init__ function for class tk
    def __init__(self, *args, **kwargs):  # *args and **kwargs allow for any number of arguments
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different pages
        for F in (StartPage, BasicCalc, Solve, Matrix, Trigonometry, SystemEquations, TwoSystems, ThreeSystems,
                  Inverse, Geometry, Area, Volume, Circle, Square, Triangle, Cube, Cylinder, Pyramid,
                  Sphere, Cone):
            frame = F(container, self)

            # initializing frame of that object from the start page, BasicCalc, Solve, etc respectively with for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Home page", font="Times 16 bold underline")
        label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        button1 = ttk.Button(self, text="Basic Calculator", command=lambda: controller.show_frame(BasicCalc))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Solve for Variable", command=lambda: controller.show_frame(Solve))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Matrix", command=lambda: controller.show_frame(Matrix))
        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = ttk.Button(self, text="Trigonometry", command=lambda: controller.show_frame(Trigonometry))
        button4.grid(row=4, column=1, padx=10, pady=10)

        button5 = ttk.Button(self, text="System of Equations", command=lambda: controller.show_frame(SystemEquations))
        button5.grid(row=5, column=1, padx=10, pady=10)

        button6 = ttk.Button(self, text="Inverse", command=lambda: controller.show_frame(Inverse))
        button6.grid(row=1, column=2)

        button7 = ttk.Button(self, text="Geometry", command=lambda: controller.show_frame(Geometry))
        button7.grid(row=2, column=2)


class BasicCalc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Inserts each number
        def button_click(number):
            current = entry.get()
            entry.delete(0, END)
            entry.insert(0, str(current) + str(number))

        # Calculation functions
        def button_add():
            first_number = entry.get()
            global f_num  # Global variable so it can be used by any of the functions
            global math_var  # Makes variable 'math' global, allows it to be used in all functions
            math_var = "Add"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_subtract():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Subtract"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_times():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Multiply"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_division():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Divide"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_exponent():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Exponent"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_square_root():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Square root"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_natural_logarithm():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Natural logarithm"
            f_num = int(first_number)
            entry.delete(0, END)

        def button_log_of_ten():
            first_number = entry.get()
            global f_num
            global math_var
            math_var = "Log of ten"
            f_num = int(first_number)
            entry.delete(0, END)

        def clear():
            entry.delete(0, END)

        # Calculates answer, depending on which button/symbol is used
        def button_equal():
            second_number = entry.get()
            entry.delete(0, END)

            if math_var == "Add":
                entry.insert(0, f_num + int(second_number))

            if math_var == "Subtract":
                entry.insert(0, f_num - int(second_number))

            if math_var == "Multiply":
                entry.insert(0, f_num * int(second_number))

            if math_var == "Divide":
                entry.insert(0, f_num / int(second_number))

            if math_var == "Exponent":
                entry.insert(0, f_num ** int(second_number))

            if math_var == "Square root":
                entry.insert(0, f_num ** 0.5)

            if math_var == "Natural logarithm":
                entry.insert(0, np.log(np.array(f_num)))  # numpy and array calculate logarithms

            if math_var == "Log of ten":
                entry.insert(0, np.log10(np.array(f_num)))

        # Where user types in basic equation (no variables)
        entry = Entry(self, width=44)
        entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        # Basic calculator's buttons, starting with the return to start page button
        button_home = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="7", command=lambda: button_click(7))
        button1.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        button2 = ttk.Button(self, text="8", command=lambda: button_click(8))
        button2.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        button3 = ttk.Button(self, text="9", command=lambda: button_click(9))
        button3.grid(row=1, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")

        button4 = ttk.Button(self, text="4", command=lambda: button_click(4))
        button4.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        button5 = ttk.Button(self, text="5", command=lambda: button_click(5))
        button5.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        button6 = ttk.Button(self, text="6", command=lambda: button_click(6))
        button6.grid(row=2, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")

        button7 = ttk.Button(self, text="1", command=lambda: button_click(1))
        button7.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        button8 = ttk.Button(self, text="2", command=lambda: button_click(2))
        button8.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        button9 = ttk.Button(self, text="3", command=lambda: button_click(3))
        button9.grid(row=3, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")

        button0 = ttk.Button(self, text="0", command=lambda: button_click(0))
        button0.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_plus = ttk.Button(self, text="+", command=lambda: button_add())
        button_plus.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_minus = ttk.Button(self, text="-", command=lambda: button_subtract())
        button_minus.grid(row=3, column=3, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_multiply = ttk.Button(self, text="*", command=lambda: button_times())
        button_multiply.grid(row=2, column=3, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_divide = ttk.Button(self, text="/", command=lambda: button_division())
        button_divide.grid(row=1, column=3, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_equal = ttk.Button(self, text="=", command=button_equal)
        button_equal.grid(row=5, column=3, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_sqrt = ttk.Button(self, text="Sqrt", command=lambda: button_square_root())
        button_sqrt.grid(row=5, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_exp = ttk.Button(self, text="Exponent", command=lambda: button_exponent())
        button_exp.grid(row=5, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_nat_log = ttk.Button(self, text="LN", command=lambda: button_natural_logarithm())
        button_nat_log.grid(row=5, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")

        button_log = ttk.Button(self, text="Log", command=lambda: button_log_of_ten())
        button_log.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")


class Solve(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve_for_x():
            first_number = entrym.get()
            second_number = entryb.get()
            entry_label.config(text="")
            m = float(first_number)
            b = float(second_number)
            answer = (b*-1)/m
            entry_label.config(text=round(answer, 2))

        def clear_entries():
            entrym.delete(0, END)
            entryb.delete(0, END)
            entry_label.config(text="")

        instructions = ttk.Label(self, text="mx + b = 0, where first entry is m, second entry is b")
        instructions.grid(row=1, column=1, columnspan=5)

        entrym = Entry(self, width=8)
        entrym.grid(row=2, column=1, sticky="e")

        entryb = Entry(self, width=8)
        entryb.grid(row=2, column=3)

        entry_label = ttk.Label(self, text="")
        entry_label.grid(row=3, column=3)

        label1 = ttk.Label(self, text="Solve for variable")
        label1.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

        label2 = ttk.Label(self, text="= 0")
        label2.grid(row=2, column=5)

        label3 = ttk.Label(self, text="x = ")
        label3.grid(row=3, column=2)

        label4 = ttk.Label(self, text="x              +")
        label4.grid(row=2, column=2, columnspan=3, sticky="w")

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_solve = ttk.Button(self, text="Solve for x", command=lambda: solve_for_x())
        button_solve.grid(row=5, column=3)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear_entries())
        button_clear.grid(row=4, column=3)


class Matrix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        def calculate_matrix():
            array1 = list(map(int, entry1.get().split()))
            matrix1 = np.array(array1).reshape(int(entry_rows1.get()), int(entry_columns1.get()))
            array2 = list(map(int, entry2.get().split()))
            matrix2 = np.array(array2).reshape(int(entry_rows2.get()), int(entry_columns2.get()))
            answer_label2.config(text=np.dot(matrix1, matrix2))

        def clear():
            entry_rows1.delete(0, END)
            entry_columns1.delete(0, END)
            entry_rows2.delete(0, END)
            entry_columns2.delete(0, END)
            entry1.delete(0, END)
            entry2.delete(0, END)
            answer_label2.config(text="")

        rows1 = ttk.Label(self, text="Rows:")
        rows1.grid(row=1, column=1)
        entry_rows1 = Entry(self, width=3)
        entry_rows1.grid(row=1, column=2, columnspan=3)

        columns1 = ttk.Label(self, text="Columns:")
        columns1.grid(row=2, column=1)
        entry_columns1 = Entry(self, width=3)
        entry_columns1.grid(row=2, column=2, columnspan=3)

        entry1 = Entry(self, width=20)
        entry1.grid(row=3, column=1, columnspan=4)

        rows2 = ttk.Label(self, text="Rows:")
        rows2.grid(row=4, column=1)
        entry_rows2 = Entry(self, width=3)
        entry_rows2.grid(row=4, column=2, columnspan=3)

        columns2 = ttk.Label(self, text="Columns:")
        columns2.grid(row=5, column=1)
        entry_columns2 = Entry(self, width=3)
        entry_columns2.grid(row=5, column=2, columnspan=3)

        entry2 = Entry(self, width=20)
        entry2.grid(row=6, column=1, columnspan=4)

        answer_label = ttk.Label(self, text="Answer:")
        answer_label.grid(row=7, column=1)
        answer_label2 = ttk.Label(self, text="")
        answer_label2.grid(row=8, column=1, columnspan=5)

        button_make = ttk.Button(self, text="Create", command=lambda: calculate_matrix())
        button_make.grid(row=9, column=1)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=9, column=2)


class Trigonometry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        def sine():
            number = float(entry.get())
            new_number = math.sin(math.radians(number))
            entry.delete(0, END)
            entry.insert(0, round(new_number, 9))  # Rounded 9 digits to match output of my calculator

        def cosine():
            number = float(entry.get())
            new_number = math.cos(math.radians(number))
            entry.insert(0, round(new_number, 9))

        def tangent():
            number = float(entry.get())
            new_number = math.tan(math.radians(number))
            entry.insert(0, round(new_number, 9))

        def arcsin():
            number = float(entry.get())
            new_number = math.asin(number)
            new_number = (new_number * 180)/pi
            entry.insert(0, round(new_number, 9))

        def arccos():
            number = float(entry.get())
            new_number = math.acos(number)
            new_number = (new_number * 180)/pi
            entry.insert(0, round(new_number, 9))

        def arctan():
            number = float(entry.get())
            new_number = math.atan(number)
            new_number = (new_number * 180)/pi
            entry.insert(0, round(new_number, 9))

        def clear():
            entry.delete(0, END)

        entry = Entry(self, width=44)
        entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        button_sin = Button(self, text="Sin", command=lambda: sine())
        button_sin.grid(row=1, column=1, padx=10, pady=10)

        button_cos = Button(self, text="Cos", command=lambda: cosine())
        button_cos.grid(row=1, column=2, padx=10, pady=10)

        button_tan = Button(self, text="Tan", command=lambda: tangent())
        button_tan.grid(row=1, column=3, padx=10, pady=10)

        button_asin = Button(self, text="Sin^-1", command=lambda: arcsin())
        button_asin.grid(row=2, column=1, padx=10, pady=10)

        button_acos = Button(self, text="Cos^-1", command=lambda: arccos())
        button_acos.grid(row=2, column=2, padx=10, pady=10)

        button_atan = Button(self, text="Tan^-1", command=lambda: arctan())
        button_atan.grid(row=2, column=3, padx=10, pady=10)

        button_clear = Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=3, column=1, padx=10, pady=10)


class SystemEquations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_two = ttk.Button(self, text="2 equations, 2 variables",
                                command=lambda: controller.show_frame(TwoSystems))
        button_two.grid(row=1, column=1)

        button_three = ttk.Button(self, text="3 equations, 3 variables",
                                  command=lambda: controller.show_frame(ThreeSystems))
        button_three.grid(row=2, column=1)


class TwoSystems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_back = ttk.Button(self, text="Systems page", command=lambda: controller.show_frame(SystemEquations))
        button_back.grid(row=1, column=0)

        def solve():
            matrix1 = np.array([[entry_x1.get(), entry_y1.get()], [entry_x2.get(), entry_y2.get()]], dtype='float')
            inverse1 = np.linalg.inv(matrix1)
            matrix2 = np.array([answer1.get(), answer2.get()], dtype='float')
            answer_matrix = np.round(inverse1.dot(matrix2), decimals=10)
            final_answer_label2_x.config(text=round(answer_matrix[0], 2))
            final_answer_label2_y.config(text=round(answer_matrix[1], 2))

            # To solve for x and y, dot multiply the inverse of the first matrix with the answer matrix
            # AX = B, so X = inv(A)B -> A = first matrix, B = answer matrix, X = x and y values

        def clear():
            entry_x1.delete(0, END)
            entry_y1.delete(0, END)
            entry_x2.delete(0, END)
            entry_y2.delete(0, END)
            answer1.delete(0, END)
            answer2.delete(0, END)
            final_answer_label2_x.config(text="")
            final_answer_label2_y.config(text="")

        entry_x1 = Entry(self, width=5)
        entry_x1.grid(row=1, column=1)
        label_x1 = ttk.Label(self, text="x   +   ")
        label_x1.grid(row=1, column=2)

        entry_y1 = Entry(self, width=5)
        entry_y1.grid(row=1, column=3)
        label_y1 = ttk.Label(self, text="y   =   ")
        label_y1.grid(row=1, column=4)

        answer1 = Entry(self, width=5)
        answer1.grid(row=1, column=5)

        entry_x2 = Entry(self, width=5)
        entry_x2.grid(row=2, column=1)
        label_x2 = ttk.Label(self, text="x   +   ")
        label_x2.grid(row=2, column=2)

        entry_y2 = Entry(self, width=5)
        entry_y2.grid(row=2, column=3)
        label_y2 = ttk.Label(self, text="y   =   ")
        label_y2.grid(row=2, column=4)

        answer2 = Entry(self, width=5)
        answer2.grid(row=2, column=5)

        solve_button = ttk.Button(self, text="Solve", command=lambda: solve())
        solve_button.grid(row=3, column=1, columnspan=2)

        clear_button = ttk.Button(self, text="Clear", command=lambda: clear())
        clear_button.grid(row=3, column=3, columnspan=2)

        final_answer_label_x = ttk.Label(self, text="x   =   ")
        final_answer_label_x.grid(row=4, column=2)
        final_answer_label2_x = ttk.Label(self, text="")
        final_answer_label2_x.grid(row=4, column=3)

        final_answer_label_y = ttk.Label(self, text="y   =   ")
        final_answer_label_y.grid(row=5, column=2)
        final_answer_label2_y = ttk.Label(self, text="")
        final_answer_label2_y.grid(row=5, column=3)


class ThreeSystems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            array1 = np.array([[entry_x1.get(), entry_y1.get(), entry_z1.get()],
                               [entry_x2.get(), entry_y2.get(), entry_z2.get()],
                               [entry_x3.get(), entry_y3.get(), entry_z3.get()]], dtype="float")
            array2 = np.array([answer1.get(), answer2.get(), answer3.get()], dtype="float")
            final_answer = np.linalg.solve(array1, array2)
            final_x_label2.config(text=round(final_answer[0], 2))
            final_y_label2.config(text=round(final_answer[1], 2))
            final_z_label2.config(text=round(final_answer[2], 2))

        def clear():
            entry_x1.delete(0, END)
            entry_y1.delete(0, END)
            entry_z1.delete(0, END)
            entry_x2.delete(0, END)
            entry_z2.delete(0, END)
            entry_y2.delete(0, END)
            entry_x3.delete(0, END)
            entry_y3.delete(0, END)
            entry_z3.delete(0, END)
            answer1.delete(0, END)
            answer2.delete(0, END)
            answer3.delete(0, END)
            final_x_label2.config(text="")
            final_y_label2.config(text="")
            final_z_label2.config(text="")

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

        button_back = ttk.Button(self, text="Systems page", command=lambda: controller.show_frame(SystemEquations))
        button_back.grid(row=1, column=0)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=4, column=1, columnspan=2)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=4, column=4, columnspan=2)

        entry_x1 = Entry(self, width=5)
        entry_x1.grid(row=1, column=1)
        label_x1 = ttk.Label(self, text="x   +   ")
        label_x1.grid(row=1, column=2)

        entry_y1 = Entry(self, width=5)
        entry_y1.grid(row=1, column=3)
        label_y1 = ttk.Label(self, text="y   +   ")
        label_y1.grid(row=1, column=4)

        entry_z1 = Entry(self, width=5)
        entry_z1.grid(row=1, column=5)
        label_z1 = ttk.Label(self, text="z   =   ")
        label_z1.grid(row=1, column=6)

        answer1 = Entry(self, width=5)
        answer1.grid(row=1, column=7)

        entry_x2 = Entry(self, width=5)
        entry_x2.grid(row=2, column=1)
        label_x2 = ttk.Label(self, text="x   +   ")
        label_x2.grid(row=2, column=2)

        entry_y2 = Entry(self, width=5)
        entry_y2.grid(row=2, column=3)
        label_y2 = ttk.Label(self, text="y   +   ")
        label_y2.grid(row=2, column=4)

        entry_z2 = Entry(self, width=5)
        entry_z2.grid(row=2, column=5)
        label_z2 = ttk.Label(self, text="z   =   ")
        label_z2.grid(row=2, column=6)

        answer2 = Entry(self, width=5)
        answer2.grid(row=2, column=7)

        entry_x3 = Entry(self, width=5)
        entry_x3.grid(row=3, column=1)
        label_x3 = ttk.Label(self, text="x   +   ")
        label_x3.grid(row=3, column=2)

        entry_y3 = Entry(self, width=5)
        entry_y3.grid(row=3, column=3)
        label_y3 = ttk.Label(self, text="y   +   ")
        label_y3.grid(row=3, column=4)

        entry_z3 = Entry(self, width=5)
        entry_z3.grid(row=3, column=5)
        label_z3 = ttk.Label(self, text="z   =   ")
        label_z3.grid(row=3, column=6)

        answer3 = Entry(self, width=5)
        answer3.grid(row=3, column=7)

        final_x_label = ttk.Label(self, text="             x=")
        final_x_label.grid(row=5, column=0)
        final_x_label2 = ttk.Label(self, text="")
        final_x_label2.grid(row=5, column=1)

        final_y_label = ttk.Label(self, text="y=")
        final_y_label.grid(row=5, column=2)
        final_y_label2 = ttk.Label(self, text="")
        final_y_label2.grid(row=5, column=3)

        final_z_label = ttk.Label(self, text="z=")
        final_z_label.grid(row=5, column=4)
        final_z_label2 = ttk.Label(self, text="")
        final_z_label2.grid(row=5, column=5)


class Inverse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            m = int(m_entry.get())
            b = int(m_entry.get())
            equation = (str(m) + "x + " + str(b))
            inverse = ("(x - " + str(b) + ")/ " + str(m))
            f_label2.config(text=equation)
            f_inv_label2.config(text=inverse)

        def clear():
            m_entry.delete(0, END)
            b_entry.delete(0, END)
            f_label2.config(text="")
            f_inv_label2.config(text="")

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=6, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=6, column=2)

        formula_label = ttk.Label(self, text="y = mx + b: ")
        formula_label.grid(row=1, column=1, columnspan=2)

        m_label = ttk.Label(self, text="m = ")
        m_label.grid(row=2, column=1)
        m_entry = Entry(self, width=10)
        m_entry.grid(row=2, column=2)

        b_label = ttk.Label(self, text="b = ")
        b_label.grid(row=3, column=1)
        b_entry = Entry(self, width=10)
        b_entry.grid(row=3, column=2)

        f_label = ttk.Label(self, text="f(x) = ")
        f_label.grid(row=4, column=1)
        f_label2 = ttk.Label(self, text="")
        f_label2.grid(row=4, column=2)

        f_inv_label = ttk.Label(self, text="f^-1(x) = ")
        f_inv_label.grid(row=5, column=1)
        f_inv_label2 = ttk.Label(self, text="")
        f_inv_label2.grid(row=5, column=2)


class Geometry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_area = ttk.Button(self, text="Area of shape", command=lambda: controller.show_frame(Area))
        button_area.grid(row=1, column=1)

        button_volume = ttk.Button(self, text="Volume of object", command=lambda: controller.show_frame(Volume))
        button_volume.grid(row=2, column=1)


class Area(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_back = ttk.Button(self, text="Geometry page", command=lambda: controller.show_frame(Geometry))
        button_back.grid(row=1, column=0, padx=10, pady=10)

        area_label = ttk.Label(self, text="Area of: ")
        area_label.grid(row=1, column=2)

        button_circle = ttk.Button(self, text="Circle", command=lambda: controller.show_frame(Circle))
        button_circle.grid(row=2, column=2)

        button_square = ttk.Button(self, text="Square", command=lambda: controller.show_frame(Square))
        button_square.grid(row=3, column=2)

        button_triangle = ttk.Button(self, text="Triangle", command=lambda: controller.show_frame(Triangle))
        button_triangle.grid(row=4, column=2)


class Circle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            radius = int(radius_entry.get())
            area = ((radius * radius) * pi)
            circumference = (2 * pi * radius)
            area_label2.config(text=round(area, 2))
            circumference_label2.config(text=round(circumference, 2))

        def clear():
            radius_entry.delete(0, END)
            area_label2.config(text="")
            circumference_label2.config(text="")

        button_home = ttk.Button(self, text="Area page", command=lambda: controller.show_frame(Area))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=5, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=5, column=2)

        radius_label = ttk.Label(self, text="Radius: ")
        radius_label.grid(row=1, column=1)
        radius_entry = Entry(self, width=10)
        radius_entry.grid(row=1, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=2, column=1, columnspan=2)

        area_label = ttk.Label(self, text="Area: ")
        area_label.grid(row=3, column=1)
        area_label2 = ttk.Label(self, text="")
        area_label2.grid(row=3, column=2)

        circumference_label = ttk.Label(self, text="Circumference: ")
        circumference_label.grid(row=4, column=1)
        circumference_label2 = ttk.Label(self, text="")
        circumference_label2.grid(row=4, column=2)


class Square(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            length = int(length_entry.get())
            width = int(width_entry.get())
            area = (length * width)
            perimeter = 2 * (length + width)
            area_label2.config(text=round(area, 2))
            perimeter_label2.config(text=round(perimeter, 2))

        def clear():
            length_entry.delete(0, END)
            width_entry.delete(0, END)
            area_label2.config(text="")
            perimeter_label2.config(text="")

        button_home = ttk.Button(self, text="Area page", command=lambda: controller.show_frame(Area))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=6, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=6, column=2)

        length_label = ttk.Label(self, text="Length: ")
        length_label.grid(row=1, column=1)
        length_entry = Entry(self, width=10)
        length_entry.grid(row=1, column=2)

        width_label = ttk.Label(self, text="Width: ")
        width_label.grid(row=2, column=1)
        width_entry = Entry(self, width=10)
        width_entry.grid(row=2, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=3, column=1, columnspan=2)

        area_label = ttk.Label(self, text="Area: ")
        area_label.grid(row=4, column=1)
        area_label2 = ttk.Label(self, text="")
        area_label2.grid(row=4, column=2)

        perimeter_label = ttk.Label(self, text="Perimeter: ")
        perimeter_label.grid(row=5, column=1)
        perimeter_label2 = ttk.Label(self, text="")
        perimeter_label2.grid(row=5, column=2)


class Triangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            side1 = int(side1_entry.get())
            side2 = int(side2_entry.get())
            base = int(base_entry.get())
            height = int(height_entry.get())
            area = (base * height) * 0.5
            perimeter = (side1 + side2 + base)
            area_label2.config(text=round(area, 2))
            perimeter_label2.config(text=round(perimeter, 2))

        def clear():
            side1_entry.delete(0, END)
            side2_entry.delete(0, END)
            base_entry.delete(0, END)
            height_entry.delete(0, END)
            area_label2.config(text="")
            perimeter_label2.config(text="")

        button_home = ttk.Button(self, text="Area page", command=lambda: controller.show_frame(Area))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=8, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=8, column=2)

        side1_label = ttk.Label(self, text="Side: ")
        side1_label.grid(row=1, column=1)
        side1_entry = Entry(self, width=10)
        side1_entry.grid(row=1, column=2)

        side2_label = ttk.Label(self, text="Side: ")
        side2_label.grid(row=2, column=1)
        side2_entry = Entry(self, width=10)
        side2_entry.grid(row=2, column=2)

        base_label = ttk.Label(self, text="Base: ")
        base_label.grid(row=3, column=1)
        base_entry = Entry(self, width=10)
        base_entry.grid(row=3, column=2)

        height_label = ttk.Label(self, text="Height: ")
        height_label.grid(row=4, column=1)
        height_entry = Entry(self, width=10)
        height_entry.grid(row=4, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=5, column=1, columnspan=2)

        area_label = ttk.Label(self, text="Area: ")
        area_label.grid(row=6, column=1)
        area_label2 = ttk.Label(self, text="")
        area_label2.grid(row=6, column=2)

        perimeter_label = ttk.Label(self, text="Perimeter: ")
        perimeter_label.grid(row=7, column=1)
        perimeter_label2 = ttk.Label(self, text="")
        perimeter_label2.grid(row=7, column=2)


class Volume(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_home = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(StartPage))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_back = ttk.Button(self, text="Geometry page", command=lambda: controller.show_frame(Geometry))
        button_back.grid(row=1, column=0, padx=10, pady=10)

        volume_label = ttk.Label(self, text="Volume of: ")
        volume_label.grid(row=2, column=2)

        button_cube = ttk.Button(self, text="Cube", command=lambda: controller.show_frame(Cube))
        button_cube.grid(row=3, column=2)

        button_cylinder = ttk.Button(self, text="Cylinder", command=lambda: controller.show_frame(Cylinder))
        button_cylinder.grid(row=4, column=2)

        button_pyramid = ttk.Button(self, text="Pyramid", command=lambda: controller.show_frame(Pyramid))
        button_pyramid.grid(row=5, column=2)

        button_sphere = ttk.Button(self, text="Sphere", command=lambda: controller.show_frame(Sphere))
        button_sphere.grid(row=6, column=2)

        button_cone = ttk.Button(self, text="Cone", command=lambda: controller.show_frame(Cone))
        button_cone.grid(row=7, column=2)


class Cube(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            length = int(length_entry.get())
            width = int(width_entry.get())
            height = int(height_entry.get())
            volume = (length * height * width)
            surface_area = ((2 * length * width) + (2 * length * height) + (2 * width * height))
            volume_label2.config(text=round(volume, 2))
            surface_label2.config(text=round(surface_area, 2))

        def clear():
            length_entry.delete(0, END)
            width_entry.delete(0, END)
            height_entry.delete(0, END)
            volume_label2.config(text="")
            surface_label2.config(text="")

        button_home = ttk.Button(self, text="Volume page", command=lambda: controller.show_frame(Volume))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=7, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=7, column=2)

        length_label = ttk.Label(self, text="Length: ")
        length_label.grid(row=1, column=1)
        length_entry = Entry(self, width=10)
        length_entry.grid(row=1, column=2)

        width_label = ttk.Label(self, text="Width: ")
        width_label.grid(row=2, column=1)
        width_entry = Entry(self, width=10)
        width_entry.grid(row=2, column=2)

        height_label = ttk.Label(self, text="Height: ")
        height_label.grid(row=3, column=1)
        height_entry = Entry(self, width=10)
        height_entry.grid(row=3, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=4, column=1, columnspan=2)

        volume_label = ttk.Label(self, text="Volume: ")
        volume_label.grid(row=5, column=1)
        volume_label2 = ttk.Label(self, text="")
        volume_label2.grid(row=5, column=2)

        surface_label = ttk.Label(self, text="Surface Area: ")
        surface_label.grid(row=6, column=1)
        surface_label2 = ttk.Label(self, text="")
        surface_label2.grid(row=6, column=2)


class Cylinder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            radius = int(radius_entry.get())
            height = int(height_entry.get())
            volume = (pi * (radius * radius) * height)
            surface_area = ((2 * pi * radius * height) + (2 * pi * math.pow(radius, 2)))
            volume_label2.config(text=round(volume, 2))
            surface_label2.config(text=round(surface_area, 2))

        def clear():
            radius_entry.delete(0, END)
            height_entry.delete(0, END)
            volume_label2.config(text="")
            surface_label2.config(text="")

        button_home = ttk.Button(self, text="Volume page", command=lambda: controller.show_frame(Volume))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=6, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=6, column=2)

        radius_label = ttk.Label(self, text="Radius: ")
        radius_label.grid(row=1, column=1)
        radius_entry = Entry(self, width=10)
        radius_entry.grid(row=1, column=2)

        height_label = ttk.Label(self, text="Height: ")
        height_label.grid(row=2, column=1)
        height_entry = Entry(self, width=10)
        height_entry.grid(row=2, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=3, column=1, columnspan=2)

        volume_label = ttk.Label(self, text="Volume: ")
        volume_label.grid(row=4, column=1)
        volume_label2 = ttk.Label(self, text="")
        volume_label2.grid(row=4, column=2)

        surface_label = ttk.Label(self, text="Surface Area: ")
        surface_label.grid(row=5, column=1)
        surface_label2 = ttk.Label(self, text="")
        surface_label2.grid(row=5, column=2)


class Pyramid(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            l = int(base_l_entry.get())  # length, width, and height names shortened for longer formula
            w = int(base_w_entry.get())
            h = int(height_entry.get())
            volume = (((l * w) * h)/3)
            surface_area = (l * w) + (l * math.sqrt(math.pow(w/2, 2) + math.pow(h, 2)) + (w * math.sqrt(math.pow(l/2, 2) + math.pow(h, 2))))
            volume_label2.config(text=round(volume, 2))
            surface_label2.config(text=round(surface_area, 2))

        def clear():
            base_l_entry.delete(0, END)
            base_w_entry.delete(0, END)
            height_entry.delete(0, END)
            volume_label2.config(text="")
            surface_label2.config(text="")

        button_home = ttk.Button(self, text="Volume page", command=lambda: controller.show_frame(Volume))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=7, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=7, column=2)

        base_l_label = ttk.Label(self, text="Base length: ")
        base_l_label.grid(row=1, column=1)
        base_l_entry = Entry(self, width=10)
        base_l_entry.grid(row=1, column=2)

        base_w_label = ttk.Label(self, text="Base width: ")
        base_w_label.grid(row=2, column=1)
        base_w_entry = Entry(self, width=10)
        base_w_entry.grid(row=2, column=2)

        height_label = ttk.Label(self, text="Height: ")
        height_label.grid(row=3, column=1)
        height_entry = Entry(self, width=10)
        height_entry.grid(row=3, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=4, column=1, columnspan=2)

        volume_label = ttk.Label(self, text="Volume: ")
        volume_label.grid(row=5, column=1)
        volume_label2 = ttk.Label(self, text="")
        volume_label2.grid(row=5, column=2)

        surface_label = ttk.Label(self, text="Surface Area: ")
        surface_label.grid(row=6, column=1)
        surface_label2 = ttk.Label(self, text="")
        surface_label2.grid(row=6, column=2)


class Sphere(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            radius = int(radius_entry.get())
            volume = (4/3 * pi * math.pow(radius, 3))
            surface_area = (4 * pi * math.pow(radius, 2))
            volume_label2.config(text=round(volume, 2))
            surface_label2.config(text=round(surface_area, 2))

        def clear():
            radius_entry.delete(0, END)
            volume_label2.config(text="")
            surface_label2.config(text="")

        button_home = ttk.Button(self, text="Volume page", command=lambda: controller.show_frame(Volume))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=5, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=5, column=2)

        radius_label = ttk.Label(self, text="Radius: ")
        radius_label.grid(row=1, column=1)
        radius_entry = Entry(self, width=10)
        radius_entry.grid(row=1, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=2, column=1, columnspan=2)

        volume_label = ttk.Label(self, text="Volume: ")
        volume_label.grid(row=3, column=1)
        volume_label2 = ttk.Label(self, text="")
        volume_label2.grid(row=3, column=2)

        surface_label = ttk.Label(self, text="Surface Area: ")
        surface_label.grid(row=4, column=1)
        surface_label2 = ttk.Label(self, text="")
        surface_label2.grid(row=4, column=2)


class Cone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def solve():
            radius = int(radius_entry.get())
            height = int(height_entry.get())
            volume = (1/3 * pi * math.pow(radius, 2) * height)
            surface_area = (pi * radius * (radius + math.sqrt((math.pow(height, 2) + math.pow(radius, 2)))))
            volume_label2.config(text=round(volume, 2))
            surface_label2.config(text=round(surface_area, 2))

        def clear():
            radius_entry.delete(0, END)
            height_entry.delete(0, END)
            volume_label2.config(text="")
            surface_label2.config(text="")

        button_home = ttk.Button(self, text="Volume page", command=lambda: controller.show_frame(Volume))
        button_home.grid(row=0, column=0, padx=10, pady=10)

        button_clear = ttk.Button(self, text="Clear", command=lambda: clear())
        button_clear.grid(row=6, column=1)

        button_solve = ttk.Button(self, text="Solve", command=lambda: solve())
        button_solve.grid(row=6, column=2)

        radius_label = ttk.Label(self, text="Radius: ")
        radius_label.grid(row=1, column=1)
        radius_entry = Entry(self, width=10)
        radius_entry.grid(row=1, column=2)

        height_label = ttk.Label(self, text="Height: ")
        height_label.grid(row=2, column=1)
        height_entry = Entry(self, width=10)
        height_entry.grid(row=2, column=2)

        warning_label = ttk.Label(self, text="------------------------------")
        warning_label.grid(row=3, column=1, columnspan=2)

        volume_label = ttk.Label(self, text="Volume: ")
        volume_label.grid(row=4, column=1)
        volume_label2 = ttk.Label(self, text="")
        volume_label2.grid(row=4, column=2)

        surface_label = ttk.Label(self, text="Surface Area: ")
        surface_label.grid(row=5, column=1)
        surface_label2 = ttk.Label(self, text="")
        surface_label2.grid(row=5, column=2)


root = Tk()
root.title("Calculus Calculator")
root.mainloop()
