[TOC]

# LSTM

![快速理解LSTM，从懵逼到装逼](https://pic2.zhimg.com/v2-9b62746ff2c7443b6b3157cee26a1d00_1440w.jpg?source=172ae18b)

- 输入： ![[公式]](https://www.zhihu.com/equation?tex=h_%7Bt-1%7D) （t-1时刻的隐藏层）和 ![[公式]](https://www.zhihu.com/equation?tex=x_t) （t时刻的特征向量）
- 输出： ![[公式]](https://www.zhihu.com/equation?tex=h_t) （加softmax即可作为真正输出，否则作为隐藏层）
- 主线/记忆： ![[公式]](https://www.zhihu.com/equation?tex=c_%7Bt-1%7D) 和 ![[公式]](https://www.zhihu.com/equation?tex=c_t)



## 公式

- 遗忘门

$$
f_t=\sigma(U_fh_{t-1}+W_fx_t)
$$

$$
k_t=c_{t-1}\odot f_t
$$

- 输入门

$$
i_t=\sigma(U_ih_{t-1}+W_ix_t)
$$

$$
g_t=tanh(U_gh_{t-1}+W_gx_t)
$$

$$
j_t=g_t\odot i_t
$$

$$
c_t=j_t+k_t
$$



- 输出门

$$
o_t=\sigma(U_oh_{t-1}+W_ox_t)
$$

$$
h_k=tanh(c_t\odot o_t)
$$



## LSTM vs RNN

![img](https://pic4.zhimg.com/80/v2-47137ca8f0ffc3a3778c5223881b75f7_720w.jpg)