<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lecture 9 at NICO2AI  School</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Shoya Matsumori</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
# 第9回：再帰的ニューラルネットワーク (1)

## 到達目標
* 系列データ予測の問題設定と応用先を理解する
* シンプルなRNNの順伝播・逆伝播アルゴリズムの原理を理解する
* Chainerを用いてRNNを実装できる
* 誤差逆伝播法よりBiologically-Plausibleなアルゴリズムとして、ESN及びLSMの原理を学ぶ
* Numpyを用いてESNのモデルを記述できる

## 参考文献
* 詳解ディープラーニング 巣籠 悠輔
* (Elman, 1990) Finding Structure in Time
http://machine-learning.martinsewell.com/ann/Elma90.pdf

* (Mikolov, 2010) Recurrent neural network based language model
http://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov\_interspeech2010\_IS100722.pdf

* The Unreasonable Effectiveness of Recurrent Neural Networks
http://karpathy.github.io/2015/05/21/rnn-effectiveness/

* Sample Echo State Network source codes
http://minds.jacobs-university.de/mantas/code
