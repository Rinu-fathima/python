def read_file_to_list(filename):
	with open(filename, 'r') as file:
		lines = [line.strip() for line in file]
	return lines

filename = 'example.txt'
lines_list = read_file_to_list(filename)

print(lines_list)
