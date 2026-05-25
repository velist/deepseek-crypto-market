<p align="center">
  <img src="https://img.shields.io/badge/DeepSeek-Skill-4f46e5?style=for-the-badge&logo=deepseek&logoColor=white" alt="DeepSeek Skill">
  <img src="https://img.shields.io/badge/CoinGecko-Free_API-8dc647?style=for-the-badge" alt="CoinGecko Free API">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

<h1 align="center">🪙 crypto-market</h1>
<p align="center"><strong>DeepSeek Skill — 实时加密货币行情查询</strong></p>

<p align="center">
  <img src="https://img.shields.io/github/license/velist/deepseek-crypto-market?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/velist/deepseek-crypto-market?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/badge/coins-10-blue?style=flat-square" alt="Coins">
</p>

---

## 这是什么？

一个 **DeepSeek TUI 本地 Skill**，当你在 DeepSeek 中说"看下币价"或"虚拟币行情"，它会自动调用 CoinGecko 免费 API，拉取主流币种的实时价格、市值、24h 涨跌幅，并格式化输出。

**零配置、零密钥、即装即用。**

## 快速安装

```bash
# 在 DeepSeek TUI 中执行
/skill install velist/deepseek-crypto-market
```

或者手动克隆到 skills 目录：

```bash
git clone https://github.com/velist/deepseek-crypto-market.git ~/.deepseek/skills/crypto-market
```

## 使用方式

安装后，在 DeepSeek 中直接说：

```
看下虚拟币行情
BTC 现在多少钱
最近 crypto 市场怎么样
ETH SOL ADA 价格走势
```

DeepSeek 会自动加载 skill → 运行脚本 → 返回格式化行情。

### 效果

```
**BTC**  — $76,958（¥522,105）  📈 +0.34%  市值 $1.54T  24h量 $21.7B
**ETH**  — $2,094（¥14,208）    📉 -1.07%  市值 $253B   24h量 $9.5B
**SOL**  — $84.84（¥575.61）    📉 -0.97%  市值 $49B    24h量 $2.4B
...
```

### 进阶：命令行直接使用

```bash
# 查 BTC + ETH，只要 USD
python scripts/crypto_fetch.py --coins btc,eth --vs usd

# 查所有默认币种
python scripts/crypto_fetch.py
```

## 支持的币种

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