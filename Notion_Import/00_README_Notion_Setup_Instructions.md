# 📖 HROC Notion Setup Instructions

> **Complete guide to importing and setting up your HROC Notion workspace**

---

## 🎯 What You're Creating

You're about to import 6 comprehensive Notion pages that will serve as your nonprofit's operational hub:

1. **Getting Started After 501(c)(3)** - Post-approval action plan
2. **SPV Management Guide** - Complete SPV operations manual
3. **Compliance Calendar 2025-2026** - All deadlines and requirements
4. **Officer Transition Tasks** - Critical immediate actions
5. **Web Accessibility Checklist** - Maintain an accessible website
6. **IRS Communications Log** - Track all IRS interactions

---

## 📋 Before You Start

**What you need:**
- Notion account (free or paid)
- The markdown files in the `/Notion_Import/` folder
- 15-20 minutes for import and setup

---

## 🚀 Step-by-Step Import Process

### Step 1: Create a New Notion Workspace (or use existing)

1. Open Notion
2. If you don't have an HROC workspace yet:
   - Click "+ New Page" in your sidebar
   - Name it "HROC Operations Hub" or similar
   - Choose "Empty Page"

### Step 2: Import Markdown Files

**For each markdown file:**

1. In your HROC workspace, click "+ New Page"
2. Type `/import` and select "Markdown"
3. Click "Upload file"
4. Select one of the markdown files from `/Notion_Import/`:
   - `01_Getting_Started_After_501c3.md`
   - `02_SPV_Management_Guide.md`
   - `03_Compliance_Calendar_2025_2026.md`
   - `04_Officer_Transition_Critical_Tasks.md`
   - `05_Web_Accessibility_Checklist.md`
   - `06_IRS_Communications_Log.md`
5. Click "Import"
6. Repeat for all 6 files

**Alternative method (bulk import):**
1. Select all 6 markdown files at once
2. Drag and drop them into your Notion workspace
3. Notion will create 6 new pages

---

## 🎨 Step 3: Organize Your Workspace

**Create a parent page structure:**

```
🏛️ HROC Operations Hub
├── 🎯 Getting Started After 501(c)(3)
├── 🚀 SPV Management Guide
├── 📅 Compliance Calendar 2025-2026
├── 🔄 Officer Transition Tasks
├── ♿ Web Accessibility Checklist
└── 📬 IRS Communications Log
```

**How to organize:**
1. Click and drag pages to nest them under your main hub page
2. Rearrange in logical order (suggested order above)
3. Add section dividers if desired

---

## 🤖 Step 4: Using Notion AI to Enhance Pages

Notion AI can help you customize and enhance each page. Here are specific prompts to use:

### For All Pages (General Enhancement)

**Prompt to Notion AI:**
```
Review this page and:
1. Add relevant icons/emojis to headers where missing
2. Create callout boxes for critical warnings and important notes
3. Add toggle blocks for long sections to improve readability
4. Suggest any additional organizational improvements
```

---

### For "Getting Started After 501(c)(3)" Page

**Enhancement Prompt:**
```
Enhance this post-501(c)(3) action plan by:
1. Converting the action items into Notion checkboxes
2. Creating a database view for tracking deadline status
3. Adding date properties to each major task
4. Creating a Kanban board view with columns: Not Started, In Progress, Complete
5. Add visual progress indicators
```

**Database Creation Prompt:**
```
Create a database from the immediate action items with these properties:
- Task name (title)
- Due date (date)
- Status (select: Not Started, In Progress, Complete, Blocked)
- Owner (person)
- Priority (select: 🔴 Urgent, 🟡 Important, 🟢 Low)
- Notes (text)
```

---

### For "SPV Management Guide" Page

**Enhancement Prompt:**
```
Improve this SPV management guide by:
1. Converting all checklists to Notion checkboxes
2. Creating recurring task templates for monthly/quarterly/annual tasks
3. Adding a table view for compliance deadlines
4. Creating linked databases for vehicle logs and maintenance records
5. Add callout boxes for all "Red Flags" and warnings
```

**Tracking Database Prompt:**
```
Create a "SPV Compliance Tracker" database with:
- Task name (title)
- Frequency (select: Monthly, Quarterly, Annual, One-time)
- Due date (date)
- Completed (checkbox)
- Last completed (date)
- Owner (person)
- Category (select: Financial, Legal, Operational, Insurance)
- Notes (text)
```

---

### For "Compliance Calendar" Page

**Enhancement Prompt:**
```
Transform this compliance calendar into an interactive system by:
1. Creating a master compliance database with all deadlines
2. Add calendar view showing all deadlines visually
3. Create filtered views: Federal, State, Organizational
4. Add reminder dates (30 days, 14 days, 7 days before)
5. Create templates for recurring annual tasks
6. Add linked databases for Form 990 prep and WA filings
```

**Calendar Database Prompt:**
```
Create a "Master Compliance Calendar" database with:
- Task/Filing name (title)
- Due date (date)
- Category (select: Federal, State, SPV, Organizational)
- Frequency (select: Monthly, Quarterly, Annual, One-time)
- Status (select: Upcoming, In Progress, Completed, Overdue)
- Owner (person)
- Priority (select: 🔴 Critical, 🟡 Important, 🟢 Standard)
- Reminder dates (multi-select: 30 days, 14 days, 7 days)
- Consequences of missing (text)
- Notes (text)
```

**Additional Views:**
```
Create these database views:
1. Calendar view: Show all deadlines on calendar
2. Timeline view: Visualize upcoming 90 days
3. Kanban view by Status
4. Table view filtered by "Overdue"
5. Table view filtered by "Due in next 30 days"
```

---

### For "Officer Transition Tasks" Page

**Enhancement Prompt:**
```
Convert this officer transition guide into a project tracker by:
1. Creating a project database with phases (Week 1, Week 2, Week 3)
2. Add progress tracking for each phase
3. Create templates for required documents
4. Add checklists for each step
5. Include file upload fields for completed documents
```

**Project Tracker Prompt:**
```
Create an "Officer Transition Project Tracker" database with:
- Task name (title)
- Phase (select: Week 1, Week 2, Week 3)
- Status (select: Not Started, In Progress, Complete)
- Due date (date)
- Owner (person)
- Required documents (files)
- Completion evidence (files)
- Notes (text)
```

---

### For "Web Accessibility Checklist" Page

**Enhancement Prompt:**
```
Make this accessibility checklist interactive by:
1. Converting all checklist items to Notion checkboxes
2. Creating a database for monthly accessibility audits
3. Add sections for tracking issues found and fixes applied
4. Create templates for audit reports
5. Add linked database for accessibility improvements
```

**Audit Tracker Prompt:**
```
Create a "Monthly Accessibility Audit" database with:
- Audit date (date)
- Page/Section audited (title)
- Issues found (number)
- Critical issues (number)
- Lighthouse score (number)
- axe DevTools results (text)
- Status (select: Not Started, In Progress, Complete)
- Issues list (text or relation to Issues database)
```

---

### For "IRS Communications Log" Page

**Enhancement Prompt:**
```
Transform this IRS log into a tracking system by:
1. Creating a communications database with all IRS interactions
2. Add timeline view to see communication history
3. Create filtered views: Pending Response, Completed, Awaiting IRS
4. Add file upload fields for correspondence
5. Create templates for common communication types
```

**Communications Database Prompt:**
```
Create an "IRS Communications Log" database with:
- Communication title (title)
- Date received/sent (date)
- Type (select: Phone call, Letter, Email, Notice, Submission)
- Direction (select: From IRS, To IRS)
- Action required (checkbox)
- Response deadline (date)
- Status (select: ⏳ Pending, 🔄 In Progress, ✅ Complete)
- Documents (files)
- Summary (text)
- Response sent (date)
- Notes (text)
```

---

## 🎯 Step 5: Create a Dashboard (Home Page)

**Dashboard Creation Prompt:**
```
Create a comprehensive HROC Operations Dashboard that includes:
1. Quick links to all 6 main pages
2. Embedded views of:
   - Next 5 compliance deadlines (from Compliance Calendar)
   - Active IRS communications requiring response
   - SPV tasks due this month
   - Officer transition progress percentage
3. Key metrics:
   - Days until next Form 990 deadline
   - SPV compliance status
   - Outstanding action items count
4. Add motivational quote or mission statement
5. Include contact information and key resources
```

---

## 💡 Advanced Setup with Notion AI

### Create Automations

**Ask Notion AI:**
```
Help me set up automations for:
1. Email notifications 7 days before compliance deadlines
2. Slack/email alerts for new IRS communications
3. Recurring task creation for monthly SPV requirements
4. Automatic status updates based on completion dates
```

### Create Templates

**Ask Notion AI:**
```
Create templates for:
1. Monthly board meeting minutes
2. Quarterly SPV reports
3. Annual policy review checklist
4. IRS response letters
5. Grant application tracking
```

### Link Databases

**Ask Notion AI:**
```
Help me create relationships between:
1. Compliance Calendar → IRS Communications Log
2. SPV Management → Officer Transition Tasks
3. All pages → Master Document Repository
```

---

## 📊 Step 6: Customize for Your Workflow

### Add Team Members

1. Click "Share" at top right of any page
2. Invite board members with appropriate permissions:
   - **Full Access:** Board Chair, Treasurer
   - **Can Edit:** All board members
   - **Can Comment:** Advisors, partners
   - **Can View:** Public transparency (if desired)

### Set Up Notifications

1. Go to Settings & Members → My Notifications
2. Enable notifications for:
   - Page updates
   - Comments and mentions
   - Reminders (set for all compliance deadlines)

### Create Workspace Views

**Ask Notion AI:**
```
Create different views optimized for:
1. Board Chair: Governance overview, upcoming meetings, action items
2. Treasurer: Financial deadlines, Form 990 prep, budget tracking
3. SPV Manager: Vehicle operations, maintenance, compliance
4. All Board Members: Dashboard with key metrics and deadlines
```

---

## 🎨 Visual Enhancements

### Add Cover Images

1. Click "Add cover" at top of each page
2. Use relevant images:
   - **Getting Started:** Celebration or checkmark image
   - **SPV Guide:** Vehicle or road image
   - **Compliance Calendar:** Calendar or planner image
   - **Officer Transition:** Handshake or transition image
   - **Accessibility:** Universal access symbol
   - **IRS Log:** Government building or filing cabinet

### Add Icons

Each page already has emoji icons in headers, but you can:
1. Hover over page title
2. Click to change icon
3. Choose from Notion's icon library or upload custom

### Use Callout Blocks

**Convert important sections to callouts:**
1. Select text
2. Type `/callout`
3. Choose background color:
   - 🔴 Red: Critical warnings
   - 🟡 Yellow: Important notes
   - 🟢 Green: Success criteria
   - 🔵 Blue: Information

---

## ✅ Final Checklist

After import and AI enhancement, verify:

- [ ] All 6 pages imported successfully
- [ ] Pages organized in logical hierarchy
- [ ] Databases created for tracking
- [ ] Calendar views showing deadlines
- [ ] Team members invited with appropriate permissions
- [ ] Notifications enabled for critical deadlines
- [ ] Dashboard created with embedded views
- [ ] Templates created for recurring tasks
- [ ] Cover images and icons added
- [ ] Mobile app installed (optional but recommended)

---

## 🚀 Next Steps

1. **Populate with your specific data:**
   - Add actual dates to compliance calendar
   - Fill in IRS communications log with past interactions
   - Update SPV checklists with your specific tasks

2. **Establish routines:**
   - Weekly: Review upcoming week's tasks
   - Monthly: Run accessibility audit, update IRS log
   - Quarterly: SPV board reports, compliance review
   - Annually: Policy reviews, renewal filings

3. **Train your team:**
   - Schedule orientation session for board members
   - Create video walkthrough of key pages
   - Assign page owners for each section

4. **Iterate and improve:**
   - Use Notion AI to continuously enhance pages
   - Add new databases as needs arise
   - Request feedback from team members

---

## 🆘 Troubleshooting

### Import Issues

**Problem:** Markdown formatting looks wrong
**Solution:**
- Re-import the file
- Use "Plain text" import instead of Markdown
- Manually fix formatting using Notion editor

**Problem:** Tables not displaying correctly
**Solution:**
- Convert tables to Notion databases for better functionality
- Ask Notion AI: "Convert this table to a database"

### AI Enhancement Issues

**Problem:** Notion AI suggestions don't match your needs
**Solution:**
- Be more specific in your prompts
- Break complex requests into smaller steps
- Use the exact prompts provided above

---

## 📞 Need Help?

**Notion Resources:**
- [Notion Help Center](https://www.notion.so/help)
- [Notion Community](https://www.notion.so/community)
- [Notion Templates Gallery](https://www.notion.so/templates)

**HROC-Specific Questions:**
- Review the original markdown files for full context
- Consult with board members on customization needs
- Iterate based on actual usage patterns

---

## 💡 Pro Tips

1. **Use Notion Web Clipper** to save relevant nonprofit resources directly to your workspace
2. **Enable offline mode** in Notion mobile app for access anywhere
3. **Create filtered views** for each board member showing only their responsibilities
4. **Use @mentions** to assign tasks and get notifications
5. **Set up Slack integration** to get notifications in your communication channel
6. **Use relations** to connect related items across databases
7. **Create a "Quick Add" database** for capturing tasks on the go
8. **Export pages to PDF** for board packets or compliance documentation

---

## 🎯 Success Metrics

Your Notion workspace is successful when:

✅ All board members can find what they need in <2 minutes
✅ No compliance deadlines are missed
✅ IRS communications are tracked and responded to on time
✅ SPV management is documented and transparent
✅ Officer transition happens smoothly with clear handoff
✅ Website accessibility is monitored monthly
✅ Team actually uses the system (not just set it up)

---

**Congratulations! You've created a professional nonprofit operations hub!**

Questions? Suggestions? Contact your board chair or technical lead.

**Last Updated:** December 2025

