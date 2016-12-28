def split_show_views(line):
    show, views = line.split(",")
    return (show, views)

# function 
# show_views = show_channel_file.map(split_show_channel)