# 🤖 HROC Notion AI Setup Guide
## Complete Step-by-Step Instructions

> **Follow these prompts IN ORDER for the best results. Each prompt is optimized for Notion AI's capabilities.**

---

## 📋 Before You Start

1. Import all 6 markdown files into Notion (drag & drop them all at once)
2. Create a parent page called "🏛️ HROC Operations Hub"
3. Nest all 6 imported pages under this parent page
4. Open Notion AI (Space bar or click AI button)

**Estimated Time:** 30-45 minutes for complete setup

---

## 🎯 STEP 1: Create Master Dashboard

**What:** Your main operations hub homepage

**Where:** Create a new page called "📊 HROC Dashboard"

**Prompt to Notion AI:**
```
Create a comprehensive nonprofit operations dashboard for Healing Roots Outreach Collective with these sections:

1. HEADER: Welcome banner with:
   - Organization name and mission statement
   - 501(c)(3) status and EIN: 39-3295288
   - Quick stats: 5 board members, King & Pierce Counties service area

2. QUICK LINKS section with buttons to:
   - Getting Started After 501(c)(3)
   - SPV Management Guide
   - Compliance Calendar
   - Officer Transition Tasks
   - Web Accessibility Checklist
   - IRS Communications Log

3. URGENT ACTIONS callout box (red background) showing:
   - Officer transition (board vote needed)
   - SPV BOI Report due Oct 28, 2025
   - WA Annual Report filing

4. UPCOMING DEADLINES section (next 30 days)

5. KEY METRICS section showing:
   - Days until Form 990 deadline (May 15, 2026)
   - Compliance score: 72%
   - Open action items count
   - Next board meeting date

6. RECENT ACTIVITY section (placeholder for updates)

7. RESOURCES footer with:
   - IRS Customer Service: 877-829-5500
   - WA Secretary of State: 1-800-332-4483
   - Links to key policies

Use emojis, callout boxes, and visual organization. Make it scannable and action-oriented.
```

**After AI generates:**
- Review and adjust layout
- Add actual dates where placeholders exist
- Link the quick link buttons to your actual pages (use @mention)

---

## 🎯 STEP 2: Transform Compliance Calendar into Database

**What:** Turn the static calendar into an interactive tracking system

**Where:** Open "03_Compliance_Calendar_2025_2026.md" page

**Prompt 1 - Create Database:**
```
Convert this compliance calendar into a comprehensive database called "Master Compliance Tracker" with these properties:

PROPERTIES:
- Task/Filing (title) - Name of the compliance requirement
- Due Date (date) - When it's due
- Category (select) - Federal | State | SPV | Organizational
- Frequency (select) - Monthly | Quarterly | Annual | One-time
- Status (select) - 🔴 Overdue | 🟡 Due Soon | ⏳ Upcoming | ✅ Complete
- Priority (select) - 🔴 Critical | 🟡 Important | 🟢 Standard
- Owner (person) - Who is responsible
- Reminder Set (checkbox) - Has reminder been configured
- Consequences (text) - What happens if missed
- Notes (text) - Additional information

INITIAL ENTRIES - Add these critical deadlines:
1. Form 990 for 2025 | May 15, 2026 | Federal | Annual | Critical
2. WA Annual Report - HROC | July 31, 2026 | State | Annual | Critical
3. WA Annual Report - SPV LLC | July 31, 2026 | State | Annual | Critical
4. SPV BOI Report to FinCEN | October 28, 2025 | Federal | One-time | Critical
5. WA Charitable Registration Renewal | [Check date] | State | Annual | Important
6. SPV Monthly Financial Statement | 5th of each month | SPV | Monthly | Important
7. SPV Quarterly Board Report | Oct 5, Jan 5, Apr 5, Jul 5 | SPV | Quarterly | Important
8. Annual Conflict of Interest Disclosures | January 2026 | Organizational | Annual | Important
9. Donor Acknowledgment Letters | January 31, 2026 | Federal | Annual | Important
10. Annual Policy Review | July 2026 | Organizational | Annual | Standard

Create the database at the top of this page.
```

**Prompt 2 - Create Views:**
```
For the Master Compliance Tracker database, create these views:

1. CALENDAR VIEW: "📅 Deadline Calendar"
   - Show all deadlines on a visual calendar
   - Color code by Priority (red=critical, yellow=important, green=standard)

2. TABLE VIEW: "🚨 Overdue & Due Soon"
   - Filter: Status is "Overdue" OR "Due Soon"
   - Sort: Due Date (ascending)
   - Group by: Category

3. TIMELINE VIEW: "📊 Next 90 Days"
   - Show upcoming 3 months
   - Color code by Category

4. KANBAN VIEW: "📋 By Status"
   - Group by: Status
   - Sort by: Due Date

5. TABLE VIEW: "🔴 Critical Only"
   - Filter: Priority is "Critical"
   - Sort: Due Date (ascending)

6. TABLE VIEW: "📌 My Responsibilities"
   - Filter by: Owner (set to current user)
   - Sort: Due Date (ascending)

Set "Deadline Calendar" as the default view.
```

**After AI generates:**
- Verify all dates are correct
- Add owners to each task
- Set up actual Notion reminders (click due date → Add reminder)

---

## 🎯 STEP 3: Create SPV Compliance Tracker

**What:** Track all SPV monthly, quarterly, and annual tasks

**Where:** Open "02_SPV_Management_Guide.md" page

**Prompt:**
```
Create an "SPV Compliance Tracker" database for tracking all SPV management tasks:

PROPERTIES:
- Task Name (title)
- Frequency (select) - Daily | Weekly | Monthly | Quarterly | Annual | One-time
- Due Date (date)
- Last Completed (date)
- Next Due (date - formula based on Frequency and Last Completed)
- Category (select) - Financial | Legal | Operations | Insurance | Vehicle
- Status (checkbox) - Completed this period
- Owner (person)
- Documentation Required (files)
- Notes (text)

POPULATE WITH TASKS FROM THE GUIDE:

MONTHLY (Due 5th of month):
- Prepare monthly SPV financial statement
- Reconcile SPV bank account
- Process vendor payments
- Update vehicle mileage logs
- Review insurance coverage

QUARTERLY (Due 5th of Oct, Jan, Apr, Jul):
- Submit SPV Manager report to HROC Board
- Update asset inventory
- Update authorized driver list
- Review budget vs actual
- Finance Committee reviews compliance

ANNUAL (Various due dates):
- File WA Annual Report - SPV (July 31)
- Renew vehicle insurance (check policy date)
- Renew general liability insurance (check policy date)
- Annual SPV performance review (July)
- Review Operating Agreement (July)
- Review Inter-Entity Agreement (July)
- Compliance audit by Finance Committee (Q1)
- Update registered agent info (if changed)
- Conduct risk assessment (July)

Create this database below the main content. Add views for: By Frequency, By Category, Monthly Tasks, Overdue.
```

**After AI generates:**
- Add specific due dates for annual items
- Assign owners
- Upload any existing documentation

---

## 🎯 STEP 4: Create IRS Communications Tracker

**What:** Database to log all IRS interactions

**Where:** Open "06_IRS_Communications_Log.md" page

**Prompt:**
```
Create an "IRS Communications Log" database to track all IRS interactions:

PROPERTIES:
- Communication Title (title) - Brief description
- Date (date) - Date received or sent
- Type (select) - 📞 Phone Call | 📧 Email | 📬 Letter | 📋 Notice | 📤 Submission
- Direction (select) - ← From IRS | → To IRS
- Action Required (checkbox) - Does this need a response?
- Response Deadline (date) - When response is due
- Status (select) - ⏳ Pending | 🔄 In Progress | ✅ Complete | 🔴 Overdue
- IRS Contact Name (text) - Name of IRS agent if applicable
- Documents (files) - Upload correspondence
- Summary (text) - What it's about
- Our Response (text) - What we sent/said
- Response Date (date) - When we responded
- Follow-up Needed (checkbox)
- Notes (text)

EXISTING ENTRIES - Add these:
1. EIN Assignment | [Date CP-575 received] | Notice | From IRS | Complete
   Summary: "Received CP-575 confirming EIN 39-3295288"

2. Form 1023 Submission | August 25, 2025 | Submission | To IRS | Complete
   Summary: "Submitted Form 1023 Application for 501(c)(3) status"

3. Supplemental Packet Submission | August 11, 2025 | Submission | To IRS | Complete
   Summary: "Submitted supplemental information requested by IRS"

4. Determination Letter | Expected Dec 2025-Feb 2026 | Letter | From IRS | Pending
   Summary: "Awaiting determination on 501(c)(3) status"
   Action Required: Yes (when received - must file with state)

Create views: By Status, Pending Response, Timeline (all communications chronologically), By Type.
```

**After AI generates:**
- Add actual dates for items you know
- Upload any existing IRS correspondence
- Set reminders for pending items

---

## 🎯 STEP 5: Create Officer Transition Project Tracker

**What:** Track the urgent officer transition with phases and deadlines

**Where:** Open "04_Officer_Transition_Critical_Tasks.md" page

**Prompt:**
```
Create an "Officer Transition Project" database to track this urgent transition:

PROPERTIES:
- Task (title) - What needs to be done
- Phase (select) - Week 1: Board Meeting | Week 2: Internal Docs | Week 3: State Filings | Week 4: Public Updates
- Due Date (date)
- Status (select) - ⚪ Not Started | 🔵 In Progress | ✅ Complete | 🔴 Blocked
- Owner (person) - Who is responsible
- Completion Evidence (files) - Upload completed documents
- Dependencies (relation) - Link to tasks that must be done first
- Notes (text)

TASKS TO ADD:

WEEK 1 - BOARD MEETING (Target: This week):
- Schedule special board meeting (2 days notice)
- Prepare meeting agenda with officer election
- Hold board meeting and vote on officers
- Draft meeting minutes documenting election
- Obtain signatures on minutes

WEEK 2 - INTERNAL DOCS (Days 4-7):
- Update board roster with new titles
- Sign updated board roster
- Review policies for title references
- Update organizational chart
- Update email signatures

WEEK 3 - STATE FILINGS (Days 10-14):
- File WA Annual Report with updated officers
- Update WA Charitable Registration
- Download filing confirmations
- Update IRS records (or plan for next Form 990)

WEEK 4 - PUBLIC UPDATES (Days 14-21):
- Update website board page
- Update grant applications in progress
- Notify partners and stakeholders
- Update GuideStar/Candid profile

NEW OFFICER STRUCTURE:
- Brianna Bear → Chair/President
- Jonathan Mallinger → Secretary
- Lilly Fedas → Treasurer

Create Kanban view by Status and Timeline view by Phase. Set default to Kanban.
```

**After AI generates:**
- Assign due dates based on when you can schedule board meeting
- Assign owners
- Mark any already-completed tasks

---

## 🎯 STEP 6: Create Website Accessibility Audit Tracker

**What:** Monthly accessibility testing log

**Where:** Open "05_Web_Accessibility_Checklist.md" page

**Prompt:**
```
Create a "Website Accessibility Audits" database to track monthly testing:

PROPERTIES:
- Audit Date (date) - When audit was performed
- Page/Section Audited (title) - What was tested
- Lighthouse Score (number) - Accessibility score (0-100)
- axe DevTools Results (select) - ✅ No Issues | ⚠️ Minor Issues | 🔴 Critical Issues
- Issues Found (number) - Total count
- Critical Issues (number) - Count of critical
- Issues Detailed (text) - Specific problems found
- Status (select) - 📝 Planned | 🔄 Testing | ⚠️ Fixing Issues | ✅ Complete
- Next Audit Due (date - formula: Audit Date + 30 days)
- Auditor (person) - Who performed the test
- Notes (text)

TESTING CHECKLIST (add as relation or linked database):
Create a related "Accessibility Issues" database with:
- Issue Description (title)
- Severity (select) - 🔴 Critical | 🟡 Moderate | 🟢 Minor
- WCAG Criterion (text) - Which standard it violates
- Page Affected (text)
- Fix Applied (text) - How it was resolved
- Status (select) - Open | In Progress | Fixed | Won't Fix
- Date Found (date)
- Date Fixed (date)

Create views: By Month, Critical Issues Only, Open Issues, Audit Calendar.

Add first entry:
- Audit Date: [Today's date]
- Page: Homepage
- Status: Planned
- Next Audit Due: [30 days from today]
```

**After AI generates:**
- Schedule your first audit
- Set recurring monthly reminder
- Link to your actual website URL in notes

---

## 🎯 STEP 7: Create Document Templates

**What:** Reusable templates for common tasks

**Where:** Create a new page called "📝 Document Templates"

**Prompt:**
```
Create a template gallery page with these reusable templates for HROC:

1. BOARD MEETING MINUTES TEMPLATE
   Include sections for:
   - Meeting date, time, location
   - Attendees (with checkboxes)
   - Agenda items
   - Motions made and votes (table)
   - Action items assigned
   - Next meeting date
   - Signature blocks

2. QUARTERLY SPV REPORT TEMPLATE
   Include sections for:
   - Reporting period
   - Operational status summary
   - Financial summary (revenue, expenses, variance)
   - Compliance updates checklist
   - Risk management issues
   - Performance metrics
   - Recommendations

3. MONTHLY FINANCIAL REPORT TEMPLATE
   Include sections for:
   - Month/Year
   - Income summary (table)
   - Expense summary (table)
   - Budget vs Actual comparison
   - Cash flow statement
   - Bank reconciliation confirmation
   - Significant variances explained
   - Treasurer signature block

4. IRS RESPONSE LETTER TEMPLATE
   Include:
   - Organization name and EIN on each page
   - Date
   - IRS address
   - RE: line referencing their request
   - Point-by-point responses
   - Attached documentation list
   - Authorized signature block

5. GRANT APPLICATION TRACKING TEMPLATE
   Include properties for:
   - Grant name and organization
   - Amount requested
   - Deadline
   - Status (Researching, Drafting, Submitted, Awarded, Denied)
   - Required documents checklist
   - Submission confirmation
   - Reporting requirements if awarded

6. POLICY REVIEW CHECKLIST TEMPLATE
   For annual policy reviews:
   - Policy name
   - Last reviewed date
   - Review checklist
   - Changes needed (if any)
   - Board approval date
   - Next review due date

Make each template easily duplicatable with clear instructions at the top.
```

**After AI generates:**
- Review each template
- Add your specific details (EIN, addresses, etc.)
- Test duplicating one template to ensure it works

---

## 🎯 STEP 8: Link Everything Together

**What:** Create relationships between databases

**Where:** Your main dashboard page

**Prompt:**
```
Help me create relationships and linked database views across my HROC workspace:

1. On the DASHBOARD page, add these LINKED DATABASE VIEWS:
   - "🚨 Critical Deadlines (Next 30 Days)" - from Master Compliance Tracker
     Filter: Due Date is within next 30 days AND Priority is Critical
     Properties to show: Task, Due Date, Owner, Status
     Sort: Due Date ascending

   - "⏳ Pending IRS Items" - from IRS Communications Log
     Filter: Status is Pending OR In Progress
     Properties to show: Title, Date, Response Deadline, Status
     Sort: Response Deadline ascending

   - "📋 Officer Transition Progress" - from Officer Transition Project
     Filter: Status is not Complete
     Properties to show: Task, Phase, Status, Owner
     Group by: Phase

2. On the COMPLIANCE CALENDAR page, add:
   - Linked view of IRS Communications showing items that have compliance deadlines

3. On the SPV MANAGEMENT GUIDE page, add:
   - Linked view of Master Compliance Tracker filtered to SPV category only

4. Create RELATIONS between databases:
   - Link Compliance Calendar items to relevant IRS Communications
   - Link Officer Transition tasks to Compliance Calendar items
   - Link Accessibility Audits to Issues Found

Add clear section headers and explanatory text above each linked view.
```

**After AI generates:**
- Verify filters are working correctly
- Adjust which properties display in each view
- Test that linked views update when main databases change

---

## 🎯 STEP 9: Set Up Automations & Reminders

**What:** Ensure you never miss a deadline

**Where:** Various pages with databases

**Prompt:**
```
Help me set up a comprehensive reminder and notification system for HROC:

CRITICAL DEADLINES REMINDERS:
For the Master Compliance Tracker database, help me set reminders for:
- 30 days before due date
- 14 days before due date
- 7 days before due date
- Day of deadline

SPECIFICALLY SET THESE:
1. Form 990 (May 15, 2026):
   - Remind Feb 15: Begin preparation
   - Remind Apr 15: Finalize
   - Remind May 1: Final review
   - Remind May 14: Last chance

2. WA Annual Reports (July 31, 2026):
   - Remind June 1: Prepare information
   - Remind July 1: File reports
   - Remind July 24: Last week

3. SPV BOI Report (October 28, 2025):
   - Remind September 28: Gather info
   - Remind October 14: Prepare filing
   - Remind October 21: Last week

RECURRING TASK REMINDERS:
For SPV Compliance Tracker:
- Monthly tasks: Remind on 1st of each month
- Quarterly tasks: Remind 2 weeks before quarter end

IRS COMMUNICATIONS:
- Set up notification when new items added to log
- Remind 3 days before response deadlines

Provide step-by-step instructions for setting up these reminders in Notion.
```

**After AI generates:**
- Follow the instructions to set up each reminder
- Test that reminders appear in Notion's notification center
- Add calendar reminders in your phone/Outlook/Google Calendar as backup

---

## 🎯 STEP 10: Create Mobile-Optimized Views

**What:** Ensure everything works great on mobile

**Where:** Main dashboard

**Prompt:**
```
Optimize the HROC workspace for mobile access by creating simplified views:

1. Create a "📱 Mobile Quick View" page with:
   - Today's date and next board meeting
   - Urgent action items only (red priority, due within 7 days)
   - Simple checklist of today's tasks
   - One-tap links to most used pages
   - Emergency contacts (IRS phone, WA SOS phone)
   - Quick add buttons for common items

2. Simplify database views for mobile:
   - Hide less critical properties when viewing on phone
   - Create gallery/card views instead of table views
   - Add cover images to make items visually distinct
   - Use emojis for status instead of long text

3. Create a "Quick Add" inbox database where anyone can quickly add:
   - Action items
   - IRS communications
   - Tasks to review
   - Questions for board

Make everything accessible with thumbs, not precision taps. Use large buttons and clear typography.
```

**After AI generates:**
- Install Notion mobile app if you haven't
- Test accessing your pages on mobile
- Bookmark "Mobile Quick View" on your phone home screen
- Adjust any layouts that don't work well on small screens

---

## 🎯 STEP 11: Add Visual Enhancements

**What:** Make everything beautiful and easy to scan

**Where:** All pages

**Prompt:**
```
Enhance the visual design of all HROC Notion pages:

1. ADD COVER IMAGES to each main page:
   - Dashboard: Professional team or organization photo
   - Getting Started: Celebration or checkmark
   - SPV Guide: Vehicle or road
   - Compliance Calendar: Calendar or planner
   - Officer Transition: Handshake or collaboration
   - Accessibility: Universal access symbol
   - IRS Log: Government building or files

   Suggest specific free image sources (Unsplash keywords).

2. ADD CALLOUT BOXES for:
   - 🔴 Critical warnings (use red background, light)
   - 💡 Pro tips (use blue background, light)
   - ✅ Success criteria (use green background, light)
   - ⚠️ Important notes (use yellow background, light)

3. ADD DIVIDERS between major sections

4. ADD TOGGLE BLOCKS for:
   - Long explanatory text
   - Detailed instructions
   - Reference materials
   - Less frequently accessed content

5. ADD PROGRESS BARS using database formulas for:
   - Overall compliance percentage
   - Officer transition completion
   - SPV setup progress

6. ADD EMOJI HEADERS to all major sections consistently

Provide specific recommendations for which existing sections should become callouts or toggles.
```

**After AI generates:**
- Add the recommended images (search Unsplash.com with provided keywords)
- Convert text to callouts where recommended
- Create toggles for long sections
- Test that everything is easy to navigate

---

## 🎯 STEP 12: Create Onboarding Guide for Board Members

**What:** Help new users understand the workspace

**Where:** Create a new page called "👋 Welcome to HROC Notion"

**Prompt:**
```
Create a comprehensive onboarding guide for HROC board members new to this Notion workspace:

Include:

1. WELCOME section explaining:
   - What this workspace contains
   - Why we use Notion
   - How it helps with compliance and operations

2. QUICK START GUIDE:
   - How to navigate the sidebar
   - What each main page is for
   - How to use databases (filtering, sorting, views)
   - How to add new entries
   - How to find information quickly

3. YOUR RESPONSIBILITIES by role:
   - Board Chair: What to monitor
   - Treasurer: Financial pages to review
   - Secretary: Meeting minutes and documents
   - SPV Manager: SPV compliance tracker
   - All Members: Compliance calendar, policies

4. COMMON TASKS with step-by-step:
   - How to log an IRS communication
   - How to add a compliance deadline
   - How to complete a monthly SPV checklist
   - How to update the officer transition tracker
   - How to run an accessibility audit

5. BEST PRACTICES:
   - Check dashboard daily for urgent items
   - Update your assigned tasks promptly
   - Use @mentions to notify others
   - Add comments for collaboration
   - Upload documents directly to relevant entries

6. TIPS & TRICKS:
   - Keyboard shortcuts
   - Mobile app usage
   - Offline access
   - Sharing with external stakeholders

7. SUPPORT section:
   - How to get help
   - Who manages this workspace
   - Where to suggest improvements

8. VIDEO TUTORIAL placeholder with:
   - "Coming soon: 5-minute walkthrough video"
   - Link to Notion's official tutorials

Make it beginner-friendly with screenshots placeholders and simple language.
```

**After AI generates:**
- Review for accuracy
- Add actual screenshots (take them yourself)
- Share this page with new board members first
- Consider recording a simple screen recording walkthrough

---

## ✅ FINAL STEP: Workspace Settings & Permissions

**What:** Configure access and settings

**Where:** Workspace settings (top left menu → Settings & Members)

**Prompt:**
```
Help me configure the optimal Notion workspace settings and permissions for a nonprofit board:

TEAM MEMBERS TO ADD:
- Board Chair (Brianna Bear) - Full Access
- Secretary (Jonathan Mallinger) - Full Access
- Treasurer (Lilly Fedas) - Full Access
- Board Members (James, Vania) - Can Edit
- Advisors (if any) - Can Comment
- Public transparency pages - Can View (specific pages only)

PERMISSION LEVELS explained:
- Full Access: Can delete, change permissions
- Can Edit: Can create/edit but not delete major pages
- Can Comment: Can view and comment only
- Can View: Read-only access

SETTINGS TO CONFIGURE:
1. Workspace name: "HROC Operations"
2. Workspace icon: Choose or upload HROC logo
3. Domain: Connect custom domain if you have Notion paid plan
4. Notifications: Enable for all compliance deadlines
5. Public access: Decide which pages to share publicly
6. Mobile optimization: Ensure all have mobile app

SECURITY BEST PRACTICES:
- Enable two-factor authentication for all full access members
- Regularly review member list
- Use page-level permissions for sensitive financial data
- Export backups monthly

Provide step-by-step instructions for each setting.
```

**After AI generates:**
- Follow instructions to set up permissions
- Invite team members with appropriate access
- Configure notification settings
- Set up 2FA for admins

---

## 🎉 CONGRATULATIONS!

You've created a world-class nonprofit operations hub!

## 📊 What You've Built:

✅ **6 Comprehensive Guide Pages**
✅ **5 Interactive Databases** (Compliance, SPV, IRS, Officer Transition, Accessibility)
✅ **Professional Dashboard** with live metrics
✅ **Document Templates** for recurring tasks
✅ **Linked Database Views** showing relevant info on each page
✅ **Mobile-Optimized Views** for on-the-go access
✅ **Onboarding Guide** for new team members
✅ **Proper Permissions** and security settings

## 🎯 Daily Workflow:

**Every Morning:**
1. Check Dashboard for urgent items
2. Review "Due Today" tasks
3. Clear notifications

**Weekly:**
1. Update SPV tasks
2. Review compliance calendar for next 7 days
3. Check IRS log for pending responses

**Monthly:**
1. Run accessibility audit
2. Review all databases for accuracy
3. Export backup

---

## 💡 Next Level Enhancements (Optional):

If you have Notion Plus/Business, consider:
- Automations for recurring tasks
- Connected to Slack for notifications
- Custom domains for public pages
- Advanced permissions by page section
- Version history retention

---

## 🆘 Need Help?

**Notion Support:**
- Help Center: https://notion.so/help
- Community: https://notion.so/community
- Live chat: Available in app

**HROC-Specific:**
- Contact your board chair
- Review the onboarding guide
- Check Notion's video tutorials

---

**🌟 You're all set! Your Notion workspace is now a powerful nonprofit management system.**

Save this guide for reference when adding new features or onboarding new team members.

**Last Updated:** December 2025

