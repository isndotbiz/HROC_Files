# 🤖 Codex Parallel Agents System

A sophisticated multi-agent coordination system for launching autonomous Claude Code agents to work on your codebase in parallel.

## Overview

The **Codex Parallel Agents** system allows you to:

- ✅ Launch multiple autonomous agents simultaneously
- ✅ Distribute work based on specialization
- ✅ Coordinate agents through git and shared TODO lists
- ✅ Maximize throughput with true parallelism
- ✅ Maintain code quality and consistency
- ✅ Track progress and findings across all agents

## Quick Start

### 1. Initialize the Parallel Agent System

```bash
./codex-parallel-agents.sh "my-task-name" 4
```

This creates:
- System prompt with Codex guidelines
- Task definitions for each agent
- Shared coordination files
- Agent-specific task files
- Logging directories

### 2. View Launch Instructions

```bash
.codex-work/launch-agents.sh
```

Output shows exact commands to launch each agent.

### 3. Launch Agents

Open 4 terminal windows and run:

**Terminal 1:**
```bash
cat .codex-work/agent-1-task.md
# Copy the content and provide to Claude Code
```

**Terminal 2:**
```bash
cat .codex-work/agent-2-task.md
# Copy the content and provide to Claude Code
```

**Terminal 3:**
```bash
cat .codex-work/agent-3-task.md
# Copy the content and provide to Claude Code
```

**Terminal 4:**
```bash
cat .codex-work/agent-4-task.md
# Copy the content and provide to Claude Code
```

### 4. Monitor Progress

```bash
# Watch all agent logs in real-time
tail -f .codex-work/agent-logs/*.log

# Check shared coordination
cat .codex-work/shared-todos.md

# Monitor git commits
git log --oneline -10 --graph
```

## Agent Specializations

### Agent 1: Code Analysis & Architecture
- Analyzes codebase structure and organization
- Maps dependencies and relationships
- Identifies architectural patterns
- Reports on code quality metrics
- **Focus:** Understanding and documenting the codebase

### Agent 2: Bug Fixes & Testing
- Searches for and identifies bugs
- Tests edge cases and error conditions
- Creates fixes for issues
- Adds regression tests
- **Focus:** Correctness and robustness

### Agent 3: Features & Implementation
- Implements new requested features
- Enhances existing functionality
- Writes comprehensive tests
- Ensures integration with existing code
- **Focus:** Feature completeness and quality

### Agent 4: Quality & Optimization
- Optimizes performance
- Improves code quality
- Refactors for maintainability
- Enforces best practices
- **Focus:** Efficiency and cleanliness

## Codex System Prompt

All agents operate under unified guidelines emphasizing:

### Core Principles
- **Tool Preference**: Use specialized tools over raw shell commands
- **Autonomy**: Proactive work without waiting for prompts
- **Parallelization**: Independent execution with coordination
- **Quality First**: Correctness and clarity over speed
- **No Risky Shortcuts**: Robust, well-tested code only

### Key Practices
- Batch edits instead of micro-edits
- Parallelize independent operations
- Reuse code and existing patterns
- Type-safe implementations
- Explicit error handling (never silent)

### Git Safety
- Never use destructive commands (`git reset --hard`, etc.)
- Respect existing changes
- Commit frequently with clear messages
- Push regularly to avoid conflicts

## Coordination Mechanism

### Shared TODO List
The `.codex-work/shared-todos.md` file is the coordination hub:

```markdown
✅ Task completed
⏳ Task in progress
⚠️ Blocker/issue found
```

Agents check this before starting and update it as they work.

### Git as Source of Truth
- Each agent commits their work frequently
- Main branch always remains stable
- Git logs show who did what and when
- Merge conflicts detected automatically

### Agent Logs
Individual log files in `.codex-work/agent-logs/` for:
- Progress tracking
- Findings and discoveries
- Blocker reporting
- Cross-agent communication

## Running a Parallel Task

### Scenario: "Refactor HROC Website for Performance"

```bash
# 1. Initialize
./codex-parallel-agents.sh "website-perf-refactor" 4

# 2. Check what needs to happen
cat .codex-work/HANDOFF.md

# 3. View agent assignments
ls .codex-work/agent-tasks/

# 4. In 4 separate terminals, launch agents
# Each agent will:
# - Read their task
# - Review system prompt
# - Check shared TODO
# - Begin autonomous work
```

### What Happens in Parallel

```
Time 0:00 - All 4 agents start
  Agent 1: Analyzing codebase architecture
  Agent 2: Searching for performance issues
  Agent 3: Planning optimizations
  Agent 4: Reviewing best practices

Time 0:15 - Agents report findings
  Agent 1: Commits architecture analysis
  Agent 2: Commits bug findings
  Agent 3: Updates shared TODO with blockers
  Agent 4: Commits quality report

Time 0:30 - Agents implement fixes
  All agents working on their areas
  Frequent commits to git
  Logging progress

Time 1:00 - Agents complete work
  Final commits pushed
  Shared TODO updated
  Results aggregated
```

## Monitoring & Debugging

### Watch Real-Time Progress

```bash
# Monitor all logs
tail -f .codex-work/agent-logs/*.log

# Monitor git
watch -n 5 'git log --oneline -5'

# Monitor TODO
watch -n 10 'cat .codex-work/shared-todos.md'
```

### Check Individual Agent Progress

```bash
# Agent 1 findings
cat .codex-work/agent-logs/agent-1.log

# Agent 2 issues found
cat .codex-work/agent-logs/agent-2.log

# Agent 3 implementations
cat .codex-work/agent-logs/agent-3.log

# Agent 4 optimizations
cat .codex-work/agent-logs/agent-4.log
```

### If Agents Conflict

When multiple agents touch the same file:

1. **Detection**: Git will flag the conflict
2. **Communication**: Agents log findings about the conflict
3. **Resolution**: Agents read each other's logs and merge carefully
4. **Verification**: Run tests to ensure nothing broke

## Directory Structure

```
.codex-work/
├── codex-system-prompt.txt      # Unified Codex guidelines
├── shared-task.md               # Task definition & strategy
├── shared-todos.md              # Coordination TODO list
├── HANDOFF.md                   # Detailed handoff instructions
├── launch-agents.sh             # Agent launch script
├── agent-tasks/
│   ├── agent-1-task.md         # Code Analysis focus
│   ├── agent-2-task.md         # Bug Fixes focus
│   ├── agent-3-task.md         # Features focus
│   └── agent-4-task.md         # Quality focus
└── agent-logs/
    ├── agent-1.log             # Agent 1 progress log
    ├── agent-2.log             # Agent 2 progress log
    ├── agent-3.log             # Agent 3 progress log
    └── agent-4.log             # Agent 4 progress log
```

## Best Practices

### For Users Launching Agents

1. **Clear Task Definition**: Write specific, actionable task goals
2. **Distinct Specializations**: Don't overlap agent focus areas
3. **Frequent Monitoring**: Check logs and TODO regularly
4. **Communication**: Use logs to communicate between agents
5. **Patience**: Let agents work autonomously; intervene only if blocked

### For Each Agent

1. **Read Everything First**: System prompt, task, TODO, logs
2. **Clear Progress Log**: Update your log as you work
3. **Commit Frequently**: Don't batch work; commit every 5-10 minutes
4. **Update Shared TODO**: Mark progress and report blockers
5. **Check for Conflicts**: Look for other agents working on same files
6. **Test Your Work**: Don't commit broken code

## Advanced Usage

### Custom Agent Count

```bash
# Launch 6 agents instead of 4
./codex-parallel-agents.sh "large-refactor" 6
```

### Custom Task Definition

Create a task description before running:

```bash
# Create custom-tasks.md with your detailed task
./codex-parallel-agents.sh "custom-work" 4 custom-tasks.md
```

### Background Execution

Run agents in the background:

```bash
# Launch agents in tmux or screen
tmux new-session -d -s agent-1 "bash .codex-work/agent-1-launch.sh"
tmux new-session -d -s agent-2 "bash .codex-work/agent-2-launch.sh"
# ... etc
```

### Results Aggregation

After all agents complete:

```bash
# View results
cat .codex-work/results-*.txt

# Create final summary
git log --oneline --grep="Agent" -20 > final-summary.txt

# Archive work
tar czf codex-work-backup-$(date +%s).tar.gz .codex-work/
```

## Example: Real HROC Task

```bash
# Initialize for HROC website optimization
./codex-parallel-agents.sh "hroc-website-optimization" 4

# Agent assignments:
# 1. Analyze current HROC website architecture
# 2. Find performance bottlenecks and bugs
# 3. Implement new features (more images, animations)
# 4. Optimize CSS, JavaScript, images

# Launch in 4 terminals, each gets their task
# All agents work simultaneously
# Git captures all changes
# Shared TODO tracks dependencies
```

## Troubleshooting

### Agent Seems Stuck

- Check the agent's log file for what it's doing
- Review shared TODO for blockers
- Look at git to see last commit timestamp
- If truly stuck >30 min, check if agent is waiting for user input

### Agents Conflicting on Same File

This is normal! Agents will:
1. Detect the conflict via git
2. Log the conflict in their files
3. Communicate via logs about the conflict
4. Merge changes carefully
5. Test to ensure nothing broke

### Want to Pause All Agents

Stop them in their respective terminals (Ctrl+C). Work is already committed to git, so nothing is lost.

### Want to Restart a Single Agent

Just stop that agent and restart the task in a fresh terminal. Git will handle syncing the current state.

## Support

- **System Prompt Issues**: Review `codex-system-prompt.txt`
- **Coordination Issues**: Check `shared-todos.md`
- **Agent-Specific Issues**: Read the agent's task file and log
- **Git Conflicts**: Use `git status` and `git diff` to understand conflicts

## Summary

This system enables:
- **True Parallelism**: 4+ agents working simultaneously
- **Clear Specialization**: Each agent has distinct focus
- **Autonomous Operation**: Agents work without constant supervision
- **Safe Coordination**: Git + shared TODO prevent conflicts
- **Quality Assurance**: Each agent follows Codex guidelines
- **Transparent Progress**: Logs and git history show everything

Launch your parallel agents and let them deliver quality code faster than any single developer could!

---

**Created by Claude Code** 🤖
**Powered by Codex Guidelines**
**Coordinated by Git & Shared State**

