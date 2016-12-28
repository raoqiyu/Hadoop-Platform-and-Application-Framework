def split_show_channel(line):
    show, channel = line.split(",")
    return (show, channel)


# function 
# show_channel = show_channel_file.map(split_show_channel)
# joined_dataset = show_channel.join(show_views)