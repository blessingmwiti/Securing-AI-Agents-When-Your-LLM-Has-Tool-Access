# Scenario 02 — The Poisoned File ☠️

## Concept
**Indirect Prompt Injection** — the most underestimated attack vector in AI agents.

The attacker doesn't talk to your agent directly. They put instructions inside content that your agent reads — a file, a webpage, a PDF, an email. The agent reads it and executes those instructions as if they came from you.

## What to watch for
- The user only asks for a summary
- The agent calls `list_directory` — the user never asked for that
- The agent attempts to write sensitive data to disk — the user never asked for that
- Every rogue action was triggered by content inside the file or webpage

> "Who sent those instructions?"

## Run it
```bash
python run.py
```

## Why this is the scariest one
- Works on any agent that reads external content
- The user's request looks completely innocent
- The malicious instructions are invisible at a glance
- There's no "attack" in the traditional sense — the agent just did its job

## Real-world analogues
- Agent summarizing customer emails — attacker sends an email with injected instructions
- Agent browsing the web for research — attacker poisons the target page
- Agent reading uploaded documents — attacker embeds instructions in a PDF
