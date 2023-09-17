# LangChain

<a href="https://ai-bot.cn/what-is-large-language-model/">大语言模型（LLM）</a>正在成为一种变革性技术，使开发人员能够构建以前无法构建的应用程序。但是，单独使用这些LLM通常不足以创建一个真正强大的应用程序——当你可以将它们与其他计算或知识来源相结合时，便可能实现其真正的能力。

LangChain是一个用于开发由语言模型驱动的应用程序的框架，允许开发人员将语言模型连接到其他数据源并与其环境相交互。LangChain旨在帮助开发者在以下六个主要领域，按照复杂性递增的顺序：
<ul>
 	<li>📃 LLMs and Prompts: 这包括提示管理、提示优化、适用于所有 LLM 的通用界面以及用于处理 LLM 的通用实用程序。</li>
 	<li>🔗 Chains: 链不仅仅是单个 LLM 调用，而是调用序列（无论是对 LLM 还是对不同的实用程序）。 LangChain 为链提供标准接口、与其他工具的大量集成以及用于常见应用程序的端到端链。</li>
 	<li>📚 Data Augmented Generation: 数据增强生成涉及特定类型的链，这些链首先与外部数据源交互以获取数据以用于生成步骤。 这方面的例子包括对长文本的总结和对特定数据源的问答。</li>
 	<li>🤖 Agents: 代理涉及 LLM 做出关于采取哪些行动的决定，采取该行动，看到一个观察，并重复直到完成。LangChain 为代理提供了一个标准接口，可供选择的代理选择，以及端到端代理的示例。</li>
 	<li>🧠 Memory: 内存是链/代理调用之间持久状态的概念。 LangChain 提供了内存的标准接口、内存实现的集合以及使用内存的链/代理的示例。</li>
 	<li>🧐 Evaluation: [BETA] 众所周知，生成模型很难用传统指标进行评估。 评估它们的一种新方法是使用语言模型本身进行评估，LangChain 提供了一些提示/链来协助这一点。</li>
</ul>