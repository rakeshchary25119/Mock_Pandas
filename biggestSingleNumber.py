import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers = my_numbers.drop_duplicates('num', keep=False)\
    .max().to_frame().rename(columns = {0: "num"})
    return my_numbers