"""
Unified PDF generator for Aythnyk poems.

Supports 3 modes:
- 'paid'        → Sold via Gumroad ($2.99) — no badges, clean look
- 'admin'       → Internal review by Cynthia — "DRAFT · REVISION COPY" badge
- 'lead_magnet' → Free in exchange for email — "FREE COPY" badge + final CTA page

Visual identity (header, watermark, footer, typography) is IDENTICAL across modes.
Only badges and the optional CTA page differ.
"""

import os
from django.conf import settings
from weasyprint import HTML


# ─────────────────────────────────────────────────────────────
# Mode-specific configuration
# ─────────────────────────────────────────────────────────────

MODE_CONFIG = {
    'paid': {
        'badge_text': None,
        'badge_color': None,
        'show_cta_page': False,
    },
    'admin': {
        'badge_text': 'INTERNAL COPY',
        'badge_color': '#8a6a2f',  # gold-brown, sober
        'show_cta_page': False,
    },
    'lead_magnet': {
        'badge_text': 'FREE COPY',
        'badge_color': '#c8102e',  # crimson, attention-getting
        'show_cta_page': True,
    },
}

CTA_TEXT = {
    'es': {
        'eyebrow': 'AYTHNYK · ETERFLAME',
        'heading_red': '¿TE CONMOVIÓ',
        'heading_gold': 'ESTE POEMA?',
        'body': (
            'Descubre más poemas, canciones y prints en la tienda Aythnyk. '
            'Cada pieza es su propio mundo.'
        ),
        'button': 'EXPLORAR LA TIENDA →',
        'link': 'AYTHNYK · ETERFLAME',
        'footer_note': (
            'Esta es una muestra gratuita del catálogo Aythnyk. '
            'Los PDF de poemas individuales normalmente cuestan $2.99.'
        ),
    },
    'en': {
        'eyebrow': 'AYTHNYK · ETERFLAME',
        'heading_red': 'DID THIS POEM',
        'heading_gold': 'MOVE YOU?',
        'body': (
            'Discover more poems, songs and prints in the Aythnyk shop. '
            'Each piece is its own world.'
        ),
        'button': 'EXPLORE THE SHOP →',
        'link': 'AYTHNYK · ETERFLAME',
        'footer_note': (
            'This is a free sampler from the Aythnyk catalog. '
            'Individual poem PDFs normally cost $2.99.'
        ),
    },
}

SHOP_URL = 'https://eterflame-web-ab680e12c17d.herokuapp.com/aythnyk/shop/'
AYTHNYK_HOME_URL = 'https://eterflame-web-ab680e12c17d.herokuapp.com/aythnyk/'


def generate_poem_pdf(poem, lang='es', mode='paid'):
    """
    Generate a PDF of a poem in one of three modes.

    Args:
        poem: Poem instance
        lang: 'es' or 'en' (defaults to 'es')
        mode: 'paid' | 'admin' | 'lead_magnet' (defaults to 'paid')

    Returns:
        bytes: PDF content
    """
    if mode not in MODE_CONFIG:
        raise ValueError(
            f"Invalid mode '{mode}'. Must be one of: {list(MODE_CONFIG.keys())}"
        )

    config = MODE_CONFIG[mode]

    # Footer prefix: admin mode adds 'INTERNAL COPY · ' before the footer text.
    # Always defined (empty string for non-admin modes) to avoid NameError.
    footer_badge_prefix = ''
    if mode == 'admin' and config['badge_text']:
        footer_badge_prefix = f"{config['badge_text']}  ·  "


    # ─── Logo path resolution (same strategy as legacy) ───────
    static_base = settings.STATIC_ROOT
    logo_path = os.path.join(
        static_base, "images", "aythnyk", "logoAyth_transp.png",
    )
    if not os.path.exists(logo_path):
        static_base = os.path.join(settings.BASE_DIR, "static")
        logo_path = os.path.join(
            static_base, "images", "aythnyk", "logoAyth_transp.png",
        )
    # Fallback to .webp if .png is not available
    if not os.path.exists(logo_path):
        logo_path = logo_path.replace(".png", ".webp")
    logo_url = f"file://{logo_path}"

    # ─── Language-aware content ───────────────────────────────
    if lang == 'en':
        title_text = poem.title_en or poem.title_es
        body_text = poem.body_en or poem.body_es
        collection_label = "Collection"
    else:
        title_text = poem.title_es or poem.title_en
        body_text = poem.body_es or poem.body_en
        collection_label = "Colección"

    collection_name = str(poem.collection) if poem.collection else "Aythnyk"

    # ─── Title split: first word crimson, rest gold ───────────
    title_parts = title_text.split()
    if len(title_parts) >= 2:
        title_html = (
            f'<span style="color:#c8102e">{title_parts[0]}</span> '
            f'<span style="color:#c49a40">{" ".join(title_parts[1:])}</span>'
        )
    else:
        title_html = f'<span style="color:#c8102e">{title_text}</span>'

    # ─── Body: stanzas as paragraphs (better page flow) ───────
    stanzas = [s.strip() for s in body_text.split("\n\n") if s.strip()]
    body_html = "".join(
        f'<p class="poem-stanza">{stanza.replace(chr(10), "<br>")}</p>'
        for stanza in stanzas
    )

    # ─── Badge HTML (only for admin / lead_magnet) ────────────
    badge_html = ''
    if config['badge_text']:
        badge_html = f'''
        <div class="mode-badge" style="
            position: absolute;
            top: -22mm;
            right: 0;
            background: {config['badge_color']};
            color: #ffffff;
            font-family: 'DM Sans', sans-serif;
            font-size: 5.5pt;
            letter-spacing: 2pt;
            padding: 2mm 6mm;
            text-transform: uppercase;
            z-index: 10;
        ">{config['badge_text']}</div>
        '''

    # ─── CTA page HTML (only for lead_magnet) ─────────────────
    cta_html = ''
    if config['show_cta_page']:
        t = CTA_TEXT[lang if lang in CTA_TEXT else 'es']
        cta_html = f'''
        <div class="cta-page">
          <div class="cta-content">
            <p class="cta-eyebrow">{t['eyebrow']}</p>
            <h2 class="cta-heading">
              <span style="color:#c8102e">{t['heading_red']}</span>
              <span style="color:#c49a40">{t['heading_gold']}</span>
            </h2>
            <p class="cta-body">{t['body']}</p>
            <a href="{SHOP_URL}" class="cta-button">{t['button']}</a>
            <a href="{AYTHNYK_HOME_URL}" class="cta-link">{t['link']}</a>
            <div class="cta-divider"></div>
            <p class="cta-footer-note">{t['footer_note']}</p>
          </div>
        </div>
        '''

    # ─── Full HTML document ───────────────────────────────────
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Sans:wght@300;400&display=swap');

        @page {{
          size: A4;
          margin-top: 35mm;
          margin-bottom: 20mm;
          margin-left: 0;
          margin-right: 0;

          @top-left {{
            content: "AYTHNYK";
            font-family: 'Cormorant Garamond', serif;
            font-size: 11pt;
            letter-spacing: 6pt;
            color: #c49a40;
            text-transform: uppercase;
            background: #1a1a1a;
            width: 100%;
            padding: 7mm 15mm;
            vertical-align: middle;
            border-bottom: 0.8mm solid #c49a40;
          }}

          @top-right {{
            content: "ETERFLAME · POESÍA";
            font-family: 'DM Sans', sans-serif;
            font-size: 6pt;
            letter-spacing: 2pt;
            color: rgba(196,154,64,0.6);
            text-transform: uppercase;
            background: #1a1a1a;
            padding: 7mm 15mm 7mm 0;
            vertical-align: middle;
            white-space: nowrap;
            border-bottom: 0.8mm solid #c49a40;
          }}

          @bottom-center {{
            content: "{footer_badge_prefix}© 2026 Aythnyk  ·  eterflame.com  ·  " counter(page) " / " counter(pages);
            font-family: 'DM Sans', sans-serif;
            font-size: 6pt;
            letter-spacing: 1.2pt;
            color: #bbb;
            text-transform: uppercase;
            border-top: 0.3mm solid #eee;
            padding-top: 3mm;
            width: 100%;
            text-align: center;
            white-space: nowrap;
          }}
        }}

        @page:first {{
          margin-top: 25mm;
        }}

        * {{
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }}

        body {{
          width: 210mm;
          min-height: 297mm;
          background: #ffffff;
          position: relative;
          font-family: 'Cormorant Garamond', Georgia, serif;
        }}

        .watermark {{
          position: fixed;
          top: 52%;
          left: 50%;
          transform: translate(-50%, -50%) scale(1.08);
          width: 185mm;
          height: 185mm;
          opacity: 0.045;
          object-fit: contain;
          z-index: 0;
          mix-blend-mode: normal;
          filter: blur(0.2px);
        }}

        .inner {{
          padding: 10mm 20mm 25mm;
          position: relative;
          z-index: 1;
        }}

        .left-bar {{
          position: absolute;
          left: 0;
          top: 0;
          bottom: 0;
          width: 1.5mm;
          background: #c8102e;
          opacity: 0.5;
        }}

        .collection {{
          font-family: 'DM Sans', sans-serif;
          font-size: 6pt;
          letter-spacing: 4pt;
          text-transform: uppercase;
          color: #c8102e;
          text-align: center;
          margin-bottom: 6mm;
          opacity: 0.8;
        }}

        .title {{
          font-family: 'Cormorant Garamond', serif;
          font-size: 31pt;
          font-weight: 600;
          text-align: center;
          letter-spacing: 3pt;
          text-transform: uppercase;
          line-height: 1.05;
          margin-bottom: 2mm;
        }}

        .author {{
          font-family: 'DM Sans', sans-serif;
          font-size: 7pt;
          letter-spacing: 3pt;
          color: #8a6a2f;
          text-align: center;
          text-transform: uppercase;
          margin-bottom: 6mm;
        }}

        .rule-gold {{
          width: 18mm;
          height: 0.35mm;
          background: #9c762c;
          margin: 0 auto 8mm;
        }}

        .body {{
          font-family: 'Cormorant Garamond', Georgia, serif;
          font-size: 13pt;
          color: #111111;
          line-height: 1.68;
          letter-spacing: 0.2px;
          text-align: left;
          max-width: 118mm;
          margin: 0 auto;
          padding-top: 0;
          padding-bottom: 20mm;
          orphans: 4;
          widows: 4;
        }}

        .poem-stanza {{
          margin: 0 0 4mm;
          break-inside: avoid;
          page-break-inside: avoid;
        }}

        .bottom-accent {{
          margin-top: 10mm;
          display: flex;
          height: 0.3mm;
        }}

        .bottom-gold {{
          flex: 1;
          background: #c49a40;
          opacity: 0.35;
        }}

        .bottom-red {{
          flex: 1;
          background: #c8102e;
          opacity: 0.35;
        }}

        /* ─── CTA Page (lead_magnet mode only) ─── */
        .cta-page {{
          page-break-before: always;
          position: relative;
          width: 100%;
          min-height: 230mm;
          padding: 20mm 30mm;
          text-align: center;
        }}

        .cta-watermark {{
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%) scale(1.1);
          width: 180mm;
          opacity: 0.04;
          z-index: 0;
        }}

        .cta-content {{
          position: relative;
          z-index: 1;
          padding-top: 30mm;
        }}

        .cta-eyebrow {{
          font-family: 'DM Sans', sans-serif;
          font-size: 7pt;
          letter-spacing: 4pt;
          color: #c49a40;
          text-transform: uppercase;
          margin-bottom: 12mm;
        }}

        .cta-heading {{
          font-family: 'Cormorant Garamond', serif;
          font-size: 28pt;
          font-weight: 600;
          letter-spacing: 2pt;
          text-transform: uppercase;
          line-height: 1.15;
          margin-bottom: 8mm;
        }}

        .cta-body {{
          font-family: 'Cormorant Garamond', serif;
          font-size: 13pt;
          color: #333;
          line-height: 1.7;
          max-width: 110mm;
          margin: 0 auto 15mm;
          font-style: italic;
        }}

        .cta-button {{
          display: inline-block;
          background: #c8102e;
          color: #ffffff;
          font-family: 'DM Sans', sans-serif;
          font-size: 9pt;
          letter-spacing: 3pt;
          padding: 5mm 14mm;
          text-decoration: none;
          text-transform: uppercase;
          margin-bottom: 6mm;
        }}

        .cta-link {{
          display: block;
          font-family: 'DM Sans', sans-serif;
          font-size: 7pt;
          letter-spacing: 3pt;
          color: #c49a40;
          text-decoration: none;
          text-transform: uppercase;
          margin-bottom: 18mm;
        }}

        .cta-divider {{
          width: 25mm;
          height: 0.35mm;
          background: #c49a40;
          margin: 0 auto 6mm;
          opacity: 0.6;
        }}

        .cta-footer-note {{
          font-family: 'Cormorant Garamond', serif;
          font-size: 9pt;
          font-style: italic;
          color: #8a6a2f;
          max-width: 90mm;
          margin: 0 auto;
          line-height: 1.5;
        }}
      </style>
    </head>

    <body>
      <img class="watermark" src="{logo_url}" alt="" />

      <div class="inner">
        {badge_html}
        <div class="left-bar"></div>

        <div class="collection">{collection_label} · {collection_name}</div>
        <h1 class="title">{title_html}</h1>
        <p class="author">Cynthia Pinedo</p>

        <div class="rule-gold"></div>

        <div class="body">
          {body_html}
        </div>

        <div class="bottom-accent">
          <div class="bottom-gold"></div>
          <div class="bottom-red"></div>
        </div>
      </div>

      {cta_html}
    </body>
    </html>
    """

    return HTML(string=html_content, base_url=static_base).write_pdf()
