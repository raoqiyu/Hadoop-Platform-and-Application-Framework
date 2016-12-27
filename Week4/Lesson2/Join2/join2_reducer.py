#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# What is the total number of viewers for shows on ABC?
#
# Hourly_Sports,DEF   # channel
# Hourly_Sports,21    # number
# --------------------------------------------------------------------------


abc_found = False
total_cnt = 0
prev_key = ""

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    key_in, value_in = key_value[:]

    if key_in != prev_key:
        if abc_found :
            print("%s %s"%(prev_key,total_cnt))
        total_cnt = 0
        prev_key = key_in

    if value_in == "ABC":
        abc_found = True
    else:
        total_cnt += int(value_in)
