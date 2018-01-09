<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lecture 1 at NICO2AI  School</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Takuma Yagi</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

# 第1回：Python入門

## 到達目標
* Pythonのデータ型と各データ型の取り扱い方を覚える。
* Pythonで頻出する概念を覚える。
* Numpyを用いてベクトル・行列の計算及び操作を記述し、実行できる。
* csvファイルを題材として、実データの読み書きができる。

## キーワード
* データ型 (int, float, double)
* 文字列 (string)
* map, reduce, filter
* numpy
* osモジュール

## タイムスケジュール

### 講義 (65分)
1. ガイダンス (水谷) 10分
2. コネクトーム講義 (水谷) 15分
3. 汎用人工知能講義 20分
4. Python3入門 20分
    * 講義スケジュールの説明
    * 講義の狙い
    * PythonとNumpy
    * 機械学習の取り巻く状況

### 基礎演習 (25分+60分)
#### Part 1: Python3入門 (45分)
注：必要に応じて飛ばす
* (print文、データ型)
* (制御文 (if, for) と比較演算子)
* 関数
* (クラス)
* range文
* リスト、タプル、辞書
* 小課題1: フィボナッチ数列の計算 10分

#### Part 2: Numpy入門 (1) (25分)
* numpyのインポート
* 配列の生成(np.ones, np.zeros, np.arange)
* リスト内包表記
* 配列へのアクセス (advanced indexing除く)
* ブロードキャスティング
* 小課題2: 配列の計算とブロードキャスティング

#### Part 3: ファイルの入出力(15分)
* csvファイルのフォーマットと読み込み戦略
* osモジュール
* ファイルの読み込み
* csvの読み込み
* ファイルへの書き込み

### 実践演習(30分)
#### 課題1: 脳領域間コネクティビティデータの読み書き
* データ解説 5分
* コネクティビティデータの読み込み 20分
* 正解解説 5分

## 参考文献
### Pythonチュートリアル (公式)
https://docs.python.jp/3/tutorial/

### 100 numpy exercises (推奨)
http://www.labri.fr/perso/nrougier/teaching/numpy.100/

### Dive Into Python 3 日本語版 (経験者向け)
http://diveintopython3-ja.rdy.jp/index.html

### PEP 8 -- Style Guide for Python Code
https://www.python.org/dev/peps/pep-0008/
