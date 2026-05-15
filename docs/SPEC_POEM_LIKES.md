# Sistema de Likes Públicos para Poemas

**Estado:** Spec para implementar  
**Fecha:** 15 mayo 2026  
**Sprint:** Sprint 2 — apoyo a futura estrategia de Lead Magnets  
**Tiempo estimado:** ~45 min de implementación

---

## Contexto y motivación

Necesitamos **datos sobre qué poemas resuenan más** con visitantes para:

- Futuras decisiones de curación (qué poemas destacar)
- Lead magnets segmentados (en un futuro: "Los más leídos del año")
- Validar dirección creativa con audiencia real
- Mostrar prueba social ("47 personas dieron like a este poema")

## Diferenciación: Likes vs Favoritos

| Concepto       | Likes públicos              | Favoritos privados            |
|----------------|----------------------------|-------------------------------|
| **Audiencia**  | Cualquier visitante         | Usuario logged-in              |
| **Símbolo**    | 👍 thumbs-up                | ❤ corazón (sistema existente)         |
| **Persistencia** | localStorage del browser  | DB many-to-many user ↔ poem    |
| **Estado**     | YA en DB hoy (campo nuevo)  | YA existe                      |
| **Reversible** | No (one-way "me gustó")     | Sí (toggle favorito/no)         |
| **Counter**    | Sí, agregado global         | No (es lista personal)         |
| **Anti-spam**  | localStorage per browser    | Auth requerido por Django       |

## Decisiones tomadas

| Decisión | Valor | Razón |
|----------|-------|-------|
| Símbolo | 👍 fa-thumbs-up | Universal, casual, neutro |
| Ubicación | Solo poem_detail | Force al usuario a leer antes |
| Counter visible | Solo si `>= 2 likes` | Evita "0 likes" deprimente en cards nuevos |
| Anti-duplicación | localStorage | Honesto para sitio pequeño; no es Wall St |
| Reversible | No | "Me gustó" no se reversa después |
| Filtrar/sort en admin | Sí | Para ver top poemas en backend |

## Modelo de datos

**Archivo:** `poetry/models.py`

Añadir a la clase `Poem`:

```python
class Poem(models.Model):
    # ... campos existentes ...
    favorites = models.ManyToManyField(  # YA EXISTE
        User, related_name='favorite_poems', blank=True
    )
    
    # NUEVO:
    likes_count = models.PositiveIntegerField(
        default=0,
        help_text="Likes públicos anónimos (counter global)"
    )
```

**Migration:** `python manage.py makemigrations poetry`  
- Default=0 cubre los 93 poemas existentes
- No rompe nada

## URL routing

**Archivo:** `poetry/urls.py`

```python
path('<slug:slug>/like/', views.poem_like, name='poem_like'),
```

Endpoint final: `/aythnyk/<slug>/like/`

## Vista (POST only)

**Archivo:** `poetry/views.py`

```python
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import F
from django.shortcuts import get_object_or_404

@require_POST
def poem_like(request, slug):
    """
    Public like endpoint. Increments counter atomically.
    No login required. Anti-spam handled client-side via localStorage.
    """
    poem = get_object_or_404(Poem, slug=slug, active=True)
    poem.likes_count = F('likes_count') + 1
    poem.save(update_fields=['likes_count'])
    poem.refresh_from_db(fields=['likes_count'])
    
    return JsonResponse({
        'ok': True,
        'likes': poem.likes_count,
        'show_count': poem.likes_count >= 2,
    })
```

**Detalles técnicos:**
- `F('likes_count') + 1` es atómico (evita race conditions en DB)
- `refresh_from_db` necesario porque F-expressions retornan SQL refs, no valores
- Filtro `active=True` consistente con el resto de las queries del módulo

## Template (poem_detail.html)

Añadir cerca del título del poema, antes o después del contenido:

```html
<div class="poem-like-bar">
  <button class="poem-like-btn"
          type="button"
          data-poem-like
          data-poem-slug="{{ poem.slug }}"
          data-likes-url="{% url 'poetry:poem_like' poem.slug %}"
          aria-label="Like this poem">
    <i class="fas fa-thumbs-up" aria-hidden="true"></i>
    <span class="poem-like-count"
          data-likes-display
          {% if poem.likes_count < 2 %}hidden{% endif %}>
      {{ poem.likes_count }}
    </span>
  </button>
</div>
```

## JavaScript (poem-like.js)

**Archivo nuevo:** `static/js/poem-like.js`

```javascript
/* Public like system for poems
 * Anti-spam: localStorage per browser
 * Idempotent: once liked, button is permanently disabled in this browser
 */
(function() {
  'use strict';
  
  const buttons = document.querySelectorAll('[data-poem-like]');
  
  buttons.forEach(function(btn) {
    const slug = btn.dataset.poemSlug;
    const likedKey = 'poem_liked_' + slug;
    
    // Already liked in this browser? Disable button.
    if (localStorage.getItem(likedKey)) {
      btn.classList.add('is-liked');
      btn.disabled = true;
      btn.setAttribute('aria-label', 'You already liked this poem');
      return;
    }
    
    btn.addEventListener('click', async function(e) {
      e.preventDefault();
      
      btn.disabled = true;
      
      try {
        const response = await fetch(btn.dataset.likesUrl, {
          method: 'POST',
          headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCsrfToken(),
          },
          credentials: 'same-origin',
        });
        
        if (!response.ok) throw new Error('Network error');
        
        const data = await response.json();
        
        if (data.ok) {
          // Mark as liked in localStorage (permanent for this browser)
          localStorage.setItem(likedKey, '1');
          btn.classList.add('is-liked');
          
          // Update counter
          const display = btn.querySelector('[data-likes-display]');
          if (display) {
            display.textContent = data.likes;
            if (data.show_count) {
              display.removeAttribute('hidden');
            }
          }
          
          // Toast feedback (reuse existing toast system)
          if (window.efToast) {
            window.efToast('Thanks for the like!', 'success');
          }
        }
      } catch (err) {
        btn.disabled = false;
        if (window.efToast) {
          window.efToast('Could not register your like. Try again?', 'error');
        }
      }
    });
  });
  
  function getCsrfToken() {
    // Extract CSRF from cookie (Django sets csrftoken cookie)
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }
})();
```

**Cargar en base.html** (cerca de toast.js):
```html
<script src="{% static 'js/poem-like.js' %}?v={% now 'U' %}"></script>
```

## CSS (en base.css o poem.css)

```css
.poem-like-bar {
  display: flex;
  justify-content: center;
  margin: 2rem 0;
}

.poem-like-btn {
  background: transparent;
  border: 1px solid rgba(212, 184, 124, 0.3);
  color: var(--gold);
  padding: 0.6rem 1.2rem;
  border-radius: 999px;
  font-size: 0.95rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.poem-like-btn:hover:not(:disabled) {
  background: rgba(212, 184, 124, 0.1);
  transform: translateY(-1px);
}

.poem-like-btn.is-liked {
  background: rgba(212, 184, 124, 0.15);
  color: var(--gold-bright);
  cursor: default;
}

.poem-like-btn.is-liked i {
  /* Animation could go here — gentle pulse on success */
}

.poem-like-count {
  font-variant-numeric: tabular-nums;
  font-weight: 500;
}

.poem-like-count[hidden] {
  display: none;
}
```

## Admin (poetry/admin.py)

Añadir `likes_count` al admin:

```python
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'collection', 'likes_count', 'active', 'published')
    list_filter = ('collection', 'active')
    search_fields = ('title', 'body')
    ordering = ('-likes_count', '-published')  # Top liked primero
    readonly_fields = ('likes_count',)
    # ...
```

## Testing checklist

Después de implementar:

- [ ] Migration corre sin errores: `python manage.py migrate`
- [ ] Poemas existentes tienen `likes_count = 0` (default)
- [ ] Visitar `/aythnyk/poems/<slug>/`: el botón thumbs-up aparece
- [ ] Click thumbs-up: contador NO se ve (porque es <2)
- [ ] Click 2do thumbs-up desde otro browser/incognito: counter aparece "2"
- [ ] Refresh página: botón sigue en "liked" state (localStorage)
- [ ] Limpiar localStorage: botón vuelve a clickeable
- [ ] Admin: poemas ordenados por likes_count descendente
- [ ] Toast aparece después de like ("Thanks for the like!")

## Deploy

Heroku ya tiene release phase configurado (commit `ce54009`):
1. `git push origin main`
2. Heroku corre `python manage.py migrate --noinput` automáticamente
3. Cambios visibles inmediatamente

## Próximos pasos relacionados (no incluidos en este spec)

- **Wallpapers como lead magnet:** spec aparte (cuando produzcas el diseño en Canva)
- **PDF de top 2 poemas:** después de 3+ meses de data acumulada
- **"Most loved" sección en shop:** cuando haya >50 likes en algunos poemas
- **Sistema de comentarios públicos:** otra discusión

## Pendientes de pulir

- Cambiar `published` en `Poem` por boolean si no existe (verificar)
- ¿Like también desde `poem_list` cards? — decisión postergada
- ¿Recompensa visual cuando un poema llega a 10, 50, 100 likes? — futuro
