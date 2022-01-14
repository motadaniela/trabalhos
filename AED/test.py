userdata = open("userdata.txt")
line=userdata.readline()
pos=line.index(";")
username = line[(line.index(";", pos+1)+1):(line.index("\n"))-1]

print(username)

input()