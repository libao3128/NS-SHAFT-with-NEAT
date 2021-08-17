# NS-SHAFT-with-NEAT
Team member:黃立鈞、簡言哲、卓灝辰、廖振亦

利用NEAT(NeuroEvolution of Augmenting Topologies)演算法讓AI操控經典電腦遊戲「小朋友下樓梯」。
遊戲中，玩家可以操控左右方向鍵讓小朋友向左或向右移動，隨著平台不斷上升，目標是讓小朋友能夠往下最多的樓層數。
小朋友一共有10點生命值，在接觸到天花板的尖刺或是尖刺平台後都會受到4點傷害，當小朋友被天花板的尖刺傷害時會強迫離開所在的平台往下跳，而當生命值歸零或是小朋友掉落谷底時遊戲結束。
平台的種類分為:
1. 普通平台:
沒有任何效果，每當小朋友站上此平台可以回復一點生命值。
![](https://i.imgur.com/GrQFB9N.png)
2. 假平台:
假平台會在小朋友踩過後翻轉，並在翻轉期間不能作為平台使用，每當小朋友站上此平台可以回復一點生命值。
![](https://i.imgur.com/MIvhxAe.png)
3. 彈簧平台:
彈簧平台會在小朋友踩過後將其往上彈一段距離，可以重複並且同時使用，小朋友不能藉此平台回復生命。
![](https://i.imgur.com/HlHWpE9.png)

4. 履帶平台(向左或向右)
小朋友在踩上履帶平台後會因為履帶平台往右或往左轉動而向左或向右平移，但可以透過自身位移抵銷，每當小朋友站上此平台可以回復一點生命值。
![](https://i.imgur.com/m9nisUu.png) 
向右履帶
![](https://i.imgur.com/0HWEyut.png)
向左履帶
5. 尖刺平台
在小朋友踏上平台後給予他4點傷害。
![](https://i.imgur.com/prNjzT5.png)

# GitHub code we refer to 
1. [NEAT-Python](https://github.com/CodeReclaimers/neat-python/blob/master/docs/index.rst)
這次project中，我們使用NEAT-Python套件作為我們神經網路的建構模組，透過修改模組中的config檔，我們可以輕易地修改整個網路的許多有關Reproduction、Genome、Stagnation的參數，相關的code為config-feedforward檔。
2. [visualize.py](https://github.com/CodeReclaimers/neat-python/blob/master/examples/xor/visualize.py?fbclid=IwAR2UfJ_GkPcvN0Hen4RpTXbQbcZD_YSSh7mSYZ66Z1cAsatyfJbUycOnkLg)
visualize是NEAT_Python中包含將模型視覺化的檔案，需要另外安裝[Graphviz](https://graphviz.org/)套件才能使用，方便我們了解現在模型的node、connection、weight等相關資訊。

在使用前請先安裝上述兩個library，請參閱report.pdf來了解我們的研究結果。
