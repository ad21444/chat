def read_file(filename):
    lines = []
    with open(filename , 'r',encoding='utf-8') as f:  #若出現 \ueff 為 byte order mark , encoding 就要為 utf8-sig
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    
    return new

def write_file(filename, lines):
    with open(filename, 'w') as g:
        for line in lines:
            g.write(line + '\n')
            print (line)
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('out.txt' ,lines)
    

main()