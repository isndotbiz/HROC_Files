╔══════════════════════════════════════════════════════════════════════════════╗
║                     CODEX PHASE 3 HROC WEBSITE HANDOFF                        ║
║              Multi-Agent Parallel Optimization & Feature Design               ║
╚══════════════════════════════════════════════════════════════════════════════╝

You are Codex, based on GPT-5. You are running as a coding agent in the Codex CLI on a user's computer.

CRITICAL DIRECTIVE: Launch and coordinate 12 agents in parallel to execute Phase 3 simultaneously. Do not wait for sequential completion. Aim for aggressive parallelization.

═══════════════════════════════════════════════════════════════════════════════

***PHASE 3: WEBSITE OPTIMIZATION & FEATURE ENHANCEMENT***

Overview
  Primary: Optimize website performance, accessibility, SEO for maximum impact
  Secondary: Design 3 ambitious improvement features (PWA, CMS, Analytics)
  Tertiary: Prepare enterprise-grade deployment & monitoring
  Status: Website live at https://hrocinc.org with 60+ images, deployed to NAS

Current State (Phase 2 Complete ✅)
  Commit: 7d6d4bf (website transformation: 3 founders, 60+ images, 400+ CSS lines)
  Website: Live at https://hrocinc.org (Cloudflare Tunnel, HTTPS, mobile responsive)
  Deployment: NAS server (10.0.0.89), 415 files, Nginx running
  Accessibility: WCAG 2.2 AA compliant, 100% alt text, semantic HTML
  Images: 61 total deployed (community, hero, founders, service icons)
  Code Quality: Responsive design, CSS custom properties, performance optimized

Targets for Phase 3
  Performance: Lighthouse score 95+ (all metrics)
  Accessibility: WCAG 2.2 AAA (advanced level)
  SEO: Rank top 3 for "nonprofit harm reduction [city]"
  Features Designed: PWA, Headless CMS, Analytics (ready for Phase 4 dev)
  Enterprise Ready: Monitoring, backups, disaster recovery

═══════════════════════════════════════════════════════════════════════════════

***PARALLEL AGENT LAUNCHES (12 TOTAL)***

TIER 1: CRITICAL PATH (4 Agents - Must Complete First)

Agent 1: Performance & Lighthouse Optimization
  Mission: Achieve Lighthouse 95+ across all metrics

  Tasks:
    • Run Lighthouse audit: https://hrocinc.org
      Target: Performance 95+, Accessibility 95+, Best Practices 95+, SEO 95+
    • Identify bottlenecks (images, CSS, JS, fonts)
    • Optimize image delivery:
      - Modern formats (WebP with JPEG fallback)
      - Responsive images (srcset for different viewport sizes)
      - Critical images prioritized
    • CSS optimization:
      - Minification (current: 43 KB)
      - Unused CSS removal (purge if using Tailwind concepts)
      - Critical CSS inline for above-fold content
    • JavaScript optimization:
      - Minify script.js (current: 12 KB)
      - Lazy load non-critical scripts
      - Remove any unused code
    • Core Web Vitals:
      - LCP (Largest Contentful Paint): <2.5s
      - FID (First Input Delay): <100ms
      - CLS (Cumulative Layout Shift): <0.1
    • Font optimization:
      - System fonts or variable fonts
      - font-display: swap for web fonts
      - Preload critical fonts
    • Caching strategy:
      - Browser cache headers
      - Service worker for static assets (Agent 8 may assist)

  Deliverable: Optimized index.html, styles.css, script.js
  Report: LIGHTHOUSE_OPTIMIZATION_REPORT.md
    - Before/after Lighthouse scores
    - Breakdown by metric
    - Size reductions achieved
    - Recommendations for further optimization

Agent 2: Advanced Accessibility Audit (WCAG 2.2 AAA)
  Mission: Achieve WCAG 2.2 AAA (advanced) compliance

  Tasks:
    • Current state: WCAG 2.2 AA verified ✅
    • Enhance to AAA level:
      - Color contrast: 7:1 for normal text (vs 4.5:1 AA requirement)
      - Focus indicators: Visible, high contrast focus states
      - Motion: Prefers-reduced-motion media query implementation
      - Language markup: lang attributes on all elements
      - Form labels: Explicit labels for all inputs
      - Error messages: Clear, specific error descriptions
      - Help text: Contextual help available
    • Keyboard navigation:
      - Tab order logical
      - Skip links functional
      - All interactive elements accessible
    • Screen reader optimization:
      - ARIA labels where needed
      - Landmark regions properly marked
      - Lists properly structured
    • Temporal media:
      - Captions for any videos
      - Audio descriptions for images
    • Testing:
      - Screen reader testing (NVDA/JAWS simulation)
      - Keyboard-only navigation
      - Color contrast analysis tool
      - Axe DevTools full scan

  Deliverable: Updated index.html with AAA enhancements
  Report: ACCESSIBILITY_AAA_REPORT.md
    - Gap analysis (AA → AAA)
    - Changes made with rationale
    - Testing results
    - Compliance checklist (all AAA criteria)
    - Remaining opportunities for future enhancement

Agent 3: SEO & Metadata Optimization
  Mission: Rank #1-3 for relevant nonprofit harm reduction keywords

  Tasks:
    • Current state audit:
      - Existing meta tags (check index.html)
      - Current keyword targeting
      - Schema markup present/missing
    • Keyword research:
      - Target keywords: "nonprofit harm reduction", "opioid crisis support", "peer support services"
      - Location-based: "[City] harm reduction", "[City] overdose prevention"
      - Long-tail: "evidence-based harm reduction nonprofit", "community outreach services"
    • On-page optimization:
      - Title tags (50-60 chars, keyword-rich)
      - Meta descriptions (150-160 chars, compelling)
      - H1 optimization (one per page, keyword-aligned)
      - Internal linking strategy (site structure optimization)
      - Schema markup implementation:
        * Organization schema (name, description, logo, contact)
        * LocalBusiness schema (address, phone, service area)
        * Service schema (each service with description)
        * Person schema (founders with bios)
        * BreadcrumbList (navigation structure)
    • Technical SEO:
      - robots.txt optimization
      - sitemap.xml generation & submission
      - Canonical tags (prevent duplicate content)
      - Open Graph tags (social sharing)
      - Twitter card tags
    • Content optimization:
      - Keyword density analysis
      - Readability score (target: Grade 8-10)
      - Content length (1,000+ words for main sections)
      - LSI keywords (semantically related)
    • Image SEO:
      - Image alt text (already ✅ but verify)
      - Image file names (keyword-rich)
      - Image size optimization (Agent 1 handles performance)
    • Mobile optimization:
      - Viewport meta tag (already ✅)
      - Mobile-first content hierarchy
      - Touch-friendly buttons (48x48px minimum)

  Deliverable: Updated index.html with SEO enhancements, sitemap.xml, robots.txt
  Report: SEO_OPTIMIZATION_STRATEGY.md
    - Keyword targeting plan
    - Competitive analysis
    - Implementation checklist
    - Expected ranking timeline
    - Monthly monitoring metrics

Agent 4: Mobile & Responsive Design Deep Dive
  Mission: Optimize for all devices (mobile-first perfection)

  Tasks:
    • Test across devices:
      - Viewports: 320px, 375px, 768px, 1024px, 1440px+
      - Devices: iPhone SE, iPhone 14 Pro, iPad, Android phones (Samsung, Google Pixel)
      - Browsers: Chrome, Safari, Firefox, Edge
    • Mobile optimization:
      - Touch target sizing (48x48px minimum)
      - Viewport configuration (already set, verify)
      - Mobile menu interaction (hamburger tested)
      - Form inputs (large enough for touch)
      - Typography scales appropriately
    • Responsive breakpoints:
      - Review current: 640px, 768px, 1024px, 1280px
      - Verify all content readable at each breakpoint
      - No horizontal scroll at any resolution
      - Images scale appropriately
    • Landscape vs portrait:
      - Proper rotation handling
      - Content not hidden in landscape
      - Bottom nav (if present) not covering content
    • Touch interactions:
      - No hover-only features (hover not available on touch)
      - Swipe support (if carousel/sliders present)
      - Pinch-zoom working (if intentional)
    • Performance on slow networks:
      - Test on 4G throttle
      - Progressive enhancement (content loads even if JS fails)
      - Images lazy load properly
    • Screen captures:
      - Document appearance on 3+ device sizes
      - Note any layout quirks or improvements needed

  Deliverable: Updated styles.css with responsive enhancements
  Report: MOBILE_RESPONSIVE_REPORT.md
    - Device compatibility matrix
    - Responsive design testing results
    - Screenshots from multiple viewports
    - Issues found and fixed
    - Performance on mobile networks

═══════════════════════════════════════════════════════════════════════════════

TIER 2: OPTIMIZATION & QUALITY (4 Agents)

Agent 5: Code Quality & Maintainability
  Mission: Ensure code is production-grade and maintainable

  Tasks:
    • HTML analysis:
      - Semantic HTML (proper heading hierarchy, landmark regions)
      - No deprecated elements
      - Valid HTML5 (check with W3C validator)
      - Proper form structure
      - Comment code where complex
    • CSS analysis:
      - CSS follows BEM or similar methodology (current: custom properties + grid)
      - No duplicate selectors
      - Organized sections (current: ~390 lines)
      - CSS custom properties used consistently
      - Media queries properly grouped
      - Remove any unused CSS rules
      - Minification ready
    • JavaScript analysis:
      - Code style consistent (camelCase, naming conventions)
      - Functions have single responsibility
      - Event listeners properly cleaned up
      - No console.log statements in production
      - Error handling present
      - Comments explain "why" not "what"
    • Documentation:
      - README.md updated with architecture
      - Code comments for complex logic
      - CSS custom property guide
      - JavaScript module overview
    • Linting (if tools available):
      - Stylelint for CSS issues
      - ESLint for JavaScript
      - HTMLLint for HTML issues

  Deliverable: Clean, documented code in all files
  Report: CODE_QUALITY_REPORT.md
    - Code review findings
    - Refactoring completed
    - Documentation improvements
    - Best practices implemented
    - Maintainability score

Agent 6: Analytics & Monitoring Setup
  Mission: Implement analytics to track HROC impact

  Tasks:
    • Analytics implementation (privacy-first):
      - Choose provider: Plausible, Fathom, or Matomo (privacy-focused, GDPR compliant)
      - Alternative: Google Analytics 4 (with privacy settings)
      - Avoid: Unnecessary data collection
    • Key metrics to track:
      - Page views by section (Hero, Services, Gallery, About, Impact)
      - Conversion: Donations (frequency, amount)
      - Engagement: Time on page, scroll depth
      - Referral sources (where users come from)
      - Device/browser breakdown
      - Geographic distribution
    • Implementation:
      - Add tracking script to index.html
      - Event tracking for key actions:
        * Button clicks (Donate, Contact, Learn More)
        * Form submissions
        * External links
      - Custom dimensions: User type (first-time, returning), referral source
    • Privacy compliance:
      - No PII collected
      - Cookie consent (if needed)
      - Privacy policy updated
      - GDPR compliant (if EU audience)
    • Dashboard setup:
      - Create monitoring dashboard
      - Set baseline metrics (current traffic patterns)
      - Monthly reporting structure
    • Goals/Conversions:
      - Donation goal tracking
      - Volunteer signup goal
      - Contact form submission goal

  Deliverable: Analytics implementation in index.html
  Report: ANALYTICS_SETUP_GUIDE.md
    - Provider selected + rationale
    - Tracking implementation
    - Privacy considerations
    - Key metrics dashboard
    - Baseline metrics established
    - Monthly reporting template

Agent 7: Deployment & DevOps Enhancement
  Mission: Harden deployment, add monitoring, enable CI/CD

  Tasks:
    • Current deployment review:
      - NAS server (10.0.0.89, /var/www/hroc/)
      - Cloudflare Tunnel (active, free SSL)
      - Nginx (running, HTTP→HTTPS redirect)
      - Status: ✅ Working
    • Enhancements:
      - Automated backups:
        * Daily backups to secondary storage
        * Backup verification
        * 30-day retention
      - Health monitoring:
        * Uptime monitoring (UptimeRobot or similar)
        * Certificate expiration alerts
        * 404 error alerts
      - Disaster recovery:
        * Backup restoration procedure documented
        * Alternative server ready (if possible)
      - CI/CD pipeline:
        * GitHub Actions workflow for deployments
        * Auto-deploy on git push to main
        * Verification tests before deploy
      - SSL/TLS:
        * Verify certificate auto-renewal (Let's Encrypt)
        * HSTS header enabled
      - Security headers:
        * Content-Security-Policy
        * X-Frame-Options
        * X-Content-Type-Options
        * Referrer-Policy
    • Nginx configuration:
      - GZIP compression (text assets)
      - Caching headers (long-term for assets, short for HTML)
      - Security headers implementation
      - Performance tuning
    • Documentation:
      - Deployment runbook
      - Emergency recovery procedure
      - Monitoring dashboard access

  Deliverable: Updated nginx.conf, automated backup script, CI/CD workflow
  Report: DEVOPS_ENHANCEMENT_REPORT.md
    - Current infrastructure review
    - Enhancements implemented
    - Backup/recovery procedures
    - Monitoring setup
    - CI/CD workflow documentation
    - Security hardening checklist

Agent 8: Progressive Web App (PWA) Design
  Mission: Design PWA capabilities (Phase 4 implementation-ready)

  Tasks:
    • PWA requirements analysis:
      - Service Worker strategy
      - Offline functionality
      - App manifest
      - Installation on home screen
    • Design service worker approach:
      - Which assets to cache (all images, CSS, JS)
      - Cache strategies (cache-first, network-first, stale-while-revalidate)
      - Update strategy (how to handle new content)
      - Offline fallback page
    • App manifest design:
      - App name, short name
      - Icons (192x192, 512x512)
      - Theme color, background color
      - Display mode (standalone)
      - Orientation (portrait)
      - Start URL
    • Installation UX:
      - Install prompt timing
      - Custom install button
      - Post-install experience
      - Splash screen design
    • Offline capability:
      - Core content accessible offline
      - Message for offline experience
      - When connectivity returns
    • Web app features:
      - Status bar color
      - Window control overlay (optional)
      - Share target (receive shared content)
      - File handling (if applicable)

  Deliverable: PWA design documentation + manifest.json template
  Report: PWA_DESIGN_SPECIFICATION.md
    - PWA benefits for HROC
    - Service worker strategy
    - Cache management approach
    - Installation flow design
    - Offline experience design
    - Implementation timeline & effort estimate

═══════════════════════════════════════════════════════════════════════════════

TIER 3: FUTURE FEATURES DESIGN (4 Agents)

Agent 9: Headless CMS Architecture Design
  Mission: Design CMS system to manage content without developer involvement

  Tasks:
    • CMS requirement analysis:
      - What content changes frequently? (News, events, impact stories)
      - What content is managed? (Services, team, partners)
      - What requires governance? (Nonprofit compliance, accuracy)
    • CMS options evaluation:
      - Self-hosted: Strapi, Payload CMS, Directus
      - Cloud: Contentful, Sanity, Prismic
      - Hybrid: Webflow (visual + CMS)
      - Consideration: Budget, ease of use, integrations
    • Content model design:
      - Blog posts (title, excerpt, content, date, category)
      - Impact stories (title, description, image, impact metric)
      - Events (name, date, time, location, description)
      - Services (name, description, icon, details)
      - Team members (name, role, bio, photo, social links)
      - Partners (name, logo, description)
    • Integration architecture:
      - Static site generation (11ty, Hugo) vs dynamic (fetch from API)
      - Build triggers (on content change, scheduled builds)
      - Content preview (preview before publish)
      - Versioning (track changes, rollback)
    • Governance & workflow:
      - User roles (editor, reviewer, publisher, admin)
      - Approval workflows (for sensitive content)
      - Scheduling (publish at specific date/time)
      - Internationalization (if multilingual needed)
    • Technical implementation:
      - API design (REST vs GraphQL)
      - Caching strategy (cache invalidation on updates)
      - Backup strategy
      - Search capability

  Deliverable: CMS architecture design document
  Report: CMS_ARCHITECTURE_DESIGN.md
    - Recommended CMS platform + rationale
    - Content model schema
    - Integration approach
    - Governance workflow
    - User roles & permissions
    - Implementation timeline & cost estimate
    - Migration strategy from current static content

Agent 10: Community Impact Analytics Dashboard
  Mission: Design analytics dashboard to visualize nonprofit impact

  Tasks:
    • Dashboard purpose:
      - Show donors/volunteers impact of their support
      - Demonstrate effectiveness to funders
      - Track progress toward goals
      - Community engagement insights
    • Key metrics to display:
      - Lives impacted (cumulative)
      - Volunteer hours contributed
      - Naloxone kits distributed
      - Peer support sessions
      - Events hosted
      - Donations received (total, trend)
      - Geographic reach
    • Visual design:
      - Real-time impact counter
      - Progress toward annual goals (bar chart)
      - Impact timeline (how impact has grown)
      - Map of service areas
      - Recent stories carousel
      - Top donors wall (if public)
    • Data sources:
      - Internal database (impact tracking)
      - Donation platform API
      - Volunteer management system
      - Event attendance data
    • Technical approach:
      - Frontend: Chart library (Chart.js, D3.js, Recharts)
      - Backend: API endpoint for metrics
      - Real-time updates: WebSocket or polling
      - Mobile responsive dashboard
    • Privacy considerations:
      - No donor PII displayed
      - Donor privacy respected
      - Volunteer anonymity (if desired)
      - Community stories (with consent)

  Deliverable: Dashboard design mockup + technical specification
  Report: IMPACT_DASHBOARD_DESIGN.md
    - Dashboard layout mockup
    - Key metrics defined
    - Data architecture
    - Real-time update strategy
    - Mobile responsiveness
    - Privacy framework
    - Development estimate for Phase 4
    - Maintenance requirements

Agent 11: Social & Community Features Design
  Mission: Design features for community connection & engagement

  Tasks:
    • Feature brainstorm:
      - User profiles (volunteer, donor, community member)
      - Community forum (support discussions)
      - Event RSVP & social sharing
      - Volunteer opportunities marketplace
      - Referral tracking (for donors)
      - Leaderboard (top volunteers, donors - if incentive-based)
    • Social features:
      - Follow organizations/volunteers
      - Share impact stories
      - Peer support group messaging
      - Event comments & discussions
      - Donation gift (in-kind donation tracking)
    • Community engagement:
      - Newsletter signup
      - SMS updates (opt-in)
      - Podcast/video feed
      - Resource library downloads
      - Discussion forums moderation
    • Technical architecture:
      - User authentication (OAuth with nonprofits/social)
      - Database schema for profiles, connections, content
      - Real-time messaging (WebSocket)
      - Push notifications (optional)
      - Content moderation tools
    • Privacy & governance:
      - Terms of service for community
      - Content policy (what's not allowed)
      - Moderation workflow
      - Abuse reporting mechanism
      - GDPR/privacy compliance
    • Phased rollout:
      - Phase 1: Basic profiles + following
      - Phase 2: Messaging + events
      - Phase 3: Forums + advanced social

  Deliverable: Social features design specification
  Report: SOCIAL_FEATURES_DESIGN.md
    - Feature set definition
    - User journey mapping
    - Database schema
    - Authentication flow
    - Moderation framework
    - Privacy & governance policy
    - Phased development roadmap
    - Effort & timeline estimate

Agent 12: Phase 4 Roadmap & Strategic Planning
  Mission: Synthesize Phase 3 work into comprehensive launch & growth plan

  Tasks:
    • Consolidate Phase 3 deliverables:
      - Performance metrics achieved
      - Accessibility improvements
      - SEO implementation
      - Feature designs (PWA, CMS, Dashboard, Social)
      - DevOps enhancements
    • Phase 4 prioritization:
      - High impact features first (PWA, CMS for content management)
      - Revenue-generating features (improved donation flow)
      - Community-building features (social, forums)
      - Advanced analytics (dashboard)
    • Strategic roadmap:
      - Q1: PWA implementation, CMS integration, donation flow optimization
      - Q2: Social features beta, impact dashboard MVP
      - Q3: Community forums, advanced analytics
      - Q4: Scaling & performance optimization
    • Resource planning:
      - Team size needed (frontend, backend, devops)
      - Timeline estimates for each feature
      - Budget allocation
      - Vendor/third-party integrations
    • Success metrics:
      - User growth targets (monthly)
      - Engagement metrics (time on site, actions)
      - Conversion goals (donations, volunteers)
      - Retention goals (returning visitors)
    • Marketing & growth plan:
      - Launch campaign (press release, social)
      - SEO growth timeline (3-6 months to rank #1)
      - Influencer/partnership strategy
      - Community partnerships (other nonprofits)
      - Grant opportunities (for technical nonprofits)
    • Risk mitigation:
      - Potential blockers identified
      - Contingency plans
      - Technical debt management
      - Scaling challenges prepared for
    • Team handbook:
      - Code style guide
      - Deployment procedures
      - Incident response
      - Documentation requirements

  Deliverable: Comprehensive Phase 4 roadmap + team handbook
  Report: PHASE_4_STRATEGIC_ROADMAP.md
    - Phase 3 summary (achievements & metrics)
    - Phase 4 feature prioritization
    - Quarterly breakdown
    - Resource & timeline planning
    - Success metrics & KPIs
    - Marketing & growth strategy
    - Risk management plan
    - Team handbook excerpt
    - 12-month vision for HROC website

═══════════════════════════════════════════════════════════════════════════════

***EXECUTION PROTOCOL***

Understand Current State:
  ✅ Commit: 7d6d4bf (website transformation complete)
  ✅ Website: Live at https://hrocinc.org
  ✅ Deployment: NAS server 10.0.0.89, Cloudflare Tunnel, HTTPS
  ✅ Images: 61 deployed (community, hero, founders, icons)
  ✅ Code: 47 KB HTML, 43 KB CSS, 12 KB JS
  ✅ Accessibility: WCAG 2.2 AA compliant
  ✅ Mobile: Responsive design tested
  ⏳ Performance: Baseline Lighthouse scores needed (Agent 1)
  ⏳ Advanced features: PWA, CMS, Analytics designed (Agents 8-11)

Launch All 12 Agents Immediately:
  • Do NOT wait for Tier 1 agents to finish before starting Tier 2 & 3
  • Parallelization is critical for efficiency
  • Target: All agents complete in 45-90 minutes
  • Tier 1 must complete before deployment (but others proceed in parallel)

Monitor & Coordinate:
  • Tier 1 (Critical path): Monitor closely, escalate blockers immediately
  • Tier 2 (Quality): Proceed in parallel, integrate findings with Tier 1
  • Tier 3 (Design): Fully independent, no blocking dependencies
  • Use shared TODO to track progress (like main Codex system)
  • Communicate via logs if agents discover cross-dependencies

Deliverables Consolidation:
  • Agent 12 synthesizes all reports into comprehensive document
  • Prioritize: LIGHTHOUSE_OPTIMIZATION_REPORT.md, SEO_OPTIMIZATION_STRATEGY.md
  • Archive all .md files for team reference
  • Create summary with before/after metrics

═══════════════════════════════════════════════════════════════════════════════

***SUCCESS CRITERIA***

Phase 3 Complete When:
  ✅ Lighthouse 95+ across all metrics (Performance, Accessibility, Best Practices, SEO)
  ✅ WCAG 2.2 AAA accessibility compliance verified
  ✅ SEO optimization implemented (schema markup, metadata, keywords)
  ✅ Mobile responsiveness tested across all viewports
  ✅ Code quality reviewed, refactored for maintainability
  ✅ Analytics setup (tracking, goals, baseline metrics)
  ✅ DevOps enhancements (backups, monitoring, CI/CD ready)
  ✅ PWA architecture designed (Phase 4 ready)
  ✅ Headless CMS designed (content management ready)
  ✅ Impact dashboard designed (analytics visualization)
  ✅ Social features designed (community building)
  ✅ Phase 4 strategic roadmap complete (12-month vision)
  ✅ All agents' reports delivered and organized
  ✅ Website deployed with Phase 3 enhancements
  ✅ Team handbook created (for handoff to developers)

═══════════════════════════════════════════════════════════════════════════════

***KEY FILES & CONTEXT***

Current Code:
  • HROC_Website_New/index.html (47 KB)
  • HROC_Website_New/styles.css (43 KB)
  • HROC_Website_New/script.js (12 KB)
  • HROC_Website_New/generated_images/ (56 website images)
  • Generated_Images/Founders/ (founder portraits)

Documentation:
  • WEBSITE_TRANSFORMATION_SUMMARY.md (Phase 2 summary)
  • IMAGE_GENERATION_SUMMARY.md (image inventory)
  • DEPLOYMENT_GUIDE.md (deployment procedures)

Project Context:
  • HROC_FILES/README.md (project overview)
  • CLAUDE.md (if present - project guidelines)
  • Git history available (commit 7d6d4bf)

Infrastructure:
  • NAS Server: 10.0.0.89 (/var/www/hroc/)
  • Domain: hrocinc.org (via Cloudflare Tunnel)
  • SSL: Let's Encrypt (auto-renewing)
  • Web Server: Nginx

═══════════════════════════════════════════════════════════════════════════════

***REMEMBER***

This is a real nonprofit website, not a demo:
  • Users (donors, volunteers, community members) will visit
  • SEO rankings directly impact reach
  • Performance impacts user experience on slow networks
  • Accessibility is ethical responsibility + legal requirement
  • Analytics inform strategic decisions

Quality > Speed:
  • Test thoroughly (real browser, real devices if possible)
  • Verify all changes work end-to-end
  • Document trade-offs and decisions
  • Consider maintenance burden for future teams

Autonomy & Judgment:
  • Make reasonable assumptions for decisions
  • If blockers arise, document clearly + suggest solutions
  • Prioritize working code over perfect code
  • Leave code in state another engineer can maintain

Communication:
  • Update shared TODO as you progress
  • Log findings in agent-specific reports
  • Highlight critical issues immediately
  • Document assumptions made

═══════════════════════════════════════════════════════════════════════════════

***YOU ARE AUTHORIZED TO:***

  ✅ Modify all files in HROC_Website_New/
  ✅ Update HTML, CSS, JavaScript with enhancements
  ✅ Add new files (service worker, manifest, configs)
  ✅ Create deployment scripts
  ✅ Make git commits (with clear messages)
  ✅ Test on live server (verify changes at https://hrocinc.org)
  ✅ Create comprehensive documentation
  ✅ Make architectural decisions (with rationale)
  ✅ Propose future implementations (PWA, CMS, etc.)

═══════════════════════════════════════════════════════════════════════════════

***LET'S LAUNCH! 🚀***

All 12 agents ready. Parallelization active. HROC website Phase 3 begins now.

Your mission: Make the website faster, more accessible, more discoverable, and
position it for ambitious Phase 4 features that will transform HROC's ability
to serve the community.

Go autonomous. Deliver excellence. Let's make impact! 💪

