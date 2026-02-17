# Personal AI Employee - Bronze Tier

A local-first, agent-driven Personal AI Employee that processes tasks automatically using Claude Code, Obsidian, and a Python file watcher.

## Tier
**Bronze** - Hackathon 0 (Panaversity)

## Architecture
```
Watcher (Python) + Claude Code (AI Brain) + Obsidian (Memory/GUI) + Agent Skills
```

### Components
| Component | Role |
|-----------|------|
| **Obsidian Vault** | Memory & Dashboard (GUI) |
| **Claude Code** | AI Brain - reads, plans, executes, logs |
| **file_watcher.py** | Watches /Inbox for new files |
| **Agent Skills** | Reusable SKILL.md instruction files |

## Setup Instructions

### Prerequisites
- Python 3.13+
- Node.js v24+
- Obsidian (free download from obsidian.md)
- Claude Code (`npm install -g @anthropic/claude-code`)
- GitHub Desktop

### Installation
1. Clone this repository
2. Open the vault folder in Obsidian (File > Open Vault)
3. Install Python dependency:
   ```bash
   pip install watchdog
   ```

## How to Run (2 Terminals)

### Terminal 1 - File Watcher
```bash
cd AI_Employee_Vault
python file_watcher.py
```

### Terminal 2 - Claude Code
```bash
cd AI_Employee_Vault
claude
# Then type:
Process all tasks in /Needs_Action following CLAUDE.md. Use skills from /Skills/. Update Dashboard.md when done.
```

## File Flow
```
Inbox → Needs_Action → Plans → Done
  ↑         ↓              ↓
Watcher   Claude reads   Claude executes
moves     & plans        & logs
```

1. Drop a file into `/Inbox`
2. Watcher detects it and moves to `/Needs_Action` with timestamp
3. Claude Code reads it, creates a plan in `/Plans`
4. Claude executes the task, moves to `/Done`
5. Dashboard.md is updated automatically

## Folder Structure
```
AI_Employee_Vault/
├── Inbox/              ← Drop files here
├── Needs_Action/       ← Watcher moves files here
├── Plans/              ← Claude writes plans here
├── Done/               ← Completed tasks
├── Logs/               ← Activity records
├── Skills/             ← Agent Skill files (SKILL.md)
│   ├── summarize-file/
│   └── process-task/
├── Pending_Approval/   ← Sensitive tasks wait here
├── Approved/           ← Approved tasks
├── Rejected/           ← Rejected tasks
├── Dashboard.md        ← Real-time status board
├── Company_Handbook.md ← AI rules and behavior
├── CLAUDE.md           ← Master instructions for Claude
├── file_watcher.py     ← Python watcher script
└── README.md           ← This file
```

## Security
- `.gitignore` excludes: `.env`, `credentials.json`, `__pycache__/`, `.obsidian/`, `*.secret`, `*.token`
- All data stays local on your machine
- Human-in-the-loop: sensitive tasks go to `/Pending_Approval`

## Agent Skills
- **summarize-file**: Summarizes any file with key points and action items
- **process-task**: General task processing with planning and execution
