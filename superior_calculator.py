from tkinter import *
# main import we use for this program
import math as m
# this is used to help with some of the calculations

bruh = Tk()
# making an object of the Tk() class, which contains the window/functions we're going to use
bruh.title("A very nice mf calculator")
# just gives the window we're going to print a title

e = Entry(bruh, width=55, borderwidth=5)
# this line assigns the entry box to a variable
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
# this line actually prints it to the screen

# Both of these can be condensed into one line but it's more organized to seperate them

def click(input):
    e.insert(END, input)


# this inserts ONLY the numbers that the user inputs through the buttons

def clear():
    e.delete(0, END)


# this deletes all the contents of the entry box


def add(num1, num2):
    return float(num1) + float(num2)


def mult(num1, num2):
    return float(num1) * float(num2)


def sub(num1, num2):
    return float(num1) - float(num2)


def div(num1, num2):
    return float(num1) / float(num2)


def square_root(num1):
    return m.sqrt(float(num1))


def percentage(num1):
    return float(num1) / 100


def squared(num1):
    return float(num1) * float(num1)


# all of those pretty much do what they say, they take parameters and make calculations accordingly


# this is where it gets fun
def equals():
    nums = e.get().split()
    # this takes all the contents of the input box, and 'splits' each element into a separate element into a list,
    # making it very easy to sift through
    i = 0
    # this is the counter variable we're going to use to traverse the list
    while '%' in nums:
        # if a % sign is in the list at all, this loop will go through and make the necessary calculations
        if nums[i] == '%':
            yeah = percentage(nums[i - 1])
            nums.remove(nums[i])
            nums.remove(nums[i - 1])
            nums.insert(i - 1, yeah)
            i = 0
            # basically, if the element I'm on is a % sign, I know that the number before it should be divided by
            # 100, so I make 'yeah' the new number after I pass it through the "percentage" function, remove the old
            # elements from the list, and insert in the new number, divided by 100, and without the % sign
        else:
            i += 1
            # if the element if on ISN'T a % sign, but I know that there's still a % sign somewhere cause I'm
            # still in the loop, just add one to the count
    while "^2" in nums:
        if nums[i] == "^2":
            yeah = squared(nums[i - 1])
            nums.remove(nums[i])
            nums.remove(nums[i - 1])
            nums.insert(i - 1, yeah)
            i = 0
            # The reason I set i back to 0 if I come across an element is because the element is no longer in the list,
            # and I need to start back at the beginning to find more operations to do, if there is any
        else:
            i += 1
    while "sqrt{" in nums:
        if nums[i] == "sqrt{":
            yeah = square_root(nums[i + 1])
            nums.remove(nums[i])
            nums.remove(nums[i])
            nums.insert(i, yeah)
            i = 0
        else:
            i += 1
    while ("x" in nums) or ("/" in nums):
        if nums[i] == "x":
            yeah = mult(nums[i - 1], nums[i + 1])
            nums.remove(nums[i + 1])
            nums.remove(nums[i])
            nums.remove(nums[i - 1])
            nums.insert(i - 1, yeah)
            i = 0
        elif nums[i] == "/":
            yeah = div(nums[i - 1], nums[i + 1])
            nums.remove(nums[i + 1])
            nums.remove(nums[i])
            nums.remove(nums[i - 1])
            nums.insert(i - 1, yeah)
            i = 0
        else:
            i += 1
            # most of these follow the same logic of "if it's in the list, do the calculation, replace the components
            # with the answer, and then start back over at the beginning of the list. Order actually does matter, and
            # that's why I have the 'x' and '/' before the '+' and the '-'
    while ("+" in nums) or ("-" in nums):
        if nums[i] == "+":
            yeah = add(nums[i - 1], nums[i + 1])
            nums.remove(nums[i + 1])
            nums.remove(nums[i])
            nums.remove(nums[i - 1])
            nums.insert(0, yeah)
            i = 0
        elif nums[i] == "-":
            yeah = sub(nums[i - 1], nums[i + 1])
            nums.remove(nums[i + 1])
            nums.remove(nums[i])
            nums.remove(nums[i - 1])
            nums.insert(0, yeah)
            i = 0
        else:
            i += 1
    e.delete(0, END)
    # clears the input box
    e.insert(0, nums[0])
    # after all those calculations, 'nums' is only going to have one attribute left : the answer. So I just insert
    # the answer into the box and bam, you have a working calculator


button1 = Button(bruh, text="1", padx=50, pady=50, command=lambda: click(1))
button2 = Button(bruh, text="2", padx=50, pady=50, command=lambda: click(2))
button3 = Button(bruh, text="3", padx=50, pady=50, command=lambda: click(3))
button4 = Button(bruh, text="4", padx=50, pady=50, command=lambda: click(4))
button5 = Button(bruh, text="5", padx=50, pady=50, command=lambda: click(5))
button6 = Button(bruh, text="6", padx=50, pady=50, command=lambda: click(6))
button7 = Button(bruh, text="7", padx=50, pady=50, command=lambda: click(7))
button8 = Button(bruh, text="8", padx=50, pady=50, command=lambda: click(8))
button9 = Button(bruh, text="9", padx=50, pady=50, command=lambda: click(9))
button0 = Button(bruh, text="0", padx=108, pady=50, command=lambda: click(0))
button_equal = Button(bruh, text="=", padx=108, pady=50, command=equals)
button_clear = Button(bruh, text="Clear", padx=97, pady=50, command=clear)
button_add = Button(bruh, text="+", padx=50, pady=50, command=lambda: e.insert(END, " + "))
button_sub = Button(bruh, text="-", padx=50, pady=50, command=lambda: e.insert(END, " - "))
button_mult = Button(bruh, text="x", padx=50, pady=50, command=lambda: e.insert(END, " x "))
button_decimal = Button(bruh, text=".", padx=52, pady=50, command=lambda: e.insert(END, "."))
button_div = Button(bruh, text="/", padx=50, pady=50, command=lambda: e.insert(END, " / "))
button_squared = Button(bruh, text="x^2", padx=50, pady=50, command=lambda: e.insert(END, " ^2 "))
button_sqrt = Button(bruh, text="sqrt", padx=50, pady=50, command=lambda: e.insert(END, " sqrt{ "))
button_perc = Button(bruh, text="%", padx=54, pady=50, command=lambda: e.insert(END, " % "))
# This is just me defining all the buttons and all their attributes

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)
button_add.grid(row=4, column=3)
button_clear.grid(row=5, column=0, columnspan=2)
button_mult.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_div.grid(row=1, column=3)
button_decimal.grid(row=4, column=2)
button_sqrt.grid(row=1, column=4)
button_perc.grid(row=3, column=4)
button_squared.grid(row=2, column=4)
# This is me actually adding the buttons to the window with me specifying where I want them

bruh.mainloop()
# I really don't know what this does, but it makes the program works so I added it here
