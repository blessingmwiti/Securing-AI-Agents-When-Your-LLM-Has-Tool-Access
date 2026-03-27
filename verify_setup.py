"""
verify_setup.py — Run this first to confirm your environment is ready.

Checks:
  - Python version
  - Required packages installed
  - .env file exists
  - OPENROUTER_API_KEY is set
  - API key is valid (makes a minimal test call)
"""

import sys
import os

print("\n  🔍 Verifying lab setup...\n")

# ── Python version ─────────────────────────────────────────────────────────────
version = sys.version_info
if version.major < 3 or (version.major == 3 and version.minor < 10):
    print(f"  ❌ Python 3.10+ required. You have {version.major}.{version.minor}")
    sys.exit(1)
print(f"  ✅ Python {version.major}.{version.minor}.{version.micro}")

# ── Package checks ─────────────────────────────────────────────────────────────
required = ["openai", "dotenv", "colorama"]
missing = []
for pkg in required:
    try:
        __import__(pkg)
        print(f"  ✅ {pkg}")
    except ImportError:
        print(f"  ❌ {pkg} not installed")
        missing.append(pkg)

if missing:
    print(f"\n  Run: pip install {' '.join(missing)}\n")
    sys.exit(1)

# ── .env file ─────────────────────────────────────────────────────────────────
from dotenv import load_dotenv
load_dotenv()

if not os.path.exists(".env"):
    print("  ❌ .env file not found")
    print("     Run: cp .env.example .env  — then add your API key\n")
    sys.exit(1)
print("  ✅ .env file found")

# ── API key ────────────────────────────────────────────────────────────────────
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key or api_key == "your_openrouter_api_key_here":
    print("  ❌ OPENROUTER_API_KEY not set in .env")
    print("     Get a free key at https://openrouter.ai\n")
    sys.exit(1)
print(f"  ✅ API key found (...{api_key[-6:]})")

# ── Live API test ──────────────────────────────────────────────────────────────
print("\n  🌐 Testing API connection...\n")
try:
    from openai import OpenAI
    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    )
    model = os.getenv("OPENROUTER_MODEL", "mistralai/mistral-7b-instruct")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Reply with exactly three words: setup is complete"}],
        max_tokens=20
    )
    reply = response.choices[0].message.content.strip()
    print(f"  ✅ API responded: \"{reply}\"")
    print(f"  ✅ Model: {model}")
except Exception as e:
    print(f"  ❌ API call failed: {e}")
    print("     Check your key and internet connection.\n")
    sys.exit(1)

# ── All good ───────────────────────────────────────────────────────────────────
print(f"""
  {'='*50}
  ✅ All checks passed. You're ready for the lab.
  
  Run scenarios with:
    python run_all.py         ← full guided flow
    python scenarios/01-hello-obedience/run.py  ← individual
  {'='*50}
""")
