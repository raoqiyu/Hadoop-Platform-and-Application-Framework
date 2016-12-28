def split_fileB(line):
    # split the input line into word, date and count_string
    date_word, count_string = line.split(",")
    date, word = date_word.split(" ")
    return (word, date + " " + count_string) 