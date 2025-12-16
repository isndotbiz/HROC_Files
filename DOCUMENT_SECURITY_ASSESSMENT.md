# HROC Document Security Assessment & Recommendations

**Date:** December 15, 2025
**Status:** Ready for Implementation

---

## Executive Summary

Currently, **43 documents** are publicly accessible via your website. Based on best practices for nonprofit transparency and security, we recommend moving **11-15 sensitive documents** behind a secure authentication wall while keeping **28-32 documents** public to demonstrate transparency and good governance.

---

## PUBLIC DOCUMENTS (Keep Accessible)
### ✅ **Transparency & Good Governance**

#### Policies (7 files - KEEP PUBLIC)
- Code_of_Conduct_Policy.pdf
- Conflict_of_Interest_Policy.pdf
- Document_Retention_and_Destruction_Policy.pdf
- Financial_Controls_and_Reimbursement_Policy.pdf
- Gift_Acceptance_and_Acknowledgment_Policy.pdf
- Policies_and_Procedures_Overview.pdf
- Whistleblower_Protection_Policy.pdf

**Rationale:** Demonstrates organizational best practices, commitment to ethics, and transparent governance. Donors and partners expect to see these.

#### Governance Documents (4 files - KEEP PUBLIC)
- Articles_of_Incorporation_0022584962.pdf
- Articles_of_Incorporation_Certificate.pdf
- Articles_of_Incorporation_Congratulations_0022584962.pdf
- Governance_and_Policies_Adoption.pdf

**Rationale:** Legally required disclosures that establish legitimacy and 501(c)(3) status.

#### Registrations & Licenses (4 files - KEEP PUBLIC)
- Business_License_My_DOR.pdf
- Business_License_Receipt_2025-08-08.pdf
- Charitable_Organization_Registration_0000567751.pdf
- Charity_Organization_Information_0000567751.pdf

**Rationale:** Compliance documentation that proves you're a legitimate, registered nonprofit.

#### IRS Documents (2 files - KEEP PUBLIC)
- IRS_CP575_EIN_Letter_39-3295288.pdf
- IRS_General_Guidance.pdf

**Rationale:** EIN letter proves 501(c)(3) status; general guidance is educational.

#### Miscellaneous Guides (4 files - KEEP PUBLIC)
- Starting_a_Nonprofit_in_WA_Guide_2023.pdf
- IRS_Tax_Code_and_Official_Guidance.pdf
- Understanding_IRS_Guidance_Primer.pdf
- (Keep Proton_Recovery_Kit.pdf if it's security-related guidance)

**Rationale:** Educational resources that help partners and other nonprofits.

#### Operations (1 file - KEEP PUBLIC)
- Fiscal_Sponsor_Onboarding.pdf

**Rationale:** Demonstrates operational transparency and partnership structures.

---

## SENSITIVE DOCUMENTS (Move Behind Secure Wall)
### ⚠️ **Requires Authentication**

#### Financial Plans (3 files - SECURE)
- **Projected_Budget_2025_Signed.pdf**
  - Contains: Specific budget allocations, financial forecasts
  - Risk: Competitive vulnerability, donor targeting information

- **Financial_Projections_3yr_Signed.pdf**
  - Contains: Multi-year financial strategy
  - Risk: Reveals organizational financial capacity and constraints

- **Fundraising_Plan.pdf**
  - Contains: Donor strategy, targeting approaches
  - Risk: Competitors could use to recruit donors; donors could be targeted by others

#### Board Minutes (2-3 files - SECURE)
- **Board_Meeting_First.pdf**
  - Contains: Initial strategic decisions, leadership discussions
  - Risk: Internal discussions may include sensitive personnel or strategy info

- **Board_Meeting_Special.pdf**
  - Contains: Special session discussions (likely sensitive matters)
  - Risk: Could contain personnel, conflict, or crisis management discussions

- **Board_Resolutions** (2025-03 & 2025-04)
  - Contains: Board-level decisions that may include sensitive directives
  - Risk: Could reveal internal priorities, personnel changes, or strategic pivots

#### Board Roster (1 file - SECURE)
- **Board_Roster_Certified.pdf**
  - Contains: Full names and titles of board members
  - Risk: Privacy & safety concerns; board members don't necessarily want public exposure

#### IRS Documents (2 files - SECURE)
- **IRS_Form_1023_Application_Signed.pdf**
  - Contains: Detailed organizational structure, programs, financial projections
  - Risk: Competitors could replicate; detailed internal information

- **IRS_Supplemental_Packet_2025-08-11_Filled.pdf**
  - Contains: Extremely detailed financial and organizational data
  - Risk: Comprehensive operational blueprint exposed

#### SPV LLC Documents (6-7 files - SECURE)
- **SPV_Operating_Agreement.pdf**
  - Contains: Internal governance structure, member agreements
  - Risk: Reveals business structure vulnerabilities

- **SPV_Organizational_Charter.pdf**
  - Contains: Internal organizational structure

- **SPV_and_HROC_Agreement.pdf**
  - Contains: Relationship terms between entities

- **SPV_Manager.pdf**
  - Contains: Management structure and decision-making authority

- **SPV_LLC_Protections_and_Compliance_Checklist.pdf**
  - Contains: Internal compliance strategy

- **RV_Lease_Market_Analysis_for_Mobile_Outreach_Operations.pdf**
  - Contains: Operational strategy and market analysis
  - Risk: Competitors learn operational approach

- **SPV_Protection_Approval.pdf**
  - Contains: Legal approvals and decisions

- **Business_License_Application_Healing_Roots_Outreach.pdf**
  - Contains: Operational details in application format

- **Formation_Timeline_and_Critical_Compliance_Deadlines.pdf**
  - Contains: Strategic timeline and internal deadlines

- **Annual_Report_Filing_Year_2026.pdf**
  - Contains: Detailed annual reporting (may include sensitive metrics)

---

## Implementation Options

### **Option 1: Basic Password Protection** (Recommended - Easy)
- Simple login screen for all sensitive documents
- One password shared with board, donors, and partners
- Implementation: ~2 hours

### **Option 2: Tiered Access** (Recommended - Better)
- Public tier: Policies, registrations, articles
- Board tier: Requires board email login
- Partner tier: Requires approved partner email
- Implementation: ~4-6 hours with backend support

### **Option 3: Remove from Web** (Most Secure)
- Remove all sensitive documents from website
- Provide via email upon request with verification
- Implementation: ~1 hour (remove links from documents.html)

---

## Recommended Action Plan

1. **Immediate (This Sprint):**
   - Move 11-15 sensitive documents to a `/pdfs/private/` folder
   - Keep 28-32 public documents in `/pdfs/public/`
   - Update `documents.html` to show both sections with access notes

2. **Short Term (This Week):**
   - Implement basic password protection or tiered access
   - Update footer to explain document access policies
   - Notify board members of new document access procedures

3. **Medium Term (This Month):**
   - Review all PDFs for unnecessary sensitive information
   - Redact personal information (board member names/contact info) from public documents
   - Create board-specific document portal

---

## Privacy & Legal Considerations

- ✅ **Recommended:** Board members should know documents are less accessible
- ✅ **Recommended:** Donors and partners should have easy access to key compliance docs
- ⚠️ **Consider:** Some documents may need redaction (personal information)
- ⚠️ **Consider:** Ensure policies are dated and clearly marked as current

---

## Benefits of Secure Document Strategy

1. **Transparency:** Public documents show good governance
2. **Security:** Sensitive financial/strategic information protected
3. **Professional:** Demonstrates mature nonprofit practices
4. **Compliance:** Still meets transparency requirements
5. **Control:** Board can share sensitive docs selectively

---

## Next Steps

1. Approve recommendation level (Option 1, 2, or 3)
2. Provide list of who should have access to secure tier
3. Implement technical solution
4. Test and verify all links work correctly

---

**Prepared by:** Claude Code
**Status:** Pending Your Approval
