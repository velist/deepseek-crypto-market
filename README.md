<p align="center">
  <img src="https://img.shields.io/badge/AI_Agent-Skill-4f46e5?style=for-the-badge" alt="AI Agent Skill">
  <img src="https://img.shields.io/badge/CoinGecko-Free_API-8dc647?style=for-the-badge" alt="CoinGecko Free API">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

<h1 align="center">🪙 crypto-market</h1>
<p align="center"><strong>通用 AI Agent Skill — 实时加密货币行情查询</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/compatible-Claude_Code-7b5ea7?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/compatible-DeepSeek_TUI-4f46e5?style=flat-square" alt="DeepSeek TUI">
  <img src="https://img.shields.io/badge/compatible-Codex-10a37f?style=flat-square" alt="Codex">
  <img src="https://img.shields.io/badge/compatible-OpenClaw-ff6b35?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/compatible-Cursor-00b4d8?style=flat-square" alt="Cursor">
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/velist/deepseek-crypto-market?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/velist/deepseek-crypto-market?style=flat-square" alt="Stars">
</p>

---

## 这是什么？

一个 **通用 AI Agent Skill**，兼容 Claude Code / DeepSeek TUI / Codex / OpenClaw / Cursor / Windsurf 等主流 AI 编程助手。

当你在任意兼容 Agent 中说"看下币价"或"虚拟币行情"，Agent 会自动调用 CoinGecko 免费 API，拉取 10 种主流币种的实时价格、市值、24h 涨跌幅，并格式化输出。

**零配置、零密钥、即装即用。**

## 兼容的 Agent

| Agent | 安装命令 |
|-------|---------|
| **Claude Code** | `git clone ... ~/.claude/skills/crypto-market` |
| **DeepSeek TUI** | `/skill install velist/deepseek-crypto-market` |
| **Codex** | `git clone ... .codex/skills/crypto-market` |
| **OpenClaw** | `git clone ... .openclaw/skills/crypto-market` |
| **Cursor** | `git clone ... .cursor/skills/crypto-market` |
| **Windsurf** | `git clone ... .windsurf/skills/crypto-market` |

## 快速安装

```bash
# 通用安装（替换为你的 agent 对应目录）
git clone https://github.com/velist/deepseek-crypto-market.git <skills-dir>/crypto-market

# 示例：Claude Code
git clone https://github.com/velist/deepseek-crypto-market.git ~/.claude/skills/crypto-market

# 示例：DeepSeek TUI（内置 skill-installer）
/skill install velist/deepseek-crypto-market
```

## 使用方式

安装后，在任何兼容 Agent 中直接说：

```
看下虚拟币行情
BTC 现在多少钱
最近 crypto 市场怎么样
ETH SOL ADA 价格走势
What's Bitcoin price today?
Show me the crypto market
```

Agent 会自动加载 skill → 运行脚本 → 返回格式化行情。

### 效果

```
**BTC**  — $76,958（¥522,105）  📈 +0.34%  市值 $1.54T  24h量 $21.7B
**ETH**  — $2,094（¥14,208）    📉 -1.07%  市值 $253B   24h量 $9.5B
**SOL**  — $84.84（¥575.61）    📉 -0.97%  市值 $49B    24h量 $2.4B
**XRP**  — $1.35（¥9.13）       📉 -1.01%  市值 $83B    24h量 $1.1B
**BNB**  — $656.31（¥4,453）    ➖ -0.02%  市值 $88B    24h量 $608M
...
```

### 进阶：命令行直接使用

```bash
# 查 BTC + ETH，只要 USD
python scripts/crypto_fetch.py --coins btc,eth --vs usd

# 查所有默认币种
python scripts/crypto_fetch.py
```

## 支持的币种（10 种）

| 别名 | 名称 | CoinGecko ID |
|:-----|:-----|:-------------|
| BTC  | Bitcoin | bitcoin |
| ETH  | Ethereum | ethereum |
| SOL  | Solana | solana |
| XRP  | Ripple | ripple |
| ADA  | Cardano | cardano |
| BNB  | Binance Coin | binancecoin |
| DOGE | Dogecoin | dogecoin |
| TRX  | TRON | tron |
| AVAX | Avalanche | avalanche-2 |
| SUI  | Sui | sui |

## 文件结构

```
crypto-market/
├── SKILL.md                    # Skill 元数据与 Agent 指令
├── README.md                   # 你正在看的这个文件
├── index.html                  # Web 行情面板（可浏览器打开）
└── scripts/
    └── crypto_fetch.py         # CoinGecko API 封装脚本
```

## Web 面板

仓库中包含一个独立的 Web 行情面板（`index.html`），无需后端，浏览器直接打开即可查看实时行情。

👉 [在线预览](https://velist.github.io/deepseek-crypto-market/)

## 依赖

- **Python 3.8+**（仅标准库，无第三方依赖）
- CoinGecko **免费公开 API**，无需注册

## 数据来源

价格数据来自 [CoinGecko API](https://www.coingecko.com/en/api)，有 1-3 分钟延迟。免费 Tier 限制约 30 次/分钟。

## License

MIT