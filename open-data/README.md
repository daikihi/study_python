# このディレクトリは何？

このディレクトリでは、'Python ではじめるオープンデータ解析' の本を教本にして、色々やってみる。

## オリジナルデータ

[https://github.com/python-opendata-analysis/python-opendata-analysis-book/tree/main](https://github.com/python-opendata-analysis/python-opendata-analysis-book/tree/main)

この書籍を買ったので、これをサンプルに、先ずはフォローしながら色々できたらと思っている。

# sect-3

第三章、統計の基礎

オリジナルでは、Python 内のDataframe に直接ぶち込んでたけど、一旦CSV ファイルに入れて置くことにした。 :memo:

## 実行場所

`${PROJECT_ROOT}` で実行しても理屈上は良いが、色々腐っている可能性もあるし、 `open-data` 内で完結させることにする。

初回のみ

```bash
cd ${PROJECT_ROOT}/opendata
python3.13 -m venv venv
```

2回目から

```bash
cd ${PROJECT_ROOT}/opendata
source venv/bin/activate
```
