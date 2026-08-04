# Update Website Content Based on Provided PDF

This document outlines the phased implementation plan for updating the content of the Parlemen Bayangan website based on the provided Indonesian document. The website appears to have both a comprehensive single-page structure (`index.html`) and separate pages for each section (`manifesto.html`, `kriteria.html`, `komisi.html`, `panel.html`, `faq.html`, `gabung.html`). We will ensure consistency across all relevant files.

## User Review Required

> [!IMPORTANT]
> The plan below will update both `index.html` (the long scrolling landing page) AND all individual pages (`manifesto.html`, `faq.html`, etc.) to ensure the content is complementary and consistent. We will also preserve the existing form link inside `index.html` for the recommendation button. Please review the phased approach below and click **Proceed** if you approve.

## Proposed Changes

We will execute the updates in phases to ensure accuracy and structural integrity.

---

### Phase 1: Update Manifesto & Introduction
Update the hero section and manifesto text.
- **Content**: "Sudah Saatnya Setiap Gagasan Diuji, Bukan Sekadar Dipercaya." and the 3 paragraphs explaining the role of Parlemen Bayangan as a civil society coalition.
#### [MODIFY] index.html
#### [MODIFY] manifesto.html

---

### Phase 2: Update Kriteria (Criteria) Section
Update the member criteria section.
- **Content**: "Kami Mencari Mereka Yang Tidak Mudah Percaya." followed by the 8 criteria (Kritis, Analitis, Substantif, Berbasis Bukti, Mampu Berargumentasi, Memiliki Perspektif Tanding, Independen, Terbuka untuk Diperdebatkan).
#### [MODIFY] index.html
#### [MODIFY] kriteria.html

---

### Phase 3: Update Komisi (Commissions) List
Update the list of commissions/portfolios.
- **Content**: "Sejajar, Kritis, Berbasis Pengawasan." and the list of 14 Komisi + 15 Juru Bicara Parlemen Bayangan.
#### [MODIFY] index.html
#### [MODIFY] komisi.html

---

### Phase 4: Update Panel Selection & FAQ
Update the panel description and the Frequently Asked Questions.
- **Content Panel**: "Mereka Yang Menilai" and the explanation of the independent panel.
- **Content FAQ**: 7 questions and answers regarding what it is, why it's needed, affiliation, how it works, who is behind it, financial payment, and public involvement.
#### [MODIFY] index.html
#### [MODIFY] panel.html
#### [MODIFY] faq.html

---

### Phase 5: Update Call to Action (Gabung/Join)
Update the sections for recommending candidates and joining.
- **Content**: "Anda Punya Nama Kandidat Atau Ingin Terlibat Langsung?" including the recommendation form and contact email (`PANITIA@PARLEMENBAYANGAN.ID`).
#### [MODIFY] index.html
#### [MODIFY] gabung.html

## Verification Plan

### Manual Verification
- I will open each modified HTML file and verify that the text matches the provided PDF document.
- I will check the visual rendering (using `view_file` to ensure HTML tags are properly closed and styling classes are intact) to ensure the layout wasn't broken by the text replacement.
- I will generate a walkthrough artifact summarizing the changes once completed.
