import discord
import json
  
  if message.content.startswith('$orc'):
        textToTranslate = message.content[11:]
        print(message.channel)
        await message.channel.send(orc(textToTranslate))

def translate(text):
    #this is where you would do the actual translating. for example, text.maketrans(args)

    #this is an example:
    translated = ""
    for char in text:
        if (char == "a"):
            translated = translated + "a"
        elif (char == "A"): 
            translated = translated + "A"
            
        elif (char == "b"): 
            translated = translated + "z" 
        elif (char == "B"): 
            translated = translated + "Z"

        elif (char == "c"): 
            translated = translated + "y"
        elif (char == "C"): 
            translated = translated + "Y"
            
        elif (char == "d"): 
            translated = translated + "x"
        elif (char == "D"): 
            translated = translated + "X"
            
        elif (char == "e"): 
            translated = translated + "e"
        elif (char == "E"): 
            translated = translated + "E"
            
        elif (char == "f"): 
            translated = translated + "w"
        elif (char == "F"): 
            translated = translated + "W"
            
        elif (char == "g"): 
            translated = translated + "v"
        elif (char == "G"): 
            translated = translated + "V"
            
        elif (char == "h"): 
            translated = translated + "t"
        elif (char == "H"): 
            translated = translated + "T"
            
        elif (char == "i"): 
            translated = translated + "i"
        elif (char == "I"): 
            translated = translated + "I"
            
        elif (char == "j"): 
            translated = translated + "s"
        elif (char == "J"): 
            translated = translated + "S"
            
        elif (char == "k"): 
            translated = translated + "r"
        elif (char == "K"): 
            translated = translated + "R"
            
        elif (char == "l"): 
            translated = translated + "l"
        elif (char == "L"): 
            translated = translated + "L"
            
        elif (char == "m"): 
            translated = translated + "p"
        elif (char == "M"): 
            translated = translated + "P"
            
        elif (char == "n"): 
            translated = translated + "n"
        elif (char == "N"): 
            translated = translated + "N"
            
        elif (char == "o"): 
            translated = translated + "o"
        elif (char == "O"): 
            translated = translated + "O"
            
        elif (char == "p"): 
            translated = translated + "m"
        elif (char == "P"): 
            translated = translated + "M"
            
        elif (char == "q"): 
            translated = translated + "q"
        elif (char == "Q"): 
            translated = translated + "Q"
            
        elif (char == "r"): 
            translated = translated + "k"
        elif (char == "R"): 
            translated = translated + "K"
            
        elif (char == "s"): 
            translated = translated + "j"
        elif (char == "S"): 
            translated = translated + "J"
            
        elif (char == "t"): 
            translated = translated + "h"
        elif (char == "T"): 
            translated = translated + "H"
            
        elif (char == "u"): 
            translated = translated + "u"
        elif (char == "U"): 
            translated = translated + "U"
            
        elif (char == "v"): 
            translated = translated + "g"
        elif (char == "V"): 
            translated = translated + "G"
            
        elif (char == "w"): 
            translated = translated + "f"
        elif (char == "W"): 
            translated = translated + "F"
            
        elif (char == "x"): 
            translated = translated + "d"
        elif (char == "X"): 
            translated = translated + "D"
            
        elif (char == "y"): 
            translated = translated + "c"
        elif (char == "Y"): 
            translated = translated + "C"
            
        elif (char == "z"): 
            translated = translated + "b"
        elif (char == "Z"): 
            translated = translated + "B"
            
        elif (char == "l"):
            translated = translated + "1"
        elif (char == "2"):
            translated = translated + "2"
        elif (char == "3"):
            translated = translated + "3"
        elif (char == "4"):
            translated = translated + "4"
        elif (char == "5"):
            translated = translated + "5"
        elif (char == "6"):
            translated = translated + "6"
        elif (char == "7"):
            translated = translated + "7"
        elif (char == "8"):
            translated = translated + "8"
        elif (char == "9"):
            translated = translated + "9"
        elif (char == "0"):
            translated = translated + "0"
            
        elif (char == "‘"):
            translated = translated + "‘"       
        elif (char == "“"):
            translated = translated + "“"               
        elif (char == ","):
            translated = translated + ","     
        elif (char == "!"):
            translated = translated + "!"
        elif (char == "."):
            translated = translated + "."            
        elif (char == ";"):
            translated = translated + ";"
        elif (char == ":"):
            translated = translated + ":"
        elif (char == "?"):
            translated = translated + "?"
            
            
        elif (char != " "):
            translated = translated + "X"
        else:
            translated = translated + " "
    return translated
