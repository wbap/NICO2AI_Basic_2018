<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lecture 10 at NICO2AI  School</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Shoya Matsumori</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
# 第10回：再帰的ニューラルネットワーク (2)

## 到達目標
* 勾配爆発・消失問題を理解する
* LSTMの目的と働きを数式を追いながら理解する
* Chainerを用いてLSTMを用いたモデルを記述できる
* RNN特有の学習テクニックを理解し、正しく使用できる
* RNNの用途とより高度の使い方を知る

## キーワード
* Long Short-Term Memory (LSTM)
* 長期依存/短期依存
* 勾配爆発 (消失) 問題
* Gradient Clipping
* Neural Turing Machine (NTM)
* Differential Neural Computers (DNC)

## 参考文献
* わかるLSTM ～ 最近の動向と共に
http://qiita.com/t\_Signull/items/21b82be280b46f467d1b

* Deep Learning Lecture 12: Recurrent Neural Nets and LSTMs
https://www.youtube.com/watch?v=56TYLaQN4N8

* Deep Learning Lecture 13: Alex Graves on Hallucination with RNNs
https://www.youtube.com/watch?v=-yX1SYeDHbg

* (Karpathy, 2016) Visualizing and Understanding Recurrent Networks
https://pdfs.semanticscholar.org/8390/c96f0b2ff3b36b232f7f9918401e51632f4e.pdf

* (Bengio, 1994) Learning long-term dependencies with gradient descent is difficult
http://www.dsi.unifi.it/~paolo/ps/tnn-94-gradient.pdf

* (Hochreiter, 1997) Long Short-Term Memory
http://www.bioinf.jku.at/publications/older/2604.pdf

* (Pascanu, 2012) On the difficulty of training recurrent neural networks
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.421.8930&rep=rep1&type=pdf

* (Bishop, 1994) Mixture Density Networks
https://publications.aston.ac.uk/373/1/NCRG\_94\_004.pdf

* (Graves, 2013) Generating Sequences With Recurrent Neural Networks
https://arxiv.org/abs/1308.0850

* IAM On-Line Handwriting Database (IAM-OnDB)
http://www.fki.inf.unibe.ch/databases/iam-on-line-handwriting-database

* Handwriting Generation Demo in TensorFlow (Blog)
http://blog.otoro.net/2015/12/12/handwriting-generation-demo-in-tensorflow/

* Generative Handwriting Demo using TensorFlow (GitHub)
https://github.com/hardmaru/write-rnn-tensorflow

* LSTMVis: Visual Analysis for Recurrent Neural Networks
http://lstm.seas.harvard.edu/
