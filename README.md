# Personal AI Employee - Bronze Tier

> Hackathon 0 | Panaversity | Bronze Tier Submission

A local-first, agent-driven **Personal AI Employee** that automatically processes tasks using Claude Code as its AI brain, Obsidian as its memory/dashboard, and a Python file watcher as its trigger system.

---

## What It Does

Drop any file into the `/Inbox` folder — the AI Employee picks it up, plans the work, executes it, and logs everything. No manual intervention needed.

---

## Architecture

```
Inbox (file drop)
     ↓
file_watcher.py  (Python - detects new files)
     ↓
/Needs_Action    (staged for processing)
     ↓
Claude Code      (AI Brain - reads, plans, executes)
     ↓
/Plans → /Done   (plan created then completed)
     ↓
Dashboard.md     (real-time status board updated)
     ↓
/Logs            (every action recorded)
```

---

## Components

| Component | Role |
|---|---|
| `file_watcher.py` | Watches `/Inbox`, moves files to `/Needs_Action` with timestamp + metadata |
| `CLAUDE.md` | Master instructions — tells Claude how to behave as an employee |
| `Company_Handbook.md` | Business rules, priorities, safety constraints |
| `Dashboard.md` | Live status board visible in Obsidian |
| `Skills/` | Reusable SKILL.md instruction files for specific task types |
| Obsidian Vault | GUI — view dashboard, logs, plans, and files visually |

---

## Folder Structure

```
hackathon_0_bronze_tier/
├── AI_Digital_Employee.pdf       ← Project documentation
└── AI_Employee_Vault/
    ├── Inbox/                    ← Drop files here to trigger the AI
    ├── Needs_Action/             ← Watcher moves files here (with timestamp)
    ├── Plans/                    ← Claude writes a plan before every task
    ├── Done/                     ← Completed tasks and their plans
    ├── Logs/                     ← Daily activity logs
    ├── Pending_Approval/         ← Sensitive tasks wait for human approval
    ├── Approved/                 ← Human-approved tasks
    ├── Rejected/                 ← Rejected tasks
    ├── Skills/
    │   ├── summarize-file/       ← Skill: summarize any file
    │   └── process-task/        ← Skill: general task processing
    ├── Dashboard.md              ← Real-time status board
    ├── Company_Handbook.md       ← AI rules and behavior policy
    ├── CLAUDE.md                 ← Master instructions for Claude Code
    └── file_watcher.py          ← Python automation script
```

---

## How to Run

### Prerequisites

- Python 3.13+
- Node.js v24+
- [Obsidian](https://obsidian.md) (free)
- Claude Code: `npm install -g @anthropic/claude-code`

### Installation

```bash
git clone https://github.com/safiatahir2211-ui/hackathon_0_bronze_tier.git
cd hackathon_0_bronze_tier/AI_Employee_Vault
pip install watchdog
```

Open Obsidian → **File > Open Vault** → select the `AI_Employee_Vault` folder.

### Run (2 Terminals)

**Terminal 1 — File Watcher:**
```bash
cd AI_Employee_Vault
python file_watcher.py
```

**Terminal 2 — Claude Code (AI Brain):**
```bash
cd AI_Employee_Vault
claude
```
Then type:
```
Process all tasks in /Needs_Action following CLAUDE.md. Use skills from /Skills/. Update Dashboard.md when done.
```

---

## Task Flow

1. Drop any `.txt` or file into `/Inbox`
2. Watcher detects it → moves to `/Needs_Action` with a timestamp prefix and creates a `.md` metadata file
3. Claude Code reads the task, checks `Company_Handbook.md` for rules
4. Claude writes a plan in `/Plans/PLAN_[taskname].md`
5. Claude executes step by step using the matching skill from `/Skills/`
6. If a step is sensitive (payment, deletion, etc.) → moved to `/Pending_Approval` and paused
7. On completion → task moved to `/Done`, `Dashboard.md` updated, log written to `/Logs/`

---

## Agent Skills

### `summarize-file`
Summarizes any file dropped into the inbox:
- Reads full file contents
- Extracts key points and action items
- Appends a `## Summary` section to the file
- Moves to `/Done` and updates dashboard

### `process-task`
General-purpose task processing:
- Determines priority (URGENT / HIGH / NORMAL / LOW)
- Creates a structured plan
- Executes each step
- Routes sensitive steps to `/Pending_Approval`

---

## Safety & Security

- Sensitive tasks (payments, deletions, outbound messages) are **never executed automatically** — they go to `/Pending_Approval` for human review
- `.gitignore` excludes `.env`, `credentials.json`, `.obsidian/`, `__pycache__/`, `*.secret`, `*.token`
- All data stays **local on your machine**
- Human-in-the-loop is built into the workflow by design

---

## Priority Levels

| Level | Handle Within |
|---|---|
| URGENT | Immediately |
| HIGH | 4 hours |
| NORMAL | 24 hours |
| LOW | 1 week |

---

## Tech Stack

- **Claude Code** (Anthropic) — AI reasoning and task execution
- **Python + Watchdog** — File system event monitoring
- **Obsidian** — Local markdown-based knowledge base and GUI
- **Markdown** — All memory, logs, plans stored as plain `.md` files

---

## Hackathon

**Event:** Hackathon 0 — Panaversity
**Tier:** Bronze
**Theme:** AI-Driven & AI-Native Development
