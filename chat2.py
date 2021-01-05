# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 轉換對話紀錄
def convert(lines):
    Allen_word_count = 0
    Allen_stick_count = 0
    Allen_image_count = 0
    Viki_word_count = 0
    Viki_stick_count = 0
    Viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_stick_count += 1
            elif s[2] == '圖片':
                Allen_image_count += 1
            else:
                for m in s[2:]:
                    Allen_word_count += len(m)

        if name == 'Viki':
            if s[2] == '貼圖':
                Viki_stick_count += 1
            elif s[2] == '圖片':
                Viki_image_count += 1
            else:
                for m in s[2:]:
                    Viki_word_count += len(m)

    print('Allen說左', Allen_word_count, '個字')
    print('Allen傳左', Allen_stick_count, '個貼圖')
    print('Allen傳左', Allen_image_count, '張圖片') 

    print('Viki說左', Viki_word_count, '個字')
    print('Viki傳左', Viki_stick_count, '個貼圖')
    print('Viki傳左', Viki_image_count, '張圖片') 


# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()