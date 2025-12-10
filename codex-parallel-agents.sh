#!/bin/bash

################################################################################
# CODEX PARALLEL AGENTS - Multi-Agent Codebase Coordination Script
#
# This script launches multiple Codex agents in parallel to work on different
# aspects of your codebase. Each agent operates autonomously but coordinates
# through shared git state, TODO tracking, and parallel execution.
#
# Usage: ./codex-parallel-agents.sh [task-name] [num-agents] [instructions-file]
# Example: ./codex-parallel-agents.sh "website-refactor" 4 tasks.md
################################################################################

set -e

# Configuration
TASK_NAME="${1:-codex-task}"
NUM_AGENTS="${2:-4}"
INSTRUCTIONS_FILE="${3:-.codex-instructions}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
WORK_DIR="${REPO_ROOT}/.codex-work"
AGENT_LOG_DIR="${WORK_DIR}/agent-logs"
AGENT_TASKS_DIR="${WORK_DIR}/agent-tasks"
RESULT_FILE="${WORK_DIR}/results-${TASK_NAME}.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║           CODEX PARALLEL AGENTS - Task Coordinator             ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Initialize working directories
mkdir -p "$AGENT_LOG_DIR" "$AGENT_TASKS_DIR"

# Create the Codex system prompt
cat > "${WORK_DIR}/codex-system-prompt.txt" << 'SYSTEMPROMPT'
You are Codex, based on GPT-5. You are running as a coding agent in the Codex CLI on a user's computer.

# Core Principles

## General
- When searching for text or files, prefer using `rg` or `rg --files` because it's much faster than alternatives.
- If a tool exists for an action, prefer tools over shell commands (e.g., read_file over cat).
- Strictly avoid raw cmd/terminal when a dedicated tool exists.
- Default to solver tools: `git`, `rg` (search), `read_file`, `list_dir`, `glob_file_search`, `apply_patch`, `todo_write`.
- Use `cmd`/`run_terminal_cmd` only when no listed tool can perform the action.
- When multiple tool calls can be parallelized, do so instead of sequential calls.
- Code chunks may include inline line numbers in the form "Lxxx:LINE_CONTENT" - treat the "Lxxx:" prefix as metadata only.
- Default expectation: deliver working code, not just a plan.

## Autonomy and Persistence
- You are an autonomous senior engineer: once you receive a direction, proactively gather context, plan, implement, test, and refine without waiting for additional prompts.
- Persist until the task is fully handled end-to-end within the current turn whenever feasible.
- Do not stop at analysis or partial fixes; carry changes through implementation, verification, and clear explanation of outcomes.
- Bias to action: default to implementing with reasonable assumptions; avoid excessive clarifications unless truly blocked.
- Avoid excessive looping; if you find yourself re-reading the same files without progress, stop and summarize.

## Code Implementation
- Act as a discerning engineer: optimize for correctness, clarity, and reliability over speed.
- Avoid risky shortcuts, speculative changes, and messy hacks.
- Conform to codebase conventions: follow existing patterns, naming, formatting, and localization.
- Comprehensiveness: ensure you cover all relevant surfaces so behavior stays consistent.
- Behavior-safe defaults: preserve intended behavior and UX; gate intentional changes.
- Tight error handling: no broad catches or silent defaults; propagate errors explicitly.
- No silent failures: do not early-return without logging/notification consistent with repo patterns.
- Efficient, coherent edits: read enough context before changing files and batch logical edits together.
- Keep type safety: changes should pass build and type-check.
- Reuse: search first for prior art before adding new helpers or logic.
- Bias to action: default to implementing; every rollout should conclude with a concrete edit.

## Editing Constraints
- Default to ASCII when editing files.
- Add succinct code comments only when code is not self-explanatory.
- Use apply_patch for single file edits when possible.
- You may be in a dirty git worktree; never revert changes you didn't make unless explicitly requested.
- NEVER use destructive commands like `git reset --hard` unless specifically requested.

## Exploration and Reading Files
- Think first: decide ALL files/resources you need before making tool calls.
- Batch everything: if you need multiple files, read them together.
- Use parallelization for independent operations.
- Only make sequential calls if you truly cannot know the next file without seeing results first.
- Always maximize parallelism.

## Final Deliverables
- Lead with a quick explanation of changes.
- Give details on where and why changes were made.
- Suggest logical next steps briefly; add verify steps if you couldn't do something.
- Use inline code for file paths.
- Be concise and friendly.
SYSTEMPROMPT

echo -e "${GREEN}✓ Codex system prompt initialized${NC}"
echo ""

# Create task distribution strategy
echo -e "${YELLOW}📋 Task Distribution Strategy${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Agents will be assigned tasks based on their specialization:"
echo ""
echo "  Agent 1: Code Analysis & Architecture"
echo "    • Analyze codebase structure"
echo "    • Identify patterns and conventions"
echo "    • Report on architecture and dependencies"
echo ""
echo "  Agent 2: Bug Fixes & Issues"
echo "    • Search for and identify bugs"
echo "    • Test edge cases"
echo "    • Create fixes for identified issues"
echo ""
echo "  Agent 3: Features & Enhancements"
echo "    • Implement new features"
echo "    • Enhance existing functionality"
echo "    • Add tests for new features"
echo ""
echo "  Agent 4: Quality & Optimization"
echo "    • Optimize performance"
echo "    • Improve code quality"
echo "    • Ensure best practices"
echo ""

# Create individual agent instruction files
for i in $(seq 1 $NUM_AGENTS); do
  AGENT_NUM=$i
  AGENT_NAME="Agent-${i}"
  AGENT_TASK_FILE="${AGENT_TASKS_DIR}/agent-${i}-task.md"

  # Assign tasks based on agent number
  case $i in
    1)
      SPECIALIZATION="Code Analysis & Architecture"
      FOCUS="Analyze the codebase structure, identify patterns, conventions, and architectural decisions. Report on code organization, dependencies, and potential improvements."
      ;;
    2)
      SPECIALIZATION="Bug Fixes & Testing"
      FOCUS="Search for potential bugs, test edge cases, identify issues in the codebase, and create fixes. Focus on correctness and robustness."
      ;;
    3)
      SPECIALIZATION="Features & Implementation"
      FOCUS="Implement new features requested, enhance existing functionality, and add comprehensive tests for new code."
      ;;
    4)
      SPECIALIZATION="Quality & Optimization"
      FOCUS="Optimize code performance, improve quality metrics, refactor for maintainability, and ensure adherence to best practices."
      ;;
    *)
      SPECIALIZATION="General Development"
      FOCUS="General development tasks as needed."
      ;;
  esac

  cat > "$AGENT_TASK_FILE" << AGENTINSTRUCTIONS
# ${AGENT_NAME} Task Assignment

**Specialization:** ${SPECIALIZATION}

**Focus Area:** ${FOCUS}

**Task Identifier:** ${TASK_NAME}

## Your Mission

You are ${AGENT_NAME}, operating as a specialized Codex agent in a parallel multi-agent system.

Your focus is: **${FOCUS}**

## Operating Principles

1. **Autonomy**: Work independently and make decisions proactively.
2. **Coordination**: Check the shared TODO list in \`.codex-work/shared-todos.md\` for coordination.
3. **Parallelization**: Your work runs in parallel with other agents - avoid conflicts by communicating via the shared TODO.
4. **Quality**: Deliver working, tested code following the Codex guidelines.
5. **Progress Tracking**: Log your progress in \`.codex-work/agent-logs/agent-${i}.log\`.

## Starting Checklist

- [ ] Read the Codex system prompt in \`.codex-work/codex-system-prompt.txt\`
- [ ] Review the shared task file: \`.codex-work/shared-task.md\`
- [ ] Check the shared TODO: \`.codex-work/shared-todos.md\`
- [ ] Review any blocking issues or dependencies
- [ ] Begin work on your assigned focus area

## Communication

Log progress and blockers to: \`.codex-work/agent-logs/agent-${i}.log\`

If you encounter:
- **Blockers**: Document in the shared TODO with ⚠️ tag
- **Discoveries**: Share findings in your log for other agents
- **Progress**: Log completed tasks and what comes next

## Success Criteria

- [ ] Your focus area has been thoroughly addressed
- [ ] All code changes pass tests
- [ ] Code follows codebase conventions
- [ ] Changes are well-documented
- [ ] No conflicts with other agents' work

Good luck, ${AGENT_NAME}! 🚀

AGENTINSTRUCTIONS

  echo -e "${GREEN}✓ Created task file for ${AGENT_NAME}${NC}"
done

# Create shared task description
cat > "${WORK_DIR}/shared-task.md" << SHAREDTASK
# Parallel Codex Agents - Shared Task: ${TASK_NAME}

**Initiated:** $(date)
**Number of Agents:** ${NUM_AGENTS}
**Repository:** ${REPO_ROOT}

## Task Overview

This is a coordinated, parallel code task involving ${NUM_AGENTS} specialized agents working on the same codebase.

### Agent Assignments

- **Agent 1**: Code Analysis & Architecture
- **Agent 2**: Bug Fixes & Testing
- **Agent 3**: Features & Implementation
- **Agent 4**: Quality & Optimization

(Additional agents may take on supporting roles or specialized tasks)

## Coordination Guidelines

1. **Parallel Execution**: All agents run simultaneously to maximize efficiency.
2. **Shared State**: Git is the source of truth; commit frequently and push regularly.
3. **TODO Coordination**: Use the shared TODO list to track work and avoid conflicts.
4. **Communication**: Log progress and blockers to the agent-specific log files.
5. **Conflict Resolution**: If agents touch the same file, use git to merge; discuss in logs if needed.

## Key Files

- **System Prompt**: \`.codex-work/codex-system-prompt.txt\` - Codex operating guidelines
- **Shared TODO**: \`.codex-work/shared-todos.md\` - Coordination and task tracking
- **Agent Logs**: \`.codex-work/agent-logs/agent-N.log\` - Individual agent progress
- **Results**: \`.codex-work/results-${TASK_NAME}.txt\` - Final aggregated results

## Starting Work

Each agent should:

1. Read their individual task file in \`.codex-work/agent-tasks/\`
2. Review the Codex system prompt
3. Check the shared TODO list
4. Begin work on their focus area
5. Log progress and findings
6. Commit changes regularly
7. Update the shared TODO as work progresses

## Expected Outcomes

- [ ] Agent 1 completes codebase analysis and architecture report
- [ ] Agent 2 identifies and fixes bugs
- [ ] Agent 3 implements requested features with tests
- [ ] Agent 4 optimizes and improves code quality
- [ ] All agents commit their work to git
- [ ] Final results aggregated in results file

## Notes

- All agents have access to the full Codex system prompt
- Each agent operates autonomously but coordinates through git and shared TODO
- Code quality and correctness are paramount
- Commit messages should be clear and reference agent number and focus area

Good luck, agents! 🤖

SHAREDTASK

# Create shared TODO list
cat > "${WORK_DIR}/shared-todos.md" << SHAREDTODO
# Shared TODO - Codex Parallel Agents

**Task:** ${TASK_NAME}
**Created:** $(date)
**Status:** In Progress

## Coordination Notes

- All agents should review this file before starting work
- Update this file as you complete tasks or discover blockers
- Use ✅ for completed items, ⏳ for in-progress, ⚠️ for blockers
- Prefix your updates with your agent number (e.g., "Agent 1: ...")

## Agent 1: Code Analysis & Architecture

- ⏳ Analyze codebase structure and organization
- ⏳ Map out key dependencies and module relationships
- ⏳ Identify architectural patterns and conventions
- ⏳ Document findings in analysis report
- ⏳ Highlight potential improvements or pain points

## Agent 2: Bug Fixes & Testing

- ⏳ Search codebase for potential bugs or issues
- ⏳ Test edge cases and error conditions
- ⏳ Create fixes for identified problems
- ⏳ Add tests to prevent regression
- ⏳ Verify all fixes pass tests

## Agent 3: Features & Implementation

- ⏳ Review requested features from task file
- ⏳ Implement new functionality
- ⏳ Write comprehensive tests for new features
- ⏳ Ensure features integrate well with existing code
- ⏳ Document new features

## Agent 4: Quality & Optimization

- ⏳ Performance analysis and optimization
- ⏳ Code quality improvements
- ⏳ Refactoring for maintainability
- ⏳ Best practices enforcement
- ⏳ Documentation and comments

## Cross-Agent Coordination

- 🔄 Monitor for file conflicts (notify other agents via logs)
- 🔄 Share findings that might affect other agents' work
- 🔄 Coordinate if multiple agents need to touch the same file
- 🔄 Final sync and integration testing

## Blockers & Issues

(To be updated as agents discover issues)

## Completed Items

(To be updated as agents complete tasks)

---
Last Updated: $(date)
SHAREDTODO

echo -e "${GREEN}✓ Created shared coordination files${NC}"
echo ""

# Create agent launcher script
cat > "${WORK_DIR}/launch-agents.sh" << 'LAUNCHER'
#!/bin/bash

# This script launches the individual agents
# In a real implementation, this would spawn Claude Code instances
# For now, it outputs the commands needed to launch each agent

NUM_AGENTS=${1:-4}
WORK_DIR="$(dirname "$(realpath "$0")")"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         CODEX PARALLEL AGENTS - Agent Launch Script            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "To launch agents in parallel, run these commands in separate terminals:"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

for i in $(seq 1 $NUM_AGENTS); do
  echo "Terminal $i - Agent $i:"
  echo ""
  echo "  AGENT_NUM=$i WORK_DIR=$WORK_DIR codex --task agent-${i}"
  echo ""
  echo "  OR: export AGENT_NUM=$i && export WORK_DIR=$WORK_DIR && codex run-agent"
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
done

echo ""
echo "Each agent will:"
echo "  1. Load their task file from .codex-work/agent-tasks/"
echo "  2. Review the shared TODO in .codex-work/shared-todos.md"
echo "  3. Read the Codex system prompt"
echo "  4. Work autonomously on their assigned focus area"
echo "  5. Commit changes to git"
echo "  6. Log progress to their individual log file"
echo ""
echo "Monitor progress:"
echo "  - Watch agent logs: tail -f .codex-work/agent-logs/*.log"
echo "  - Check shared TODO: cat .codex-work/shared-todos.md"
echo "  - Monitor git: git log --oneline -20"
echo ""
LAUNCHER

chmod +x "${WORK_DIR}/launch-agents.sh"

echo ""
echo "📊 Parallel Execution Plan Created"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Generate final handoff document
cat > "${WORK_DIR}/HANDOFF.md" << 'HANDOFF'
# 🤖 Codex Parallel Agents - Handoff Document

## Setup Complete ✅

Your parallel multi-agent Codex system is ready to launch.

### What Was Created

1. **System Files**
   - `codex-system-prompt.txt` - Unified Codex operating guidelines
   - `shared-task.md` - Shared task definition and coordination strategy
   - `shared-todos.md` - Coordination TODO list for all agents
   - `HANDOFF.md` - This handoff document
   - `launch-agents.sh` - Agent launch script with instructions

2. **Agent Task Files** (in `agent-tasks/`)
   - `agent-1-task.md` - Code Analysis & Architecture
   - `agent-2-task.md` - Bug Fixes & Testing
   - `agent-3-task.md` - Features & Implementation
   - `agent-4-task.md` - Quality & Optimization

3. **Agent Logging** (in `agent-logs/`)
   - Individual log files for each agent
   - Progress tracking and blocker reporting
   - Cross-agent communication channel

## How to Launch

### Option 1: Manual Launch (Recommended for Testing)

Open 4 separate terminal windows and run:

```bash
# Terminal 1
export AGENT_NUM=1 && export WORK_DIR=.codex-work && \
  cat .codex-work/agent-1-task.md

# Terminal 2
export AGENT_NUM=2 && export WORK_DIR=.codex-work && \
  cat .codex-work/agent-2-task.md

# Terminal 3
export AGENT_NUM=3 && export WORK_DIR=.codex-work && \
  cat .codex-work/agent-3-task.md

# Terminal 4
export AGENT_NUM=4 && export WORK_DIR=.codex-work && \
  cat .codex-work/agent-4-task.md
```

Then provide each task to Claude Code in its respective terminal.

### Option 2: Automated Launch Script

```bash
.codex-work/launch-agents.sh
```

This will output the exact commands to launch each agent.

### Option 3: Claude Code Integration

If using Claude Code with agent support:

```bash
codex agents launch --num-agents 4 --work-dir .codex-work
```

## Agent Specializations

| Agent | Specialization | Focus |
|-------|----------------|-------|
| Agent 1 | Code Analysis & Architecture | Structure, patterns, dependencies |
| Agent 2 | Bug Fixes & Testing | Issues, edge cases, testing |
| Agent 3 | Features & Implementation | New features, enhancements |
| Agent 4 | Quality & Optimization | Performance, quality, refactoring |

## Coordination Strategy

### Parallel Execution
- All 4 agents run simultaneously
- Each operates on their assigned focus area
- Work is coordinated through git and shared TODO

### Git as Source of Truth
- Agents commit frequently to capture progress
- Main branch is always stable
- Use feature branches if large changes planned

### Shared TODO List
- All agents read `shared-todos.md` before starting
- Update with progress, blockers, discoveries
- Use prefixes: ✅ (done), ⏳ (in-progress), ⚠️ (blocker)
- This is the primary coordination mechanism

### Agent Logs
- Each agent logs to `.codex-work/agent-logs/agent-N.log`
- Logs contain progress, decisions, and findings
- Other agents can review logs to understand impact on their work

## Monitoring Progress

### Watch Real-Time Progress
```bash
# Monitor all agent logs
tail -f .codex-work/agent-logs/*.log

# Watch git commits
git log --oneline -20 --graph

# Check shared TODO
watch -n 5 'cat .codex-work/shared-todos.md'
```

### Review Individual Agent Output
```bash
# Agent 1 analysis
cat .codex-work/agent-logs/agent-1.log

# Agent 2 bug findings
cat .codex-work/agent-logs/agent-2.log

# Agent 3 features
cat .codex-work/agent-logs/agent-3.log

# Agent 4 optimizations
cat .codex-work/agent-logs/agent-4.log
```

## Expected Workflow

1. **Initialization Phase**
   - Each agent reads their task file
   - Reviews system prompt and shared TODO
   - Identifies their focus area

2. **Execution Phase**
   - Agents work autonomously on their areas
   - Make frequent commits to git
   - Log progress to individual log files
   - Update shared TODO with discoveries/blockers

3. **Integration Phase**
   - Agents check for conflicts
   - Collaborate via logs if needed
   - Resolve any merge conflicts
   - Ensure all work integrates smoothly

4. **Completion Phase**
   - All agents commit final changes
   - Update shared TODO with completion status
   - Generate final results report
   - Archive working directory for reference

## System Prompt Access

All agents have access to the unified Codex system prompt which emphasizes:

- **Tool Preference**: Use specialized tools over shell commands
- **Autonomy**: Proactive planning and implementation
- **Parallelization**: Independent execution with coordination
- **Quality**: Correctness, clarity, and reliability
- **Efficiency**: Batch edits, avoid repetition
- **Git Safety**: No destructive operations

## Results & Handoff

Upon completion:

1. Check `.codex-work/results-{task-name}.txt` for aggregated results
2. Review git log for all commits by agents
3. Archive `.codex-work/` directory for reference
4. Integrate any required changes to main
5. Create final commit summarizing parallel agent work

## Support & Troubleshooting

### If Agents Conflict on the Same File
- Agents will detect this via git and communicate via logs
- Resolve by merging changes carefully
- Document resolution in shared TODO

### If Agent Gets Blocked
- Mark as ⚠️ in shared TODO with specific reason
- Log the blocker in their log file
- Other agents can review and offer solutions

### If Agent Needs Another Agent's Output
- Leave a note in shared TODO with @agent-X mention
- Agent will see it and provide what's needed
- Document the dependency

## Next Steps

1. Run `./codex-work/launch-agents.sh` to see launch commands
2. Open 4 terminals (one per agent)
3. Run the appropriate command in each terminal
4. Provide the task instructions to each Claude Code instance
5. Monitor progress via logs and git
6. Let agents work autonomously - they're designed to handle conflicts
7. Upon completion, review results and integrate changes

---

**Remember:** These agents are autonomous, operating in parallel, and coordinating through git and shared files. Trust the process - they follow the Codex guidelines strictly and will deliver quality work.

Good luck, and happy parallel coding! 🚀

HANDOFF

echo "✅ **Setup Complete!**"
echo ""
echo "Files created in \`.codex-work/\`:"
echo "  - codex-system-prompt.txt (Unified guidelines)"
echo "  - shared-task.md (Task definition)"
echo "  - shared-todos.md (Coordination)"
echo "  - HANDOFF.md (This guide)"
echo "  - agent-tasks/ (4 specialized task files)"
echo "  - agent-logs/ (Progress tracking)"
echo "  - launch-agents.sh (Launch instructions)"
echo ""
echo -e "${GREEN}To view launch instructions:${NC}"
echo "  ./.codex-work/launch-agents.sh"
echo ""
echo -e "${GREEN}To monitor progress:${NC}"
echo "  tail -f .codex-work/agent-logs/*.log"
echo ""
echo -e "${GREEN}To check coordination:${NC}"
echo "  cat .codex-work/shared-todos.md"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🤖 Your parallel agent system is ready!"
echo "Each agent will operate autonomously while coordinating through git."
echo ""
