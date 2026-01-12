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


# データの種類区分
#  データを　名義尺度、順序尺度、間隔尺度、非尺度に分類する
# 今回のデータでは、　`会社名, 会社コード, 上場区分, 業種, 従業員数, 資本金` がINDEX になっている
#  会社名は名義尺度
#  会社コードは順序尺度 <---- 名義尺度：会社コードにジュウン所の意味合いがほぼ無いので、ここでは順序尺度ではなくて名義尺度が妥当
#  上場区分は、名義尺度
#  業種は名義尺度
#  従業員数は非尺度
#  資本金は非尺度
# となる
