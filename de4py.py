import sys
import tokenize
from Protections import StringEncryption

class de4py:
    file_path : str
    tokens : list


    def __init__(self):
       try:
          self.file_path = sys.argv[1]
       except IndexError:
          print("usage: de4py <script.py>")
          raise IndexError
       try:
          with open(self.file_path, 'rb') as f:
            self.tokens = list(tokenize.tokenize(f.readline))
       except FileNotFoundError:
            raise FileNotFoundError


    def execute_protections(self):
        StringEncryption.HexStringEncryption.decode(self.tokens)


if __name__ == "__main__":
    deobfuscator = de4py()

    deobfuscator.execute_protections()

    with open("out.py", 'wb') as f:
        f.write(tokenize.untokenize(deobfuscator.tokens))

    input()
    

