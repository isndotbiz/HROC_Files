#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Redesign service pages with:
1. Reduced text (50% less)
2. Table-based layout (image | text, alternating)
3. New image prompts for generation
"""
import sys
import io
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

SERVICE_REDESIGNS = {
    'service-overdose-prevention': {
        'title': 'Overdose Prevention',
        'sections': [
            {
                'heading': 'What We Provide',
                'text': 'Overdose is preventable. We distribute free naloxone kits, fentanyl test strips, and overdose response training directly to people in our community. Over 5,000 naloxone kits distributed. Every kit represents a life saved.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Program Components',
                'text': '• Naloxone Distribution: Free kits with instructions\n• Overdose Response Training: Community education\n• Fentanyl Test Strips: No-cost harm reduction\n• Peer Support: Lived-experience counselors\n• Healthcare Linkage: Connection to treatment',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'How to Access',
                'text': 'Find us 3-5 days per week throughout King and Pierce Counties. Mobile outreach brings naloxone directly to communities. Call 253-881-7377 or text to schedule training. Free, confidential, judgment-free services.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-syringe-exchange': {
        'title': 'Syringe Exchange Services',
        'sections': [
            {
                'heading': 'What is Syringe Exchange?',
                'text': 'Evidence-based harm reduction saves lives. We provide sterile syringes, safer injection equipment, disease prevention testing, and peer support to people who inject drugs. No requirements, no judgment, no limits on supplies.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Services Offered',
                'text': '• Sterile Injection Equipment: Multiple gauges, free\n• Safe Disposal: Puncture-resistant containers\n• Disease Testing: HIV, Hepatitis C screening\n• Wound Care: Assessment and treatment\n• Overdose Prevention: Naloxone distribution\n• Peer Navigation: Treatment connections',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Impact & Access',
                'text': '15,000+ sterile syringes distributed. 500+ people connected to care. Research shows syringe exchange reduces HIV transmission by 50% and increases treatment entry 5x. Mobile outreach 3-5 days weekly. Call 253-881-7377.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-wound-care': {
        'title': 'Wound Care Services',
        'sections': [
            {
                'heading': 'Why Wound Care Matters',
                'text': 'Untreated wounds become life-threatening infections. We provide professional assessment, sterile cleaning, infection prevention, and emergency referrals. 500+ wounds treated annually with 95% infection prevention rate.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Services Offered',
                'text': '• Wound Assessment: Professional evaluation\n• First Aid & Cleaning: Sterile technique\n• Infection Prevention: Education & supplies\n• Abscess Management: Drainage support\n• Chronic Wound Care: Long-term follow-up\n• Medical Referrals: Emergency transport',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'How to Access',
                'text': 'Find our mobile unit 3-5 days per week in King and Pierce Counties. No appointment needed. Free, confidential, judgment-free care. Call 253-881-7377 for urgent wounds or to request a visit.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-health-screening': {
        'title': 'Health Screening Services',
        'sections': [
            {
                'heading': 'What We Screen',
                'text': 'Free health screenings connect people to care early. We test for HIV, Hepatitis C, blood pressure, diabetes, and other common conditions. Early detection prevents complications and saves lives.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Services Offered',
                'text': '• Blood-borne Disease Testing: HIV, HCV rapid tests\n• Vital Signs: Blood pressure, temperature\n• Health Education: Prevention & management\n• Referrals: Connection to primary care\n• Vaccination: Hepatitis A & B series\n• Documentation: Medical records for continuity',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Access & Support',
                'text': 'Mobile health screening 3-5 days per week. No insurance, ID, or appointment required. Results explained with compassion. Peer navigators help connect you to treatment. Call 253-881-7377.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-peer-support': {
        'title': 'Peer Support Services',
        'sections': [
            {
                'heading': 'What is Peer Support?',
                'text': 'Lived experience creates trust. Our peer counselors understand substance use, homelessness, and recovery from direct experience. We provide crisis support, resource navigation, and hope for healing.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Support We Provide',
                'text': '• Crisis Intervention: 24/7 support available\n• Resource Navigation: Housing, benefits, food\n• Treatment Connections: Medication-assisted care\n• Harm Reduction Counseling: Non-judgmental guidance\n• Case Management: Long-term support planning\n• Community Building: Peer groups & activities',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Get Support',
                'text': 'Connect with peer counselors during mobile outreach or call 253-881-7377 anytime. Free, confidential, judgment-free support. We meet you where you are on your recovery journey.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-housing-support': {
        'title': 'Housing Support Services',
        'sections': [
            {
                'heading': 'Why Housing Matters',
                'text': 'Housing is health care. We help people access emergency shelter, transitional housing, and permanent supportive housing. Stable housing enables recovery and health.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Support Offered',
                'text': '• Emergency Shelter: Referral & placement\n• Transitional Housing: Bridge to stability\n• Permanent Supportive Housing: Long-term solutions\n• Housing Navigation: Barrier removal\n• Rental Assistance: Financial support\n• Case Management: Coordinated support',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Access Housing Help',
                'text': 'No one sleeps outside if we can help. Call 253-881-7377 for housing navigation. Peer navigators work to solve barriers to housing. Free support connecting you to shelter and stability.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-cultural-healing': {
        'title': 'Cultural Healing Services',
        'sections': [
            {
                'heading': 'Indigenous-Led Healing',
                'text': 'Our Indigenous roots inform our approach to healing. We integrate traditional healing practices with harm reduction. Cultural connection supports recovery and wellness for all community members.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Healing Offered',
                'text': '• Traditional Practices: Smudging, talking circles\n• Cultural Connection: Community events\n• Spiritual Support: Honoring diverse beliefs\n• Healing Circles: Peer-led support groups\n• Arts & Expression: Creative healing\n• Land-Based Activities: Connection to nature',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Join Us',
                'text': 'Healing is personal and cultural. Join circles, events, and activities that honor your identity and support your recovery. Call 253-881-7377 to learn about upcoming gatherings.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-education-training': {
        'title': 'Education & Training Services',
        'sections': [
            {
                'heading': 'What We Teach',
                'text': 'Education empowers change. We provide training on harm reduction, overdose response, safer substance use, blood-borne disease prevention, and health literacy to individuals and organizations.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Training Topics',
                'text': '• Overdose Response: Recognition & naloxone use\n• Safer Injection: Vein care & harm reduction\n• Disease Prevention: Blood-borne infection screening\n• Mental Health: Trauma-informed approaches\n• Resource Navigation: Finding community support\n• Leadership Development: Peer trainer certification',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Get Trained',
                'text': 'Community training provided free 3-5 days per week. Organization training available by request. Call 253-881-7377 to schedule education at your location.',
                'image': 4,
                'layout': 'left'
            }
        ]
    },
    'service-resource-navigation': {
        'title': 'Resource Navigation Services',
        'sections': [
            {
                'heading': 'Finding Your Way',
                'text': 'Systems are complex. Our navigators help you find housing, benefits, healthcare, employment, food, and community resources. One-on-one support removes barriers to access.',
                'image': 2,
                'layout': 'left'
            },
            {
                'heading': 'Resources Accessed',
                'text': '• Housing: Shelter, transitional, permanent\n• Income: Benefits, food stamps, employment\n• Healthcare: Primary care, specialists, mental health\n• Legal: Public defender, expungement support\n• ID: Replacement documents\n• Community: Peer groups, events, activities',
                'image': 3,
                'layout': 'right'
            },
            {
                'heading': 'Start Navigating',
                'text': 'Don\'t navigate alone. Our peer navigators remove barriers and find solutions. Free, confidential support. Call 253-881-7377 to start getting connected to resources.',
                'image': 4,
                'layout': 'left'
            }
        ]
    }
}

def create_table_row(image_url, image_caption, text, layout='left', img_width='300px'):
    """Create a table row with image and text"""
    padding = '20px'

    if layout == 'left':
        return f'''        <tr>
          <td style="width: 45%; padding: {padding}; vertical-align: top;">
            <img src="{image_url}" alt="{image_caption}" style="width: {img_width}; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy">
            <p style="text-align: center; font-size: 14px; color: #666; margin-top: 10px;"><em>{image_caption}</em></p>
          </td>
          <td style="width: 55%; padding: {padding}; vertical-align: top; line-height: 1.6;">
            {text}
          </td>
        </tr>'''
    else:  # right
        return f'''        <tr>
          <td style="width: 55%; padding: {padding}; vertical-align: top; line-height: 1.6;">
            {text}
          </td>
          <td style="width: 45%; padding: {padding}; vertical-align: top;">
            <img src="{image_url}" alt="{image_caption}" style="width: {img_width}; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy">
            <p style="text-align: center; font-size: 14px; color: #666; margin-top: 10px;"><em>{image_caption}</em></p>
          </td>
        </tr>'''

def convert_section_text(text):
    """Convert bullet points to HTML"""
    lines = text.split('\n')
    html_lines = []
    for line in lines:
        if line.startswith('•'):
            html_lines.append(f'<div style="margin: 8px 0; padding-left: 20px;">{line}</div>')
        else:
            html_lines.append(f'<p style="margin: 12px 0;">{line}</p>')
    return ''.join(html_lines)

def main():
    print("\n" + "="*60)
    print("Redesigning service pages with table layout")
    print("="*60 + "\n")

    # For now, just print the image prompts that should be generated
    print("📸 IMAGE GENERATION NEEDED:")
    print("Generate new images for each service with these themes:\n")

    image_prompts = {
        'service-overdose-prevention': [
            'Image 2: Healthcare worker holding naloxone kits and fentanyl test strips in a modern clinic setting, professional photography',
            'Image 3: Diverse peer counselors conducting overdose prevention training in community center, real people',
            'Image 4: Mobile outreach van parked in Seattle neighborhood with community members accessing services'
        ],
        'service-syringe-exchange': [
            'Image 2: Organized display of sterile syringes and safer injection supplies in multiple gauges',
            'Image 3: Peer health worker conducting health screening and education session',
            'Image 4: Mobile outreach unit with healthcare providers and community members'
        ],
        'service-wound-care': [
            'Image 2: Healthcare worker performing professional wound assessment and care',
            'Image 3: Supplies for wound care laid out professionally - bandages, sterile gloves, dressings',
            'Image 4: Mobile unit providing wound care to community member'
        ],
        'service-health-screening': [
            'Image 2: Health screening station with rapid test kits and vital sign equipment',
            'Image 3: Peer health worker taking vital signs and explaining results',
            'Image 4: Community health event with multiple people being screened'
        ],
        'service-peer-support': [
            'Image 2: Peer counselors in supportive conversation, diverse group',
            'Image 3: Support group circle in community space',
            'Image 4: Peer navigators helping someone access resources'
        ],
        'service-housing-support': [
            'Image 2: Housing options displayed - shelter, transitional, permanent supportive housing',
            'Image 3: Housing navigator helping someone fill out applications',
            'Image 4: Person moving into stable housing with support'
        ],
        'service-cultural-healing': [
            'Image 2: Indigenous healing circle with traditional elements',
            'Image 3: Community members in cultural gathering space',
            'Image 4: Land-based healing activity in nature'
        ],
        'service-education-training': [
            'Image 2: Trainer demonstrating naloxone use to community',
            'Image 3: Interactive training session with diverse participants',
            'Image 4: Certified peer trainers presenting at community event'
        ],
        'service-resource-navigation': [
            'Image 2: Resource guide or navigator tool with pathways',
            'Image 3: Navigator meeting with person to plan resources',
            'Image 4: Success story - person accessing multiple resources'
        ]
    }

    for service, prompts in image_prompts.items():
        print(f"\n{service}:")
        for prompt in prompts:
            print(f"  • {prompt}")

    print("\n" + "="*60)
    print("Next: Run image generation, then redesign HTML pages")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
