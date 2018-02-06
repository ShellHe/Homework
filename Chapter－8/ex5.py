def analyze(str):
    s_without_punct = ""
    for letter in str:
        if letter not in string.punctuation:
            s_without_punct.split()
    mylist=s_without_punct.split()
    count = 0
    for i in mylist:
        if i.find("e")>=0
            count+=1
    numwords = len(mylist)
    percentage = count / numwords *100

    return 'your text contains (0) words, of which (1) ({2:.2f}%) contain an "e".'.format(numwords,count,percentage)

speech=""""""