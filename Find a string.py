def count_substring(string, sub_string):
    count = 0
    len_s = len(string)
    len_sb = len(sub_string)
    for i in range(0, len_s - len_sb +1):
        if(string[i:len_sb+i] == sub_string):
            count += 1
    return count

