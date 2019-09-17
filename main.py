import sys

args = sys.argv
with open("source.s", "w") as f:
    f.write(".intel_syntax noprefix\n")
    f.write(".global main\n")
    f.write("main:\n")


    def main():
        string = args[1]
        while True:
            


        f.write("        mov rax, {}\n".format(0))
        f.write("        ret\n")


    if __name__ == '__main__':
        main()
