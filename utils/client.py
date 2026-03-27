"""
Shared OpenRouter client and utilities for all lab scenarios.
"""

import os
import json
import logging
from openai import OpenAI
from dotenv import load_dotenv
from colorama import Fore, Style, init

init(autoreset=True)
load_dotenv()

# ── Logging setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    filename="agent_audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# ── OpenRouter client ──────────────────────────────────────────────────────────
def get_client():
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set in .env")
    return OpenAI(api_key=api_key, base_url=base_url)

def get_model():
    return os.getenv("OPENROUTER_MODEL", "mistralai/ministral-14b-2512")

# ── Pretty printers ────────────────────────────────────────────────────────────
def print_header(title):
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}{Style.RESET_ALL}\n")

def print_user(msg):
    print(f"{Fore.GREEN}[USER]  {msg}{Style.RESET_ALL}")

def print_agent(msg):
    print(f"{Fore.YELLOW}[AGENT] {msg}{Style.RESET_ALL}")

def print_tool_call(tool_name, args):
    print(f"{Fore.MAGENTA}[TOOL CALL] → {tool_name}({json.dumps(args)}){Style.RESET_ALL}")
    logging.info(f"TOOL_CALL | {tool_name} | {json.dumps(args)}")

def print_danger(msg):
    print(f"{Fore.RED}[⚠️  DANGER] {msg}{Style.RESET_ALL}")

def print_safe(msg):
    print(f"{Fore.GREEN}[✅ SAFE] {msg}{Style.RESET_ALL}")

def print_lesson(msg):
    print(f"\n{Fore.CYAN}[📌 LESSON] {msg}{Style.RESET_ALL}\n")
