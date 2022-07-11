import pandas as pd

file_path = "/home/nacnano/Documents/github/mal-data-warehouse/data/anime.csv"
df = pd.read_csv(file_path, delimiter=",")
new_df = df[df["members"] < 200000]

end_path = "/home/nacnano/Documents/github/mal-data-warehouse/data/unheard_anime.csv"
new_df.to_csv(end_path, index=False)
