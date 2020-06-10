def read_file(filename):
    lines = []
    with open(filename , 'r',encoding='utf-8') as f:  #若出現 \ueff 為 byte order mark , encoding 就要為 utf8-sig
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    a_word_count = 0
    b_word_count = 0
    a_sticker_count = 0
    b_sticker_count = 0
    a_image_count = 0
    b_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                a_sticker_count += 1
            elif s[2] == '圖片':
                a_image_count += 1
            else:    
                for m in s[2:]:
                    a_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                b_sticker_count += 1
            elif s[2] == '圖片':
                b_image_count += 1
            else:
                for m in s[2:]:
                    b_word_count += len(m)
    print('a說了' , a_word_count , '貼圖數' , a_sticker_count , '圖片數' , a_image_count )
    print('b說了' , b_word_count , '貼圖數' , b_sticker_count , '圖片數' , a_image_count)            
    return new

def write_file(filename, lines):
    with open(filename, 'w') as g:
        for line in lines:
            g.write(line + '\n')
            print (line)
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('out.txt' ,lines)
    

main()