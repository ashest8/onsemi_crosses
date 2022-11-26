import pandas as pd

database = pd.read_csv("datasource/CrossReferenceReport_07_26_2022.csv", sep = ',')
print(database[database["competitor_part"]=="LM5070SD-80"])