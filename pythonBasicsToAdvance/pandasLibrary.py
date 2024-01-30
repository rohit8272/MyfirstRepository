import pandas as pd

# dataset = {
#     "cars" : ["bmw", "i10" , "kwid" , "fortuner"],
#     "company" : ["bmw" , "hundai" , "maruti" , "toyto"]
# }

dataset1 = {
    "day1" : 100,
    "day2" : 200,
    "day3" : 300,
    "day4" : 400   
}

# data = pd.DataFrame(dataset)
data = pd.Series(dataset1 , )
print(data)