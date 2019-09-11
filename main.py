import tkinter.filedialog
import os

"""
def main():
    root = tkinter.Tk()
    root.withdraw()
    file_type = [("file", "*")]
    idir = os.path.abspath(os.path.dirname(__file__))
    filename = tkinter.filedialog.askopenfilename(filetypes=file_type,
                                                  initialdir=idir)
    with open(filename, "r") as f:
        """

source = "(+;1,2)"
operator_stack = []
pointer = 0


def add_operator():
    pass


while True:
    data = list(source)
    print(data)
    if data[pointer] == "(":
        pointer += 1
        continue
    if data[pointer] == "+":
        operator_stack.append("+")

    break
