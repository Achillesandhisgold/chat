def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	news = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			news.append(person + ':' + line)
	return news

def write_file(filename, news):
	with open(filename, 'w') as f:
		for line in news:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	news = convert(lines)
	write_file('output.txt', news)
main()