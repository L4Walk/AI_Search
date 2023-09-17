# JAX

GoogleJAX是一个用于变换数值函数的机器学习框架，Google称其为为结合了修改版本的Autograd（通过函数微分自动获得梯度函数）和<a href="https://ai-bot.cn/sites/48.html">TensorFlow</a>的XLA（加速线性代数）。该框架的设计尽可能遵循<a href="https://ai-bot.cn/sites/780.html">NumPy</a>的结构和工作流程，并与TensorFlow和<a href="https://ai-bot.cn/sites/61.html">PyTorch</a>等各种现有框架协同工作。

JAX的主要功能是包括：
<ul>
 	<li>grad：自动微分</li>
 	<li>jit：编译</li>
 	<li>vmap：自动矢量化</li>
 	<li>pmap：SPMD编程</li>
</ul>