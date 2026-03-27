"""
run_all.py — Run all lab scenarios in sequence.

"""

import subprocess
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

SCENARIOS = [
    ("01 — Hello Obedience",       "scenarios/01-hello-obedience/run.py"),
    ("02 — The Poisoned File",     "scenarios/02-poisoned-file/run.py"),
    ("03 — Over-Permissioned",     "scenarios/03-over-permissioned/run.py"),
    ("04 — Whisper in Pipeline",   "scenarios/04-whisper-pipeline/run.py"),
    ("05 — The Fix",               "scenarios/05-the-fix/run.py"),
]

def banner(title: str, index: int, total: int):
    print(f"\n{Fore.CYAN}{'█'*60}")
    print(f"  SCENARIO {index}/{total}: {title}")
    print(f"{'█'*60}{Style.RESET_ALL}\n")

def prompt_continue(label: str):
    input(f"\n{Fore.YELLOW}  ▶  Press Enter to start: {label} ...{Style.RESET_ALL}\n")

def run_scenario(path: str):
    result = subprocess.run(
        [sys.executable, path],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    return result.returncode

if __name__ == "__main__":
    print(f"\n{Fore.CYAN}")
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║   Securing AI Agents: When Your LLM Has Tool Access  ║")
    print("  ║   AI Sec Eng Kenya — Live Lab                        ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)

    total = len(SCENARIOS)

    for i, (label, path) in enumerate(SCENARIOS, start=1):
        prompt_continue(label)
        banner(label, i, total)
        code = run_scenario(path)
        if code != 0:
            print(f"\n{Fore.RED}  Scenario exited with code {code}. Check your .env and retry.{Style.RESET_ALL}")
            sys.exit(code)

    print(f"\n{Fore.GREEN}{'='*60}")
    print("  All scenarios complete.")
    print("  You've seen the attacks. You've seen the defenses.")
    print("  Now go build secure agents.")
    print(f"{'='*60}{Style.RESET_ALL}\n")
