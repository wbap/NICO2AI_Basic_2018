<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lecture 5 at NICO2AI  School</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Yoshihiro Nagano</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

# 第5回：勾配法と誤差逆伝播法

## 到達目標
* 基本的な勾配降下法のアルゴリズムを理解する
* ロジスティック回帰における勾配法を実装できる
* フィードフォワードニューラルネットワーク及び誤差逆伝播法の仕組みを理解する
* 指導を受けながら、誤差逆伝播法の実装を体験する

## キーワード
* 勾配降下法
* クロスエントロピー誤差
* フィードフォワードニューラルネットワーク
* 誤差逆伝播法
* 確率的勾配降下法 (SGD)
* ミニバッチ確率的勾配降下法 (MSGD)

## 参考文献
* 岡谷貴之『機械学習プロフェッショナルシリーズ 深層学習』(講談社、2015)
* C.M.ビショップ『パターン認識と機械学習 上』(丸善出版、2012)
* CS231n: Convolutional Neural Networks for Visual Recognition: Lecture 4
http://vision.stanford.edu/teaching/cs231n/2017/syllabus.html
