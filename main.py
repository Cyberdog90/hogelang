import sys
args = sys.argv
with open("source.s", "w") as f:
    f.write(".intel_syntax noprefix\n")
    f.write(".global main\n")
    f.write("main:\n")
    f.write("        mov rax, {}\n".format(args[1]))
    f.write("        ret\n")

    def main():
        pass


    if __name__ == '__main__':
        main()
