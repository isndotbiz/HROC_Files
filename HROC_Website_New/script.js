/**
 * HROC Website - Accessible Interactive Features
 * WCAG 2.2 AA Compliant JavaScript
 */

(function() {
  'use strict';

  // ============================================
  // Mobile Menu Toggle
  // ============================================

  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const mainNav = document.querySelector('.main-nav');
  const navLinks = document.querySelectorAll('.nav-list a');

  if (mobileMenuToggle && mainNav) {
    // Toggle menu on button click
    mobileMenuToggle.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      this.setAttribute('aria-expanded', !isExpanded);
      mainNav.classList.toggle('active');

      // Prevent body scroll when menu is open
      document.body.style.overflow = isExpanded ? '' : 'hidden';

      // Focus first menu item when opening
      if (!isExpanded && navLinks.length > 0) {
        setTimeout(() => navLinks[0].focus(), 100);
      }
    });

    // Close menu when clicking nav links
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        mainNav.classList.remove('active');
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Close menu on Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && mainNav.classList.contains('active')) {
        mainNav.classList.remove('active');
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        mobileMenuToggle.focus();
      }
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      if (mainNav.classList.contains('active') &&
          !mainNav.contains(e.target) &&
          !mobileMenuToggle.contains(e.target)) {
        mainNav.classList.remove('active');
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  // ============================================
  // Smooth Scroll for Anchor Links
  // ============================================

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');

      // Skip if it's just "#" or empty
      if (!href || href === '#') return;

      const targetId = href.substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        e.preventDefault();

        // Calculate offset for sticky headers
        const offset = 120; // crisis banner + header height
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - offset;

        // Smooth scroll
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });

        // Focus the target element for accessibility
        setTimeout(() => {
          targetElement.setAttribute('tabindex', '-1');
          targetElement.focus();
          targetElement.removeAttribute('tabindex');
        }, 500);
      }
    });
  });

  // ============================================
  // Form Enhancement & Validation
  // ============================================

  // Donation form
  const donateForm = document.querySelector('.donate-form');
  const customAmountInput = document.getElementById('custom-amount');
  const amountRadios = document.querySelectorAll('input[name="amount"]');

  if (donateForm && customAmountInput) {
    // Enable custom amount input when custom radio is selected
    amountRadios.forEach(radio => {
      radio.addEventListener('change', function() {
        if (this.value === 'custom') {
          customAmountInput.disabled = false;
          customAmountInput.focus();
        } else {
          customAmountInput.disabled = true;
          customAmountInput.value = '';
        }
      });
    });

    // Form submission (placeholder - would connect to payment processor)
    donateForm.addEventListener('submit', function(e) {
      e.preventDefault();

      const frequency = document.querySelector('input[name="frequency"]:checked').value;
      const amountSelected = document.querySelector('input[name="amount"]:checked').value;
      const amount = amountSelected === 'custom' ? customAmountInput.value : amountSelected;

      if (!amount || amount <= 0) {
        alert('Please select or enter a donation amount.');
        return;
      }

      // In production, this would connect to payment processor
      console.log('Donation:', { frequency, amount });
      alert(`Thank you for your ${frequency} donation of $${amount}! (Payment processing would happen here in production)`);
    });
  }

  // Contact form
  const contactForm = document.querySelector('.contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();

      const formData = new FormData(this);
      const data = Object.fromEntries(formData);

      // In production, this would send email or save to database
      console.log('Contact form:', data);

      // Show success message
      const successMessage = document.createElement('div');
      successMessage.className = 'form-success';
      successMessage.style.cssText = 'padding: 1rem; background: #d1fae5; border: 2px solid #047857; border-radius: 0.5rem; margin-top: 1rem; color: #065f46;';
      successMessage.innerHTML = '<strong>✓ Message sent!</strong><br>Thank you for reaching out. We\'ll get back to you soon.';

      this.appendChild(successMessage);
      this.reset();

      // Announce to screen readers
      announceToScreenReader('Your message has been sent successfully');

      // Remove success message after 5 seconds
      setTimeout(() => {
        successMessage.remove();
      }, 5000);
    });
  }

  // ============================================
  // Accessibility Utilities
  // ============================================

  /**
   * Announce message to screen readers
   */
  function announceToScreenReader(message) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = message;

    document.body.appendChild(announcement);

    setTimeout(() => {
      document.body.removeChild(announcement);
    }, 1000);
  }

  // ============================================
  // Intersection Observer for Animations (Accessible)
  // ============================================

  // Only animate if user hasn't requested reduced motion
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReducedMotion) {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, observerOptions);

    // Observe service cards
    document.querySelectorAll('.service-card, .value-card').forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      observer.observe(card);
    });
  }

  // ============================================
  // Lazy Image Reveal (prevents images staying hidden)
  // ============================================

  const lazyImages = document.querySelectorAll('img[loading="lazy"]');

  if (lazyImages.length > 0) {
    lazyImages.forEach((img) => {
      const revealImage = () => {
        img.classList.remove('is-loading');
        img.classList.add('loaded');
      };

      if (img.complete) {
        revealImage();
        return;
      }

      img.classList.add('is-loading');
      img.addEventListener('load', revealImage, { once: true });
      img.addEventListener('error', revealImage, { once: true });
    });
  }

  // ============================================
  // Scroll Progress Indicator
  // ============================================

  function updateScrollProgress() {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight - windowHeight;
    const scrolled = window.scrollY;
    const progress = (scrolled / documentHeight) * 100;

    // Could add a progress bar here if desired
    // For now, just update FAB visibility
    const fabContainer = document.querySelector('.fab-container');
    if (fabContainer) {
      if (scrolled > 300) {
        fabContainer.style.opacity = '1';
        fabContainer.style.pointerEvents = 'auto';
      } else {
        fabContainer.style.opacity = '0';
        fabContainer.style.pointerEvents = 'none';
      }
    }
  }

  window.addEventListener('scroll', updateScrollProgress);
  updateScrollProgress(); // Initial call

  // ============================================
  // External Links - Open in New Tab with Warning
  // ============================================

  document.querySelectorAll('a[href^="http"]').forEach(link => {
    // Only for links not already configured
    if (!link.getAttribute('target')) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');

      // Add screen reader text
      const srText = document.createElement('span');
      srText.className = 'sr-only';
      srText.textContent = ' (opens in new tab)';
      link.appendChild(srText);
    }
  });

  // ============================================
  // Focus Trap for Mobile Menu
  // ============================================

  function trapFocus(element) {
    const focusableElements = element.querySelectorAll(
      'a[href], button:not([disabled]), textarea, input, select'
    );
    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    element.addEventListener('keydown', function(e) {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    });
  }

  if (mainNav) {
    trapFocus(mainNav);
  }

  // ============================================
  // Print Optimization
  // ============================================

  window.addEventListener('beforeprint', function() {
    // Expand all collapsed sections for printing
    document.querySelectorAll('details').forEach(details => {
      details.setAttribute('open', '');
    });
  });

  // ============================================
  // Console Welcome Message
  // ============================================

  console.log('%c🌱 Healing Roots Outreach Collective', 'font-size: 20px; font-weight: bold; color: #047857;');
  console.log('%cIndigenous-led, trauma-informed mobile harm reduction services', 'font-size: 14px; color: #475569;');
  console.log('%c💙 Rooted in community. Growing toward healing.', 'font-size: 12px; color: #0066cc; font-style: italic;');
  console.log('%cWebsite built with accessibility and mobile-first design', 'font-size: 11px; color: #64748b;');

  // ============================================
  // Service Worker Registration (for PWA - optional)
  // ============================================

  if ('serviceWorker' in navigator) {
    // Uncomment to enable offline support
    // window.addEventListener('load', () => {
    //   navigator.serviceWorker.register('/sw.js')
    //     .then(reg => console.log('Service Worker registered'))
    //     .catch(err => console.log('Service Worker registration failed'));
    // });
  }

})();
