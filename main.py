import pandas as pd

cross = input("What competitor part do you wish to cross?\n")

pd.set_option('display.max_columns', None)

database = pd.read_csv("datasource/CrossReferenceReport_07_26_2022.csv", sep = ',')
#database = pd.DataFrame("datasource/CrossReferenceReport_07_26_2022.csv", sep = ',')

print(database[database["competitor_part"]==cross])