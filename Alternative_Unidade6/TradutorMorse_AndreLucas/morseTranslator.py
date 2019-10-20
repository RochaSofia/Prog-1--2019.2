def morseTranslete(code):
    word = ""
    morse = {
        '.-'  : "a",    '.---': "j",    '...' : "s",
        '-...': "b",    '-.-' : "k",    '-'   : "t",
        '-.-.': "c",    '.-..': "l",    '..-' : "u",
        '-..' : "d",    '--'  : "m",    '...-': "v",
        '.'   : "e",    '-.'  : "n",    '.--' : "w",
        '..-.': "f",    '---' : "o",    '-..-': "x",
        '--.' : "g",   '.--.' : "p",    '-.--': "y",
        '....': "h",    '--.-': "q",    '--..': "z",
        '..'  : "i",    '.-.' : "r",
    }
    for v in code: word += morse[v]
    return word

assert morseTranslete(['.--.', '-.--', '-', '....', '---', '-.']) == 'python'

