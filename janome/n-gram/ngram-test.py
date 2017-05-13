def ngram(s, sum):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+sum]
