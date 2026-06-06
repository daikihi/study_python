# PyTorch は、数値計算や機械学習・深層学習でよく使われるライブラリです。
# import torch と書くことで、このファイル内で torch.tensor() などの機能を使えるようになります。
import torch


def main():
    # 現在インストールされている PyTorch のバージョンを表示します。
    print("PyTorch version:", torch.__version__)

    # torch.tensor() を使って、PyTorch の Tensor を作成します。
    #
    # Tensor とは、数値をまとめて扱うためのデータ構造です。
    # Python の list に少し似ていますが、
    # PyTorch の Tensor は高速な数値計算や機械学習に向いています。
    #
    # 数学的には「ベクトル」のようなものです。
    x = torch.tensor([1, 2, 3])

    # こちらも同じく Tensor を作成しています。
    # y は [10, 11, 12] という値を持つ 1 次元 Tensor です。
    #
    # x と y はどちらも要素数が 3 つなので、
    # 後で x + y のように要素ごとの計算ができます。
    y = torch.tensor([10, 11, 12])

    print(x)
    print(y)

    print("x + y =")

    # x + y を計算して表示します。
    # Tensor 同士の足し算では、同じ位置にある要素同士が足されます。
    # なので、
    # x + y = [1+10, 2+11, 3+12]
    #       = [11,   13,   15]
    #
    # 出力例:
    # tensor([11, 13, 15])
    print(x + y)

    # @ は Python では「行列積」や「内積」を表す演算子として使われます。
    print("x @ y = ")

    # 今回の x と y はどちらも 1 次元 Tensor です。
    # 1 次元 Tensor 同士に @ を使うと、「内積」が計算されます。
    #
    # 内積とは、対応する要素同士を掛け算して、その結果を全部足す計算です。
    #
    # x = [1, 2, 3]
    # y = [10, 11, 12]
    #
    # x @ y = 1*10 + 2*11 + 3*12
    #       = 10 + 22 + 36
    #       = 68
    #
    # 出力例:
    # tensor(68)
    #
    # 注意:
    # x @ y は「内積」なので結果は 1 つの数値になります。
    print(x @ y)


if __name__ == "__main__":
    main()
