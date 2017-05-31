def countWord(filepath, word):
	count = 0
	with open(path) as f:
		line = f.readline()
		while(line!=""):
			word_list = line.split()
			for i in word_list:
				if(i.lower() == word.lower()):
					count += 1
			line = f.readline()
		return count
