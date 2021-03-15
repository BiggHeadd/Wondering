# Logistic Regression

## 1. 模型介绍

- 本质：假设数据服从这个分布，然后使用极大似然估计做参数的估计

### 1.1 logistic 分布

- 连续型的概率分布（其中， μ 表示**位置参数**， γ>0 为**形状参数**。）

![分布_密度函数](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\分布_密度函数.jpg)

- 图像特征👇

![对数几率函数](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\对数几率函数.png)

![logistic_图像特征](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\logistic_图像特征.jpg)

- 对数几率函数是一个常用的替代函数，替代单位阶跃函数

![对数几率函数](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\对数几率函数.png)

### 1.2 logistic 回归

- **几率（odds）**
  - y视为x为正例的概率，则1-y为x为其反例的概率，两者的比值称为**几率（odds）**
  - 指该事件发生与不发生的概率比值

![对数几率](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\对数几率.png)

![对数几率函数_化简](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\对数几率函数_化简.png)

- 事件发生的**概率**为 p，y是为类后验概率估计

![类后验概率估计](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\类后验概率估计.jpg)

- **逻辑回归的思路**是，先拟合决策边界(不局限于线性，还可以是多项式，wx+b)，再建立这个边界与分类的概率联系[P(Y=1|x)]，从而得到了二分类情况下的概率。

> 在这我们思考个问题，我们使用对数几率的意义在哪？
>
> s通过上述推导我们可以看到 Logistic 回归实际上是使用线性回归模型的预测值逼近分类任务真实标记的对数几率，其优点有：
> 直接对**分类的概率**建模，无需实现假设数据分布，从而避免了假设分布不准确带来的问题；
> 不仅可预测出类别，还能得到该**预测的概率**，这对一些利用概率辅助决策的任务很有用；
> 对数几率函数是**任意阶可导的凸函数**，有许多数值优化算法都可以求出最优解。



### 1.3 代价函数

- 似然函数

![似然函数](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\似然函数.png)

- 等式两边同取对数，写成对数似然函数

![对数似然函数](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\对数似然函数.jpg)

- 取整个数据集上的平均对数似然损失

![平均对数似然损失](C:\Users\bigheading\Documents\Algorithm\Wondering\machine_learning\logistic_regression\平均对数似然损失.png)

- **最大化似然函数**和**最小化损失函数**实际上是等价的