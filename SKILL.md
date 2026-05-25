---
name: crypto-market
description: 查询加密货币实时行情。当用户询问币价、虚拟币行情、加密货币市场、比特币/以太坊/Solana 价格、涨跌幅、市值，或表达想看盘、看行情时触发。支持 CoinGecko 免费 API，无需密钥。
---

# Crypto Market Skill

拉取主流加密货币的实时价格、市值、24h 涨跌幅和成交量，并以结构化格式呈现。

## 触发条件

当用户消息包含以下任一关键词或意图时，加载本 Skill：

- 币价、虚拟币、加密货币、数字货币、coin、token
- 行情、盘面、大盘、涨跌、市值、走势
- BTC、ETH、SOL、XRP、ADA、BNB、DOGE、TRX、AVAX、SUI 等代币符号
- "帮我看下币"、"最近 crypto 怎么样"、"虚拟币今天什么情况"

## 工作流

### 1. 解析用户意图

从用户消息中提取：
- 目标币种（默认：BTC、ETH、SOL、XRP、ADA、BNB、DOGE、TRX、AVAX、SUI）
- 关注指标（价格、涨跌幅、市值、成交量）
- 计价货币（默认：USD + CNY）

### 2. 运行脚本

```bash
python scripts/crypto_fetch.py --coins BTC,ETH,SOL [--coins ...]
```

脚本参数：
- `--coins btc,eth,sol,...`  币种 ID 或别名（小写逗号分隔）
- `--vs usd,cny`            计价货币

脚本默认返回完整 JSON（含市值、交易量、24h涨跌）。

### 3. 解析并展示

解析 JSON 输出，按以下格式展示每个币种（每币一行，信息紧凑）：

```
**BTC** — $76,958（¥522,105）  📈 +0.34%  市值 $1.54T  24h量 $24.1B
```

格式规则：
- 涨跌幅用 emoji：📈 +x% / 📉 -x% / ➖ ~0%
- 市值、交易量保留合理精度（>1B 用 B，>1M 用 M）
- 按市值从大到小排列
- 附市场概述段落：谁领涨/领跌、资金流向方向、情绪判断

## 脚本说明

`scripts/crypto_fetch.py` 是一个纯 Python 3 脚本，依赖仅标准库。调用 CoinGecko 免费公开 API，无需注册或 API Key。单次请求覆盖所有目标币种。

### 可用别名

| 别名 | CoinGecko ID |
|------|-------------|
| btc  | bitcoin     |
| eth  | ethereum    |
| sol  | solana      |
| xrp  | ripple      |
| ada  | cardano     |
| bnb  | binancecoin |
| doge | dogecoin    |
| trx  | tron        |
| avax | avalanche-2 |

## 注意事项

- CoinGecko 免费 API 有速率限制（~30 次/分钟），短时间频繁调用可能被限
- 价格数据有 1-3 分钟延迟，非毫秒级实时
- 如果 API 不可达，脚本会输出明确错误信息；此时应告知用户并建议稍后重试
- 不要对同一请求反复重试超过 3 次