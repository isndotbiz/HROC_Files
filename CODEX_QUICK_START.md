# 🚀 Codex Parallel Agents - Quick Start Guide

## 60-Second Setup

```bash
# 1. Initialize parallel agent system
./codex-parallel-agents.sh "my-task-name" 4

# 2. Check the generated files
ls -la .codex-work/

# 3. View launch instructions
.codex-work/launch-agents.sh
```

That's it! You now have a complete multi-agent system ready.

---

## 5-Minute Complete Walkthrough

### Step 1: Initialize (30 seconds)

```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
./codex-parallel-agents.sh "improve-website" 4
```

Output:
```
╔════════════════════════════════════════════════════════════════╗
║           CODEX PARALLEL AGENTS - Task Coordinator             ║
╚════════════════════════════════════════════════════════════════╝

✓ Codex system prompt initialized
✓ Created task file for Agent-1
✓ Created task file for Agent-2
✓ Created task file for Agent-3
✓ Created task file for Agent-4

✅ Setup Complete!
```

### Step 2: Review the System (30 seconds)

```bash
# Read the handoff document
cat .codex-work/HANDOFF.md

# Check what each agent will do
cat .codex-work/agent-tasks/agent-*.md
```

### Step 3: Launch Agents (2 minutes)

Open **4 separate terminal windows**:

**Window 1 - Agent 1 (Code Analysis):**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-1-task.md
# → Copy the entire task and provide to Claude Code
```

**Window 2 - Agent 2 (Bug Fixes):**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-2-task.md
# → Copy the entire task and provide to Claude Code
```

**Window 3 - Agent 3 (Features):**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-3-task.md
# → Copy the entire task and provide to Claude Code
```

**Window 4 - Agent 4 (Quality):**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-4-task.md
# → Copy the entire task and provide to Claude Code
```

In each Claude Code session, paste the task content and agents will immediately:
1. Read the Codex system prompt
2. Review the shared TODO
3. Begin autonomous work
4. Commit frequently to git
5. Log progress

### Step 4: Monitor (1 minute, ongoing)

In a **5th terminal window**, watch progress:

```bash
cd /Users/jonathanmallinger/Documents/HROC_Files

# Option A: Watch all logs
tail -f .codex-work/agent-logs/*.log

# Option B: Check status every 10 seconds
while true; do
  clear
  echo "=== Shared TODO Status ==="
  grep -E "⏳|⚠️|✅" .codex-work/shared-todos.md | head -10
  echo ""
  echo "=== Recent Git Commits ==="
  git log --oneline -5
  sleep 10
done

# Option C: Watch individual agent
tail -f .codex-work/agent-logs/agent-1.log
```

---

## Real-World Example: HROC Website Optimization

### Complete Task Walkthrough

**Goal:** Optimize the HROC website for performance, add new features, fix bugs, improve code quality - all in parallel!

### Initialize

```bash
./codex-parallel-agents.sh "hroc-website-v2" 4
```

### Agent Assignments (Automatically Done)

| Agent | Focus |
|-------|-------|
| **Agent 1** | Analyze index.html, styles.css, script.js - map dependencies, identify slow patterns |
| **Agent 2** | Find bugs in image loading, navigation, form handling - add tests |
| **Agent 3** | Implement hero section animations, add image lazy-load library |
| **Agent 4** | Minify CSS/JS, optimize image sizes, add performance metrics |

### Launch (Copy-paste ready)

**Terminal 1:**
```bash
cat /Users/jonathanmallinger/Documents/HROC_Files/.codex-work/agent-1-task.md
```
Provide to Claude Code → Agent 1 starts analyzing

**Terminal 2:**
```bash
cat /Users/jonathanmallinger/Documents/HROC_Files/.codex-work/agent-2-task.md
```
Provide to Claude Code → Agent 2 starts testing

**Terminal 3:**
```bash
cat /Users/jonathanmallinger/Documents/HROC_Files/.codex-work/agent-3-task.md
```
Provide to Claude Code → Agent 3 starts implementing

**Terminal 4:**
```bash
cat /Users/jonathanmallinger/Documents/HROC_Files/.codex-work/agent-4-task.md
```
Provide to Claude Code → Agent 4 starts optimizing

**Terminal 5 (Monitoring):**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
watch -n 5 'echo "=== TODO Status ===" && cat .codex-work/shared-todos.md | head -20'
```

### Watch It Happen

```
Time 0:00 → All 4 agents start simultaneously
Time 0:15 → Agent 1 commits: "Code Analysis: Identified 3 performance bottlenecks"
Time 0:20 → Agent 2 commits: "Found bug in image lazy-load implementation"
Time 0:30 → Agent 3 commits: "Added hero section animation with CSS transitions"
Time 0:45 → Agent 4 commits: "Minified CSS (43KB → 38KB), optimized images"
Time 1:00 → Agents detect no conflicts, all merging successfully
Time 1:15 → Final commits, shared TODO marked complete
```

### Results

After completion:
```bash
# View all agent work
git log --oneline | head -20

# See what each agent did
cat .codex-work/agent-logs/agent-*.log

# Check the final TODO status
cat .codex-work/shared-todos.md

# Test the optimized website
open http://10.0.0.89:8081/HROC_Website_New/
```

---

## Command Reference

### Setup Commands

```bash
# Create 4-agent system
./codex-parallel-agents.sh "task-name" 4

# Create 6-agent system (for larger tasks)
./codex-parallel-agents.sh "big-task" 6

# View what to launch
.codex-work/launch-agents.sh
```

### Monitoring Commands

```bash
# All agent logs (real-time)
tail -f .codex-work/agent-logs/*.log

# Specific agent
tail -f .codex-work/agent-logs/agent-1.log

# Shared coordination
cat .codex-work/shared-todos.md

# Recent commits
git log --oneline -20

# All agent commits
git log --oneline | grep -i agent
```

### During Execution

```bash
# Check if agents are running (terminal processes)
ps aux | grep -i claude

# See what agents are committing
git log --oneline --follow -10

# View current git status
git status

# Check for conflicts
git status | grep conflict
```

### After Completion

```bash
# View results
cat .codex-work/results-*.txt

# See all agent work
git log --all --decorate --oneline --graph | head -30

# Archive for reference
tar czf codex-work-$(date +%Y%m%d).tar.gz .codex-work/

# Clean up (keep git history)
rm -rf .codex-work/
```

---

## Agent Behavior: What to Expect

### Agent 1 (Code Analysis & Architecture)
- Reads through your entire codebase
- Maps out structure and dependencies
- Identifies patterns and conventions
- Reports on potential issues
- **Output:** Analysis document in log

### Agent 2 (Bug Fixes & Testing)
- Searches for bugs systematically
- Tests edge cases
- Creates fixes for issues found
- Adds regression tests
- **Output:** Fixed code + tests in git

### Agent 3 (Features & Implementation)
- Implements requested features
- Integrates with existing code
- Writes comprehensive tests
- Documents new functionality
- **Output:** New features in git with tests

### Agent 4 (Quality & Optimization)
- Optimizes performance
- Improves code quality
- Refactors for maintainability
- Enforces best practices
- **Output:** Optimized code in git

All agents:
- Commit frequently (every 5-10 min)
- Log progress to individual files
- Update shared TODO
- Handle conflicts via git
- Follow Codex guidelines strictly

---

## Troubleshooting

### "Agent hasn't committed in 10 minutes"
- Check the agent's log file: `tail .codex-work/agent-logs/agent-N.log`
- It might be thinking/analyzing
- If truly stuck, stop and restart

### "Multiple agents edited the same file"
- This is normal and expected
- Git will flag it as a merge conflict
- Agents read each other's logs and resolve carefully
- Tests catch any issues

### "Want to add more agents"
```bash
# Stop current agents (Ctrl+C in each terminal)
# Restart with more agents
./codex-parallel-agents.sh "task-name" 6
```

### "Want to cancel everything"
```bash
# Stop agents in their terminals (Ctrl+C)
# Work is saved in git
# Review what was done
git log --oneline -20
```

---

## Best Practices

### For You (Task Coordinator)
1. ✅ Give clear, specific task definitions
2. ✅ Let agents work autonomously - don't micromanage
3. ✅ Check logs occasionally but let them complete tasks
4. ✅ Only intervene if truly blocked (check logs first)
5. ✅ Trust the Codex system - it works

### For the Agents (Follows Automatically)
1. ✅ Read task and system prompt
2. ✅ Work autonomously on focus area
3. ✅ Commit frequently
4. ✅ Update shared TODO
5. ✅ Log findings and blockers
6. ✅ Test work before committing
7. ✅ Handle git conflicts gracefully

---

## Next Steps

### Ready to Go?

```bash
# 1. Initialize
./codex-parallel-agents.sh "my-first-task" 4

# 2. Open 5 terminals (4 for agents + 1 for monitoring)

# 3. In each of the first 4 terminals, provide task:
cat .codex-work/agent-N-task.md

# 4. In the 5th terminal, watch progress:
tail -f .codex-work/agent-logs/*.log

# 5. Sit back and let them work! ✨
```

That's it! Your parallel agent system is now running.

---

## Tips & Tricks

### Speed Up by Pre-Committing
If you have local changes, commit them first:
```bash
git add .
git commit -m "baseline: before parallel agents"
```
This gives agents a clean starting point.

### Monitor Git in Real-Time
```bash
git log --oneline -20 -f  # Follow mode
```

### Share Findings Between Agents
Each agent has a log file - they read each other's logs:
```bash
# Agent 1 findings
cat .codex-work/agent-logs/agent-1.log
# → Agent 2 reads this and adjusts work accordingly
```

### Check Agent Specialization
```bash
head -20 .codex-work/agent-tasks/agent-N-task.md
```

---

**Your parallel coding system is ready! 🚀**

Agent 1 handles architecture, Agent 2 handles bugs, Agent 3 handles features, Agent 4 handles quality.

All working simultaneously. All coordinated through git.

Go launch them! 🤖

