# Vercel AI SDK

Vercel AI SDK是前端网站开发和托管平台及Next.js开发团队「Vercel」推出的，用于快速构建AI聊天机器人网站应用程序的开发套件，可以帮助开发人员使用JavaScript和TypeScript构建对话式的AI用户界面。
<h2>Vercel AI SDK的特性</h2>
<ol>
 	<li>支持React/Next.js、Svelte/SvelteKit和Vue/Nuxt等前端框架，以及Node.js、Serverless和Edge Runtime</li>
 	<li>内置各种AI模型的适配器，支持LangChain、OpenAI、Anthropic和Hugging Face等提供的大语言模型</li>
 	<li>提供交互式在线提示playground（<a class="external" href="https://sdk.vercel.ai/" target="_blank" rel="noopener">sdk.vercel.ai</a>），其中包含20个开源和云LLM。可以实时展示不同对话模型的聊天界面，并且可以快速生成代码。</li>
 	<li>提供多个AI聊天机器人的模板和示例，你可以克隆/复制Vercel提供的基于不同框架和模型开发的AI聊天机器人的初始模板</li>
</ol>
<h2>如何使用Vercel AI SDK</h2>
<ol>
 	<li>前提条件需要在电脑上安装Node.js 18+版本，如果要开发基于OpenAI的GPT聊天机器人，需要获得OpenAI API密钥</li>
 	<li>使用Next.js（<code>pnpm dlx create-next-app my-ai-app</code>）或者Svelte（<code>pnpm create svelte@latest my-ai-app</code>）等框架创建一个全新的项目，并定位到创建好的目录（<code>cd my-ai-app</code>）</li>
 	<li>安装依赖项，<code>pnpm install ai openai-edge</code></li>
 	<li>配置 OpenAI API 密钥，<code>.env.local</code>在项目根目录中创建一个文件并添加您的 OpenAI API 密钥</li>
 	<li>创建API路由并连接UI，完成后使用<code>pnpm run dev</code>运行启动应用程序</li>
</ol>