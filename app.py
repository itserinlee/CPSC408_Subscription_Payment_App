from models.parser import Parser

def main():
    p = Parser()
    p.process_file()
    print(p)
    
if __name__ == "__main__":
    main()
    print("done")