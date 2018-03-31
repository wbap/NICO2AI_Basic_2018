<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lecture 7 at NICO2AI  School</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Yuichiro Tsuchiya</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
# 第7回：畳み込みニューラルネットワーク (2)

## 到達目標
* 一般物体認識を題材に、CNNのより詳細な性質に立ち入る
* 前処理をはじめとしたCNNの学習トリックを理解し、使用できる
* フィルタ及び特徴マップの可視化を通じて、学習済みのCNNがどのような性質を持つかを垣間見る
* CNNの進化を通じて、CNNと視覚情報処理との類似点・相違点を理解する

## キーワード
* 一般物体認識
* Data Augmentation
* DeConcolution/Unpooling
* GoogLeNet/VGGNet/ResNet

## 参考文献
### CS231n: CS231n: Convolutional Neural Networks for Visual Recognition
http://cs231n.stanford.edu/

### Visualizing and Understanding Convolutional Networks M.D. Zeiler, R. Fergus ECCV 2014
https://www.cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf
