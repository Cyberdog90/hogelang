with open("source.asm", "w") as f:
    f.write(".intel_syntax noprefix\n")
    f.write(".global main\n")
    f.write("main:\n")
    f.write("        mov rax, 42\n")
    f.write("        ret\n")

    def main():
        pass


    if __name__ == '__main__':
        main()
