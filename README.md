<p align="center">
  <img src="https://img.shields.io/badge/AI_Agent-Skill-4f46e5?style=for-the-badge" alt="AI Agent Skill">
  <img src="https://img.shields.io/badge/CoinGecko-Free_API-8dc647?style=for-the-badge" alt="CoinGecko Free API">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

<h1 align="center">🪙 crypto-market</h1>
<p align="center"><strong>Universal AI Agent Skill — Real-time Cryptocurrency Prices</strong></p>

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
  <a href="README_CN.md">中文文档</a>
</p>

---

## What is this?

A **universal AI Agent Skill** compatible with Claude Code / DeepSeek TUI / Codex / OpenClaw / Cursor / Windsurf and other mainstream AI coding assistants.

When you say "show me crypto prices" or "what's Bitcoin at" in any compatible agent, it automatically calls the CoinGecko free API to fetch real-time prices, market cap, 24h change, and volume for 10 major cryptocurrencies — then formats the output.

**Zero config. Zero API keys. Drop it in and go.**

## Compatible Agents

| Agent | Install Command |
|-------|----------------|
| **Claude Code** | `git clone ... ~/.claude/skills/crypto-market` |
| **DeepSeek TUI** | `/skill install velist/deepseek-crypto-market` |
| **Codex** | `git clone ... .codex/skills/crypto-market` |
| **OpenClaw** | `git clone ... .openclaw/skills/crypto-market` |
| **Cursor** | `git clone ... .cursor/skills/crypto-market` |
| **Windsurf** | `git clone ... .windsurf/skills/crypto-market` |

## Quick Install

```bash
# Generic install (replace with your agent's skills directory)
git clone https://github.com/velist/deepseek-crypto-market.git <skills-dir>/crypto-market

# Example: Claude Code
git clone https://github.com/velist/deepseek-crypto-market.git ~/.claude/skills/crypto-market

# Example: DeepSeek TUI (built-in skill installer)
/skill install velist/deepseek-crypto-market
```

## Usage

Once installed, just talk to your agent naturally:

```
Show me crypto prices
What's Bitcoin at right now?
How's the crypto market today?
Check ETH SOL ADA prices
看下虚拟币行情
```

The agent auto-loads the skill → runs the script → returns formatted output.

### Sample Output

```
**BTC**  — $76,958（¥522,105）  📈 +0.34%  MCap $1.54T  Vol $21.7B
**ETH**  — $2,094（¥14,208）    📉 -1.07%  MCap $253B   Vol $9.5B
**SOL**  — $84.84（¥575.61）    📉 -0.97%  MCap $49B    Vol $2.4B
**XRP**  — $1.35（¥9.13）       📉 -1.01%  MCap $83B    Vol $1.1B
**BNB**  — $656.31（¥4,453）    ➖ -0.02%  MCap $88B    Vol $608M
...
```

### CLI Usage

```bash
# Fetch BTC + ETH, USD only
python scripts/crypto_fetch.py --coins btc,eth --vs usd

# All defaults (10 coins, USD+CNY)
python scripts/crypto_fetch.py
```

## Supported Coins (10)

| Ticker | Name | CoinGecko ID |
|:-------|:-----|:-------------|
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

## File Structure

```
crypto-market/
├── SKILL.md                    # Skill metadata & agent instructions
├── README.md                   # This file (English)
├── README_CN.md                # Chinese docs
├── index.html                  # Web dashboard (open in browser)
└── scripts/
    └── crypto_fetch.py         # CoinGecko API wrapper
```

## Web Dashboard

A standalone, zero-backend web dashboard (`index.html`) with dark theme and Chinese/English toggle. Just open it in a browser.

👉 [Live Preview](https://velist.github.io/deepseek-crypto-market/)

## Dependencies

- **Python 3.8+** (stdlib only — zero third-party packages)
- CoinGecko **free public API** — no registration required

## Data Source

Prices via [CoinGecko API](https://www.coingecko.com/en/api). 1–3 minute delay. Free tier: ~30 req/min.

## License

MIT