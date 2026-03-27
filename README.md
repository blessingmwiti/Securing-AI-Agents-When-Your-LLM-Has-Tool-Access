# 🔐 Securing AI Agents: When Your LLM Has Tool Access

> *"You didn't give it a gun. You gave it a keyboard. That's worse."*

**AI Sec Eng Kenya — Live Lab Repository**

This repo contains all hands-on scenarios for the talk. Each scenario is self-contained, runs via OpenRouter, and is designed to make you uncomfortable in the right way.

---

## 🛠️ Prerequisites

```bash
# Python 3.10+
pip install openai python-dotenv colorama
```

Create a `.env` file in the root:

```env
OPENROUTER_API_KEY=your_openrouter_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=mistralai/mistral-7b-instruct
```

> **No GPU needed. No local model needed. Just an OpenRouter API key.**
> Cost for the full lab: under $0.05 per participant.

---

## 🧪 Scenarios

| # | Scenario | Concept | Danger Level |
|---|---|---|---|
| 01 | [Hello Obedience](./scenarios/01-hello-obedience/) | Agents execute without confirmation | 🟢 |
| 02 | [The Poisoned File](./scenarios/02-poisoned-file/) | Indirect prompt injection | 🔴 |
| 03 | [Over-Permissioned](./scenarios/03-over-permissioned/) | Excessive agency | 🟠 |
| 04 | [Whisper in the Pipeline](./scenarios/04-whisper-pipeline/) | Direct prompt injection | 🟠 |
| 05 | [The Fix](./scenarios/05-the-fix/) | Hardened agent — all defenses on | 🟢 |

---

## 🚀 Running the Lab

```bash
# Run scenarios in order
cd scenarios/01-hello-obedience && python run.py
cd scenarios/02-poisoned-file   && python run.py
cd scenarios/03-over-permissioned && python run.py
cd scenarios/04-whisper-pipeline  && python run.py
cd scenarios/05-the-fix           && python run.py
```

Each scenario prints clearly what the agent is doing and why it's dangerous (or safe).

---

## ⚠️ Disclaimer

This lab is for **educational purposes only**. All destructive operations are simulated — no files are actually deleted, no data is actually exfiltrated. The point is to understand the attack surface, not to cause harm.

---

## 📌 Resources

- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Simon Willison on Prompt Injection](https://simonwillison.net/2022/Sep/12/prompt-injection/)
- [Embrace the Red Blog](https://embracethered.com/blog/)
- [OpenRouter Docs](https://openrouter.ai/docs)

---

*Built for AI Sec Eng Kenya | Follow along at the live session*
