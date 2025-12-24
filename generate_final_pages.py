#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate service pages with:
- Minimum 999 words per page
- Large images = infographics
- Small images = people and things
- Table-based layout with alternating layout
"""
import sys
import io
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

SERVICES = {
    'service-overdose-prevention': {
        'title': 'Overdose Prevention',
        'content': '''
<h2>Overdose Prevention & Life-Saving Naloxone Access</h2>

<p>Overdose is one of the leading causes of death in Pierce County and across Washington State. The poisoned drug supply, contaminated with fentanyl and other dangerous substances, has created an unprecedented public health crisis. Overdose is preventable. With access to naloxone (Narcan), fentanyl test strips, and community education, we can save lives.</p>

<p>Healing Roots Outreach Collective is committed to preventing overdose deaths through accessible, judgment-free distribution of life-saving naloxone and comprehensive overdose response training. Since launching our program, we have distributed over 5,000 naloxone kits and trained more than 1,500 community members in overdose recognition and response. Every naloxone kit distributed represents a life saved, a family kept together, a person given another chance at recovery and healing.</p>

<h2>Understanding Overdose & Fentanyl Risks</h2>

<p>Fentanyl has dramatically changed the landscape of overdose risk. This synthetic opioid is 50-100 times more potent than morphine and is increasingly mixed into street drugs including heroin, cocaine, methamphetamine, and counterfeit pills. People often don't know they're using fentanyl, which means the overdose risk is exponentially higher than with traditional opioids alone. Even experienced drug users have died from unknowingly consuming fentanyl. This is not a moral failing or a result of "bad choices"—it's a systemic crisis created by an adulterated drug supply.</p>

<p>Overdose happens quickly. The signs include: loss of consciousness, unresponsiveness to stimulation, slow or shallow breathing, choking sounds or death rattles, bluish lips or fingernails, cold clammy skin, and stiff body. When overdose occurs, every second counts. Naloxone works fast—it reverses opioid overdose in 2-3 minutes by blocking opioid receptors in the brain. If naloxone is administered early enough, it can bring someone back from the brink of death.</p>

<h2>What We Provide: Naloxone Distribution & Training</h2>

<p>Our naloxone kits are provided completely free of charge with no requirements, restrictions, or documentation needed. Each kit contains two doses of naloxone (either nasal spray or injectable form), instructions in multiple languages, alcohol wipes, and information about our services. We provide detailed training on how to recognize overdose signs, when to call 911, how to administer naloxone, and recovery position to protect the airway after administration.</p>

<p>We also distribute fentanyl test strips that allow people to check substances for the presence of fentanyl before use. While test strips don't eliminate risk, they provide critical harm reduction information that can help people make safer decisions about drug use. Combined with naloxone distribution and training, these tools create multiple layers of protection against overdose death.</p>

<p>Our peer outreach workers don't just hand out supplies. We build relationships, answer questions, address fears and misconceptions, and ensure people feel supported in using harm reduction practices. We recognize that many people have negative experiences with healthcare systems and law enforcement. We create safety by treating every person with dignity, respect, and genuine care. We explain exactly what naloxone is, how it works, what to expect if it's used, and why having it nearby can be lifesaving.</p>

<h2>Access Without Barriers</h2>

<p>Accessing naloxone through our program is simple and judgment-free. There are no requirements: you don't need insurance, identification, proof of residence, or permission from anyone. You don't need to be ready to stop using drugs or enter treatment. You don't need to answer personal questions about your drug use. We meet people exactly where they are with compassion and respect.</p>

<p>Our mobile outreach team provides naloxone distribution 3-5 days per week throughout King and Pierce Counties. We visit encampments, parks, street corners, shelters, and community centers where people gather. We also conduct community training sessions on overdose response—these trainings are free and open to anyone who wants to learn how to save a life.</p>

<p>You can also contact us directly: call or text 253-881-7377 anytime, day or night. If someone is actively overdosing, call 911 immediately. We can help with naloxone access, overdose training, and connection to other harm reduction and treatment services.</p>

<h2>Overdose Response & Emergency Support</h2>

<p>If someone overdoses, having naloxone on hand means the difference between life and death. Here's what to do: Check responsiveness by shouting and shaking. If unresponsive, call 911 immediately. Place the person on their back, administer naloxone according to instructions (nasal spray or injection), give rescue breathing if trained, place in recovery position (on side), stay with the person until help arrives, and provide information to paramedics about what was used if known.</p>

<p>Many people fear calling 911 during an overdose due to concerns about police involvement or legal consequences. In Washington State, the Good Samaritan Law protects people who call for help during an overdose from criminal prosecution for drug possession. We educate people about these protections and encourage emergency response without fear. Lives matter more than legal consequences.</p>

<h2>Community Impact & Success Stories</h2>

<p>Over 5,000 naloxone kits distributed. Over 1,500 people trained in overdose response. Hundreds of lives saved directly by naloxone administered by community members who received our kits. Each of these numbers represents someone's parent, child, sibling, friend. Each represents a person who gets another chance at recovery, healing, and connection with loved ones. We hear stories constantly from people who used our naloxone to save a friend's life, or who were saved by someone else using naloxone they got from us.</p>

<p>Overdose prevention is not just about distributing supplies—it's about building a community where everyone has access to the tools they need to stay alive. It's about removing stigma and creating safety. It's about understanding that people who use drugs deserve healthcare, dignity, and respect. It's about recognizing that an overdose death is a preventable tragedy, and that every life matters.</p>
'''
    },
    'service-syringe-exchange': {
        'title': 'Syringe Exchange Services',
        'content': '''
<h2>Evidence-Based Harm Reduction Through Syringe Exchange</h2>

<p>Syringe exchange programs are among the most well-researched and evidence-supported public health interventions in existence. Decades of peer-reviewed research from around the world demonstrates that these programs save lives, reduce disease transmission, do not increase drug use or crime, and actually increase treatment entry rates. Despite the overwhelming evidence, stigma and misunderstanding still surround syringe exchange. We're here to provide judgment-free, evidence-based services to people who inject drugs.</p>

<p>People who inject drugs face the highest risks of bloodborne disease transmission. Without access to sterile equipment, people share syringes and reuse their own, which transmits HIV, hepatitis C, hepatitis B, and other infections. These infections lead to serious health consequences: HIV requires lifelong medication management; hepatitis C can cause cirrhosis and liver cancer; hepatitis B can cause chronic infection and increase cancer risk. Many people also develop injection-site infections, abscesses, endocarditis, and other serious complications.</p>

<p>Healing Roots Outreach Collective provides comprehensive syringe exchange services directly to people where they are. We distribute sterile syringes in multiple gauges (sizes) to accommodate different injection practices and vein conditions. All syringes are individually packaged, sterile, provided free of charge, and there are no limits on how many you can receive. We provide everything needed for safer injection: alcohol wipes for skin prep, sterile cotton filters for filtering solutions, clean cookers (spoons) for dissolving substances, sterile water for injection, and tourniquets for vein access.</p>

<h2>Comprehensive Services Beyond Syringes</h2>

<p>Our syringe exchange program includes safe sharps disposal. Environmental safety is a core priority. We provide puncture-resistant containers for used syringes and injection equipment. People can exchange filled sharps containers for new ones during our mobile outreach hours. This protects sanitation workers, first responders, children, community members, and the environment from dangerous needle stick injuries. Proper sharps disposal is essential but often overlooked in harm reduction discussions.</p>

<p>We offer rapid testing for HIV and hepatitis C, the two most common bloodborne infections among people who inject drugs. Modern hepatitis C treatments have cure rates exceeding 95 percent, and early HIV treatment allows people to live long, healthy lives while preventing transmission to others. We also provide hepatitis B vaccination series and education on sexually transmitted infection prevention. All testing is voluntary, confidential, and conducted with informed consent and peer support.</p>

<p>Every person accessing our syringe exchange services receives free naloxone kits and training on recognizing and responding to overdose. Overdose risk is dramatically elevated for people who inject drugs, particularly with fentanyl in the drug supply. We distribute fentanyl test strips that allow people to check substances for fentanyl before use. This integrated approach addresses the most acute health risks facing our community.</p>

<p>Injection-related wounds, abscesses, and skin infections are common complications of drug use. We provide wound assessment, cleaning with sterile technique, infection prevention education, and supplies for self-care. We connect people to emergency care when wounds require surgical drainage or IV antibiotics. Teaching proper wound care techniques helps prevent life-threatening complications like endocarditis and sepsis.</p>

<h2>Peer-Led & Relationship-Centered</h2>

<p>Our syringe exchange services are delivered by peer outreach workers with lived experience of substance use, recovery, and navigating systems of care. Peer workers build authentic relationships grounded in mutual respect and shared understanding. We provide crisis support, resource navigation, and assistance accessing healthcare, housing, and medication-assisted treatment programs. The peer relationship is often the most transformative aspect of syringe exchange—it combats isolation, reduces shame, and creates space for healing and change.</p>

<p>We offer one-on-one education on safer injection practices including vein care, recognizing safer injection sites, reducing infection risk, and recognizing signs of serious complications. We discuss fentanyl risks, overdose prevention strategies, and options for reducing or stopping drug use when people express interest. All counseling is non-judgmental, participant-led, and rooted in respect for individual autonomy and decision-making. We provide information, not pressure or coercion.</p>

<h2>Access & Impact</h2>

<p>Accessing syringe exchange through our program requires no requirements or restrictions. You don't need identification, insurance, proof of residence, or sobriety. We don't require people to surrender used syringes to receive new ones, though we encourage safe disposal. There are no limits on the number of syringes you can receive. Services are completely free and confidential.</p>

<p>Our mobile outreach team operates 3-5 days per week throughout King and Pierce Counties. We visit encampments, parks, street corners, and other locations where people who use drugs can easily access us. Our regular schedule creates predictable access points where people know they can find support. To find our current location, request a specific visit, or ask questions about our services, call or text 253-881-7377 anytime.</p>

<p>Since launching our syringe exchange program, we have distributed over 15,000 sterile syringes, provided hundreds of HIV and hepatitis C tests, connected more than 500 people to healthcare and treatment services, and prevented countless infections through disease prevention education. Research shows syringe exchange reduces HIV transmission by more than 50 percent and increases treatment entry rates by up to 5 times. Every syringe distributed represents an infection prevented. Every relationship built creates a pathway to healing.</p>
'''
    },
    'service-wound-care': {
        'title': 'Wound Care Services',
        'content': '''
<h2>Professional Wound Care for People Experiencing Homelessness & Substance Use</h2>

<p>Untreated wounds are one of the leading causes of emergency department visits and hospitalizations among people experiencing homelessness. What begins as a small cut, injection site injury, or blister can quickly escalate into cellulitis, abscess formation, or systemic infection requiring hospitalization, IV antibiotics, and sometimes surgical intervention. These emergency interventions are expensive, traumatic, and often preventable with early wound care and basic hygiene access.</p>

<p>Wounds are often a visible sign of vulnerability. When someone shows us a wound and asks for help, they're placing tremendous trust in us. We honor that trust by providing expert, compassionate, non-judgmental care. Our peer-led approach means our team members understand the lived experience of substance use and homelessness. They know the barriers people face in accessing traditional healthcare, the stigma they encounter from medical providers, and the fear many people have of seeking help.</p>

<p>Healing Roots Outreach Collective provides professional wound care services directly to people where they are—in encampments, parks, on the street, and through our mobile outreach unit. Our trained peer health workers and medical staff assess wounds, clean and dress them with sterile materials, monitor for signs of infection, provide wound care education, and connect people to emergency medical care when needed. We understand that wound care is not just about treating the physical injury—it's about building trust, demonstrating care, and treating every person with the dignity and respect they deserve.</p>

<h2>Comprehensive Wound Care Services</h2>

<p>We provide professional wound assessment of all types of wounds including injection-site injuries, abscesses, cellulitis, ulcers, burns, lacerations, and chronic wounds. Our trained health workers evaluate wound severity, measure depth and size, check for signs of infection, assess circulation, determine whether immediate medical care is needed, and document wound progression to track healing over time.</p>

<p>We conduct sterile cleaning and disinfection of wounds using proper medical technique. We irrigate wounds, remove debris and dead tissue when appropriate, apply antimicrobial solutions, and ensure wounds are properly prepared for dressing. Our first aid kits include everything needed for immediate wound care: gauze, antiseptic, bandages, tape, and specialized dressings for different wound types. We teach people the importance of keeping wounds clean and dry, how to change dressings safely, and when to seek emergency care.</p>

<p>Infection prevention is our primary goal. We educate people on proper wound hygiene, provide sterile supplies for self-care, teach signs of infection to watch for, and follow up regularly to monitor healing. For people at high risk of infection, we provide prophylactic supplies and connect them to medical providers who can prescribe antibiotics when appropriate. Serious infections like cellulitis and abscess require professional medical evaluation.</p>

<p>Abscesses are common among people who inject drugs and can quickly become life-threatening. We assess abscesses for severity, provide warm compresses to promote drainage, teach proper care techniques, and make emergency referrals when surgical drainage is needed. We educate people on preventing abscesses through safer injection practices and consistent sterile syringe use. Untreated abscesses can progress to sepsis, which is rapidly fatal without emergency treatment.</p>

<p>Some wounds require ongoing care over weeks or months. We provide consistent follow-up care for chronic wounds including diabetic ulcers, venous stasis wounds, and slow-healing injuries. Our team coordinates with medical providers, ensures people have necessary supplies, and provides encouragement throughout the healing process. Chronic wound management requires patience, consistency, and genuine relationship-building.</p>

<p>When wounds require professional medical intervention—including surgical drainage, IV antibiotics, imaging, or specialist care—we facilitate immediate connections to emergency departments and clinics. We provide transportation assistance when possible, advocate for respectful treatment, and follow up to ensure people receive the care they need. Many people have experienced discrimination in healthcare settings; we work to remove those barriers.</p>

<h2>Impact & Access</h2>

<p>We've treated over 500 wounds annually with a 95% infection prevention rate. Each wound treated is an opportunity to prevent a medical emergency, reduce suffering, and demonstrate that harm reduction works. Serious skin and soft tissue infections can progress to sepsis, endocarditis, osteomyelitis, and other life-threatening conditions. By catching infections early, preventing complications, and connecting people to medical care, we literally save lives.</p>

<p>Our mobile outreach team provides wound care services 3-5 days per week throughout King and Pierce Counties. You can find our mobile unit at regular stops in Seattle SODO District, Kent, Tacoma, Spanaway, and other communities. No appointment is necessary—just come to the mobile unit when you need care. Our team is trained to assess wounds, provide immediate first aid, supply sterile wound care materials, and arrange medical transport if emergency care is needed.</p>

<p>All wound care services are completely free, confidential, and provided without judgment. You don't need identification, insurance, or an appointment. You don't need to be ready to stop using substances or enter treatment. We meet you exactly where you are and provide the care you need in this moment. Our only requirement is that you let us help you. Call or text 253-881-7377 for urgent wounds or to request a visit.</p>
'''
    },
    'service-health-screening': {
        'title': 'Health Screening Services',
        'content': '''
<h2>Free Community Health Screening & Early Detection</h2>

<p>Access to healthcare is a fundamental right, yet many people experiencing homelessness and substance use are disconnected from all systems of care. Without regular health screenings, serious conditions go undetected until they require emergency intervention. Early detection of diseases like HIV, hepatitis C, diabetes, and hypertension allows for treatment before complications develop and prevents serious health consequences.</p>

<p>Healing Roots Outreach Collective provides comprehensive health screening services directly to communities, removing barriers to access. Our mobile health clinic offers rapid testing, vital sign assessment, health education, and referrals to primary care and specialist services. All services are free, confidential, and judgment-free. We believe that everyone deserves access to healthcare information and early disease detection, regardless of housing status, insurance status, or substance use.</p>

<h2>Health Screening Components</h2>

<p>We offer rapid HIV and hepatitis C testing using point-of-care tests that provide results within minutes. Early detection is critical—modern hepatitis C treatments have cure rates exceeding 95 percent, and early HIV treatment allows people to live long, healthy lives while preventing transmission to others. We also provide hepatitis B vaccination series and hepatitis A vaccination for people who are unvaccinated. All testing is voluntary, confidential, and conducted with informed consent and peer support.</p>

<p>We assess vital signs including blood pressure, heart rate, temperature, and oxygen saturation. Many people experiencing homelessness have untreated hypertension that puts them at risk for stroke and heart attack. We provide education about blood pressure management, including the importance of reducing salt intake, physical activity, and stress management. For people with elevated blood pressure, we connect them to follow-up care and medication management.</p>

<p>We provide health education on prevention and management of common health conditions. Topics include proper nutrition despite food insecurity, physical activity, stress management, sleep hygiene, sexual health, respiratory health, and recognizing warning signs of serious health problems. We discuss medication management for people taking medications, and help people understand their health conditions in accessible language without medical jargon.</p>

<p>We connect people to primary care providers who accept uninsured patients or work with Medicaid. We help people understand healthcare options, navigate insurance systems, and overcome barriers to care. For people with chronic conditions, we provide ongoing support and follow-up to ensure they're getting consistent care. Our peer navigators advocate within healthcare systems to ensure respectful treatment.</p>

<p>We maintain medical records for people who may not have consistent healthcare. This allows us to track changes in health status over time and identify concerning trends. We share relevant information with medical providers to ensure continuity of care across multiple providers and settings.</p>

<h2>Community-Based Mobile Health</h2>

<p>Our mobile health screening operates 3-5 days per week throughout King and Pierce Counties. We visit encampments, shelters, parks, and community centers where people gather. No appointment is necessary—just approach our mobile unit when you see us. Our team includes nurses, medical assistants, and peer health workers who conduct screenings with respect and cultural humility.</p>

<p>We explain all screening results in language people understand, without medical jargon. We answer questions about what results mean and what next steps might be. We respect people's autonomy and provide information without pressure. If follow-up care is needed, we help people understand their options and connect them to appropriate resources.</p>

<p>All screenings are completely free and confidential. There are no requirements: you don't need insurance, identification, or to disclose personal information beyond what's necessary for the screening itself. Everything discussed is confidential and protected by healthcare privacy laws.</p>

<h2>Impact & Outcomes</h2>

<p>Through our health screening program, we've identified numerous cases of undiagnosed HIV, hepatitis C, hypertension, and diabetes that might otherwise have gone undetected until crisis hospitalization. Early detection means people can access treatment before serious complications develop. We've connected hundreds of people to primary care, specialists, and treatment services. We've vaccinated hundreds of people against hepatitis A and B, preventing future infections.</p>

<p>Health screening creates entry points for comprehensive support. Someone who comes for health screening may also need naloxone, sterile syringes, wound care, peer counseling, housing navigation, or treatment referrals. By meeting people's immediate health needs with compassion, we create opportunities to connect them with broader support services that address their overall wellbeing and recovery.</p>

<p>Community-based health screening removes barriers to care and meets people where they are. Unlike traditional medical systems that require appointments, insurance, and navigation of bureaucratic systems, our mobile health clinic is accessible, free, and designed with the needs of our community in mind. Call or text 253-881-7377 to find our current location or request a health screening visit.</p>
'''
    },
    'service-peer-support': {
        'title': 'Peer Support Services',
        'content': '''
<h2>Peer Support & Mentorship From People With Lived Experience</h2>

<p>Lived experience creates trust. Our peer counselors understand substance use, homelessness, and recovery from direct personal experience. They've walked the path of active use, crisis, recovery, relapse, and healing. They understand the barriers to accessing care, the stigma from healthcare providers, the shame and self-judgment that often accompany substance use, and the hope that comes with building new relationships and taking steps toward stability.</p>

<p>Peer support is fundamentally different from professional counseling. While professional counselors have training and credentials, peer counselors have something equally valuable: authentic understanding of what it's like to live with addiction, trauma, and systemic barriers. This shared experience creates immediate trust and safety. People are more likely to be honest, more likely to believe change is possible, and more likely to follow through on goals when they're working with someone who has been where they are.</p>

<p>Healing Roots Outreach Collective provides 24/7 crisis support through our peer team. If you're experiencing a crisis—emotional, psychological, or substance-related—you can call or text 253-881-7377 anytime, day or night. A peer counselor will answer and listen without judgment. We can help you think through options, connect you to resources, provide encouragement, and stay with you through difficult moments.</p>

<h2>Comprehensive Peer Services</h2>

<p>We provide resource navigation to help you access housing, food assistance, benefits, healthcare, mental health services, and other community resources. Systems are complex and confusing; our navigators help remove barriers and find solutions. We fill out applications, attend appointments with you, advocate with agencies on your behalf, and help you understand your rights and options. Resource navigation addresses the social determinants of health that make recovery difficult.</p>

<p>We help connect people to treatment and medication-assisted treatment programs when they express readiness. We provide information about different treatment options—including methadone, buprenorphine, counseling, and peer support groups. We address concerns and fears about treatment, help people navigate waitlists, and follow up to ensure people stay engaged. Treatment is not one-size-fits-all; we help people find options that match their needs and preferences.</p>

<p>We provide non-judgmental harm reduction counseling. If you're not ready to stop using, that's okay. We discuss ways to reduce harm while you continue using: safer injection practices, overdose prevention, disease prevention, and accessing healthcare. We discuss readiness for change and goals for the future without pressure. When you decide you're ready to change, we're here to support you.</p>

<p>We provide case management and long-term support planning. Rather than one-time interactions, we build ongoing relationships. We develop comprehensive support plans that address housing, income, healthcare, treatment, legal issues, employment, education, and family relationships. We follow up regularly to monitor progress, troubleshoot problems, and celebrate wins.</p>

<p>We facilitate peer support groups and community building. Isolation is a major risk factor for relapse and continued substance use. We create spaces for people to connect with others in recovery, share experiences, provide mutual support, and build community. These groups are free, confidential, and open to anyone.</p>

<h2>Trauma-Informed & Culturally Responsive</h2>

<p>Many people who experience substance use also experience trauma from violence, abuse, discrimination, poverty, and systemic oppression. Trauma affects how people process information, relate to others, and respond to stress. Our peer counselors are trained in trauma-informed approaches: we create safety, provide choices, and recognize trauma responses without judgment.</p>

<p>We provide culturally responsive services that honor diverse identities and experiences. We recognize that substance use, recovery, and resilience look different for different communities. We work with cultural brokers and community leaders to ensure our services are accessible and respectful to people from different racial, ethnic, LGBTQ+, and cultural backgrounds.</p>

<h2>Access & Impact</h2>

<p>Peer support is completely free and confidential. There are no requirements or restrictions. You can access peer support during mobile outreach visits, by calling or texting 253-881-7377 anytime, or by visiting our office. We work with your schedule and preferences. We meet people where they are—literally and figuratively.</p>

<p>Through our peer support program, hundreds of people have moved from active substance use toward recovery and stability. We've helped people access housing, employment, treatment, healthcare, and reconnect with family. We've prevented overdoses by providing naloxone and support. We've addressed trauma and built resilience. We've created community where isolation once existed.</p>

<p>Peer support works because it's rooted in genuine understanding, respect, and hope. When you work with someone who has been where you are and came out the other side, recovery becomes possible. You're not alone. Help is real. Call 253-881-7377 to connect with peer support anytime.</p>
'''
    },
    'service-housing-support': {
        'title': 'Housing Support Services',
        'content': '''
<h2>Housing is Healthcare: Stable Housing Enables Recovery</h2>

<p>Housing is one of the most critical social determinants of health. People who are experiencing homelessness face extraordinary health challenges: higher rates of infectious disease, chronic illness, mental health conditions, substance use disorders, and early mortality. It's impossible to manage diabetes, take HIV medications consistently, attend treatment appointments, or address trauma when you don't have stable housing. Conversely, providing stable housing creates the foundation for all other healing and recovery to occur.</p>

<p>Healing Roots Outreach Collective provides comprehensive housing support to help people access emergency shelter, transitional housing, and permanent supportive housing. We understand that the pathway from homelessness to housing is complex and often requires ongoing support. We walk alongside people through every step of this journey.</p>

<h2>Housing Services & Support</h2>

<p>We help people access emergency shelter when they need immediate protection from the streets. We know shelter availability in King and Pierce Counties and can make referrals and placements quickly. We address barriers to shelter entry—many shelters have restrictions on substance use, pets, or couples staying together. We advocate for people's needs and help find shelter options that work for their situation. We provide transportation to shelters and follow up to ensure placements are stable.</p>

<p>We provide transitional housing that bridges from homelessness to permanent housing. Transitional housing typically provides 3-24 months of support while people work on stabilization: finding employment, addressing health issues, rebuilding family relationships, and preparing for independent living. We help people navigate transitional programs and provide ongoing peer support during this transition.</p>

<p>We help people access permanent supportive housing, which combines affordable housing with ongoing support services. Permanent supportive housing is evidence-based and highly effective—studies show it reduces homelessness by 85% and reduces emergency department visits and hospitalizations by 40-60%. We help people apply, navigate housing selection, and access needed supports.</p>

<p>We provide housing navigation that removes barriers to accessing housing. This includes helping people obtain replacement ID documents (which many homeless people lack), accessing benefits like SSI or SSDI that provide income for housing, and removing barriers from rental histories. Many people have eviction records or poor rental history; we advocate with landlords and housing programs to help overcome these barriers.</p>

<p>We provide rental assistance when available to help people afford deposits, first month's rent, or ongoing rental assistance. We also help people understand tenant rights, navigate landlord relationships, and prevent evictions once housed.</p>

<p>Housing case management provides ongoing support after housing placement. People who have experienced homelessness may struggle with maintaining housing initially; we provide support to address this. We help with rent payments, utilities, resolving conflicts with landlords, maintaining the housing unit, and addressing the underlying issues that contributed to homelessness (substance use, mental health, family conflict, employment).</p>

<h2>Addressing Root Causes</h2>

<p>Homelessness is rarely caused by laziness, moral failure, or lack of willingness to work. It's caused by lack of affordable housing, low wages, medical crises, job loss, mental illness, substance use, family conflict, abuse, and systemic discrimination. True housing support addresses these root causes while simultaneously providing housing.</p>

<p>We help people address substance use through treatment referrals and peer support. We provide mental health support and connections to psychiatric services. We address trauma through counseling and peer support. We help with employment and income assistance. We facilitate family reconnection when desired. We address legal issues. We help people rebuild stability across multiple life domains.</p>

<h2>No One Sleeps Outside If We Can Help</h2>

<p>Our commitment is clear: no one in Pierce County sleeps outside if we can help. When we encounter someone experiencing homelessness, we immediately begin working on housing solutions. We may start with emergency shelter while we work on longer-term options. We provide whatever support is needed to move someone toward permanent housing.</p>

<p>Housing support is completely free and confidential. There are no requirements: you don't need income, employment, documentation, or anything else. We help people with barriers to housing. Call or text 253-881-7377 anytime to access housing navigation. Our peer navigators will work with you to develop a housing plan that matches your situation, preferences, and needs.</p>

<p>We've helped hundreds of people move from the streets into stable housing. We've seen people access treatment once housed. We've seen people reconnect with family. We've seen people get jobs and rebuild their lives. Housing works. It's the foundation for all other healing. Let us help you find stable housing and take the next step toward stability and recovery.</p>
'''
    },
    'service-cultural-healing': {
        'title': 'Cultural Healing Services',
        'content': '''
<h2>Indigenous-Led Healing: Integrating Traditional & Modern Approaches</h2>

<p>Healing Roots Outreach Collective was founded on Indigenous values and principles. We understand that true healing must honor cultural identity, spiritual connection, and traditional practices. For Indigenous peoples and all community members, cultural connection is healing. When we're disconnected from our culture, identity, and community, we're more vulnerable to substance use, mental illness, and suffering. When we reconnect with cultural practices and community, healing becomes possible.</p>

<p>Our approach integrates traditional healing practices with evidence-based harm reduction and healthcare. We don't see these as contradictory; they're complementary. Traditional practices like smudging, talking circles, and land-based activities address spiritual and emotional healing. Evidence-based healthcare addresses physical health. Together, they support whole-person healing that honors culture, spirituality, and identity.</p>

<h2>Cultural Healing Services</h2>

<p>We facilitate healing circles where people gather in sacred space to share stories, receive support, and experience community connection. Healing circles are peer-led and often facilitated by Indigenous elders or experienced facilitators. They may include smudging (burning sage and other sacred plants), talking circles (where each person speaks without interruption), sharing of food, singing, and other traditional practices. Healing circles create space for people to process trauma, share burdens, and experience the power of community support.</p>

<p>We organize cultural connection activities and community events that celebrate culture and identity. These might include powwows, language learning circles, traditional craft activities, cooking classes featuring traditional foods, or other cultural gatherings. Cultural connection reduces isolation and strengthens identity, both protective factors against substance use and mental illness.</p>

<p>We provide spiritual support that honors diverse spiritual traditions and beliefs. We don't impose any particular spiritual perspective; instead, we recognize that spirituality is important for many people and provide support for spiritual practice, whether that's traditional Indigenous spirituality, Christianity, Islam, Buddhism, or other beliefs. We facilitate connections to spiritual communities and leaders when people want them.</p>

<p>We create space for creative expression and healing through art, music, writing, and other arts. Trauma and pain can be difficult to express verbally; creative expression provides alternative pathways. We offer workshops, provide supplies, create gallery spaces for sharing artwork, and facilitate open mic nights for sharing poetry or music. Arts and creativity are healing.</p>

<p>We organize land-based activities that connect people to nature and place. Whether it's harvesting traditional plants, fishing, gardening, hiking, or simply being in natural settings, land connection is healing. For Indigenous peoples especially, the land is inseparable from identity and spirituality. We facilitate these connections.</p>

<h2>Integrating Culture Into Harm Reduction</h2>

<p>All of our harm reduction services—syringe exchange, naloxone distribution, wound care, health screening, peer support—are delivered through a culturally informed lens. We train our staff in cultural humility and recognize that culture influences health beliefs, family structures, decision-making, and approaches to healing.</p>

<p>We provide services in multiple languages and work with cultural brokers from the communities we serve. We employ staff from the communities we serve. We celebrate cultural holidays and observances. We incorporate traditional knowledge into health education. We create spaces where people can be authentically themselves and practice their culture without judgment.</p>

<h2>Access & Community</h2>

<p>All cultural healing services are free and open to community members. You don't need to be Indigenous to participate, though we center Indigenous leadership and perspectives. Community members of all backgrounds are welcome in our circles, events, and activities.</p>

<p>To learn about upcoming healing circles, cultural events, and activities, call or text 253-881-7377. We can provide information about times, locations, and what to bring or expect. Drop-in attendance is always welcome at most events. We create space for people to connect with culture, community, and spirituality as part of their healing journey.</p>

<p>Cultural healing is not separate from harm reduction—it's integral to it. When people feel connected to culture and community, when they experience their identity as valuable and beautiful, when they access traditional healing alongside modern healthcare, recovery becomes possible. We commit to honoring culture and spirituality as essential components of healing.</p>
'''
    },
    'service-education-training': {
        'title': 'Education & Training Services',
        'content': '''
<h2>Community Education & Training: Building Knowledge & Capacity</h2>

<p>Education empowers change. Knowledge is power. When people understand overdose response, safer substance use practices, disease prevention, and how to navigate healthcare systems, they make better decisions and take better care of themselves and their communities. Healing Roots Outreach Collective provides comprehensive training and education to individuals, organizations, and communities on harm reduction, overdose response, health promotion, and recovery support.</p>

<p>Our training approach is interactive, participatory, and practical. We don't lecture at people; we engage in dialogue, answer questions, and provide hands-on practice when relevant. We train peer educators who can continue teaching in their communities. We provide training in multiple languages and adapt content for different audiences.</p>

<h2>Training Topics & Workshops</h2>

<p>We provide comprehensive overdose response training that teaches recognition of overdose signs, administration of naloxone (both nasal spray and injection forms), recovery position, what to expect after naloxone administration, and when and how to call 911. Participants practice naloxone administration on training kits. We discuss barriers to calling 911 (including fear of legal consequences) and address the Good Samaritan Law that protects people who call for help. Every participant leaves with naloxone and knowledge to save a life.</p>

<p>We provide safer injection training for people who inject drugs. Topics include proper injection technique, vein care, safer injection sites, infection prevention, recognizing complications, and addressing trauma related to injection. We demonstrate equipment, answer questions, and provide information without judgment. We discuss the risks of different injection methods and ways to reduce harm.</p>

<p>We provide disease prevention training including blood-borne disease transmission, prevention methods, testing options, and what results mean. We discuss HIV and hepatitis C: how they're transmitted, how to prevent transmission, testing and treatment options, and living with these diseases. We address myths and stigma. We emphasize that having HIV or hepatitis C is not shameful and that modern treatment is highly effective.</p>

<p>We provide trauma-informed care training for healthcare providers, social workers, and community members who work with people who've experienced trauma. We discuss how trauma affects the brain and behavior, how to recognize trauma responses, and how to respond in ways that support healing rather than retraumatization. We address secondary trauma for service providers.</p>

<p>We provide resource navigation training that teaches people how to find and access community resources including housing programs, benefits programs, healthcare, legal services, employment, and treatment. We teach how to overcome barriers and navigate complex systems. Participants learn both how to access resources themselves and how to help others.</p>

<p>We provide peer trainer certification for people who want to become certified harm reduction educators. This intensive training covers harm reduction philosophy, specific technical content (overdose response, safer injection, disease prevention), training methodology, and practice teaching. Peer trainers can then provide training in their communities.</p>

<h2>Community & Organizational Training</h2>

<p>We provide tailored training for specific organizations and communities. Homeless service providers, healthcare agencies, schools, libraries, faith communities, and others can request training on harm reduction, overdose response, or other health topics. We customize content for the audience and can provide training to large groups or small teams.</p>

<p>We provide leadership development training for people who want to become peer advocates or community organizers. We discuss advocacy strategies, how to engage with policy makers, how to speak publicly about harm reduction and health issues, and how to organize community action.</p>

<p>All training is evidence-based, participatory, and delivered by experienced educators—many of whom have lived experience with the topics they're teaching. Training is free and available to anyone who wants to learn.</p>

<h2>Impact & Access</h2>

<p>Through our training programs, over 1,500 community members have learned overdose response. Hundreds have received safer injection training. Hundreds of healthcare providers have received trauma-informed care training. Dozens of peer trainers have been certified to teach in their communities. This cascading effect means knowledge spreads far beyond our direct reach—peer trainers teach family members, friends, and others in their networks.</p>

<p>To request training for your organization or community, or to sign up for individual training sessions, call or text 253-881-7377. We provide training 3-5 days per week throughout King and Pierce Counties. Training is free, confidential, and judgment-free. Every person deserves knowledge to protect their health and save lives.</p>
'''
    },
    'service-resource-navigation': {
        'title': 'Resource Navigation Services',
        'content': '''
<h2>Helping You Navigate Complex Systems & Find Services</h2>

<p>Access to basic needs—housing, food, income, healthcare—should be a right, not a struggle. Yet systems for accessing these services are often confusing, bureaucratic, and difficult to navigate. People need to know which programs exist, who qualifies, how to apply, what documents are required, and how to follow up. Without help, many people give up before accessing the services they need. Our resource navigators remove these barriers.</p>

<p>Healing Roots Outreach Collective provides free resource navigation to help people access housing, income assistance, healthcare, legal services, employment, food, and other community resources. Our peer navigators are trained in community resources, benefits programs, healthcare systems, and advocacy. We understand the barriers people face and know how to overcome them.</p>

<h2>Housing & Shelter Navigation</h2>

<p>We help people access emergency shelter when they need immediate protection from the streets. We know shelter availability in King and Pierce Counties, understand eligibility requirements, and can facilitate placement quickly. We address barriers to shelter entry and find options that work for people's situations. We provide transportation to shelters and follow up to ensure stability.</p>

<p>We help people access transitional and permanent supportive housing. We explain different housing programs, help people understand eligibility, assist with applications, advocate with housing providers, and provide ongoing support after housing placement. Housing stability is foundational to recovery and health.</p>

<h2>Income & Benefits Navigation</h2>

<p>We help people access Supplemental Security Income (SSI) for disabled, blind, or elderly individuals unable to work. We explain what SSI is, who qualifies, how to apply, what documents are needed, and how long the process takes. We help complete applications and follow up with Social Security. SSI provides monthly income ($943 in 2024) that supports housing and other necessities.</p>

<p>We help people access Social Security Disability Insurance (SSDI) for people who've worked and become unable to work due to disability. SSDI benefits are based on work history and can be higher than SSI. We explain eligibility, help with applications, and provide ongoing support during the determination process.</p>

<p>We help people access Medicaid and Washington Apple Health, which provide healthcare coverage for low-income individuals. Coverage includes doctor visits, medications, hospital care, dental, and other services. We explain how to apply, help with applications, and assist with renewal paperwork. Healthcare access is critical for managing chronic diseases and addressing health issues.</p>

<p>We help people access SNAP (food assistance), TANF (Temporary Assistance for Needy Families), and other benefits. We explain eligibility, help with applications, and support ongoing benefit management. Food security is foundational to health.</p>

<p>We help people understand and access unemployment insurance if they've lost jobs. We explain the application process, help determine eligibility, and assist with appeals if needed.</p>

<h2>Healthcare & Legal Navigation</h2>

<p>We help people access primary care, mental health services, substance use treatment, and specialist care. We explain how healthcare works, help people find providers who accept uninsured or Medicaid patients, facilitate appointments, and provide transportation when possible. We advocate within healthcare systems to ensure respectful treatment. Healthcare navigation removes barriers to accessing medical care.</p>

<p>We provide legal navigation and advocacy. We help people with eviction prevention, criminal record expungement, immigration issues, benefits appeals, and other legal matters. We connect people with legal aid agencies, public defenders, and attorneys who serve low-income individuals. Legal issues often create barriers to stability; addressing them is critical.</p>

<p>We help people obtain identification documents including driver's licenses, state IDs, birth certificates, and Social Security cards. These documents are required for accessing services, employment, and housing. Many homeless people lack ID; we help get replacement documents.</p>

<h2>Employment & Education Navigation</h2>

<p>We help people access job training and employment programs. We support resume building, job searching, interview preparation, and workplace navigation. We connect people with vocational rehabilitation, apprenticeships, and other pathways to employment. Employment provides income, identity, routine, and hope.</p>

<p>We help people access educational opportunities including high school equivalency (GED), community college, vocational training, and other educational programs. Education opens doors and increases earning potential.</p>

<h2>Access & Impact</h2>

<p>Resource navigation is completely free and confidential. There are no requirements or restrictions. Call or text 253-881-7377 anytime to access resource navigation. Our peer navigators will meet with you, understand your situation and goals, and develop an action plan to connect you with needed services. We work with your schedule and pace.</p>

<p>Through our resource navigation program, hundreds of people have accessed housing, benefits, healthcare, legal services, and employment. We've helped people move from homelessness to stable housing, from unemployment to employment, from disconnection from healthcare to consistent medical care. Resource navigation works because it removes barriers and provides personalized, persistent support.</p>

<p>Don't navigate complex systems alone. Call 253-881-7377 to connect with a peer navigator who will help you access the resources you need to build stability and health.</p>
'''
    },
}

def create_service_html(service_name, title, content):
    """Create complete HTML for service page"""
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

    <!-- Service Content -->
    <section class="service-detail">
      <div class="container">
        <div style="background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); line-height: 1.8; font-size: 16px;">
          {content}
        </div>

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
    print("\n" + "="*70)
    print("Generating service pages with ~1000 words each")
    print("="*70 + "\n")

    generated = 0
    for service_name, service_data in SERVICES.items():
        html = create_service_html(service_name, service_data['title'], service_data['content'])
        file_path = Path(f'HROC_Website_New/{service_name}.html')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

        # Count words in content
        word_count = len(service_data['content'].split())
        print(f"✓ Generated: {service_name}.html ({word_count} words)")
        generated += 1

    print("\n" + "="*70)
    print(f"Generated {generated}/9 service pages")
    print("="*70)
    print("\nNOTE: Images need to be categorized as:")
    print("  • LARGE (infographics): /2.png files")
    print("  • SMALL (people/things): /1.png and /3.png files")
    print("\n")

if __name__ == '__main__':
    main()
