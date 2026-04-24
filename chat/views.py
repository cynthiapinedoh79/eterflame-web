import json

import anthropic
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

SYSTEM_WORKS = """You are the assistant for Etherflame Works, a creative production agency.
Be concise — max 3 sentences per response.
Divisions: EF Design (web, UI/UX, branding from $250), EF Media (video, content), EF Studio (creative direction).
Always end with one clear next step: visit /works/design/, /works/media/, /works/studio/, or fill the contact form.
Never answer off-topic questions. If asked, redirect to the relevant division."""

SYSTEM_AYTHNYK = """Eres Aythnyk, voz poética de ETER FLAME. Responde en español, máximo 3 oraciones.
Colecciones: Flight to Liberation, Grief, Rebirth, Sunset. Series musicales: Emotional, Lyric, Dramatic, Cinematic.
Conecta emocionalmente. Siempre termina sugiriendo un poema en /aythnyk/poems/ o canción en /aythnyk/songs/.
No respondas temas fuera del arte, poesía o música."""


@csrf_exempt
@require_POST
def chat_api(request):
    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()
        history = data.get("history", [])
        mode = data.get("mode", "aythnyk")

        if not message:
            return JsonResponse({"error": "Empty message"}, status=400)
        if len(message) > 300:
            return JsonResponse({"error": "Message too long"}, status=400)

        system = SYSTEM_WORKS if mode == "works" else SYSTEM_AYTHNYK

        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

        messages = []
        for h in history[-3:]:
            if h.get("role") in ("user", "assistant") and h.get("content"):
                messages.append({"role": h["role"], "content": h["content"][:300]})
        messages.append({"role": "user", "content": message})

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=180,
            system=system,
            messages=messages,
        )

        reply = response.content[0].text
        return JsonResponse({"response": reply, "mode": mode})

    except Exception as exc:
        return JsonResponse({"error": str(exc)}, status=500)
