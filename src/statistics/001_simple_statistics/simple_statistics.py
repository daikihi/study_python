# ========================================
# 簡単な統計演習モジュール
# ========================================
# このモジュールは、基本的な数値操作と
# ランダムリストの生成・処理を学ぶための
# シンプルなプログラムです。

try:
    # 通常のインポート経路：パッケージルートから相対インポート
    from src.statistics.common import random_list_generator
except ModuleNotFoundError:
    # 直接実行時用の処理：
    # このファイルを直接実行する場合、プロジェクトルートが
    # sys.pathに含まれていないため、手動で追加する必要があります。
    # これにより、srcパッケージが正しくインポートできます。
    import sys
    from pathlib import Path

    # プロジェクトルートは、このファイルから見て
    # 3階層上の親ディレクトリ（srcの親）です
    project_root = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(project_root))
    from src.statistics.common import random_list_generator


def _sum(x: int, y: int) -> int:
    """
    2つの整数を加算して返す関数。

    Args:
        x (int): 最初の整数
        y (int): 2番目の整数

    Returns:
        int: xとyの合計
    """
    return x + y


def _list_sum() -> None:
    """
    ランダムなリストを生成して、その合計を出力する関数。

    処理内容：
    1. ランダムリスト生成関数を使用して、10個の要素を持つリストを生成
    2. リストの要素は0〜100のランダムな整数
    3. 生成されたリストの全要素の合計を計算し、出力

    Returns:
        None
    """
    # 10個の要素を持つランダムなリスト（0-100の整数）を生成
    random_list = random_list_generator.generate_random_list(10, 100)
    # リストの合計をprint出力
    print(sum(random_list))
    return None


def main():
    """
    メイン処理関数。

    実行内容：
    1. _sum関数を使用して1 + 2を計算し、結果を表示
    2. _list_sum関数を実行して、ランダムリストの合計を表示
    """
    # 2つの整数の合計を計算
    result = _sum(1, 2)
    print("simple sum : $", result)
    # ランダムリストの合計を計算・表示
    _list_sum()


if __name__ == "__main__":
    # スクリプトが直接実行された場合のみ、main関数を実行
    main()
