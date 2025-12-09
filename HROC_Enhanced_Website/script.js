/**
 * HROC Enhanced Website - Accessible JavaScript
 * WCAG 2.2 Level AA Compliant
 */

// File list data (same as original)
const filesData = [
  "00_Action_Plan/CLI_Workflow.txt",
  "00_Action_Plan/Next_Actions.txt",
  "00_Action_Plan/Schedule_30-60-90.txt",
  "01_Governance/Articles_of_Incorporation.pdf",
  "01_Governance/Articles_of_Incorporation_0022584962.pdf",
  "01_Governance/Articles_of_Incorporation_Certificate.pdf",
  "01_Governance/Articles_of_Incorporation_Congratulations_0022584962.pdf",
  "01_Governance/Board_Meeting_First.pdf",
  "01_Governance/Board_Meeting_First_notes.pdf",
  "01_Governance/Board_Meeting_Special.pdf",
  "01_Governance/Board_Meeting_Special_notes.pdf",
  "01_Governance/Board_Resolution_2025-03.pdf",
  "01_Governance/Board_Resolution_2025-03_signed_alt.pdf",
  "01_Governance/Board_Resolution_2025-04.pdf",
  "01_Governance/Board_Resolution_2025-04_signed_alt.pdf",
  "01_Governance/Board_Roster.pdf",
  "01_Governance/Board_Roster_Certified.pdf",
  "01_Governance/Bylaws.pdf",
  "01_Governance/Formation_and_Governance.pdf",
  "01_Governance/Governance_and_Policies_Adoption.pdf",
  "01_Governance/Governance_and_Policies_Adoption_notes.pdf",
  "02_Policies/Code_of_Conduct_Policy.pdf",
  "02_Policies/Conflict_of_Interest_Policy.pdf",
  "02_Policies/Conflict_of_Interest_Policy_alt.pdf",
  "02_Policies/Document_Retention_Policy.pdf",
  "02_Policies/Document_Retention_and_Destruction_Policy.pdf",
  "02_Policies/Financial_Controls_and_Reimbursement_Policy.pdf",
  "02_Policies/Financial_Controls_and_Reimbursement_Policy_alt.pdf",
  "02_Policies/Gift_Acceptance_Policy.pdf",
  "02_Policies/Gift_Acceptance_and_Acknowledgment_Policy.pdf",
  "02_Policies/Policies_and_Procedures_Overview.pdf",
  "02_Policies/Whistleblower_Protection_Policy.pdf",
  "03_Registrations_Licenses/Business_License_My_DOR.pdf",
  "03_Registrations_Licenses/Business_License_Receipt_2025-08-08.pdf",
  "03_Registrations_Licenses/Charitable_Organization_Registration_0000567751.pdf",
  "03_Registrations_Licenses/Charity_Organization_Information_0000567751.pdf",
  "03_Registrations_Licenses/WA_Charitable_Organization_Registration.pdf",
  "04_IRS/IRS_CP575_EIN_Letter_39-3295288.pdf",
  "04_IRS/IRS_CP575_EIN_Letter_copy.pdf",
  "04_IRS/IRS_Form_1023_Application.pdf",
  "04_IRS/IRS_Form_1023_Application_Signed.pdf",
  "04_IRS/IRS_Form_i1023_Blank.pdf",
  "04_IRS/IRS_General_Guidance.pdf",
  "04_IRS/IRS_Supplemental_Packet_2025-08-11_Filled.pdf",
  "05_Financial_Plans/Financial_Planning.pdf",
  "05_Financial_Plans/Financial_Projections_3yr_Signed.pdf",
  "05_Financial_Plans/Fundraising_Plan.pdf",
  "05_Financial_Plans/Projected_Budget_2025_Signed.pdf",
  "06_Operations_Plans/Fiscal_Sponsor_Onboarding.pdf",
  "06_Operations_Plans/Operational_Planning.pdf",
  "07_SPV/Annual_Report_Filing_Year_2026.pdf",
  "07_SPV/Business_License_Application_Healing_Roots_Outreach.pdf",
  "07_SPV/Formation_Timeline_and_Critical_Compliance_Deadlines.pdf",
  "07_SPV/RV_Lease_Market_Analysis_for_Mobile_Outreach_Operations.pdf",
  "07_SPV/Review_SPV_and_Fiscal_Sponsorship_Agreements.pdf",
  "07_SPV/SPV_Documents_Index.pdf",
  "07_SPV/SPV_LLC_Protections_and_Compliance_Checklist.pdf",
  "07_SPV/SPV_Manager.pdf",
  "07_SPV/SPV_Operating_Agreement.pdf",
  "07_SPV/SPV_Organizational_Charter.pdf",
  "07_SPV/SPV_Protection_Approval.pdf",
  "07_SPV/SPV_Protection_Approval_notes.pdf",
  "07_SPV/SPV_and_HROC_Agreement.pdf",
  "08_Branding_Signatures/hrocinc.png",
  "08_Branding_Signatures/notion_cover.png",
  "08_Branding_Signatures/sig_BB.png",
  "08_Branding_Signatures/sig_JDM.png",
  "08_Branding_Signatures/sig_JDM_200.png",
  "08_Branding_Signatures/sig_LF.png",
  "08_Branding_Signatures/signature.png",
  "09_Checklists_ToDos/TODO_Adopt_Document_Retention_and_Destruction_Policy.pdf",
  "09_Checklists_ToDos/TODO_Adopt_and_Log_Final_Bylaws.pdf",
  "09_Checklists_ToDos/TODO_Approve_Conflict_of_Interest_and_Collect_Signed_Forms.pdf",
  "09_Checklists_ToDos/TODO_Create_Donation_Acceptance_and_Acknowledgment_Process.pdf",
  "09_Checklists_ToDos/TODO_Establish_Financial_Controls.pdf",
  "09_Checklists_ToDos/TODO_Open_Nonprofit_Bank_Account.pdf",
  "09_Checklists_ToDos/TODO_Publish_Transparency_Hub.pdf",
  "09_Checklists_ToDos/TODO_Register_with_WA_Charities_Program_SOS.pdf",
  "09_Checklists_ToDos/TODO_Setup_IRS_Form_990N_990EZ_Process.pdf",
  "99_Misc_Guides/IRS_Guidance_Brief_Primer.pdf",
  "99_Misc_Guides/IRS_Official_Guidance.pdf",
  "99_Misc_Guides/Starting_a_Nonprofit_in_WA_Guide_2023.pdf",
  "99_Misc_Guides/Z_Proton_Recovery_Kit.pdf"
];

// Compliance data
const complianceData = [
  { label: "Governance", value: 90, note: "Articles, bylaws, resolutions set" },
  { label: "Policies", value: 88, note: "Signed core policies in place" },
  { label: "State Filings", value: 72, note: "WA Annual & Charitable updates pending" },
  { label: "IRS Evidence", value: 48, note: "Add CP-575 + signed 1023" },
  { label: "Finance Ops", value: 60, note: "Budget + bank documentation queued" },
  { label: "SPV Docs", value: 70, note: "Operating agreements in; compliance timeline next" },
];

// Timeline data
const timelineData = [
  { when: "Day 0-7", text: "Elect officers; file WA Annual + Charitable Registration; add CP-575 & Form 1023." },
  { when: "Day 8-30", text: "Build budget & cash forecast; open bank; donation + acknowledgment flow; 990-N/EZ workflow." },
  { when: "Day 31-60", text: "SPV annual report + license renewal; RV lease + insurance; program metrics log; board calendar." },
  { when: "Day 61-90", text: "Grant pipeline tracker; quarterly board under new officers; annual policy refresh; verify reminders." }
];

/**
 * Initialize file table with search and filter functionality
 */
function initFileTable() {
  const folderSelect = document.getElementById('folder-filter');
  const tbody = document.querySelector('#file-table tbody');
  const searchInput = document.getElementById('search');

  if (!folderSelect || !tbody || !searchInput) {
    console.error('Required elements not found for file table initialization');
    return;
  }

  // Transform file data
  const data = filesData.map(filePath => {
    const parts = filePath.split('/');
    const folder = parts[0];
    const name = parts.slice(1).join('/');
    const ext = (filePath.split('.').pop() || '').toUpperCase();
    return { path: filePath, folder, name, ext };
  });

  // Populate folder filter dropdown
  const uniqueFolders = [...new Set(data.map(d => d.folder))].sort();
  uniqueFolders.forEach(folder => {
    const option = document.createElement('option');
    option.value = folder;
    option.textContent = folder;
    folderSelect.appendChild(option);
  });

  /**
   * Render table rows based on current filters
   */
  function renderTable() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedFolder = folderSelect.value;

    // Filter data
    const filteredData = data
      .filter(item => !selectedFolder || item.folder === selectedFolder)
      .filter(item => item.path.toLowerCase().includes(searchTerm));

    // Clear table body
    tbody.innerHTML = '';

    // Populate table
    filteredData.forEach(item => {
      const tr = document.createElement('tr');

      // Build relative path to file
      const relativePath = `../HROC_Public/${item.path}`;

      tr.innerHTML = `
        <td><a href="${relativePath}" download>${item.name}</a></td>
        <td><span class="tag">${item.folder}</span></td>
        <td style="color: var(--color-text-muted); font-size: 0.875rem;">${item.ext}</td>
      `;

      tbody.appendChild(tr);
    });

    // Announce results to screen readers
    const resultsCount = filteredData.length;
    announceToScreenReader(`Showing ${resultsCount} file${resultsCount !== 1 ? 's' : ''}`);
  }

  // Add event listeners
  searchInput.addEventListener('input', renderTable);
  folderSelect.addEventListener('change', renderTable);

  // Initial render
  renderTable();
}

/**
 * Initialize compliance chart
 */
function initComplianceChart() {
  const chartContainer = document.getElementById('compliance-chart');

  if (!chartContainer) {
    console.error('Compliance chart container not found');
    return;
  }

  complianceData.forEach(item => {
    // Create list item
    const listItem = document.createElement('div');
    listItem.className = 'chart-item';
    listItem.setAttribute('role', 'listitem');

    // Create header
    const header = document.createElement('div');
    header.className = 'chart-header';

    const labelDiv = document.createElement('div');
    const label = document.createElement('div');
    label.className = 'chart-label';
    label.textContent = item.label;

    const note = document.createElement('div');
    note.className = 'chart-note';
    note.textContent = item.note;

    labelDiv.appendChild(label);
    labelDiv.appendChild(note);

    const value = document.createElement('span');
    value.className = 'chart-value';
    value.textContent = `${item.value}%`;

    header.appendChild(labelDiv);
    header.appendChild(value);

    // Create progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'progress-bar';
    progressBar.setAttribute('role', 'progressbar');
    progressBar.setAttribute('aria-valuenow', item.value);
    progressBar.setAttribute('aria-valuemin', '0');
    progressBar.setAttribute('aria-valuemax', '100');
    progressBar.setAttribute('aria-label', `${item.label}: ${item.value}% complete`);

    const progressFill = document.createElement('span');
    progressFill.style.width = `${item.value}%`;
    progressBar.appendChild(progressFill);

    // Append to list item
    listItem.appendChild(header);
    listItem.appendChild(progressBar);

    // Append to container
    chartContainer.appendChild(listItem);
  });
}

/**
 * Initialize timeline
 */
function initTimeline() {
  const timelineContainer = document.getElementById('timeline');

  if (!timelineContainer) {
    console.error('Timeline container not found');
    return;
  }

  timelineData.forEach((step, index) => {
    const item = document.createElement('div');
    item.className = 'timeline-item';
    item.setAttribute('role', 'listitem');

    const dot = document.createElement('div');
    dot.className = 'timeline-dot';
    dot.setAttribute('aria-hidden', 'true');

    const content = document.createElement('div');

    const when = document.createElement('div');
    when.className = 'timeline-when';
    when.textContent = step.when;

    const text = document.createElement('p');
    text.className = 'timeline-text';
    text.textContent = step.text;

    content.appendChild(when);
    content.appendChild(text);

    item.appendChild(dot);
    item.appendChild(content);

    timelineContainer.appendChild(item);
  });
}

/**
 * Announce message to screen readers
 * @param {string} message - Message to announce
 */
function announceToScreenReader(message) {
  const announcement = document.createElement('div');
  announcement.setAttribute('role', 'status');
  announcement.setAttribute('aria-live', 'polite');
  announcement.className = 'sr-only';
  announcement.textContent = message;

  document.body.appendChild(announcement);

  // Remove after announcement
  setTimeout(() => {
    document.body.removeChild(announcement);
  }, 1000);
}

/**
 * Smooth scroll for anchor links (with fallback for accessibility)
 */
function initSmoothScroll() {
  const links = document.querySelectorAll('a[href^="#"]');

  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');

      // Skip if it's the skip link
      if (href === '#main-content') {
        return;
      }

      e.preventDefault();

      const targetId = href.substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        // Check for reduced motion preference
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        targetElement.scrollIntoView({
          behavior: prefersReducedMotion ? 'auto' : 'smooth',
          block: 'start'
        });

        // Set focus to target for keyboard users
        targetElement.setAttribute('tabindex', '-1');
        targetElement.focus();

        // Update URL
        history.pushState(null, null, href);
      }
    });
  });
}

/**
 * Initialize all components when DOM is ready
 */
function init() {
  // Initialize components
  initFileTable();
  initComplianceChart();
  initTimeline();
  initSmoothScroll();

  console.log('HROC Enhanced Website initialized');
}

// Run initialization when DOM is fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
