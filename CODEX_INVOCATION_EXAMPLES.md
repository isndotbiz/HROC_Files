# 🎯 Codex Agent Invocation Examples

Complete, copy-paste ready examples for invoking parallel agents.

---

## Example 1: HROC Website Performance Optimization

### Complete Walkthrough

#### Step 1: Initialize System

```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
./codex-parallel-agents.sh "hroc-performance-v1" 4
```

#### Step 2: Open 5 Terminal Windows

**Terminal 1 - Agent 1:**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-1-task.md | pbcopy  # Copy to clipboard (Mac)
# Or: cat .codex-work/agent-1-task.md > agent1-task.txt  # For review first
```

**Terminal 2 - Agent 2:**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-2-task.md | pbcopy
```

**Terminal 3 - Agent 3:**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-3-task.md | pbcopy
```

**Terminal 4 - Agent 4:**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
cat .codex-work/agent-4-task.md | pbcopy
```

**Terminal 5 - Monitor:**
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files

# Option A: Watch logs continuously
while true; do
  clear
  echo "╔════════════════════════════════════════════════════════════╗"
  echo "║               AGENT STATUS - $(date +%H:%M:%S)                        ║"
  echo "╚════════════════════════════════════════════════════════════╝"
  echo ""
  echo "📋 TODO Status:"
  grep -E "Agent [1-4]:|⏳|✅|⚠️" .codex-work/shared-todos.md | head -15
  echo ""
  echo "📊 Recent Commits:"
  git log --oneline -5
  echo ""
  sleep 10
done

# Option B: Simpler real-time log watch
tail -f .codex-work/agent-logs/*.log
```

#### Step 3: In Claude Code, Provide Tasks

For each Claude Code session (in terminals 1-4):

**Copy and paste into Claude Code:**

```
You are Codex, based on GPT-5. You are running as a coding agent in the Codex CLI on a user's computer.

[The system will load the agent task file]

Your task is described in the file: .codex-work/agent-1-task.md [change number for each agent]

Read this file to understand your specific assignment, focus area, and coordination guidelines.

Key files you'll reference:
- .codex-work/codex-system-prompt.txt - Your operating guidelines
- .codex-work/shared-task.md - The overall task definition
- .codex-work/shared-todos.md - Coordination list (update as you work)
- .codex-work/agent-logs/agent-1.log - Your progress log [change number]

Begin by reading these files, then start autonomous work on your assigned focus area.

Remember: Commit frequently, log progress, and update the shared TODO as you work.
```

#### Step 4: Let Them Work

Agents will:
1. Auto-load the task file
2. Read system prompt and coordination files
3. Begin autonomous work
4. Commit frequently to git
5. Update shared TODO
6. Log progress

Just monitor in Terminal 5 and let them work! ✨

---

## Example 2: Add New Feature to Codebase

### Scenario: Add "Impact Metrics" Dashboard to HROC Website

```bash
# Initialize
./codex-parallel-agents.sh "add-metrics-dashboard" 4
```

**What agents will do:**

| Agent | Task |
|-------|------|
| Agent 1 | Analyze current HROC website structure and where dashboard fits |
| Agent 2 | Find any existing metrics code, test current dashboard |
| Agent 3 | Build the metrics dashboard component with HTML/CSS/JS |
| Agent 4 | Optimize dashboard performance, add animations |

**Provide to each Claude Code:**

Agent 1:
```
Read: .codex-work/agent-1-task.md

Your job: Analyze the HROC website codebase and determine:
1. Current website structure
2. Where a metrics dashboard should integrate
3. What dependencies exist
4. Architecture recommendations for the new dashboard

Report findings in your log and update shared TODO.
```

Agent 2:
```
Read: .codex-work/agent-2-task.md

Your job:
1. Search for any existing metrics or analytics code
2. Test current website functionality
3. Identify issues that should be fixed first
4. Report blockers for Agent 3's implementation

Fix any issues you find and commit to git.
```

Agent 3:
```
Read: .codex-work/agent-3-task.md

Your job:
1. Build the metrics dashboard HTML/CSS/JS
2. Integrate with existing HROC website structure
3. Display key metrics (donors, volunteers, impact numbers)
4. Make it mobile responsive
5. Write tests for dashboard functionality

Commit all code frequently.
```

Agent 4:
```
Read: .codex-work/agent-4-task.md

Your job:
1. Performance optimize the new dashboard
2. Reduce bundle size if needed
3. Add smooth animations to dashboard elements
4. Ensure accessibility (WCAG 2.2 AA)
5. Profile and improve load times

Commit optimizations to git.
```

---

## Example 3: Code Quality Refactoring

### Scenario: Improve HTML, CSS, JS Quality

```bash
./codex-parallel-agents.sh "refactor-code-quality" 4
```

**Provide to Claude Code:**

For each terminal, show the appropriate task:

**Terminal 1 - Agent 1 (Analysis):**
```bash
cat .codex-work/agent-1-task.md
# Task: Analyze index.html, styles.css, script.js for quality issues
```

**Terminal 2 - Agent 2 (Bugs):**
```bash
cat .codex-work/agent-2-task.md
# Task: Find and fix bugs in HTML/CSS/JS
```

**Terminal 3 - Agent 3 (Implementation):**
```bash
cat .codex-work/agent-3-task.md
# Task: Improve CSS organization, add CSS variables, modularize JS
```

**Terminal 4 - Agent 4 (Quality):**
```bash
cat .codex-work/agent-4-task.md
# Task: Optimize CSS/JS size, improve maintainability, enforce best practices
```

**Monitor:**
```bash
# Watch progress
tail -f .codex-work/agent-logs/*.log

# See commits
git log --oneline | head -20
```

---

## Example 4: Bug Fix Sprint

### Scenario: Fix All Known Issues

```bash
./codex-parallel-agents.sh "bug-fix-sprint" 4
```

**Setup:**

Agent 1 analyzes the codebase for issues

Agent 2 finds all bugs systematically

Agent 3 implements fixes

Agent 4 verifies and optimizes the fixes

**Invoke each agent with:**

```bash
# Get the task (same in each terminal)
cat .codex-work/agent-[1-4]-task.md

# Paste into Claude Code with this intro:
You are Codex. Read the task file for your assignment.
Focus area: Finding and fixing bugs in the HROC codebase.
Commit frequently. Update the shared TODO. Log your progress.
```

---

## Copy-Paste Ready: 4-Terminal Setup Script

Save this as `launch-codex-agents.sh`:

```bash
#!/bin/bash

TASK_NAME="${1:-my-task}"
REPO="/Users/jonathanmallinger/Documents/HROC_Files"

# Initialize
cd "$REPO"
./codex-parallel-agents.sh "$TASK_NAME" 4

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          CODEX AGENTS READY - Copy-paste tasks below            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

for i in 1 2 3 4; do
  echo "═══════════════════════════════════════════════════════════════════"
  echo "Terminal $i - Agent $i Task (copy entire block):"
  echo "═══════════════════════════════════════════════════════════════════"
  echo ""
  cat "$REPO/.codex-work/agent-$i-task.md"
  echo ""
  echo ""
done

echo "═══════════════════════════════════════════════════════════════════"
echo "Terminal 5 - Monitor Agents:"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "cd $REPO && tail -f .codex-work/agent-logs/*.log"
echo ""
```

Usage:
```bash
bash launch-codex-agents.sh "my-task-name"
```

---

## Step-By-Step: First Time Running Agents

### 1. Initialize (30 seconds)
```bash
cd /Users/jonathanmallinger/Documents/HROC_Files
./codex-parallel-agents.sh "first-test" 4
```

### 2. Open 5 Terminals

**Terminal 1:**
```
Tab title: "Agent 1"
Command: cd /Users/jonathanmallinger/Documents/HROC_Files
```

**Terminal 2:**
```
Tab title: "Agent 2"
Command: cd /Users/jonathanmallinger/Documents/HROC_Files
```

**Terminal 3:**
```
Tab title: "Agent 3"
Command: cd /Users/jonathanmallinger/Documents/HROC_Files
```

**Terminal 4:**
```
Tab title: "Agent 4"
Command: cd /Users/jonathanmallinger/Documents/HROC_Files
```

**Terminal 5:**
```
Tab title: "Monitor"
Command: cd /Users/jonathanmallinger/Documents/HROC_Files
```

### 3. Get Task Files

**Terminal 1:**
```bash
cat .codex-work/agent-1-task.md
# Copy entire output
```

**Terminal 2:**
```bash
cat .codex-work/agent-2-task.md
# Copy entire output
```

**Terminal 3:**
```bash
cat .codex-work/agent-3-task.md
# Copy entire output
```

**Terminal 4:**
```bash
cat .codex-work/agent-4-task.md
# Copy entire output
```

### 4. Launch Claude Code in Each Terminal

In each terminal with a task file displayed:

1. Open Claude Code
2. Paste the task file content
3. Say: "You are Codex. Execute this task autonomously."
4. Press Enter

Claude Code will:
- Load the system prompt
- Read the task file
- Begin autonomous work
- Commit frequently to git
- Update the shared TODO

### 5. Monitor Progress

**Terminal 5:**
```bash
# Watch logs in real-time
tail -f .codex-work/agent-logs/*.log

# Or use the watch script above
```

---

## Real-Time Monitoring Template

Save as `monitor-agents.sh`:

```bash
#!/bin/bash

REPO="/Users/jonathanmallinger/Documents/HROC_Files"
cd "$REPO"

while true; do
  clear
  echo "╔════════════════════════════════════════════════════════════════╗"
  echo "║          CODEX AGENTS - Live Status Monitor                    ║"
  echo "║                 $(date '+%Y-%m-%d %H:%M:%S')                     ║"
  echo "╚════════════════════════════════════════════════════════════════╝"
  echo ""

  echo "📊 Shared TODO Status:"
  echo "─────────────────────────────────────────────────────────────────"
  grep -E "⏳|✅|⚠️" .codex-work/shared-todos.md | head -10
  echo ""

  echo "📝 Recent Git Commits:"
  echo "─────────────────────────────────────────────────────────────────"
  git log --oneline -5
  echo ""

  echo "🤖 Agent Log Updates (Last 2 lines from each):"
  echo "─────────────────────────────────────────────────────────────────"
  for i in 1 2 3 4; do
    echo "Agent $i:"
    tail -2 .codex-work/agent-logs/agent-$i.log 2>/dev/null || echo "  (No activity yet)"
    echo ""
  done

  echo "Press Ctrl+C to stop monitoring"
  sleep 10
done
```

Usage:
```bash
bash monitor-agents.sh
```

---

## Troubleshooting Invocation

### Issue: "Agent doesn't seem to be working"

Check the log:
```bash
tail -f .codex-work/agent-logs/agent-1.log
```

If empty, the agent hasn't started yet. Make sure you provided the full task file to Claude Code.

### Issue: "How do I know if agents are running?"

Check git activity:
```bash
# Watch commits come in
git log --oneline -f | head -20
```

If commits appear every 5-10 minutes, agents are working!

### Issue: "Want to stop agents"

In each agent terminal, press: **Ctrl+C**

Work is saved in git - nothing is lost.

### Issue: "Want to restart an agent"

1. Stop the agent (Ctrl+C)
2. Open a fresh terminal
3. Provide the task file again
4. Claude Code will pick up from where git is

---

## What Agents Say When Working

You'll see output like:

```
✅ Reading task file...
✅ Loading system prompt...
✅ Reviewing shared TODO...
✅ Beginning work on Code Analysis & Architecture...

📁 Analyzing HROC_Website_New/
📝 Reading index.html (47 KB)
📝 Reading styles.css (43 KB)
📝 Reading script.js (12 KB)

📊 Architecture Analysis:
   - Single-page HTML application
   - Responsive CSS grid system
   - Vanilla JavaScript
   - 60+ images integrated
   - WCAG 2.2 AA accessible

⚠️ Found: CSS could be better organized with variables
⚠️ Found: JavaScript has no error handling in form submission
✅ Recommendations documented

📝 Committing findings...
✅ Commit: a3b4c5d "Analysis: Website architecture overview and recommendations"

📊 Updating shared TODO...
✅ Marked Agent 1 work as complete

Next: Agent 2 will fix bugs, Agent 3 will implement features, Agent 4 will optimize
```

---

## Success Indicators

### After 5 Minutes:
```bash
# You should see commits from each agent
git log --oneline | head -10
# Output: Multiple commits from agents 1-4
```

### After 15 Minutes:
```bash
# Shared TODO should show progress
cat .codex-work/shared-todos.md
# Output: Some tasks marked ✅ or ⏳
```

### After 30 Minutes:
```bash
# Agent logs should show substantial work
wc -l .codex-work/agent-logs/*.log
# Output: Each log should have 50+ lines
```

---

## Summary

1. **Initialize:** `./codex-parallel-agents.sh "task-name" 4`
2. **Open 5 Terminals:** 4 for agents + 1 for monitoring
3. **Get Task Files:** `cat .codex-work/agent-N-task.md`
4. **Provide to Claude Code:** Paste task file and say "Execute this autonomously"
5. **Monitor:** `tail -f .codex-work/agent-logs/*.log`
6. **Watch Results:** `git log --oneline`

That's it! Agents will work in parallel, commit frequently, and coordinate through git and shared TODO.

---

**Ready to invoke your agents? 🚀**

Copy any of the examples above and get started!

