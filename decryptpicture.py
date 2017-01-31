from PIL import Image

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

i = Image.open("PNG.png")

pixels = i.load()
width, height = i.size

i = 0
j = 0
all_pixels = []
message_in_morse = []
for x in range(height):
    for y in range(width):
        cpixel = pixels[y, x]
        if cpixel == 0:
            i += 1
        if cpixel == 1:
            j = i - j
            message_in_morse.append(chr(j))
            j = i
            i += 1
        all_pixels.append(cpixel)

message_in_morse_string = ''.join(message_in_morse)

print(from_morse(message_in_morse_string))

print(message_in_morse_string)





