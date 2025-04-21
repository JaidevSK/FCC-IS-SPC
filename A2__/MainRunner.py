from src.parser import *
from src.lexer import *
import argparse

def Runner(filename):
    try:
        with open(filename) as f:
            s = f.read()
    except Exception as e:
        print(e)

    try:
        tokens = lex(s)
    except Exception as e:
        print(e)
        return
    
    try:
        p = Parser(tokens)
        p.parse()
    except Exception as e:
        print(e)
        return
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the parser on a file')
    parser.add_argument('filename', type=str, help='The file to run the parser on')
    args = parser.parse_args()
    Runner(args.filename)


