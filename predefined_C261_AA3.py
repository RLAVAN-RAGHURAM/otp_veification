#FIND THE NUMBER OF LINES IN FILE

def file_len(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
         #writ the for loop and using the enumarate() method count the lines of the file
            pass
    return i + 1

 #write the print() function and inside it call the file_len() function and inside this function specify the  file name.
print(file_len("test.txt"))
