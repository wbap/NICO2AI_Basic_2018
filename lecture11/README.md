<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lecture 11 at NICO2AI  School</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Takuma Seno</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
# 第11回：強化学習 (1)

## 到達目標
* 強化学習の問題設定と、教師あり学習との違いについて説明できる
* 強化学習問題の用語を覚える
* 価値反復に基づく学習アルゴリズムを理解し、実装できる
* OpenAI Gymの基本的な使い方を覚える
* Q-learningを用いて簡単な強化学習問題 (Cartpole) が解ける

## 参考文献
* 牧野他『これからの強化学習』(森北出版、2016)

* Lecture 9: Exploration and Exploitation
http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching\_files/XX.pdf

* (Rescorla, 1972) A Theory of Pavovian Conditioning: Variations in the Effectivenes of Reinforcement and Nonreinforcement
https://sites.ualberta.ca/~egray/teaching/Rescorla%20&%20Wagner%201972.pdf

* (Schultz, 1997) A Neural Substrate of Prediction and Reward
http://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.pdf

* (Samejima, 2005) Representation of action-specific reward values in the striatum
https://www.ncbi.nlm.nih.gov/pubmed/16311337

* (Doya, 2007) Reinforcement learning: Computational theory and biological mechanisms
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2645553/pdf/HJFOA5-000001-000030\_1.pdf

* Can you beat the bandit?
http://iosband.github.io/2015/07/28/Beat-the-bandit.html

* The Neuroscience of Reinforcement Learning (ICML2009 Tutorial)
http://www.princeton.edu/~yael/ICMLTutorial.pdf

* Cart-Pole Balancing with Q-Learning
https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947
