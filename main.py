with open("source.asm", "w") as f:
    f.write(".intel_syntax noprefix\n")
    f.write(".global main")
    f.write("main:")
    f.write("        mov rax, 42")
    f.write("        ret")

    def main():
        pass


    if __name__ == '__main__':
        main()
