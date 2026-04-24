(function () {
  'use strict';

  var MAX_AI_TURNS = 3;
  var aiTurns = 0;
  var history = [];

  function getMode() {
    var p = window.location.pathname;
    return (p.startsWith('/works') || p === '/') ? 'works' : 'aythnyk';
  }

  var CONFIG = {
    works: {
      accent:      '#c49a40',
      title:       'Etherflame Works',
      subtitle:    'How can we help you?',
      placeholder: 'Tell us more...',
      send:        'Send',
      buttons: [
        { label: 'Explore Design services',  msg: 'I want to learn about EF Design services and pricing.' },
        { label: 'Explore Media services',   msg: 'I want to learn about EF Media services.' },
        { label: 'Explore Studio services',  msg: 'I want to learn about EF Studio creative direction.' },
        { label: 'Get a project estimate',   msg: 'I have a project and need a cost estimate.' },
      ],
      farewell: 'Ready to start? <a href="/works/" style="color:#c49a40">Visit Etherflame Works →</a>',
    },
    aythnyk: {
      accent:      '#e0163a',
      title:       'Aythnyk',
      subtitle:    '¿Qué buscas hoy?',
      placeholder: 'Escribe algo...',
      send:        'Enviar',
      buttons: [
        { label: 'Quiero leer poemas',     msg: 'Recuéndame un poema según cómo me siento.' },
        { label: 'Quiero escuchar música',   msg: '¿Qué canción de Aythnyk me recomendarías?' },
        { label: 'Explorar colecciones',   msg: 'Cuéntame sobre las colecciones de Aythnyk.' },
        { label: 'Descargar un poema PDF', msg: '¿Cómo puedo descargar un poema en PDF?' },
      ],
      farewell: 'Sigue explorando: <a href="/aythnyk/" style="color:#e0163a">Aythnyk →</a>',
    },
  };

  function getCookie(name) {
    var m = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return m ? m[2] : '';
  }

  function init() {
    var mode = getMode();
    var cfg  = CONFIG[mode];

    /* ── CSS ── */
    var s = document.createElement('style');
    s.textContent = (
      '#ef-btn{' +
        'position:fixed;bottom:1.75rem;right:1.75rem;z-index:9999;' +
        'width:50px;height:50px;border-radius:50%;' +
        'background:' + cfg.accent + ';border:none;cursor:pointer;' +
        'display:flex;align-items:center;justify-content:center;' +
        'box-shadow:0 4px 14px rgba(0,0,0,.5);transition:transform .2s;' +
      '}' +
      '#ef-btn:hover{transform:scale(1.1);}' +
      '#ef-btn svg{width:22px;height:22px;fill:#0a0a0a;}' +

      '#ef-box{' +
        'display:none;flex-direction:column;' +
        'position:fixed;bottom:5rem;right:1.75rem;z-index:9999;' +
        'width:320px;max-height:480px;' +
        'background:#111;border:1px solid #222;border-radius:8px;' +
        'overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,.6);' +
      '}' +
      '#ef-box.open{display:flex;}' +

      '.ef-head{' +
        'padding:.75rem 1rem;background:#0a0a0a;' +
        'border-bottom:1px solid #1e1e1e;position:relative;' +
      '}' +
      '.ef-head h4{' +
        'font-family:"Cormorant Garamond",serif;' +
        'font-size:.95rem;color:' + cfg.accent + ';margin:0 0 .1rem;' +
      '}' +
      '.ef-head p{' +
        'font-family:"DM Sans",sans-serif;font-size:.6rem;' +
        'letter-spacing:3px;text-transform:uppercase;color:#555;margin:0;' +
      '}' +
      '#ef-close{' +
        'position:absolute;top:.6rem;right:.8rem;' +
        'background:none;border:none;color:#444;' +
        'font-size:1.1rem;cursor:pointer;line-height:1;' +
      '}' +
      '#ef-close:hover{color:#aaa;}' +

      '#ef-msgs{' +
        'flex:1;overflow-y:auto;padding:.75rem;' +
        'display:flex;flex-direction:column;gap:.5rem;' +
        'scrollbar-width:thin;scrollbar-color:#222 #111;' +
      '}' +

      '.ef-m{' +
        'font-family:"DM Sans",sans-serif;font-size:.8rem;' +
        'line-height:1.5;padding:.55rem .8rem;border-radius:5px;' +
        'max-width:92%;' +
      '}' +
      '.ef-m.user{align-self:flex-end;background:#1e1e1e;color:#eee;}' +
      '.ef-m.bot{' +
        'align-self:flex-start;background:#161616;color:#ccc;' +
        'border-left:2px solid ' + cfg.accent + ';' +
      '}' +
      '.ef-m.bot a{color:' + cfg.accent + ';}' +

      '#ef-btns{' +
        'display:flex;flex-direction:column;gap:.4rem;' +
        'padding:.5rem .75rem .75rem;' +
      '}' +
      '.ef-quick{' +
        'padding:.5rem .9rem;background:#1a1a1a;' +
        'border:1px solid #2a2a2a;border-radius:4px;' +
        'font-family:"DM Sans",sans-serif;font-size:.75rem;' +
        'color:#ccc;cursor:pointer;text-align:left;' +
        'transition:border-color .2s,color .2s;' +
      '}' +
      '.ef-quick:hover{border-color:' + cfg.accent + ';color:' + cfg.accent + ';}' +

      '#ef-form{' +
        'display:none;padding:.6rem;border-top:1px solid #1e1e1e;' +
        'gap:.4rem;background:#0a0a0a;' +
      '}' +
      '#ef-form.visible{display:flex;}' +
      '#ef-input{' +
        'flex:1;padding:.5rem .7rem;background:#1a1a1a;' +
        'border:1px solid #2a2a2a;color:#f0f0f0;border-radius:4px;' +
        'font-family:"DM Sans",sans-serif;font-size:.8rem;outline:none;' +
      '}' +
      '#ef-input:focus{border-color:' + cfg.accent + ';}' +
      '#ef-send{' +
        'padding:.5rem .85rem;background:' + cfg.accent + ';' +
        'color:#0a0a0a;border:none;border-radius:4px;' +
        'font-family:"DM Sans",sans-serif;font-size:.68rem;' +
        'letter-spacing:2px;text-transform:uppercase;' +
        'font-weight:700;cursor:pointer;' +
      '}' +
      '#ef-send:hover{opacity:.85;}' +

      '.ef-limit{' +
        'font-family:"DM Sans",sans-serif;font-size:.72rem;' +
        'color:#444;text-align:center;padding:.5rem;' +
      '}' +

      '@media(max-width:420px){' +
        '#ef-box{width:calc(100vw - 2rem);right:1rem;}' +
      '}'
    );
    document.head.appendChild(s);

    /* ── FAB button ── */
    var btn = document.createElement('button');
    btn.id = 'ef-btn';
    btn.setAttribute('aria-label', 'Chat');
    btn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>';
    document.body.appendChild(btn);

    /* ── Panel ── */
    var box = document.createElement('div');
    box.id = 'ef-box';
    var quickBtns = cfg.buttons.map(function (b) {
      return '<button class="ef-quick" data-msg="' + b.msg + '">' + b.label + '</button>';
    }).join('');
    box.innerHTML = (
      '<div class="ef-head">' +
        '<h4>' + cfg.title + '</h4>' +
        '<p>' + cfg.subtitle + '</p>' +
        '<button id="ef-close">&times;</button>' +
      '</div>' +
      '<div id="ef-msgs"></div>' +
      '<div id="ef-btns">' + quickBtns + '</div>' +
      '<form id="ef-form">' +
        '<input id="ef-input" type="text" autocomplete="off" maxlength="300" placeholder="' + cfg.placeholder + '">' +
        '<button id="ef-send" type="submit">' + cfg.send + '</button>' +
      '</form>'
    );
    document.body.appendChild(box);

    /* ── Wire events ── */
    btn.addEventListener('click', function () { box.classList.toggle('open'); });
    document.getElementById('ef-close').addEventListener('click', function () {
      box.classList.remove('open');
    });

    var btnsDiv  = document.getElementById('ef-btns');
    var formEl   = document.getElementById('ef-form');
    var inputEl  = document.getElementById('ef-input');

    btnsDiv.addEventListener('click', function (e) {
      var qb = e.target.closest('.ef-quick');
      if (!qb) return;
      btnsDiv.style.display = 'none';
      formEl.classList.add('visible');
      sendMessage(qb.getAttribute('data-msg'));
    });

    formEl.addEventListener('submit', function (e) {
      e.preventDefault();
      var txt = inputEl.value.trim();
      if (!txt) return;
      inputEl.value = '';
      sendMessage(txt);
    });
  }

  function addMsg(text, sender) {
    var wrap = document.getElementById('ef-msgs');
    var div  = document.createElement('div');
    div.className = 'ef-m ' + sender;
    div.innerHTML = text;
    wrap.appendChild(div);
    wrap.scrollTop = wrap.scrollHeight;
    return div;
  }

  function lockForm() {
    var formEl = document.getElementById('ef-form');
    if (formEl) formEl.style.display = 'none';
    var msgs = document.getElementById('ef-msgs');
    if (msgs) {
      var lim = document.createElement('p');
      lim.className = 'ef-limit';
      lim.textContent = '— fin de la conversación —';
      msgs.appendChild(lim);
    }
  }

  function sendMessage(text) {
    addMsg(text, 'user');
    history.push({ role: 'user', content: text });

    if (aiTurns >= MAX_AI_TURNS) {
      var mode = getMode();
      addMsg(CONFIG[mode].farewell, 'bot');
      lockForm();
      return;
    }

    var typing = addMsg('…', 'bot');

    fetch('/api/chat/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify({
        message: text,
        history: history.slice(-6),
        mode: getMode(),
      }),
    })
    .then(function (res) { return res.json(); })
    .then(function (data) {
      typing.remove();
      if (data.response) {
        aiTurns++;
        addMsg(data.response, 'bot');
        history.push({ role: 'assistant', content: data.response });

        if (aiTurns >= MAX_AI_TURNS) {
          var mode = getMode();
          addMsg(CONFIG[mode].farewell, 'bot');
          lockForm();
        }
      } else {
        addMsg('Error. Intenta de nuevo.', 'bot');
      }
    })
    .catch(function () {
      typing.remove();
      addMsg('Error. Intenta de nuevo.', 'bot');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
