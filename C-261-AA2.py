fname=input("Enter the file name : ")
num_words=0
with open(fname,'r') as f:
	for line in f:
		word=line.split()
		num_words+=len(word)
print("Number of words : ",num_words)
