#!/bin/bash

# Link checker for HROC website
# Base URL and directory
BASE_URL="http://localhost:8080"
HROC_PUBLIC_DIR="/Users/jonathanmallinger/Documents/HROC_Files/HROC_Public"
ENHANCED_DIR="/Users/jonathanmallinger/Documents/HROC_Files/HROC_Enhanced_Website"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================="
echo "HROC Website Link Checker"
echo "========================================="
echo ""

# Counters
total_links=0
broken_links=0
missing_files=0

# Arrays to track issues
declare -a broken_list
declare -a missing_list

# Test function for HTTP links
test_http_link() {
    local url="$1"
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url" 2>/dev/null)
    
    if [ "$status_code" = "200" ]; then
        echo -e "${GREEN}✓${NC} $url (HTTP $status_code)"
        return 0
    elif [ "$status_code" = "000" ]; then
        echo -e "${RED}✗${NC} $url (Connection failed)"
        broken_list+=("$url - Connection failed")
        return 1
    else
        echo -e "${RED}✗${NC} $url (HTTP $status_code)"
        broken_list+=("$url - HTTP $status_code")
        return 1
    fi
}

# Test function for file paths
test_file() {
    local filepath="$1"
    local description="$2"
    
    if [ -f "$filepath" ]; then
        echo -e "${GREEN}✓${NC} $description"
        return 0
    else
        echo -e "${RED}✗${NC} $description (File not found: $filepath)"
        missing_list+=("$description - $filepath")
        return 1
    fi
}

# 1. Test main page resources
echo "1. Testing Main Page Resources"
echo "-----------------------------------"

# Test CSS
((total_links++))
test_file "$ENHANCED_DIR/styles.css" "styles.css" || ((broken_links++))

# Test JavaScript
((total_links++))
test_file "$ENHANCED_DIR/script.js" "script.js" || ((broken_links++))

# Test logo
((total_links++))
test_file "$HROC_PUBLIC_DIR/08_Branding_Signatures/hrocinc.png" "Logo image (hrocinc.png)" || ((broken_links++))

echo ""

# 2. Test static HTML links
echo "2. Testing Static HTML Links"
echo "-----------------------------------"

# Notion package ZIP
((total_links++))
test_file "/Users/jonathanmallinger/Documents/HROC_Files/HROC_Public_Notion.zip" "HROC_Public_Notion.zip" || ((broken_links++))

# README.txt
((total_links++))
test_file "$HROC_PUBLIC_DIR/README.txt" "README.txt" || ((broken_links++))

# Footer policy links
((total_links++))
test_file "$HROC_PUBLIC_DIR/02_Policies/Conflict_of_Interest_Policy.pdf" "Conflict of Interest Policy" || ((broken_links++))

((total_links++))
test_file "$HROC_PUBLIC_DIR/02_Policies/Financial_Controls_and_Reimbursement_Policy.pdf" "Financial Controls Policy" || ((broken_links++))

((total_links++))
test_file "$HROC_PUBLIC_DIR/02_Policies/Whistleblower_Protection_Policy.pdf" "Whistleblower Protection Policy" || ((broken_links++))

echo ""

# 3. Test external links
echo "3. Testing External Links"
echo "-----------------------------------"

((total_links++))
test_http_link "https://fonts.googleapis.com" || ((broken_links++))

((total_links++))
test_http_link "https://fonts.gstatic.com" || ((broken_links++))

((total_links++))
test_http_link "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Poppins:wght@600;700;800&display=swap" || ((broken_links++))

echo ""

# 4. Test all dynamically loaded file links from JavaScript
echo "4. Testing Dynamically Loaded File Links (from script.js)"
echo "-----------------------------------"

# Read file paths from script.js
while IFS= read -r filepath; do
    ((total_links++))
    full_path="$HROC_PUBLIC_DIR/$filepath"
    test_file "$full_path" "$filepath" || ((broken_links++))
done << 'FILELIST'
00_Action_Plan/CLI_Workflow.txt
00_Action_Plan/Next_Actions.txt
00_Action_Plan/Schedule_30-60-90.txt
01_Governance/Articles_of_Incorporation.pdf
01_Governance/Articles_of_Incorporation_0022584962.pdf
01_Governance/Articles_of_Incorporation_Certificate.pdf
01_Governance/Articles_of_Incorporation_Congratulations_0022584962.pdf
01_Governance/Board_Meeting_First.pdf
01_Governance/Board_Meeting_First_notes.pdf
01_Governance/Board_Meeting_Special.pdf
01_Governance/Board_Meeting_Special_notes.pdf
01_Governance/Board_Resolution_2025-03.pdf
01_Governance/Board_Resolution_2025-03_signed_alt.pdf
01_Governance/Board_Resolution_2025-04.pdf
01_Governance/Board_Resolution_2025-04_signed_alt.pdf
01_Governance/Board_Roster.pdf
01_Governance/Board_Roster_Certified.pdf
01_Governance/Bylaws.pdf
01_Governance/Formation_and_Governance.pdf
01_Governance/Governance_and_Policies_Adoption.pdf
01_Governance/Governance_and_Policies_Adoption_notes.pdf
02_Policies/Code_of_Conduct_Policy.pdf
02_Policies/Conflict_of_Interest_Policy.pdf
02_Policies/Conflict_of_Interest_Policy_alt.pdf
02_Policies/Document_Retention_Policy.pdf
02_Policies/Document_Retention_and_Destruction_Policy.pdf
02_Policies/Financial_Controls_and_Reimbursement_Policy.pdf
02_Policies/Financial_Controls_and_Reimbursement_Policy_alt.pdf
02_Policies/Gift_Acceptance_Policy.pdf
02_Policies/Gift_Acceptance_and_Acknowledgment_Policy.pdf
02_Policies/Policies_and_Procedures_Overview.pdf
02_Policies/Whistleblower_Protection_Policy.pdf
03_Registrations_Licenses/Business_License_My_DOR.pdf
03_Registrations_Licenses/Business_License_Receipt_2025-08-08.pdf
03_Registrations_Licenses/Charitable_Organization_Registration_0000567751.pdf
03_Registrations_Licenses/Charity_Organization_Information_0000567751.pdf
03_Registrations_Licenses/WA_Charitable_Organization_Registration.pdf
04_IRS/IRS_CP575_EIN_Letter_39-3295288.pdf
04_IRS/IRS_CP575_EIN_Letter_copy.pdf
04_IRS/IRS_Form_1023_Application.pdf
04_IRS/IRS_Form_1023_Application_Signed.pdf
04_IRS/IRS_Form_i1023_Blank.pdf
04_IRS/IRS_General_Guidance.pdf
04_IRS/IRS_Supplemental_Packet_2025-08-11_Filled.pdf
05_Financial_Plans/Financial_Planning.pdf
05_Financial_Plans/Financial_Projections_3yr_Signed.pdf
05_Financial_Plans/Fundraising_Plan.pdf
05_Financial_Plans/Projected_Budget_2025_Signed.pdf
06_Operations_Plans/Fiscal_Sponsor_Onboarding.pdf
06_Operations_Plans/Operational_Planning.pdf
07_SPV/Annual_Report_Filing_Year_2026.pdf
07_SPV/Business_License_Application_Healing_Roots_Outreach.pdf
07_SPV/Formation_Timeline_and_Critical_Compliance_Deadlines.pdf
07_SPV/RV_Lease_Market_Analysis_for_Mobile_Outreach_Operations.pdf
07_SPV/Review_SPV_and_Fiscal_Sponsorship_Agreements.pdf
07_SPV/SPV_Documents_Index.pdf
07_SPV/SPV_LLC_Protections_and_Compliance_Checklist.pdf
07_SPV/SPV_Manager.pdf
07_SPV/SPV_Operating_Agreement.pdf
07_SPV/SPV_Organizational_Charter.pdf
07_SPV/SPV_Protection_Approval.pdf
07_SPV/SPV_Protection_Approval_notes.pdf
07_SPV/SPV_and_HROC_Agreement.pdf
08_Branding_Signatures/hrocinc.png
08_Branding_Signatures/notion_cover.png
08_Branding_Signatures/sig_BB.png
08_Branding_Signatures/sig_JDM.png
08_Branding_Signatures/sig_JDM_200.png
08_Branding_Signatures/sig_LF.png
08_Branding_Signatures/signature.png
09_Checklists_ToDos/TODO_Adopt_Document_Retention_and_Destruction_Policy.pdf
09_Checklists_ToDos/TODO_Adopt_and_Log_Final_Bylaws.pdf
09_Checklists_ToDos/TODO_Approve_Conflict_of_Interest_and_Collect_Signed_Forms.pdf
09_Checklists_ToDos/TODO_Create_Donation_Acceptance_and_Acknowledgment_Process.pdf
09_Checklists_ToDos/TODO_Establish_Financial_Controls.pdf
09_Checklists_ToDos/TODO_Open_Nonprofit_Bank_Account.pdf
09_Checklists_ToDos/TODO_Publish_Transparency_Hub.pdf
09_Checklists_ToDos/TODO_Register_with_WA_Charities_Program_SOS.pdf
09_Checklists_ToDos/TODO_Setup_IRS_Form_990N_990EZ_Process.pdf
99_Misc_Guides/IRS_Guidance_Brief_Primer.pdf
99_Misc_Guides/IRS_Official_Guidance.pdf
99_Misc_Guides/Starting_a_Nonprofit_in_WA_Guide_2023.pdf
99_Misc_Guides/Z_Proton_Recovery_Kit.pdf
FILELIST

echo ""
echo "========================================="
echo "SUMMARY"
echo "========================================="
echo "Total links checked: $total_links"
echo -e "Successful: ${GREEN}$((total_links - broken_links))${NC}"
echo -e "Broken/Missing: ${RED}$broken_links${NC}"
echo ""

if [ $broken_links -gt 0 ]; then
    echo "========================================="
    echo "ISSUES FOUND"
    echo "========================================="
    
    if [ ${#missing_list[@]} -gt 0 ]; then
        echo ""
        echo "Missing Files:"
        for item in "${missing_list[@]}"; do
            echo -e "  ${RED}•${NC} $item"
        done
    fi
    
    if [ ${#broken_list[@]} -gt 0 ]; then
        echo ""
        echo "Broken HTTP Links:"
        for item in "${broken_list[@]}"; do
            echo -e "  ${RED}•${NC} $item"
        done
    fi
    
    echo ""
    exit 1
else
    echo -e "${GREEN}All links are working correctly!${NC}"
    exit 0
fi
