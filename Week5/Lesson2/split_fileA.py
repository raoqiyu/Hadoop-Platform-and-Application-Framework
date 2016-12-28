def split_fileA(line):
    # split the input line in word and count on the comma
    word, count = line.split(",")
    # turn the count to an integer  
    count = int(count)
    return (word, count)