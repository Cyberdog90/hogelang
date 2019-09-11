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

source = "(+;(+;112,2),2)"
operator_stack = []
value_stack = []
tmp_value = []
pointer = 0


def add_operator():
    pass


data = list(source)
while True:

    # print(data)
    if data[pointer] == "(":
        pointer += 1
        continue
    if data[pointer] == "+":
        operator_stack.append("+")
        pointer += 1
        continue
    if data[pointer] == ";":
        pointer += 1
        continue
    if data[pointer].isdecimal():
        tmp_value.append(data[pointer])
        while True:
            pointer += 1
            if data[pointer].isdecimal():
                tmp_value.append(data[pointer])
            else:
                break
        value_stack.append(int("".join(tmp_value)))
        tmp_value = []
    if data[pointer] == ",":
        pointer += 1
        continue
    if data[pointer] == ")":
        pointer += 1
        continue

print(pointer)
print(operator_stack)
print(value_stack)
