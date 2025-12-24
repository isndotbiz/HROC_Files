#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate redesigned service pages with table layout and reduced text
"""
import sys
import io
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Service redesigns with reduced text and table layout
SERVICES = {
    'service-overdose-prevention': {
        'title': 'Overdose Prevention',
        'icon': '💊',
        'color': '#E91E8C',
        'sections': [
            ('What We Provide', 'Overdose is preventable. We distribute free naloxone kits, fentanyl test strips, and overdose response training directly to people in our community. Over 5,000 naloxone kits distributed. Every kit represents a life saved.', 2, 'left'),
            ('Program Components', '• Naloxone Distribution: Free kits with instructions\n• Overdose Response Training: Community education\n• Fentanyl Test Strips: No-cost harm reduction\n• Peer Support: Lived-experience counselors\n• Healthcare Linkage: Connection to treatment', 3, 'right'),
            ('How to Access', 'Find us 3-5 days per week throughout King and Pierce Counties. Mobile outreach brings naloxone directly to communities. Call 253-881-7377 or text to schedule training. Free, confidential, judgment-free services.', 4, 'left'),
        ]
    },
    'service-syringe-exchange': {
        'title': 'Syringe Exchange Services',
        'icon': '💉',
        'color': '#00D4E8',
        'sections': [
            ('What is Syringe Exchange?', 'Evidence-based harm reduction saves lives. We provide sterile syringes, safer injection equipment, disease prevention testing, and peer support to people who inject drugs. No requirements, no judgment, no limits on supplies.', 2, 'left'),
            ('Services Offered', '• Sterile Injection Equipment: Multiple gauges, free\n• Safe Disposal: Puncture-resistant containers\n• Disease Testing: HIV, Hepatitis C screening\n• Wound Care: Assessment and treatment\n• Overdose Prevention: Naloxone distribution\n• Peer Navigation: Treatment connections', 3, 'right'),
            ('Impact & Access', '15,000+ sterile syringes distributed. 500+ people connected to care. Research shows syringe exchange reduces HIV transmission by 50% and increases treatment entry 5x. Mobile outreach 3-5 days weekly. Call 253-881-7377.', 4, 'left'),
        ]
    },
    'service-wound-care': {
        'title': 'Wound Care Services',
        'icon': '🩹',
        'color': '#C8E800',
        'sections': [
            ('Why Wound Care Matters', 'Untreated wounds become life-threatening infections. We provide professional assessment, sterile cleaning, infection prevention, and emergency referrals. 500+ wounds treated annually with 95% infection prevention rate.', 2, 'left'),
            ('Services Offered', '• Wound Assessment: Professional evaluation\n• First Aid & Cleaning: Sterile technique\n• Infection Prevention: Education & supplies\n• Abscess Management: Drainage support\n• Chronic Wound Care: Long-term follow-up\n• Medical Referrals: Emergency transport', 3, 'right'),
            ('How to Access', 'Find our mobile unit 3-5 days per week in King and Pierce Counties. No appointment needed. Free, confidential, judgment-free care. Call 253-881-7377 for urgent wounds or to request a visit.', 4, 'left'),
        ]
    },
    'service-health-screening': {
        'title': 'Health Screening Services',
        'icon': '🩺',
        'color': '#FFE600',
        'sections': [
            ('What We Screen', 'Free health screenings connect people to care early. We test for HIV, Hepatitis C, blood pressure, diabetes, and other common conditions. Early detection prevents complications and saves lives.', 2, 'left'),
            ('Services Offered', '• Blood-borne Disease Testing: HIV, HCV rapid tests\n• Vital Signs: Blood pressure, temperature\n• Health Education: Prevention & management\n• Referrals: Connection to primary care\n• Vaccination: Hepatitis A & B series\n• Documentation: Medical records for continuity', 3, 'right'),
            ('Access & Support', 'Mobile health screening 3-5 days per week. No insurance, ID, or appointment required. Results explained with compassion. Peer navigators help connect you to treatment. Call 253-881-7377.', 4, 'left'),
        ]
    },
    'service-peer-support': {
        'title': 'Peer Support Services',
        'icon': '🤝',
        'color': '#E91E8C',
        'sections': [
            ('What is Peer Support?', 'Lived experience creates trust. Our peer counselors understand substance use, homelessness, and recovery from direct experience. We provide crisis support, resource navigation, and hope for healing.', 2, 'left'),
            ('Support We Provide', '• Crisis Intervention: 24/7 support available\n• Resource Navigation: Housing, benefits, food\n• Treatment Connections: Medication-assisted care\n• Harm Reduction Counseling: Non-judgmental guidance\n• Case Management: Long-term support planning\n• Community Building: Peer groups & activities', 3, 'right'),
            ('Get Support', 'Connect with peer counselors during mobile outreach or call 253-881-7377 anytime. Free, confidential, judgment-free support. We meet you where you are on your recovery journey.', 4, 'left'),
        ]
    },
    'service-housing-support': {
        'title': 'Housing Support Services',
        'icon': '🏠',
        'color': '#00D4E8',
        'sections': [
            ('Why Housing Matters', 'Housing is health care. We help people access emergency shelter, transitional housing, and permanent supportive housing. Stable housing enables recovery and health.', 2, 'left'),
            ('Support Offered', '• Emergency Shelter: Referral & placement\n• Transitional Housing: Bridge to stability\n• Permanent Supportive Housing: Long-term solutions\n• Housing Navigation: Barrier removal\n• Rental Assistance: Financial support\n• Case Management: Coordinated support', 3, 'right'),
            ('Access Housing Help', 'No one sleeps outside if we can help. Call 253-881-7377 for housing navigation. Peer navigators work to solve barriers to housing. Free support connecting you to shelter and stability.', 4, 'left'),
        ]
    },
    'service-cultural-healing': {
        'title': 'Cultural Healing Services',
        'icon': '🌱',
        'color': '#C8E800',
        'sections': [
            ('Indigenous-Led Healing', 'Our Indigenous roots inform our approach to healing. We integrate traditional healing practices with harm reduction. Cultural connection supports recovery and wellness for all community members.', 2, 'left'),
            ('Healing Offered', '• Traditional Practices: Smudging, talking circles\n• Cultural Connection: Community events\n• Spiritual Support: Honoring diverse beliefs\n• Healing Circles: Peer-led support groups\n• Arts & Expression: Creative healing\n• Land-Based Activities: Connection to nature', 3, 'right'),
            ('Join Us', 'Healing is personal and cultural. Join circles, events, and activities that honor your identity and support your recovery. Call 253-881-7377 to learn about upcoming gatherings.', 4, 'left'),
        ]
    },
    'service-education-training': {
        'title': 'Education & Training Services',
        'icon': '📚',
        'color': '#FFE600',
        'sections': [
            ('What We Teach', 'Education empowers change. We provide training on harm reduction, overdose response, safer substance use, blood-borne disease prevention, and health literacy to individuals and organizations.', 2, 'left'),
            ('Training Topics', '• Overdose Response: Recognition & naloxone use\n• Safer Injection: Vein care & harm reduction\n• Disease Prevention: Blood-borne infection screening\n• Mental Health: Trauma-informed approaches\n• Resource Navigation: Finding community support\n• Leadership Development: Peer trainer certification', 3, 'right'),
            ('Get Trained', 'Community training provided free 3-5 days per week. Organization training available by request. Call 253-881-7377 to schedule education at your location.', 4, 'left'),
        ]
    },
    'service-resource-navigation': {
        'title': 'Resource Navigation Services',
        'icon': '🗺️',
        'color': '#E91E8C',
        'sections': [
            ('Finding Your Way', 'Systems are complex. Our navigators help you find housing, benefits, healthcare, employment, food, and community resources. One-on-one support removes barriers to access.', 2, 'left'),
            ('Resources Accessed', '• Housing: Shelter, transitional, permanent\n• Income: Benefits, food stamps, employment\n• Healthcare: Primary care, specialists, mental health\n• Legal: Public defender, expungement support\n• ID: Replacement documents\n• Community: Peer groups, events, activities', 3, 'right'),
            ('Start Navigating', 'Don\'t navigate alone. Our peer navigators remove barriers and find solutions. Free, confidential support. Call 253-881-7377 to start getting connected to resources.', 4, 'left'),
        ]
    },
}

def create_table_content(heading, text, image_id, service_name, layout):
    """Create HTML for table rows with alternating layout"""
    image_url = f'https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service_name}/{image_id}.png'
    image_caption = heading

    # Convert bullet points to divs
    text_html = ''
    for line in text.split('\n'):
        if line.startswith('•'):
            text_html += f'        <div style="margin: 8px 0; font-size: 15px; line-height: 1.5;">{line}</div>\n'
        else:
            text_html += f'        <p style="margin: 12px 0; font-size: 15px; line-height: 1.6;">{line}</p>\n'

    if layout == 'left':
        return f'''      <tr>
        <td style="width: 45%; padding: 30px; vertical-align: top;">
          <img src="{image_url}" alt="{image_caption}" style="width: 100%; max-width: 300px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" loading="lazy">
          <p style="text-align: center; font-size: 14px; color: #666; margin-top: 15px; font-weight: 500;">{image_caption}</p>
        </td>
        <td style="width: 55%; padding: 30px; vertical-align: top;">
          <h2 style="color: #333; margin-bottom: 15px; font-size: 22px;">{heading}</h2>
{text_html}        </td>
      </tr>
'''
    else:  # right
        return f'''      <tr>
        <td style="width: 55%; padding: 30px; vertical-align: top;">
          <h2 style="color: #333; margin-bottom: 15px; font-size: 22px;">{heading}</h2>
{text_html}        </td>
        <td style="width: 45%; padding: 30px; vertical-align: top;">
          <img src="{image_url}" alt="{image_caption}" style="width: 100%; max-width: 300px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" loading="lazy">
          <p style="text-align: center; font-size: 14px; color: #666; margin-top: 15px; font-weight: 500;">{image_caption}</p>
        </td>
      </tr>
'''

def generate_service_page(service_name, service_data):
    """Generate complete HTML for a service page"""
    title = service_data['title']
    icon = service_data['icon']

    # Build table rows
    table_rows = ''
    for heading, text, image_id, layout in service_data['sections']:
        table_rows += create_table_content(heading, text, image_id, service_name, layout)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{title} - Healing Roots Outreach Collective">
  <title>{title} | Healing Roots Outreach Collective</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" type="image/png" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23E91E8C'/><text x='50' y='60' font-size='60' text-anchor='middle' fill='white' font-weight='bold'>🌱</text></svg>">
</head>
<body>

  <!-- Skip to main content -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Crisis Banner -->
  <div class="crisis-banner" role="banner" aria-label="Emergency contact information">
    <div class="container">
      <div class="crisis-content">
        <span class="crisis-icon" aria-hidden="true">🚨</span>
        <p class="crisis-text"><strong>Need help now?</strong> Call or text us</p>
        <div class="crisis-actions">
          <a href="tel:+12538817377" class="crisis-btn crisis-btn-call" aria-label="Call 253-881-7377"><span aria-hidden="true">📞</span> Call</a>
          <a href="sms:+12538817377" class="crisis-btn crisis-btn-text" aria-label="Text 253-881-7377"><span aria-hidden="true">💬</span> Text</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Navigation -->
  <header class="main-header" role="banner">
    <div class="container">
      <div class="header-content">
        <div class="logo-wrapper">
          <div class="logo" style="width:50px; height:50px; background: linear-gradient(135deg, #E91E8C, #00D4E8); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 28px;">🌱</div>
          <div class="org-info">
            <h1 class="org-name">Healing Roots Outreach Collective</h1>
            <p class="org-tagline">Indigenous-Led Mobile Harm Reduction</p>
          </div>
        </div>
        <button class="mobile-menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="main-nav">
          <span class="hamburger" aria-hidden="true"></span>
        </button>
        <nav id="main-nav" class="main-nav" role="navigation" aria-label="Main navigation">
          <ul class="nav-list">
            <li><a href="index.html#services">Services</a></li>
            <li><a href="index.html#about">About</a></li>
            <li><a href="index.html#impact">Impact</a></li>
            <li><a href="documents.html">Documents</a></li>
            <li><a href="index.html#contact">Contact</a></li>
            <li><a href="index.html#donate" class="nav-btn-donate">Donate</a></li>
          </ul>
        </nav>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main id="main-content">

    <!-- Service Hero Section -->
    <section class="service-hero" style="background: linear-gradient(135deg, #E91E8C 0%, #00D4E8 100%);">
      <div class="container">
        <div class="service-hero-content">
          <h1>{title}</h1>
          <p class="service-hero-subtitle">Mobile harm reduction and community care</p>
        </div>
      </div>
    </section>

    <!-- Service Content with Table Layout -->
    <section class="service-detail">
      <div class="container">
        <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
          <tbody>
{table_rows}          </tbody>
        </table>

        <!-- Call to Action -->
        <div style="margin-top: 40px; padding: 40px; background: linear-gradient(135deg, #E91E8C 0%, #00D4E8 100%); border-radius: 8px; color: white; text-align: center;">
          <h2 style="color: white; margin-bottom: 15px;">Need Our Services?</h2>
          <p style="font-size: 16px; margin-bottom: 20px;">Call or text us anytime. Free, confidential, judgment-free care.</p>
          <a href="tel:+12538817377" class="btn btn-primary" style="background: white; color: #E91E8C; padding: 12px 30px; border-radius: 6px; text-decoration: none; font-weight: 600; display: inline-block; margin: 0 10px;">📞 253-881-7377</a>
          <a href="index.html#services" class="btn btn-secondary" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 30px; border-radius: 6px; text-decoration: none; font-weight: 600; display: inline-block; margin: 0 10px; border: 2px solid white;">View All Services</a>
        </div>

      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>Healing Roots Outreach Collective</h3>
          <p>Indigenous-led, trauma-informed mobile harm reduction services in Pierce County, WA.</p>
          <p><strong>EIN:</strong> 93-3295288 | <strong>501(c)(3)</strong> Nonprofit</p>
        </div>

        <div class="footer-section">
          <h3>About</h3>
          <ul>
            <li><a href="index.html#services">Our Services</a></li>
            <li><a href="index.html#about">About Us</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
        </div>

        <div class="footer-section">
          <h3>Contact</h3>
          <p>📧 <a href="mailto:admin@healingrootsoutreachcollective.org">admin@healingrootsoutreachcollective.org</a></p>
          <p>📞 <a href="tel:2536789186">(253) 678-9186</a></p>
          <p>📍 Serving Pierce County, WA</p>
        </div>
      </div>

      <!-- Official Documents & Policies Section -->
      <div class="footer-documents-section">
        <h3>Official Documents & Policies</h3>
        <p class="footer-docs-intro">Healing Roots Outreach Collective is fully transparent and compliant with all Washington State and federal requirements. <a href="documents.html">View complete policy library</a>.</p>

        <div class="documents-grid">
          <div class="document-category">
            <h4>📜 Available Policies</h4>
            <ul class="footer-links">
              <li><a href="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/pdfs/Policies/Conflict_of_Interest_Policy.pdf" target="_blank">Conflict of Interest Policy</a></li>
              <li><a href="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/pdfs/Policies/Financial_Controls_and_Reimbursement_Policy.pdf" target="_blank">Financial Controls & Reimbursement</a></li>
              <li><a href="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/pdfs/Policies/Whistleblower_Protection_Policy.pdf" target="_blank">Whistleblower Protection Policy</a></li>
              <li><a href="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/pdfs/Policies/Code_of_Conduct_Policy.pdf" target="_blank">Code of Conduct Policy</a></li>
            </ul>
          </div>

          <div class="document-category">
            <h4>📋 Registration & Tax</h4>
            <ul class="footer-links">
              <li><a href="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/pdfs/Registrations_Licenses/501c3-awarded.pdf" target="_blank">501(c)(3) Award Letter</a></li>
              <li><strong>Washington UBI:</strong> 605 944 010</li>
              <li><strong>EIN:</strong> 39-3295288</li>
              <li><strong>WA Charity Reg:</strong> 2011817</li>
              <li><strong>Status:</strong> 501(c)(3) Tax-Exempt</li>
            </ul>
          </div>

          <div class="document-category">
            <h4>🔗 Transparency</h4>
            <ul class="footer-links">
              <li><a href="documents.html">Complete Document Library</a></li>
              <li><a href="https://www.sos.wa.gov/charities" target="_blank">WA Secretary of State</a></li>
              <li><a href="https://www.irs.gov/charities-non-profits" target="_blank">IRS Non-Profit Info</a></li>
            </ul>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2025 Healing Roots Outreach Collective. All rights reserved.</p>
        <p><small>WA State Charitable Solicitations disclosure: Financial information available upon request from WA Secretary of State or at <a href="https://www.sos.wa.gov/charities" target="_blank">www.sos.wa.gov/charities</a></small></p>
      </div>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
'''
    return html

def main():
    print("\n" + "="*60)
    print("Generating redesigned service pages with table layout")
    print("="*60 + "\n")

    generated = 0
    for service_name, service_data in SERVICES.items():
        html = generate_service_page(service_name, service_data)
        file_path = Path(f'HROC_Website_New/{service_name}.html')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ Generated: {service_name}.html")
        generated += 1

    print("\n" + "="*60)
    print(f"Generated {generated}/9 service pages with table layout")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
