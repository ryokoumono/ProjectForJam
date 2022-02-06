import sys
import re


def read_text():
    regex = [r'(\$.+)' ,r'^\((\w+)\)', r'(\w+\:)(.+)\((\w+)\)', r'^`(\w+\:)(.+)\((\w+)\)', r'^`(\w+\:)(.+)', r'(\w+\:)(.+)', r'(Меню\:)', r'(\t)(.+)\((\w+)\)', r'^(?!\w+\:)(\w.+.*)\((\w+)\)', r'^(?!\w+\:)(\w.+.*)', r'\|(.+)']
    replace = [r'\1' ,r'label s\1:', r'\1 "\2"\n    jump s\3', r'#voice\n\1 "\2"\n    jump s\3', r'#voice\n\1 "\2"', r'\1 "\2"', r'menu:', r'    "\2":\n        jump s\3', r'"\1"\n    jump s\2', r'"\1"', r'#voice\ngg_"\1"']
    data = open("tmp.py", 'r', encoding='UTF-8 ')
    output = open("out.txt", 'w', encoding='UTF-8 ')
    while True:
        line = data.readline()
        if not line:
            break
        for reg in range(len(regex)):
            regexde = re.compile(regex[reg], re.MULTILINE)
            if re.search(regexde, line):
                text = re.sub(regex[reg], replace[reg], line)
                if not re.search(regex[1], line):
                    text = '    ' + text
                    write(output, text.replace('/', '{w}'), label=True)
                    break
                else:
                    write(output, text.replace('/', '{w}'), label=True)
                    break

def write(output, line, label=False):
    ''' Write parsed line into file'''
    match label:
        case True:
            print(line, file=output)
        case False:
            print(*line, file=output, end='\n', sep='\n')

if __name__ == "__main__":

    read_text()