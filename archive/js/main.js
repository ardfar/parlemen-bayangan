// Navigation
const nav = document.getElementById('mainNav');
const navToggle = document.getElementById('navToggle');
const mobileMenu = document.getElementById('mobileMenu');

// Scroll effect for nav
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    nav.style.borderBottomColor = 'rgba(30, 64, 175, 0.12)';
    nav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.05)';
  } else {
    nav.style.borderBottomColor = 'var(--border)';
    nav.style.boxShadow = 'none';
  }
});

// Mobile menu toggle
if (navToggle) {
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    mobileMenu.classList.toggle('active');
  });

  // Close mobile menu when clicking on a link
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      mobileMenu.classList.remove('active');
    });
  });
}

// Scroll reveal animation
const observerOptions = {
  threshold: 0.15,
  rootMargin: '0px 0px -40px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, i * 80);
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Tab functionality for Laporan section
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

tabBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const tabId = btn.getAttribute('data-tab');
    
    // Remove active class from all buttons and contents
    tabBtns.forEach(b => b.classList.remove('active'));
    tabContents.forEach(c => c.classList.remove('active'));
    
    // Add active class to clicked button and corresponding content
    btn.classList.add('active');
    document.getElementById(`tab-${tabId}`).classList.add('active');
  });
});

// Komentar form submission
const komentarForm = document.getElementById('komentarForm');
if (komentarForm) {
  komentarForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const formData = new FormData(komentarForm);
    const data = {
      nama: formData.get('nama') || 'Anonim',
      komisi: formData.get('komisi'),
      komentar: formData.get('komentar'),
      tanggal: new Date().toLocaleDateString('id-ID', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      })
    };
    
    // In a real implementation, this would send to a server
    console.log('Komentar submitted:', data);
    
    // Show success message
    alert('Terima kasih! Komentar Anda telah dikirim dan akan dimoderasi sebelum ditampilkan.');
    komentarForm.reset();
  });
}

// Like button functionality
document.querySelectorAll('.komentar-like').forEach(btn => {
  btn.addEventListener('click', function() {
    const currentText = this.textContent;
    const currentCount = parseInt(currentText.match(/\d+/)[0]);
    this.textContent = `👍 ${currentCount + 1}`;
    this.style.color = 'var(--blue)';
    this.style.borderColor = 'var(--blue)';
  });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Animate monitoring bars on scroll
const monitoringBars = document.querySelectorAll('.bar-fill');
const barObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const width = entry.target.style.width;
      entry.target.style.width = '0';
      setTimeout(() => {
        entry.target.style.width = width;
      }, 100);
      barObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

monitoringBars.forEach(bar => barObserver.observe(bar));

// Komisi card hover effect enhancement
document.querySelectorAll('.komisi-card').forEach(card => {
  card.addEventListener('mouseenter', function() {
    this.style.zIndex = '10';
  });
  card.addEventListener('mouseleave', function() {
    this.style.zIndex = '1';
  });
});

// Console welcome message
console.log('%c parlemenbayangan.id ', 'background: #1E40AF; color: white; font-size: 20px; font-weight: bold; padding: 10px 20px; border-radius: 8px;');
console.log('%c Pengawas dari Pengawas ', 'color: #1E40AF; font-size: 14px; padding: 5px 0;');
console.log('Situs ini mengawasi kabinetbayangan.id dengan struktur komisi layaknya DPR RI.');
