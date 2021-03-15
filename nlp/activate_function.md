[TOC]

# Activate Function

> 如果使用线性激活函数（恒等激励函数），那么神经网络仅是将输入线性组合再输出，在这种情况下，深层（多个隐藏层）神经网络与只有一个隐藏层的神经网络没有任何区别，不如去掉多个隐藏层。
>
> 对于多个隐藏层的神经网络可以简化成单层的神经网络。因此，想要使神经网络的多个隐藏层有意义，需要使用非线性激活函数，也就是说想要神经网络学习到有意思的东西只能使用非线性激活函数。



## Sigmoid

$$
g(z)=\frac{1}{1+e^{-z}}
$$

$$
g'(z)=g(z)*(1-g(z))
$$

> - 不以零为中心：Sigmoid 输出不以零为中心的。
> - 计算成本高昂：exp() 函数与其他非线性激活函数相比，计算成本高昂。



## Tanh

$$
g(z)=\frac{e^z-e^{-z}}{e^z+e{-z}}
$$

$$
g'(z)=1-(g(z))^2
$$



> Tanh 函数的输出以零为中心，因为区间在-1 到 1 之间，**解决了Sigmoid函数的不是zero-centered输出问题。**
>
> 
>
> sigmoid和tanh激活函数有共同的缺点：
>
> - 即在z很大或很小时，梯度几乎为零，因此使用梯度下降优化算法更新网络很慢。



## Relu

$$
g(z)=max(0,z)
$$

$$
\begin{equation}
        g'(z)=
       \begin{cases}
       1&\mbox{if z > 0}\\
       undefined &\mbox{if z = 0} \\
       0 &\mbox{if z < 0}
       \end{cases}
      \end{equation}
$$

> 解决了sigmoid，tanh在z很大的时候，梯度几乎为0的问题
>
> 缺点：
>
> - 当z < 0的时候，导数为0
> - 不以零为中心：和 Sigmoid 激活函数类似，ReLU 函数的输出不以零为中心。



## Leaky Relu

$$
g(z)=max(0.01z,z)
$$

$$
\begin{equation}
        g'(z)=
       \begin{cases}
       1&\mbox{if z > 0}\\
       undefined &\mbox{if z = 0} \\
       0.01 &\mbox{if z < 0}
       \end{cases}
      \end{equation}
$$

> 优点：
>
> - 该函数一定程度上缓解了 dead ReLU 问题。
>
> 缺点：
>
> - 使用该函数的结果并不连贯。尽管它具备 ReLU 激活函数的所有特征，如计算高效、快速收敛、在正区域内不会饱和。



## P-Relu（**Parametric** Relu）

$$
g(z)=max(zα,z)
$$

$$
\begin{equation}
        g'(z)=
       \begin{cases}
       1&\mbox{if z > 0}\\
       undefined &\mbox{if z = 0} \\
       α &\mbox{if z < 0}
       \end{cases}
      \end{equation}
$$

>其中α是超参数。这里引入了一个随机的超参数α ，它可以被学习，因为你可以对它进行反向传播。这使神经元能够选择负区域最好的梯度，有了这种能力，它们可以变成 ReLU 或 Leaky ReLU。



## Elu

- ELU也是为解决ReLU存在的问题而提出。

$$
\begin{equation}
        g(z)=
       \begin{cases}
       z&\mbox{if z > 0}\\
       α(e^z-1) &\mbox{otherwise}
       \end{cases}
      \end{equation}
$$

> 优点：ReLU的基本所有优点、不会有Dead ReLU问题，输出的均值接近0、零中心点问题。
>
> 
>
> 缺点：计算量稍大，原点不可导。



## Gelu

$$
\sigma(z)=\frac{z}{1+e^{-1.702z}}
$$

>bert中使用的激活函数，作者经过实验证明比relu等要好。
>
>原点可导，不会有Dead ReLU问题。
>
>**值得注意的是最近席卷NLP领域的BERT等预训练模型几乎都是用的这个激活函数。**



## Swish激活函数

- 自门控激活函数

$$
\sigma(z)=\frac{x}{1+e^{-x\beta}}
$$

> Swish跟ReLu差不多，唯一区别较大的是接近于0的负半轴区域，因此Swish 激活函数的输出可能下降，即使在输入值增大的情况下。
>
> 大多数激活函数是单调的，即输入值增大的情况下，输出值不可能下降。而 Swish 函数为 0 时具备单侧有界（one-sided boundedness）的特性，它是平滑、非单调的。
>
> 
>
> 缺点：
>
> - 只有实验证明，没有理论支持。 
> - 在浅层网络上，性能与relu差别不大。



## Selu激活函数

- 其实就是ELU乘了个lambda，关键在于这个lambda是大于1的

$$
\begin{equation}
        selu(z)=\lambda
       \begin{cases}
       z&\mbox{if z > 0}\\
       \alpha e^x-\alpha &\mbox{if z <= 0}
       \end{cases}
      \end{equation} (\lambda>1)
$$

> - 以前relu，prelu，elu这些激活函数，都是在负半轴坡度平缓，这样在activation的方差过大的时候可以让它减小，防止了梯度爆炸，但是正半轴坡度简单的设成了1。
>
> - 而selu的正半轴大于1，在方差过小的的时候可以让它增大，同时防止了梯度消失。这样激活函数就有一个不动点，网络深了以后每一层的输出都是均值为0方差为1。
>
> - 当其中参数取为λ≈1.057，α2≈1.6733时，在网络权重服从标准正态分布的条件下，各层输出的分布会向标准正态分布靠拢。这种「自我标准化」的特性可以避免梯度消失和爆炸的问题，让结构简单的前馈神经网络获得甚至超越 state-of-the-art 的性能。
>
> - selu的证明部分前提是权重服从正态分布，但是这个假设在实际中并不能一定成立，众多实验发现效果并不比relu好。

