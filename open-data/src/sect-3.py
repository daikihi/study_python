import os

import pandas as pd


def _create_data_form_from_csv_file(file_name: str) -> pd.DataFrame:
    print(f"load data and convert to DataFrame")
    current_directory = os.getcwd()
    print(f"current_directory = {current_directory}")
    if not os.path.isfile(file_name):
        print(f"invalid file path: {file_name}")
        return None
    return pd.read_csv(
        file_name,
        encoding='utf-8',
        sep=",",
        header=0
    )

def main():
    print("start use sect-3")
    sample_data = _create_data_form_from_csv_file("open-data/src/resources/sect-3.csv")
    print(sample_data)

if __name__ == "__main__":
    main()