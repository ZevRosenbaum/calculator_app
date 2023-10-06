# Basic Calculator App
# Author: Zev Rosenbaum
# Created: Oct 2023

import tkinter as tk
from tkinter import *
from tkinter import ttk

class calc( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.result = 0
        global label
        label=Label(self.master, text=self.result, font=('Aerial 18'), justify=RIGHT)
        label.pack()
        self.pack()
        self.master.title("Calculator")
        curr_result = 0


        # all clear (ac) calc button
        self.all_clear = Button( self, text = "AC", width = 25,
                               command = self.clear )
        self.all_clear.grid( row = 0, column = 1, columnspan = 1, sticky = W+E+N+S )
        # + or - button
        self.change_sign = Button( self, text = "+/-", width = 25,
                               command = self.change_signs )
        self.change_sign.grid( row = 0, column = 2, columnspan = 1, sticky = W+E+N+S )
        # % button
        self.percent_button = Button( self, text = "%", width = 25,
                               command = self.percentify )
        self.percent_button.grid( row = 0, column = 3, columnspan = 1, sticky = W+E+N+S )
        # divide button
        self.divide_button = Button( self, text = "÷", width = 25,
                               command = lambda: self.apply_operation('÷') )
        self.divide_button.grid( row = 0, column = 4, columnspan = 1, sticky = W+E+N+S )
        # 7 button
        self.seven_button = Button( self, text = "7", width = 25,
                               command = lambda: self.get_num(7) )
        self.seven_button.grid( row = 1, column = 1, columnspan = 1, sticky = W+E+N+S )
        # 8 button
        self.eight_button = Button( self, text = "8", width = 25,
                               command = lambda: self.get_num(8) )
        self.eight_button.grid( row = 1, column = 2, columnspan = 1, sticky = W+E+N+S )
        # 9 button
        self.nine_button = Button( self, text = "9", width = 25,
                               command = lambda: self.get_num(9) )
        self.nine_button.grid( row = 1, column = 3, columnspan = 1, sticky = W+E+N+S )
        # multiply button
        self.mult_button = Button( self, text = "x", width = 25,
                               command = lambda: self.apply_operation('x') )
        self.mult_button.grid( row = 1, column = 4, columnspan = 1, sticky = W+E+N+S )
        # 4 button
        self.four_button = Button( self, text = "4", width = 25,
                               command = lambda: self.get_num(4) )
        self.four_button.grid( row = 2, column = 1, columnspan = 1, sticky = W+E+N+S )
        # 5 button
        self.five_button = Button( self, text = "5", width = 25,
                               command = lambda: self.get_num(5) )
        self.five_button.grid( row = 2, column = 2, columnspan = 1, sticky = W+E+N+S )
        # 6 button
        self.six_button = Button( self, text = "6", width = 25,
                               command = lambda: self.get_num(6) )
        self.six_button.grid( row = 2, column = 3, columnspan = 1, sticky = W+E+N+S )
        # subtract button
        self.subtract_button = Button( self, text = "-", width = 25,
                               command = lambda: self.apply_operation('-') )
        self.subtract_button.grid( row = 2, column = 4, columnspan = 1, sticky = W+E+N+S )
        # 1 button
        self.one_button = Button( self, text = "1", width = 25,
                               command = lambda: self.get_num(1) )
        self.one_button.grid( row = 3, column = 1, columnspan = 1, sticky = W+E+N+S )
        # 2 button
        self.two_button = Button( self, text = "2", width = 25,
                               command = lambda: self.get_num(2) )
        self.two_button.grid( row = 3, column = 2, columnspan = 1, sticky = W+E+N+S )
        # 3 button
        self.three_button = Button( self, text = "3", width = 25,
                               command = lambda: self.get_num(3) )
        self.three_button.grid( row = 3, column = 3, columnspan = 1, sticky = W+E+N+S )
        # addition button
        self.add_button = Button( self, text = "+", width = 25,
                               command = lambda: self.apply_operation('+') )
        self.add_button.grid( row = 3, column = 4, columnspan = 1, sticky = W+E+N+S )
        # 0 button
        self.zero_button = Button( self, text = "0", width = 25,
                               command = lambda: self.get_num(0) )
        self.zero_button.grid( row = 4, column = 1, columnspan = 2, sticky = W+E+N+S )
        # decimal point button
        self.decimal_button = Button( self, text = ".", width = 25,
                               command = self.add_decimal )
        self.decimal_button.grid( row = 4, column = 3, columnspan = 1, sticky = W+E+N+S )
        # equal button
        self.eq_button = Button( self, text = "=", width = 25,
                               command = self.get_result )
        self.eq_button.grid( row = 4, column = 4, columnspan = 1, sticky = W+E+N+S )
        # quit button
        self.quit_button = Button( self, text = "Close Calculator", width = 25,
                               command = self.close_window )
        self.quit_button.grid( row = 5, column = 1, columnspan = 4, sticky = W+E+N+S )

    def apply_operation(self, operation):
        return -1
    
    def get_num(self, number):
        self.curr_result = number
        self.result = number
        print('my number is: ', number)
        self.update_result(number)

    def clear(self):
        self.result = 0
        self.curr_result = 0
        self.update_result(0)

    def change_signs(self):
        self.result *= -1
        self.curr_result = self.result
        self.update_result(self.curr_result)

    def percentify(self):
        return -1
    
    def add_decimal(self):
        return -1
    
    def get_result(self):
        self.result = self.curr_result

    def update_result(self, number):
        print("number: ", number, "curr_number: ", self.result)
        label.configure(text=number)
        #label.pack()

    def close_window(self):
        self.destroy()

def main(): 
    calc().mainloop()

if __name__ == '__main__':
    main()