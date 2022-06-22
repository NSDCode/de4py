import tokenize
import binascii
class HexStringEncryption:



    def decode(tokens):
        for n in range(len(tokens)):
            if tokens[n][0] == tokenize.STRING and tokens[n][1].startswith("b'"):
                #new_operand = eval(f"str({tokens[n][1]})")

                #print(tokens[n])
                new_operand = eval(f"binascii.unhexlify({tokens[n][1]})")

    
                print(new_operand)

               # input()

              # if (new_operand != tokens[n][1]):
              #     print(f"Restored string: {new_operand}")
              #     tokens[n] = (tokenize.STRING, f'"{new_operand}"')


                

                