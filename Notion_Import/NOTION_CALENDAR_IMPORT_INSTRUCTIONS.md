# How to Import HROC Compliance Calendar into Notion

**Quick guide for importing the comprehensive compliance calendar into your Notion workspace**

---

## Files You Have

1. **HROC_Compliance_Calendar_2026_Detailed.md** - Complete calendar with full documentation
2. **HROC_Compliance_Calendar_2026_Import.csv** - Structured data for database import
3. **HROC_Compliance_Calendar_2026_Quick_Reference.md** - One-page printable summary
4. **This file** - Import instructions

---

## Method 1: CSV Database Import (RECOMMENDED)

### Step 1: Create Notion Database

1. In Notion, create a new page: "HROC Compliance Calendar 2026"
2. Type `/database` and select "Table - Inline"
3. Name it "Compliance Calendar"

### Step 2: Import CSV

1. Click the `•••` menu in the top-right of the database
2. Select "Merge with CSV"
3. Upload `HROC_Compliance_Calendar_2026_Import.csv`
4. Map columns:
   - Task Name → Title (or Name)
   - Due Date → Date
   - Category → Select
   - Priority → Select
   - Responsible Party → Person (or Text)
   - Reminder 30 Days → Date
   - Reminder 14 Days → Date
   - Reminder 7 Days → Date
   - Estimated Cost → Text (or Number)
   - Required Documents → Text
   - Notes → Text

5. Click "Import"

### Step 3: Configure Database Views

**Calendar View:**
1. Click "+ Add a view"
2. Select "Calendar"
3. Set "Due Date" as the date property
4. Color code by "Category" or "Priority"

**Timeline View:**
1. Click "+ Add a view"
2. Select "Timeline"
3. Set "Due Date" as the date property
4. Group by "Category"

**Kanban Board (by Status):**
1. Add a new property: "Status" (Select type)
2. Options: Not Started, In Progress, Complete
3. Click "+ Add a view"
4. Select "Board"
5. Group by "Status"

**Filter Views:**
Create filtered views for:
- "Critical Deadlines" (Priority = Critical)
- "Federal Filings" (Category = Federal)
- "State Filings" (Category = State)
- "This Month" (Due Date is within next 30 days)

### Step 4: Set Up Reminders

**Option A - Manual (Free Notion):**
1. For each critical task, click "Remind"
2. Set custom reminder dates using the "Reminder 30/14/7 Days" dates

**Option B - Automated (Notion Premium):**
1. Create button automation: "Set Reminders"
2. Formula: When "Due Date" exists, auto-create reminders at Reminder 30/14/7 Days
3. Click button to set all reminders at once

---

## Method 2: Markdown Page Import

### Step 1: Import Detailed Guide

1. In Notion, create a new page
2. Click `•••` menu → "Import"
3. Select "Markdown"
4. Upload `HROC_Compliance_Calendar_2026_Detailed.md`
5. Notion will create a formatted page with all content

### Step 2: Import Quick Reference

1. Create another new page: "Quick Reference"
2. Import `HROC_Compliance_Calendar_2026_Quick_Reference.md`
3. Pin this page for easy access

### Step 3: Link Pages

1. In your main "HROC Operations Hub" page
2. Add link to "Compliance Calendar 2026 (Detailed)"
3. Add link to "Compliance Database" (from Method 1)
4. Add link to "Quick Reference"

---

## Method 3: Manual Database Creation (Most Control)

### Step 1: Create Database Structure

Create a new database with these properties:

| Property Name | Type | Options/Details |
|--------------|------|-----------------|
| **Task Name** | Title | Default title field |
| **Due Date** | Date | Include time if needed |
| **Category** | Select | Federal, State, Governance, Financial, SPV |
| **Priority** | Select | Critical, High, Medium, Low |
| **Responsible** | Person | Assign to Notion users (or use Text type) |
| **Status** | Select | Not Started, In Progress, Complete |
| **Reminder 1** | Date | 30 days before |
| **Reminder 2** | Date | 14 days before |
| **Reminder 3** | Date | 7 days before |
| **Est. Cost** | Text | Dollar range (or Number for exact) |
| **Documents** | Text | Required documents list |
| **Notes** | Text | Additional details |
| **Recurring** | Checkbox | Is this a recurring task? |
| **Frequency** | Select | Monthly, Quarterly, Annual, One-time |

### Step 2: Color Code Categories

Set colors for Select property "Category":
- Federal: Red
- State: Orange
- Governance: Purple
- Financial: Green
- SPV: Blue

### Step 3: Color Code Priorities

Set colors for Select property "Priority":
- Critical: Red
- High: Orange
- Medium: Yellow
- Low: Gray

### Step 4: Add Data

Manually add tasks from the CSV file or copy-paste from the detailed guide.

---

## Recommended Notion Setup

### Page Structure

```
📁 HROC Operations Hub
├── 📅 Compliance Calendar 2026 (Database)
│   ├── 🗓️ Calendar View
│   ├── 📊 Timeline View
│   ├── 📋 Kanban (by Status)
│   ├── 🔴 Critical Deadlines (Filter)
│   ├── 🇺🇸 Federal Filings (Filter)
│   ├── 🏛️ State Filings (Filter)
│   └── 📆 This Month (Filter)
├── 📄 Compliance Calendar - Detailed Guide (Page)
├── 📄 Compliance Calendar - Quick Reference (Page)
└── 📁 Supporting Documents
    ├── Form 990 Templates
    ├── Annual Report Templates
    └── Policy Review Checklists
```

### Dashboard View

Create a dashboard page with:

1. **Upcoming Deadlines** (Linked Database)
   - Filter: Due Date is within next 30 days
   - Sort: By Due Date (ascending)
   - View: Table or Calendar

2. **Critical Tasks** (Linked Database)
   - Filter: Priority = Critical
   - View: List or Table

3. **This Week** (Linked Database)
   - Filter: Due Date is within next 7 days
   - View: Table

4. **Overdue Tasks** (Linked Database)
   - Filter: Due Date is before today AND Status ≠ Complete
   - View: Table with red background

---

## Setting Up Automated Reminders (Notion Premium Feature)

If you have Notion Premium or Business:

### Database Automation Example

**Trigger:** When "Due Date" is 30 days away
**Action:** Send notification to "Responsible" person

**How to Set Up:**
1. In database, click "•••" → "Automations"
2. Create new automation
3. Trigger: "Edited time" or use formula for date-based triggers
4. Action: "Send notification"

**Repeat for:**
- 14 days before
- 7 days before
- Day of deadline

---

## Syncing with External Calendars

### Export to Google Calendar

**Option 1 - Manual:**
1. Export database as CSV
2. Import CSV into Google Calendar
3. Map fields: Task Name → Event, Due Date → Date

**Option 2 - Integration (Notion Premium):**
1. Use Notion API + Zapier/Make
2. Auto-sync new database entries to Google Calendar
3. Set up recurring events in Google Calendar

### Export to Outlook

1. Export database as CSV
2. Import CSV into Outlook Calendar
3. Set up recurring tasks in Outlook

---

## Best Practices

### 1. Weekly Review
- Every Monday, review "This Week" view
- Update task statuses
- Check overdue items

### 2. Monthly Board Review
- Add "Compliance Calendar Review" to every board meeting agenda
- Show "This Month" view
- Report on completed vs. pending tasks

### 3. Update Immediately
- Mark tasks complete as soon as finished
- Add notes with confirmation numbers, filing receipts
- Attach copies of filed documents

### 4. Assign Ownership
- Use "Responsible" field to assign every task
- Set up Notion notifications for assigned users
- Review assignments quarterly

### 5. Template Attachments
- Attach relevant templates to each task
- Link to Form 990 prep checklist
- Link to Annual Report instructions

---

## Troubleshooting

**Issue:** CSV won't import
- **Solution:** Open CSV in text editor, ensure UTF-8 encoding, check for special characters

**Issue:** Dates not parsing correctly
- **Solution:** Ensure dates in CSV are formatted as YYYY-MM-DD

**Issue:** Can't set reminders
- **Solution:** Notion free version has limited reminder features; use Google Calendar integration

**Issue:** Too many tasks, overwhelming
- **Solution:** Use filtered views (Critical Only, This Month, My Tasks)

---

## Mobile Access

**Notion Mobile App:**
1. Install Notion app (iOS/Android)
2. Access compliance calendar on mobile
3. Set up push notifications for reminders
4. Check off tasks on the go

**Calendar Widget:**
1. Add Notion calendar widget to phone home screen
2. Quick view of upcoming deadlines

---

## Customization Ideas

### Add These Optional Properties:

**Completion Date** (Date)
- Track when task was actually completed
- Compare to due date for performance metrics

**Link to Documents** (URL)
- Direct link to filed Form 990
- Link to confirmation emails
- Link to filed Annual Reports

**Last Year's Date** (Date)
- Track when you filed last year
- Use for year-over-year comparison

**Time Estimate** (Number)
- Estimate hours needed for each task
- Use for workload planning

**Dependencies** (Relation)
- Link tasks that depend on other tasks
- Example: "File Form 990" depends on "Board Approves Form 990"

---

## Templates to Create in Notion

### 1. Task Template - Federal Filing

```
Task Name: [Filing Name]
Due Date: [Date]
Category: Federal
Priority: Critical
Responsible: Treasurer
Status: Not Started

Pre-Filing Checklist:
- [ ] Gather all required documents
- [ ] Review with Finance Committee
- [ ] Board approval obtained
- [ ] Test e-filing credentials

Post-Filing Checklist:
- [ ] Save confirmation
- [ ] Post to website
- [ ] Notify board
- [ ] File in permanent records
```

### 2. Task Template - State Filing

```
Task Name: [Filing Name]
Due Date: [Date]
Category: State
Priority: Critical
Responsible: Secretary
Status: Not Started

Required Information:
- [ ] Registered agent current?
- [ ] Board roster updated?
- [ ] Address current?
- [ ] Fee payment ready?

Filing Steps:
1. Log into ccfs.sos.wa.gov
2. Search for entity
3. Complete online form
4. Pay fee
5. Download confirmation
```

### 3. Task Template - Board Meeting

```
Task Name: [Month] Board Meeting
Due Date: [Date]
Category: Governance
Priority: High
Responsible: Board Chair
Status: Not Started

Agenda Items:
- [ ] Call to order & quorum
- [ ] Approve prior minutes
- [ ] Financial report
- [ ] [Month-specific items]
- [ ] New business
- [ ] Adjourn

Materials Needed:
- Prior meeting minutes
- Financial statements
- Committee reports
```

---

## Support Resources

**Notion Help Center:**
- Database basics: https://www.notion.so/help/intro-to-databases
- Import & export: https://www.notion.so/help/import-and-export

**HROC Compliance Resources:**
- See "Compliance Calendar - Detailed Guide" for full requirements
- See "Quick Reference" for monthly checklists
- Contact HROC Treasurer or Board Chair with questions

---

**Created:** December 8, 2025
**For:** HROC Compliance Calendar 2026
**Questions?** Review the detailed guide or contact HROC Board Chair
