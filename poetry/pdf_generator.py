import os
from django.conf import settings
from weasyprint import HTML


def generate_poem_pdf(poem):
    # Prefer STATIC_ROOT (after collectstatic); fall back to source static dir
    static_base = settings.STATIC_ROOT
    logo_path = os.path.join(static_base, 'images', 'works', 'aythnyk', 'logoAyth_transp.png')
    if not os.path.exists(logo_path):
        static_base = os.path.join(settings.BASE_DIR, 'static')
        logo_path = os.path.join(static_base, 'images', 'works', 'aythnyk', 'logoAyth_transp.png')

    logo_url = f'file://{logo_path}'
    collection_name = str(poem.collection) if poem.collection else 'Aythnyk'
    body_html = poem.body.replace(chr(10), '<br>')

    title_parts = poem.title.split()
    if len(title_parts) >= 2:
        title_html = f'<span style="color:#c8102e">{title_parts[0]}</span> <span style="color:#c49a40">{" ".join(title_parts[1:])}</span>'
    else:
        title_html = f'<span style="color:#c8102e">{poem.title}</span>'

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400&display=swap');

      @page {{
        size: A4;
        margin-top: 32mm;
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
          padding: 6mm 15mm;
          vertical-align: middle;
        }}

        @top-right {{
          content: "ETERFLAME · POESÍA";
          font-family: 'DM Sans', sans-serif;
          font-size: 6pt;
          letter-spacing: 2pt;
          color: rgba(196,154,64,0.4);
          text-transform: uppercase;
          background: #1a1a1a;
          padding: 6mm 15mm 6mm 0;
          vertical-align: middle;
          white-space: nowrap;
        }}

        @bottom-center {{
          content: "© 2025 Aythnyk    ETER FLAME    eterflame.com";
          font-family: 'DM Sans', sans-serif;
          font-size: 6pt;
          letter-spacing: 1.5pt;
          color: #bbb;
          text-transform: uppercase;
          border-top: 0.3mm solid #eee;
          padding-top: 3mm;
          width: 100%;
          text-align: center;
        }}
      }}

      @page :first {{
        margin-top: 0;
      }}

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}

      body {{
        width: 210mm;
        min-height: 297mm;
        background: #ffffff;
        position: relative;
        font-family: 'Cormorant Garamond', Georgia, serif;
      }}

      .watermark {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -46%);
        width: 160mm;
        height: 160mm;
        opacity: 0.12;
        object-fit: contain;
        z-index: 0;
        mix-blend-mode: multiply;
      }}

      .inner {{
        padding: 10mm 20mm 25mm;
        position: relative;
        z-index: 1;
      }}

      .left-bar {{
        position: absolute;
        left: 0; top: 0; bottom: 0;
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
        font-size: 26pt;
        font-weight: bold;
        text-align: center;
        letter-spacing: 5pt;
        text-transform: uppercase;
        line-height: 1.1;
        margin-bottom: 2mm;
      }}

      .author {{
        font-family: 'DM Sans', sans-serif;
        font-size: 7pt;
        letter-spacing: 3pt;
        color: #c49a40;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 6mm;
      }}

      .rule-gold {{
        width: 15mm;
        height: 0.3mm;
        background: #c49a40;
        margin: 0 auto 2mm;
      }}

      .rule-red {{
        width: 8mm;
        height: 0.5mm;
        background: #c8102e;
        margin: 0 auto 7mm;
        opacity: 0.7;
      }}

      .body {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 11pt;
        color: #1e1e1e;
        line-height: 2.2;
        text-align: center;
        padding-bottom: 20mm;
      }}

      .stanza {{ height: 5mm; }}

      .bottom-accent {{
        margin-top: 10mm;
        display: flex;
        height: 0.3mm;
      }}

      .bottom-gold {{ flex: 1; background: #c49a40; opacity: 0.35; }}
      .bottom-red  {{ flex: 1; background: #c8102e; opacity: 0.35; }}
    </style>
    </head>
    <body>
      <img class="watermark" src="{logo_url}" alt=""/>

      <!-- Page 1 only: manual header in normal flow (page 1 has margin-top: 0) -->
      <div style="background:#1a1a1a;padding:6mm 15mm;display:flex;justify-content:space-between;align-items:center;width:100%;">
        <span style="font-family:'Cormorant Garamond',serif;font-size:10pt;letter-spacing:5pt;color:#c49a40;text-transform:uppercase;white-space:nowrap;">Aythnyk</span>
        <span style="font-family:'DM Sans',sans-serif;font-size:6pt;letter-spacing:2pt;color:rgba(196,154,64,0.4);text-transform:uppercase;white-space:nowrap;">ETERFLAME · POESÍA</span>
      </div>
      <div style="height:2mm;background:#c8102e;"></div>

      <div class="inner">
        <div class="left-bar"></div>
        <div class="collection">Colección · {collection_name}</div>
        <h1 class="title">{title_html}</h1>
        <p class="author">Cynthia Pinedo</p>
        <div class="rule-gold"></div>
        <div class="rule-red"></div>
        <div class="body">{body_html}</div>
        <div class="bottom-accent">
          <div class="bottom-gold"></div>
          <div class="bottom-red"></div>
        </div>
      </div>
    </body>
    </html>
    """

    return HTML(string=html_content, base_url=static_base).write_pdf()
