import pandas as pd
import data_io as io
import config


if __name__ == '__main__':
    # load data into dataframe
    db_df = io.load_data(config.fpath + config.infile)

    # declare variable for while-loop control
    more = 'y'

    print(db_df)

    while more == 'y':
        cross = input("What competitor part do you wish to cross?\n")
        # example: MLX83202
        part_df = io.find_part(cross, db_df)
        print(part_df)
        more = input('Cross another part? (y/n)\n')

    # pd.set_option('display.max_columns', None)

    # database = pd.read_csv("datasource/CrossReferenceReport_07_26_2022.csv", sep=',')
    # database = pd.DataFrame("datasource/CrossReferenceReport_07_26_2022.csv", sep = ',')

    # print(database[database["competitor_part"] == cross])
