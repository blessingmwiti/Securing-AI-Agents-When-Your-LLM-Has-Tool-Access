# Scenario 05 — The Fix ✅

## Concept
All five defenses applied simultaneously. The same attacks from Scenarios 02 and 04 are replayed — and they fail safely. Legitimate requests still work perfectly.

## Defenses in action

| Defense | Implementation |
|---|---|
| Input sanitization | Pattern matching blocks known injection phrases before LLM sees them |
| Content isolation | External file/web content wrapped in `<external_content>` tags so model knows it's data, not instructions |
| Least privilege | Only `read_file` and `search_knowledge_base` exposed — no delete, no shell |
| Human-in-the-loop | Destructive tools require explicit confirmation before execution |
| Audit logging | Every tool call, every blocked action written to `agent_audit.log` |

## What to watch for
- Attack 1 (poisoned file): Agent reads the file, content isolation prevents injected instructions from executing
- Attack 2 (direct injection): Input sanitizer catches it before the LLM even receives the message
- Legitimate query: Works exactly as expected — defenses are invisible to normal use

## Run it
```bash
python run.py
```

## The Closing Point
None of this is exotic. There's no PhD required. No special framework. Just intentional engineering:

```
□ Sanitize inputs
□ Scope tools to the task
□ Isolate external content
□ Confirm before destructive actions
□ Log everything
```

The difference between a vulnerable agent and a secure one is a few hundred lines of code and the decision to write them before shipping.
