import sys

args = sys.argv
with open("source.s", "w") as f:
    string = args[1]
    f.write(".intel_syntax noprefix\n")
    f.write(".global main\n")
    f.write("main:\n")
    f.write("        mov rax, {}".format(strtol(string)))

    def main():

        while True:



        f.write("        mov rax, {}\n".format(0))
        f.write("        ret\n")

    def strtol(arg):
        for i in range(len(arg)):
            if arg[0:i].isdecimal():
                continue
            return arg[0:i-1]



    if __name__ == '__main__':
        main()
