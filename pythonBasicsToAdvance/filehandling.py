f = open("demoFile1.txt" ,"a" )
f.write("this is new file content ")
f.close()

# print(f.read())
# print(f.read(6))
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x)

r = open("demoFile.txt")
print(r.read())
r.close()
