def count_substring(string, sub_string):
    n=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            n += 1
        # print(string[i:i+len(sub_string)])
    return n

print(count_substring('ABCDCDC','CDC'))