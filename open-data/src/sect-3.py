import os

import pandas as pd
import matplotlib.pyplot as plt


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

def _create_histgram(data: pd.DataFrame):
    print("drawing a histgram using 資本金")
    capital = data["資本金"]
    hist1 = (capital.value_counts(bins=range(0, 501,100), sort=False).reset_index())
    hist2 = (capital.value_counts(bins=range(0, 501,100), sort=False).reset_index().rename(
        columns={"index": "資本金階級", "count":"階級"}
    ))
    print(hist1)
    print(hist2)
    plt.hist(capital, bins=range(0, 501, 100))
    plt.show()

def _show_standard_statistics(data: pd.DataFrame):
    print(data.describe())


def main():
    print("start use sect-3")
    sample_data = _create_data_form_from_csv_file("open-data/src/resources/sect-3.csv")
    print(sample_data)
    _create_histgram(sample_data)
    _show_standard_statistics(sample_data)

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


# 会社名, ディメンション 
# 会社コード, ディメンション
# 上場区分, ディメンション
# 業種, ディメンション
# 従業員数, メジャー
# 資本金, メジャー

