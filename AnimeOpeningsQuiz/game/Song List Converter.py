with open("data.txt", encoding="utf-8") as data:
    linelines = data.readlines()
    for i in linelines:
        linearr = i.split("\t")
        print("(\"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\", \"{} ({})\", \"{}\", \"{}\",\"{}\", {}, {}, {}, \"{}\", \"{}\")".format(linearr[0], linearr[1], linearr[2], linearr[3], linearr[4], linearr[5], linearr[6], linearr[7], linearr[8], linearr[9],linearr[10], linearr[11], 1, linearr[12], linearr[13], linearr[14].strip("\n")), end="")
        if i != linelines[-1]:
            print(",")
input()
