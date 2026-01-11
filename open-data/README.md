# このディレクトリは何？

このディレクトリでは、'Python ではじめるオープンデータ解析' の本を教本にして、色々やってみる。

## オリジナルデータ

[https://github.com/python-opendata-analysis/python-opendata-analysis-book/tree/main](https://github.com/python-opendata-analysis/python-opendata-analysis-book/tree/main)

この書籍を買ったので、これをサンプルに、先ずはフォローしながら色々できたらと思っている。

# 全体的な実行

先ずは、全体的な話としての実行のアレコレ

この`open-data` ディレクトリでは、`uv` パッケージマネージャを使う。

`uv` のインストール方法

[UV](https://docs.astral.sh/uv/)

初回のみ

```bash
cd ${PROJECT_ROOT}/opendata
uv venv --python 3.13
```

2回目から

```bash
cd ${PROJECT_ROOT}/opendata
source .venv/bin/activate
```

# package のインストール

```bash
uv pip install pandas
```

# sect-3

第三章、統計の基礎

オリジナルでは、Python 内のDataframe に直接ぶち込んでたけど、一旦CSV ファイルに入れて置くことにした。 :memo:

## 実行

`${PROJECT_ROOT}` で実行しても理屈上は良いが、色々腐っている可能性もあるし、 `open-data` 内で完結させることにする。

```bash
uv run src/sect-3.py
```

uv は起動が遅いので、pip あたりを使ってしたのコマンドで python を直で呼ぶほうが早い。

（初回だけかも？）

```bash
python3.13 -m src.sect-3 
```
