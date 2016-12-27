#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# What is the total number of viewers for shows on ABC?
#
# Hourly_Sports,DEF   # channel
# Hourly_Sports,21    # number
# --------------------------------------------------------------------------



for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if value_in.isdigit():           #if this entry has <TV show, count> in value
        print( '%s\t%s' % (key_in, value_in) )  #print a string, tab, and string
    else:   # <TV show title, channel> 
        if value_in == "ABC":
            print( '%s\t%s' % (key_in, value_in) )  #print a string tab and string

