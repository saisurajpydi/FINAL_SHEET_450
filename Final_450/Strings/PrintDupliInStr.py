"""
Print all the duplicates in the input string
"""
no_of_char = 256 #no of unicode char
def counts(string , count):
    for i in string:
        count[ord(i)] += 1
    return count


def dup(string):
    count = [0] * no_of_char
    count = counts(string,count)

    k = 0

    for i in count:
        if int(i) > 1:
            print(chr(k) + " count is :" + str(i))
        k += 1
s = input(" enter the string : ")
dup(s)



