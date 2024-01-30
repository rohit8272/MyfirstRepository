import pickle

# numbers= [1,2,3,4,5,6,7,8,9]

# fileName = "pickle.pkl"
# fileObj= open(fileName,'wb')

# pickle.dump(numbers, fileObj)
# fileObj.close()

file = "pickle.pkl"

fileObj = open(file , 'rb')
filecontent = pickle.load(fileObj)
print(filecontent)