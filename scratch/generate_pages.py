import os
import re

INDEX_PATH = 'index.html'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

html_content = read_file(INDEX_PATH)

# Extract parts
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', html_content, re.DOTALL)
head = head_match.group(1) if head_match else ''

# Replace nav links in the new pages to point to .html files, and add back to home
nav_start = html_content.find('<nav id="navbar">')
nav_end = html_content.find('</nav>') + 6
nav = html_content[nav_start:nav_end]

# Modify nav links
nav = nav.replace('href="#manifesto"', 'href="./manifesto.html"')
nav = nav.replace('href="#kriteria"', 'href="./kriteria.html"')
nav = nav.replace('href="#komisi"', 'href="./komisi.html"')
nav = nav.replace('href="#panel"', 'href="./panel.html"')
nav = nav.replace('href="#faq"', 'href="./faq.html"')
nav = nav.replace('href="#gabung"', 'href="./gabung.html"')

# Add "Beranda" to nav links
nav_links_marker = '<div class="nav-links">'
nav = nav.replace(nav_links_marker, nav_links_marker + '\n      <a href="./index.html">← Beranda</a>')


footer_start = html_content.find('<footer>')
script_start = html_content.find('<!-- SCRIPTS -->')
footer = html_content[footer_start:script_start]
scripts = html_content[script_start:]

# Also add extra specific CSS for the new pages in the head
extra_css = """
    /* --- NEW PAGES EXTRA STYLES --- */
    .page-hero {
      min-height: 60vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 160px 24px 80px;
      position: relative;
      background: var(--bg);
    }
    .page-hero::before {
      content: '';
      position: absolute;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(220, 38, 38, 0.08) 0%, transparent 60%);
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      pointer-events: none;
    }
    .page-hero h1 {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: clamp(3rem, 6vw, 4.5rem);
      line-height: 1.1;
      margin-bottom: 24px;
      color: var(--text-primary);
      position: relative;
      z-index: 2;
    }
    .page-hero h1 .highlight { color: var(--red); }
    .page-hero p {
      font-size: 1.25rem;
      color: var(--text-secondary);
      max-width: 700px;
      line-height: 1.6;
      position: relative;
      z-index: 2;
    }
    
    .content-section {
      padding: 80px 24px;
      max-width: 1000px;
      margin: 0 auto;
    }
    .content-section h2 {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 2.2rem;
      margin-bottom: 32px;
      color: var(--text-primary);
    }
    .editorial-text {
      font-size: 1.15rem;
      line-height: 1.9;
      color: var(--text-secondary);
    }
    .editorial-text p { margin-bottom: 24px; }
    
    /* Timeline */
    .timeline {
      position: relative;
      max-width: 800px;
      margin: 60px auto;
      padding: 20px 0;
    }
    .timeline::before {
      content: '';
      position: absolute;
      width: 4px;
      background: var(--border);
      top: 0;
      bottom: 0;
      left: 50%;
      margin-left: -2px;
    }
    .timeline-item {
      padding: 20px 40px;
      position: relative;
      width: 50%;
    }
    .timeline-item:nth-child(odd) { left: 0; text-align: right; }
    .timeline-item:nth-child(even) { left: 50%; }
    .timeline-item::after {
      content: '';
      position: absolute;
      width: 20px;
      height: 20px;
      background: var(--bg);
      border: 4px solid var(--red);
      border-radius: 50%;
      top: 24px;
    }
    .timeline-item:nth-child(odd)::after { right: -10px; }
    .timeline-item:nth-child(even)::after { left: -10px; }
    .timeline-content h3 { font-family: 'Outfit', sans-serif; font-size: 1.4rem; margin-bottom: 8px; color: var(--text-primary); }
    .timeline-content p { font-size: 1rem; color: var(--text-secondary); line-height: 1.6; }
    
    @media (max-width: 768px) {
      .timeline::before { left: 20px; }
      .timeline-item { width: 100%; padding-left: 60px; padding-right: 20px; text-align: left !important; left: 0 !important; }
      .timeline-item::after { left: 10px !important; right: auto !important; }
    }
    
    .light-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 40px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.02);
      transition: all 0.3s;
    }
    .light-card:hover { border-color: var(--red); box-shadow: 0 15px 40px rgba(220,38,38,0.08); transform: translateY(-5px); }
    
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; }
    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; }
    
    @media (max-width: 768px) {
      .grid-2, .grid-3 { grid-template-columns: 1fr; }
    }
"""

head = head.replace('</style>', extra_css + '\n</style>')

def build_page(title, content):
    page_head = head.replace('<title>parlemenbayangan.id — mengawal kabinet bayangan, menguji gagasan</title>', f'<title>{title} — parlemenbayangan.id</title>')
    return f"""{page_head}
<body>
{nav}
{content}
{footer}
{scripts}
"""

# =======================
# MANIFESTO PAGE
# =======================
manifesto_content = """
  <section class="page-hero">
    <div class="section-label reveal">Manifesto</div>
    <h1 class="reveal">Mengawal Kabinet Bayangan, memastikan setiap kebijakan <span class="highlight">teruji.</span></h1>
    <p class="reveal">Demokrasi yang sehat menuntut perdebatan publik yang tajam. Kami hadir untuk merebut kembali ruang deliberasi.</p>
  </section>

  <section class="content-section">
    <h2 class="reveal">Latar Belakang</h2>
    <div class="editorial-text reveal">
      <p>Hari ini, gedung wakil rakyat lebih sering sunyi dari perdebatan substantif. Fungsi <em>checks and balances</em> lumpuh oleh koalisi mayoritas dan politik akomodasi. Parlemen formal yang seharusnya menjadi benteng aspirasi justru kerap berubah menjadi stempel karet bagi penguasa.</p>
      <p>Akibatnya, regulasi dan kebijakan lahir dengan tergesa-gesa, tanpa partisipasi publik yang bermakna. Mulai dari revisi UU KPK, pengesahan UU Cipta Kerja yang kontroversial, hingga berbagai kebijakan lain yang cacat prosedur. Publik dibiarkan hanya sebagai penonton, bukan aktor yang berdaulat atas nasibnya sendiri.</p>
    </div>
    
    <div class="timeline reveal">
      <div class="timeline-item">
        <div class="timeline-content">
          <h3>Kemunduran Oposisi</h3>
          <p>Dominasi koalisi mayoritas di parlemen formal membuat perdebatan kebijakan menjadi formalitas belaka. Tidak ada lagi pihak yang secara kritis membedah RUU dan anggaran.</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-content">
          <h3>Kekosongan Deliberasi</h3>
          <p>Masyarakat sipil merasa kehilangan saluran efektif untuk menyuarakan alternatif. Demo dan petisi seringkali diabaikan tanpa argumen rasional dari penguasa.</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-content">
          <h3>Lahirnya Inisiatif</h3>
          <p>Sebagai respon, <strong>parlemenbayangan.id</strong> didirikan. Sebuah institusi independen, dikawal oleh para profesional, untuk menghadirkan uji publik yang sesungguhnya.</p>
        </div>
      </div>
    </div>
  </section>
  
  <div class="divider"></div>
  
  <section class="content-section">
    <h2 class="reveal">Prinsip Kami</h2>
    <div class="grid-2 reveal">
      <div class="light-card">
        <h3 style="margin-bottom: 16px; font-family: 'Outfit'; font-size: 1.5rem; color: var(--red);">Independensi</h3>
        <p class="editorial-text">Kami tidak berafiliasi dengan partai politik mana pun, oposisi maupun koalisi. Kami berdiri di atas landasan nalar dan kepentingan publik murni.</p>
      </div>
      <div class="light-card">
        <h3 style="margin-bottom: 16px; font-family: 'Outfit'; font-size: 1.5rem; color: var(--red);">Berbasis Bukti (Evidence-Based)</h3>
        <p class="editorial-text">Setiap kritik dan kebijakan alternatif yang kami tawarkan lahir dari kajian mendalam, data yang valid, dan riset para pakar.</p>
      </div>
      <div class="light-card">
        <h3 style="margin-bottom: 16px; font-family: 'Outfit'; font-size: 1.5rem; color: var(--red);">Transparansi</h3>
        <p class="editorial-text">Semua <em>Shadow Hearing</em> disiarkan secara terbuka, dokumen kebijakan dapat diakses publik, dan proses pengambilan keputusan kami pertanggungjawabkan.</p>
      </div>
      <div class="light-card">
        <h3 style="margin-bottom: 16px; font-family: 'Outfit'; font-size: 1.5rem; color: var(--red);">Konstruktif</h3>
        <p class="editorial-text">Kami tidak hanya menolak, tetapi menawarkan jalan keluar. Kami merumuskan <em>Policy Paper</em> sebagai komparasi langsung terhadap kebijakan pemerintah.</p>
      </div>
    </div>
  </section>
  
  <div class="divider"></div>
  
  <section class="content-section text-center" style="text-align: center; padding: 100px 24px;">
    <h2 class="reveal">Mari Mengambil Peran</h2>
    <p class="editorial-text reveal" style="margin: 0 auto 40px; max-width: 700px;">Rakyat harus memegang palu sidangnya sendiri, mengawal lahirnya kebijakan alternatif, dan mengambil kembali kendali atas arah masa depan republik ini.</p>
    <a href="./gabung.html" class="btn-primary reveal" style="width: auto;">Bergabung Bersama Kami →</a>
  </section>
"""

# =======================
# KRITERIA PAGE
# =======================
kriteria_content = """
  <section class="page-hero">
    <div class="section-label reveal">Kriteria (Ajakan Terbuka)</div>
    <h1 class="reveal">Siapa yang <span class="highlight">Kami Cari</span></h1>
    <p class="reveal">Kami memanggil para pemikir tajam, pekerja keras, dan jiwa-jiwa tak terbeli untuk menjadi bagian dari penguji gagasan Kabinet Bayangan.</p>
  </section>
  
  <section class="content-section">
    <p class="editorial-text reveal" style="margin-bottom: 60px; font-size: 1.25rem;">Gagasan dan kebijakan alternatif memerlukan pengawasan dan pengujian yang kritis. Kita membutuhkan ruang di mana setiap argumen dibedah secara substantif, bukan sekadar diaminkan. Ini adalah undangan terbuka bagi Anda—para pemikir tajam, pekerja keras, dan jiwa-jiwa tak terbeli—untuk mengambil peran dalam mengawal Kabinet Bayangan.</p>
    
    <div class="criteria-grid" style="display: flex; flex-direction: column; gap: 40px;">
      <!-- Criteria 1 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start;">
        <div class="icon-box" style="background: var(--bg-soft); color: var(--text-primary); border-color: var(--border); flex-shrink: 0; box-shadow: none;">🛡️</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px;">1. Integritas Baja</h3>
          <p class="editorial-text">Tidak bisa dibeli, tidak bisa ditundukkan oleh intimidasi, bujukan oligarki, maupun godaan jabatan semu.</p>
          <div style="margin-top: 16px; padding: 16px; background: var(--bg-soft); border-left: 3px solid var(--red); border-radius: 0 8px 8px 0;">
            <strong>Indikator:</strong> Rekam jejak bebas dari kasus korupsi, konflik kepentingan, dan tidak pernah mengkompromikan prinsip demi keuntungan pribadi.
          </div>
        </div>
      </div>
      
      <!-- Criteria 2 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start;">
        <div class="icon-box" style="background: var(--bg-soft); color: var(--text-primary); border-color: var(--border); flex-shrink: 0; box-shadow: none;">⚡</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px;">2. Energi Pembaruan</h3>
          <p class="editorial-text">Membawa nyala perlawanan baru dan perspektif segar. Tidak tersandera oleh dosa dan beban masa lalu.</p>
          <div style="margin-top: 16px; padding: 16px; background: var(--bg-soft); border-left: 3px solid var(--red); border-radius: 0 8px 8px 0;">
            <strong>Indikator:</strong> Kemampuan menawarkan solusi inovatif (out-of-the-box) dan tidak terjebak dalam birokrasi berpikir konvensional.
          </div>
        </div>
      </div>
      
      <!-- Criteria 3 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start;">
        <div class="icon-box" style="background: var(--bg-soft); color: var(--text-primary); border-color: var(--border); flex-shrink: 0; box-shadow: none;">🧠</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px;">3. Ketajaman Analisis</h3>
          <p class="editorial-text">Memiliki pisau bedah keilmuan yang presisi. Berbicara dengan data, membantah dengan fakta yang tak terbantahkan.</p>
          <div style="margin-top: 16px; padding: 16px; background: var(--bg-soft); border-left: 3px solid var(--red); border-radius: 0 8px 8px 0;">
            <strong>Indikator:</strong> Kepakaran di bidangnya masing-masing, kemampuan menulis <em>policy brief</em>, dan kemampuan berdebat rasional.
          </div>
        </div>
      </div>
      
      <!-- Criteria 4 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start;">
        <div class="icon-box" style="background: var(--bg-soft); color: var(--text-primary); border-color: var(--border); flex-shrink: 0; box-shadow: none;">📜</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px;">4. Rekam Jejak Teruji</h3>
          <p class="editorial-text">Nama dan karyanya dihormati oleh publik dan gerakan sipil. Konsistensi perjuangannya tidak pernah diragukan.</p>
          <div style="margin-top: 16px; padding: 16px; background: var(--bg-soft); border-left: 3px solid var(--red); border-radius: 0 8px 8px 0;">
            <strong>Indikator:</strong> Karya akademik, advokasi, atau pengalaman lapangan yang terbukti memberikan dampak positif bagi masyarakat.
          </div>
        </div>
      </div>
      
      <!-- Criteria 5 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start;">
        <div class="icon-box" style="background: var(--bg-soft); color: var(--text-primary); border-color: var(--border); flex-shrink: 0; box-shadow: none;">🔥</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px;">5. Keberanian Moral</h3>
          <p class="editorial-text">Berani berdiri sendirian demi kebenaran. Menolak diam dan bungkam saat hak serta nalar publik diinjak-injak.</p>
        </div>
      </div>
      
      <!-- Criteria 6 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start;">
        <div class="icon-box" style="background: var(--bg-soft); color: var(--text-primary); border-color: var(--border); flex-shrink: 0; box-shadow: none;">✊</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px;">6. Loyalitas Kerakyatan</h3>
          <p class="editorial-text">Mendedikasikan waktu, tenaga, dan pikiran mutlak murni untuk kepentingan orang banyak. Tanpa kompromi sedikitpun.</p>
        </div>
      </div>
      
      <!-- Criteria 7 -->
      <div class="light-card reveal" style="display: flex; gap: 32px; align-items: flex-start; border-color: var(--red); background: var(--red-subtle);">
        <div class="icon-box" style="background: var(--red); color: white; border-color: var(--red-bright); flex-shrink: 0;">⚖️</div>
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 16px; color: var(--red);">7. Independensi Mutlak</h3>
          <p class="editorial-text" style="color: var(--text-primary);">Bebas 100% dari belenggu partai politik dan kepentingan kekuasaan. Hanya tunduk pada akal sehat konstitusi.</p>
          <div style="margin-top: 16px; padding: 16px; background: white; border-radius: 8px;">
            <strong>Mengapa Ini Kritis:</strong> Parlemen bayangan akan kehilangan marwahnya jika ditunggangi kepentingan politik praktis. Anggota tidak boleh merupakan pengurus partai politik aktif.
          </div>
        </div>
      </div>
    </div>
  </section>
  
  <div class="divider"></div>
  
  <section class="content-section">
    <h2 class="reveal">Proses Seleksi</h2>
    <div class="grid-3 reveal">
      <div class="light-card" style="text-align: center;">
        <h1 style="font-family: 'Bebas Neue'; font-size: 4rem; color: var(--border); margin-bottom: 16px;">01</h1>
        <h3 style="font-family: 'Outfit'; margin-bottom: 12px; font-size: 1.3rem;">Penjaringan</h3>
        <p class="editorial-text" style="font-size: 1rem;">Publik menominasikan kandidat atau mendaftarkan diri secara mandiri melalui form resmi.</p>
      </div>
      <div class="light-card" style="text-align: center;">
        <h1 style="font-family: 'Bebas Neue'; font-size: 4rem; color: var(--border); margin-bottom: 16px;">02</h1>
        <h3 style="font-family: 'Outfit'; margin-bottom: 12px; font-size: 1.3rem;">Audit Rekam Jejak</h3>
        <p class="editorial-text" style="font-size: 1rem;">Panel Seleksi menelusuri independensi, integritas, dan kompetensi kandidat yang lolos tahap awal.</p>
      </div>
      <div class="light-card" style="text-align: center;">
        <h1 style="font-family: 'Bebas Neue'; font-size: 4rem; color: var(--red); margin-bottom: 16px;">03</h1>
        <h3 style="font-family: 'Outfit'; margin-bottom: 12px; font-size: 1.3rem;">Pengesahan</h3>
        <p class="editorial-text" style="font-size: 1rem;">Kandidat terpilih akan diumumkan secara publik dan dilantik dalam Sidang Rakyat Pertama.</p>
      </div>
    </div>
  </section>
"""

# =======================
# KOMISI PAGE
# =======================
komisi_content = """
  <section class="page-hero">
    <div class="section-label reveal">Struktur Komisi</div>
    <h1 class="reveal">Ramping, strategis, <span class="highlight">berbasis urgensi.</span></h1>
    <p class="reveal">Lima komisi yang dirancang untuk mengawal isu-isu paling krusial. Merespons portofolio Kabinet Bayangan secara langsung dan efektif.</p>
  </section>

  <section class="content-section">
    <div style="display: flex; flex-direction: column; gap: 80px;">
    
      <!-- Komisi I -->
      <div class="reveal" style="position: relative; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px; padding: 64px 48px; overflow: hidden;">
        <div style="position: absolute; right: -20px; bottom: -40px; font-family: 'Bebas Neue'; font-size: 20rem; color: var(--border); opacity: 0.2; line-height: 0.8; z-index: 0; pointer-events: none;">I</div>
        <div style="position: relative; z-index: 1;">
          <div style="width: 60px; height: 4px; background: var(--red); border-radius: 2px; margin-bottom: 24px;"></div>
          <h2 style="font-size: 2.5rem; margin-bottom: 32px;">Politik, Hukum, Pertahanan &amp; Diplomasi</h2>
          <div class="grid-2">
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Ruang Lingkup</h4>
              <p class="editorial-text">Fokus pada reformasi hukum, tata negara, pengawasan institusi pertahanan, serta arah diplomasi Indonesia di kancah global. Memastikan tidak ada perundangan yang diselundupkan untuk kepentingan oligarki.</p>
              
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-top: 32px; margin-bottom: 16px;">Mandat Utama</h4>
              <ul class="editorial-text" style="padding-left: 20px;">
                <li>Eksaminasi produk legislasi bermasalah</li>
                <li>Pengawasan anggaran pertahanan & Alutsista</li>
                <li>Perlindungan HAM & Anti-Korupsi</li>
              </ul>
            </div>
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Anggota Komisi</h4>
              <div style="background: var(--bg-soft); padding: 24px; border-radius: 16px;">
                <p class="editorial-text" style="margin-bottom: 12px;"><strong>Feri Amsari</strong> <span style="font-size: 0.8rem; padding: 4px 8px; background: var(--red-subtle); color: var(--red); border-radius: 100px; margin-left: 8px;">Koordinator</span></p>
                <p class="editorial-text" style="margin-bottom: 12px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">Pakar Hukum Tata Negara, Akademisi Universitas Andalas</p>
                <p class="editorial-text"><strong>Shofwan Al Banna</strong> — Hubungan Internasional</p>
                <p class="editorial-text"><strong>Arman Suparman</strong> — Pemantau Peradilan</p>
                <p class="editorial-text"><strong>Yance Arizona</strong> — Hukum Adat & Agraria</p>
                <p class="editorial-text"><strong>Curie Maharani</strong> — Analis Pertahanan</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Komisi II -->
      <div class="reveal" style="position: relative; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px; padding: 64px 48px; overflow: hidden;">
        <div style="position: absolute; right: -20px; bottom: -40px; font-family: 'Bebas Neue'; font-size: 20rem; color: var(--border); opacity: 0.2; line-height: 0.8; z-index: 0; pointer-events: none;">II</div>
        <div style="position: relative; z-index: 1;">
          <div style="width: 60px; height: 4px; background: var(--red); border-radius: 2px; margin-bottom: 24px;"></div>
          <h2 style="font-size: 2.5rem; margin-bottom: 32px;">Ekonomi, Keuangan &amp; Tata Kelola</h2>
          <div class="grid-2">
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Ruang Lingkup</h4>
              <p class="editorial-text">Mengawasi stabilitas makroekonomi, keadilan fiskal, penyusunan APBN, investasi, dan tata kelola BUMN. Memastikan pembangunan ekonomi berdampak langsung pada kesejahteraan rakyat, bukan segelintir elit.</p>
            </div>
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Anggota Komisi</h4>
              <div style="background: var(--bg-soft); padding: 24px; border-radius: 16px;">
                <p class="editorial-text" style="margin-bottom: 12px;"><strong>Bhima Yudhistira</strong> <span style="font-size: 0.8rem; padding: 4px 8px; background: var(--red-subtle); color: var(--red); border-radius: 100px; margin-left: 8px;">Koordinator</span></p>
                <p class="editorial-text" style="margin-bottom: 12px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">Ekonom, Direktur CELIOS</p>
                <p class="editorial-text"><strong>Media Wahyudi</strong> — Pakar Keuangan Publik</p>
                <p class="editorial-text" style="color: var(--text-muted); font-style: italic; margin-top: 12px;">*Kursi anggota masih dalam tahap penjaringan</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Komisi III -->
      <div class="reveal" style="position: relative; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px; padding: 64px 48px; overflow: hidden;">
        <div style="position: absolute; right: -20px; bottom: -40px; font-family: 'Bebas Neue'; font-size: 20rem; color: var(--border); opacity: 0.2; line-height: 0.8; z-index: 0; pointer-events: none;">III</div>
        <div style="position: relative; z-index: 1;">
          <div style="width: 60px; height: 4px; background: var(--red); border-radius: 2px; margin-bottom: 24px;"></div>
          <h2 style="font-size: 2.5rem; margin-bottom: 32px;">Pembangunan Manusia</h2>
          <div class="grid-2">
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Ruang Lingkup</h4>
              <p class="editorial-text">Berpusat pada peningkatan kualitas hidup melalui kebijakan pendidikan, jaminan kesehatan, perlindungan perempuan dan anak, serta penguatan kelompok rentan dan layanan sosial.</p>
            </div>
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Anggota Komisi</h4>
              <div style="background: var(--bg-soft); padding: 24px; border-radius: 16px;">
                <p class="editorial-text" style="margin-bottom: 12px;"><strong>Irma Hidayana</strong> <span style="font-size: 0.8rem; padding: 4px 8px; background: var(--red-subtle); color: var(--red); border-radius: 100px; margin-left: 8px;">Koordinator</span></p>
                <p class="editorial-text" style="margin-bottom: 12px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">Pakar Kesehatan Masyarakat, Inisiator LaporCovid-19</p>
                <p class="editorial-text"><strong>Iman Zanatul H.</strong> — Kebijakan Pendidikan</p>
                <p class="editorial-text"><strong>Nabiyla Risfa I.</strong> — Hak Kelompok Rentan</p>
                <p class="editorial-text"><strong>Khoirunnisa N.</strong> — Perlindungan Perempuan</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Komisi IV -->
      <div class="reveal" style="position: relative; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px; padding: 64px 48px; overflow: hidden;">
        <div style="position: absolute; right: -20px; bottom: -40px; font-family: 'Bebas Neue'; font-size: 20rem; color: var(--border); opacity: 0.2; line-height: 0.8; z-index: 0; pointer-events: none;">IV</div>
        <div style="position: relative; z-index: 1;">
          <div style="width: 60px; height: 4px; background: var(--red); border-radius: 2px; margin-bottom: 24px;"></div>
          <h2 style="font-size: 2.5rem; margin-bottom: 32px;">Ketahanan Pangan, Lingkungan &amp; Transformasi Digital</h2>
          <div class="grid-2">
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Ruang Lingkup</h4>
              <p class="editorial-text">Mengawasi transisi energi berkeadilan, kedaulatan pangan, mitigasi krisis iklim, serta kebijakan transformasi digital yang melindungi hak privasi warga.</p>
            </div>
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 16px;">Anggota Komisi</h4>
              <div style="background: var(--bg-soft); padding: 24px; border-radius: 16px;">
                <p class="editorial-text" style="margin-bottom: 12px;"><strong>Iqbal Damanik</strong> <span style="font-size: 0.8rem; padding: 4px 8px; background: var(--red-subtle); color: var(--red); border-radius: 100px; margin-left: 8px;">Koordinator</span></p>
                <p class="editorial-text" style="margin-bottom: 12px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">Aktivis Lingkungan & Iklim Greenpeace</p>
                <p class="editorial-text"><strong>Isnawati Hidayah</strong> — Analis Transisi Energi</p>
                <p class="editorial-text"><strong>Nenden Sekar A.</strong> — Hak Digital (SAFEnet)</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Komisi V -->
      <div class="reveal" style="position: relative; background: var(--red); color: white; border-radius: 24px; padding: 64px 48px; overflow: hidden; box-shadow: 0 20px 40px rgba(220,38,38,0.2);">
        <div style="position: absolute; right: -20px; bottom: -40px; font-family: 'Bebas Neue'; font-size: 20rem; color: white; opacity: 0.1; line-height: 0.8; z-index: 0; pointer-events: none;">V</div>
        <div style="position: relative; z-index: 1;">
          <div style="width: 60px; height: 4px; background: white; border-radius: 2px; margin-bottom: 24px;"></div>
          <h2 style="font-size: 2.5rem; margin-bottom: 32px; color: white;">Sekretariat, Strategi &amp; Monitoring Kebijakan</h2>
          <div class="grid-2">
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.7); margin-bottom: 16px;">Fungsi Komando</h4>
              <p class="editorial-text" style="color: white;">Komisi ini bertindak sebagai jantung operasional Parlemen Bayangan. Mensinkronkan temuan lintas komisi, mengatur strategi komunikasi publik, dan mendistribusikan <em>Policy Paper</em> kepada masyarakat dan pengambil kebijakan.</p>
            </div>
            <div>
              <h4 style="font-family: 'Outfit'; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.7); margin-bottom: 16px;">Penanggung Jawab</h4>
              <div style="background: rgba(0,0,0,0.15); padding: 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2);">
                <p class="editorial-text" style="color: white; font-size: 1.25rem;"><strong>Ahmad Jilul Q. F.</strong></p>
                <p class="editorial-text" style="color: rgba(255,255,255,0.8);">Sekretaris Kabinet / Direktur Eksekutif</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </section>
"""

# =======================
# PANEL PAGE
# =======================
panel_content = """
  <section class="page-hero">
    <div class="section-label reveal">Panel Seleksi</div>
    <h1 class="reveal">Mereka yang <span class="highlight">Menilai.</span></h1>
    <p class="reveal">Seleksi formasi parlemen dilakukan oleh panel independen. Mereka adalah profesional dengan rekam jejak nyata di bidang hukum, ekonomi, dan tata kelola pemerintahan.</p>
  </section>
  
  <section class="content-section">
    <div class="grid-3">
      <!-- Panel 1 -->
      <div class="light-card reveal" style="text-align: center;">
        <img src="https://placehold.co/200x200/DC2626/FFFFFF?text=ZA" alt="Prof. Dr. Zainal Arifin Mochtar" style="width: 160px; height: 160px; border-radius: 50%; border: 4px solid var(--border); margin-bottom: 24px; object-fit: cover;">
        <h3 style="font-family: 'Outfit'; font-size: 1.4rem; margin-bottom: 8px;">Prof. Dr. Zainal Arifin Mochtar</h3>
        <p style="color: var(--red); font-size: 0.9rem; font-weight: 700; margin-bottom: 24px; letter-spacing: 0.05em;">PAKAR HUKUM TATA NEGARA</p>
        <p class="editorial-text" style="font-size: 1rem; margin-bottom: 24px; text-align: left;">Guru Besar Hukum Kelembagaan Negara di Fakultas Hukum UGM. Penulis Buku 'Kronik Otoritarianisme Indonesia' dan dikenal luas sebagai akademisi yang kritis terhadap regresi demokrasi dan pelemahan institusi penegak hukum.</p>
        <ul class="editorial-text" style="font-size: 0.95rem; text-align: left; padding-left: 20px;">
          <li>Mantan Direktur PUKAT Korupsi UGM</li>
          <li>Kritikus UU Cipta Kerja & Revisi UU KPK</li>
        </ul>
      </div>
      
      <!-- Panel 2 -->
      <div class="light-card reveal" style="text-align: center;">
        <img src="https://placehold.co/200x200/DC2626/FFFFFF?text=BS" alt="Bivitri Susanti" style="width: 160px; height: 160px; border-radius: 50%; border: 4px solid var(--border); margin-bottom: 24px; object-fit: cover;">
        <h3 style="font-family: 'Outfit'; font-size: 1.4rem; margin-bottom: 8px;">Bivitri Susanti</h3>
        <p style="color: var(--red); font-size: 0.9rem; font-weight: 700; margin-bottom: 24px; letter-spacing: 0.05em;">AHLI HUKUM KETATANEGARAAN</p>
        <p class="editorial-text" style="font-size: 1rem; margin-bottom: 24px; text-align: left;">Pendiri Pusat Studi Hukum dan Kebijakan (PSHK) dan pengajar di Jentera Law School. Beliau konsisten mengadvokasi pembaruan hukum, hak asasi manusia, dan mengkritisi produk legislasi yang cacat formil.</p>
        <ul class="editorial-text" style="font-size: 0.95rem; text-align: left; padding-left: 20px;">
          <li>Pendiri PSHK</li>
          <li>Pengajar STH Indonesia Jentera</li>
        </ul>
      </div>
      
      <!-- Panel 3 -->
      <div class="light-card reveal" style="text-align: center;">
        <img src="https://placehold.co/200x200/DC2626/FFFFFF?text=ER" alt="Erry Riyana Hardjapamekas" style="width: 160px; height: 160px; border-radius: 50%; border: 4px solid var(--border); margin-bottom: 24px; object-fit: cover;">
        <h3 style="font-family: 'Outfit'; font-size: 1.4rem; margin-bottom: 8px;">Erry Riyana Hardjapamekas</h3>
        <p style="color: var(--red); font-size: 0.9rem; font-weight: 700; margin-bottom: 24px; letter-spacing: 0.05em;">TOKOH ANTI-KORUPSI</p>
        <p class="editorial-text" style="font-size: 1rem; margin-bottom: 24px; text-align: left;">Wakil Ketua KPK Periode 2003–2007. Memiliki integritas tinggi dalam tata kelola pemerintahan dan BUMN. Saat ini mengetuai Koalisi Anti Korupsi Indonesia dan terus menyuarakan pentingnya etika publik.</p>
        <ul class="editorial-text" style="font-size: 0.95rem; text-align: left; padding-left: 20px;">
          <li>Wakil Ketua KPK (2003-2007)</li>
          <li>Pendiri Masyarakat Transparansi Indonesia</li>
        </ul>
      </div>
    </div>
  </section>
  
  <div class="divider"></div>
  
  <section class="content-section">
    <h2 class="reveal">Metodologi Seleksi</h2>
    <div class="editorial-text reveal">
      <p>Panel independen bekerja menggunakan matriks penilaian yang objektif. Keputusan panel bersifat mutlak dan tidak dapat diintervensi oleh pihak mana pun, termasuk inisiator Parlemen Bayangan.</p>
      
      <div style="margin: 40px 0; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; overflow: hidden;">
        <div style="background: var(--bg-soft); padding: 16px 24px; border-bottom: 1px solid var(--border); font-family: 'Outfit'; font-weight: 700;">Rubrik Penilaian Utama</div>
        <div style="padding: 24px; display: grid; grid-template-columns: 1fr 2fr; gap: 16px; border-bottom: 1px solid var(--border);">
          <strong style="color: var(--text-primary);">Independensi Politik (40%)</strong>
          <span>Kandidat harus bebas dari afiliasi partai politik, tim kampanye pemilu terakhir, dan posisi komisaris/direksi BUMN/BUMD.</span>
        </div>
        <div style="padding: 24px; display: grid; grid-template-columns: 1fr 2fr; gap: 16px; border-bottom: 1px solid var(--border);">
          <strong style="color: var(--text-primary);">Rekam Jejak Akademik & Advokasi (35%)</strong>
          <span>Karya tulis (jurnal/buku/opini), rekam jejak advokasi kebijakan publik yang terbukti membela hak masyarakat.</span>
        </div>
        <div style="padding: 24px; display: grid; grid-template-columns: 1fr 2fr; gap: 16px;">
          <strong style="color: var(--text-primary);">Analisis & Artikulasi (25%)</strong>
          <span>Kemampuan untuk menyampaikan kritik yang tajam, rasional, berbasis data, dan dapat dipahami oleh publik luas.</span>
        </div>
      </div>
      
      <p><em>*Setiap anggota panel akan menandatangani pakta integritas dan deklarasi bebas konflik kepentingan sebelum melakukan penelaahan profil kandidat.</em></p>
    </div>
  </section>
"""

# =======================
# FAQ PAGE
# =======================
faq_content = """
  <section class="page-hero">
    <div class="section-label reveal">Pertanyaan Umum (FAQ)</div>
    <h1 class="reveal">Mendedah keraguan, <span class="highlight">menjawab pertanyaan.</span></h1>
    <p class="reveal">Temukan jawaban mendalam mengenai fungsi, struktur, dan independensi parlemenbayangan.id.</p>
  </section>
  
  <section class="content-section" style="max-width: 900px;">
    <!-- Kategori 1 -->
    <h3 class="reveal" style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 24px; margin-top: 40px; color: var(--red);">Tentang Organisasi</h3>
    <div class="faq-list">
      <!-- Reuse exact same structure as homepage FAQ for styling -->
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">01</span>
          <span class="faq-text">Apa itu parlemenbayangan.id?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            Sebuah platform independen masyarakat sipil yang berfungsi khusus untuk mengawasi <em>Kabinet Bayangan</em>. Kami hadir untuk membedah, menguji, dan memastikan kualitas dari setiap alternatif kebijakan publik yang ditawarkan. Platform ini berfungsi sebagai wadah kolaborasi lintas elemen: akademisi, aktivis, teknokrat, jurnalis, hingga organisasi masyarakat.
          </div>
        </div>
      </div>
      
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">02</span>
          <span class="faq-text">Kenapa Indonesia butuh institusi "bayangan" ini?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            Fungsi pengawasan parlemen formal seringkali tumpul akibat dominasi koalisi mayoritas. Ketika sistem <em>checks and balances</em> lumpuh dan gedung wakil rakyat sekadar menjadi stempel karet, masyarakat sipil harus mengambil inisiatif untuk mengisi kekosongan ruang deliberasi tersebut demi merawat nalar publik.
          </div>
        </div>
      </div>
      
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">03</span>
          <span class="faq-text">Apakah gerakan ini berafiliasi dengan partai oposisi?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            <strong>Sama sekali tidak.</strong> Independensi adalah ruh dari gerakan ini. Parlemen Bayangan tidak terafiliasi, tidak didanai, dan tidak bekerja untuk partai politik mana pun. Kami berpihak 100% pada akal sehat konstitusi dan kepentingan masyarakat luas.
          </div>
        </div>
      </div>
      
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">04</span>
          <span class="faq-text">Dari mana pendanaan gerakan ini?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            Gerakan ini diinisiasi secara <em>crowdsourced</em> dan partisipatif oleh jaringan masyarakat sipil. Operasional ditopang melalui kerja-kerja kerelawanan pro-bono (tanpa bayaran). Jika di masa depan diperlukan penggalangan dana publik (crowdfunding), laporannya akan diaudit dan dipublikasikan secara transparan. Kami tidak menerima dana dari partai politik, korporasi penyumbang emisi/oligarki, atau lembaga asing dengan agenda politis.
          </div>
        </div>
      </div>
    </div>
    
    <!-- Kategori 2 -->
    <h3 class="reveal" style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 24px; margin-top: 80px; color: var(--red);">Sistem & Cara Kerja</h3>
    <div class="faq-list">
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">05</span>
          <span class="faq-text">Bagaimana cara kerja Parlemen Bayangan?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            Berbeda dengan LSM yang fokus pada isu tunggal, kami mengadopsi struktur komisi. Kami akan:
            <ul class="faq-bullets">
              <li>Menyelenggarakan <em>Shadow Hearing</em> (Sidang Terbuka Rakyat) yang mengundang pakar dan warga terdampak.</li>
              <li>Membedah kelemahan RUU/Kebijakan dan merilis Kertas Kebijakan Alternatif (<em>Policy Paper</em>).</li>
              <li>Mengaudit janji kampanye dan mengawasi langsung gagasan-gagasan yang ditawarkan oleh Kabinet Bayangan.</li>
            </ul>
          </div>
        </div>
      </div>
      
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">06</span>
          <span class="faq-text">Apakah anggota komisi menerima bayaran finansial?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            <strong>Tidak ada insentif finansial.</strong> Seluruh posisi di Parlemen Bayangan bersifat <em>pro bono</em> (sukarela). Anggotanya adalah para profesional dengan karir utamanya masing-masing. Di situlah letak kekuatan gerakan ini: independen, tidak terikat transaksi, dan tidak bisa dibeli.
          </div>
        </div>
      </div>
    </div>
    
    <!-- Kategori 3 -->
    <h3 class="reveal" style="font-family: 'Outfit'; font-size: 1.8rem; margin-bottom: 24px; margin-top: 80px; color: var(--red);">Partisipasi Publik</h3>
    <div class="faq-list">
      <div class="faq-item reveal">
        <button class="faq-question" onclick="toggleFaq(this)">
          <span class="faq-num">07</span>
          <span class="faq-text">Bagaimana masyarakat umum bisa terlibat?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <div class="faq-answer-inner">
            Suara Anda adalah amunisi kami. Anda bisa berpartisipasi dengan: memberikan rekomendasi tokoh kredibel untuk masuk ke dalam komisi, mengirimkan data kejanggalan kebijakan di lapangan, atau ikut berdebat secara konstruktif dalam sesi <em>Shadow Hearing</em> publik kami. Kunjungi halaman <a href="./gabung.html">Gabung</a> untuk detail lebih lanjut.
          </div>
        </div>
      </div>
    </div>
    
    <div class="reveal" style="margin-top: 80px; text-align: center; background: var(--bg-soft); padding: 48px; border-radius: 20px; border: 1px solid var(--border);">
      <h3 style="font-family: 'Outfit'; font-size: 1.6rem; margin-bottom: 16px;">Masih ada pertanyaan?</h3>
      <p class="editorial-text" style="margin-bottom: 24px;">Hubungi tim kesekretariatan kami.</p>
      <a href="mailto:panitia@parlemenbayangan.id" class="btn-primary" style="width: auto;">panitia@parlemenbayangan.id</a>
    </div>
  </section>
"""

# =======================
# GABUNG PAGE
# =======================
gabung_content = """
  <section class="page-hero">
    <div class="section-label reveal">Registrasi & Rekomendasi</div>
    <h1 class="reveal">Ambil <span class="highlight">Peranmu.</span></h1>
    <p class="reveal">Parlemen ini adalah milik publik. Kami mengundang Anda untuk mengusulkan tokoh terbaik bangsa atau mendaftarkan diri untuk mengisi kursi komisi.</p>
  </section>
  
  <section class="content-section">
    <div class="grid-2">
      <!-- Path 1 -->
      <div class="light-card reveal" style="display: flex; flex-direction: column; height: 100%; border-top: 6px solid var(--red);">
        <div style="font-family: 'Bebas Neue'; font-size: 4rem; color: var(--red); line-height: 1; opacity: 0.3; margin-bottom: 16px;">01</div>
        <h3 style="font-family: 'Outfit'; font-size: 2rem; margin-bottom: 24px; color: var(--text-primary);">Rekomendasikan Tokoh</h3>
        <div class="editorial-text" style="flex: 1;">
          <p>Anda mengenal seorang akademisi kritis, aktivis tangguh, atau profesional berintegritas yang layak menjadi penjaga nalar publik? Usulkan mereka!</p>
          <ul style="padding-left: 20px; margin-bottom: 32px;">
            <li style="margin-bottom: 8px;">Tidak harus kenal secara personal dengan kandidat.</li>
            <li style="margin-bottom: 8px;">Kandidat yang diusulkan akan kami hubungi untuk kesediaannya.</li>
            <li style="margin-bottom: 8px;">Rekomendasi bersifat rahasia (identitas Anda tidak dipublikasikan).</li>
          </ul>
        </div>
        <a href="https://forms.gle/4gugKXK7ShDKzQqE7" target="_blank" class="btn-primary" style="width: 100%; justify-content: center; margin-top: auto;">Isi Form Rekomendasi →</a>
      </div>
      
      <!-- Path 2 -->
      <div class="light-card reveal" style="display: flex; flex-direction: column; height: 100%; border-top: 6px solid var(--text-primary);">
        <div style="font-family: 'Bebas Neue'; font-size: 4rem; color: var(--text-primary); line-height: 1; opacity: 0.15; margin-bottom: 16px;">02</div>
        <h3 style="font-family: 'Outfit'; font-size: 2rem; margin-bottom: 24px; color: var(--text-primary);">Jadilah Bagian dari Kami</h3>
        <div class="editorial-text" style="flex: 1;">
          <p>Jika Anda merasa terpanggil, memiliki rekam jejak advokasi/akademik yang jelas, dan siap mendedikasikan waktu secara sukarela, mari bergabung.</p>
          <ul style="padding-left: 20px; margin-bottom: 32px;">
            <li style="margin-bottom: 8px;">Siapkan CV / Tautan LinkedIn Anda.</li>
            <li style="margin-bottom: 8px;">Sertakan 1-2 paragraf mengenai isu spesifik yang ingin Anda kawal.</li>
            <li style="margin-bottom: 8px;">Bebas dari afiliasi partai politik.</li>
          </ul>
        </div>
        <a href="mailto:panitia@parlemenbayangan.id?subject=Pendaftaran%20Anggota%20Komisi%20Parlemen%20Bayangan" class="btn-outline" style="width: 100%; justify-content: center; margin-top: auto;">Kirim Profil via Email 📧</a>
      </div>
    </div>
  </section>
  
  <div class="divider"></div>
  
  <section class="content-section">
    <h2 class="reveal text-center" style="text-align: center;">Langkah Selanjutnya</h2>
    <div class="timeline reveal">
      <div class="timeline-item">
        <div class="timeline-content">
          <h3>Pengumpulan Data</h3>
          <p>Sekretariat menghimpun semua rekomendasi dan pendaftaran mandiri. Kandidat hasil rekomendasi akan dihubungi untuk konfirmasi kesediaan.</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-content">
          <h3>Penelaahan Panel</h3>
          <p>Daftar kandidat diserahkan kepada Panel Seleksi Independen (Zainal Arifin Mochtar, Bivitri Susanti, Erry Riyana) untuk audit rekam jejak.</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-content">
          <h3>Pengumuman Formasi Final</h3>
          <p>Kandidat yang lolos seleksi panel akan dihubungi dan formasi akhir komisi akan diumumkan ke publik melalui media massa dan website ini.</p>
        </div>
      </div>
    </div>
  </section>
"""

# Write files
write_file('manifesto.html', build_page('Manifesto', manifesto_content))
write_file('kriteria.html', build_page('Kriteria', kriteria_content))
write_file('komisi.html', build_page('Komisi Parlemen', komisi_content))
write_file('panel.html', build_page('Panel Seleksi', panel_content))
write_file('faq.html', build_page('FAQ', faq_content))
write_file('gabung.html', build_page('Gabung', gabung_content))

# Update index.html
html_content = html_content.replace('href="#manifesto"', 'href="./manifesto.html"')
html_content = html_content.replace('href="#kriteria"', 'href="./kriteria.html"')
html_content = html_content.replace('href="#komisi"', 'href="./komisi.html"')
html_content = html_content.replace('href="#panel"', 'href="./panel.html"')
html_content = html_content.replace('href="#faq"', 'href="./faq.html"')
html_content = html_content.replace('href="#gabung"', 'href="./gabung.html"')

# Add "Selengkapnya" links at the end of each section in index.html
html_content = html_content.replace(
    '</p>\n    </div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- CTA / KRITERIA -->',
    '</p>\n      <div style="margin-top: 32px;"><a href="./manifesto.html" style="color: var(--red); font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Baca Selengkapnya &rarr;</a></div>\n    </div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- CTA / KRITERIA -->'
)

html_content = html_content.replace(
    '</div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- REDESIGNED KOMISI (FORMASI) SECTION -->',
    '</div>\n    <div style="margin-top: 48px; text-align: center;"><a href="./kriteria.html" style="color: var(--red); font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Lihat Detail Kriteria &rarr;</a></div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- REDESIGNED KOMISI (FORMASI) SECTION -->'
)

html_content = html_content.replace(
    '</div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- PANEL SELEKSI -->',
    '</div>\n    <div style="margin-top: 48px; text-align: center;"><a href="./komisi.html" style="color: var(--red); font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Lihat Detail Komisi &rarr;</a></div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- PANEL SELEKSI -->'
)

html_content = html_content.replace(
    '</div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- FAQ -->',
    '</div>\n    <div style="margin-top: 48px; text-align: center;"><a href="./panel.html" style="color: var(--red); font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Lihat Profil Panel &rarr;</a></div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- FAQ -->'
)

html_content = html_content.replace(
    '</div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- REGISTRATION -->',
    '</div>\n    <div style="margin-top: 48px; text-align: center;"><a href="./faq.html" style="color: var(--red); font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Lihat Semua Pertanyaan &rarr;</a></div>\n  </section>\n\n  <div class="divider"></div>\n\n  <!-- REGISTRATION -->'
)

write_file('index.html', html_content)
print("All files generated and index.html updated successfully.")
