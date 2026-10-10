# Alberto bar · пиво к закускам

Мини-меню бара Alberto (Алматы, ул. Гоголя 144): к каждому сету закусок подобрано пиво из карты бара, с описанием вкуса и пирамидой нот.

Сделано командой Flavor Tree.

## Как открыть

Это статический сайт без сборки: `index.html`, данные в `pilot/`, фото в `img/`.

- Vercel: импортировать репозиторий, Framework Preset = Other, без команд сборки.
- GitHub Pages: Settings → Pages → Deploy from branch → `main` / root.
- Локально: `python3 -m http.server 8091` и открыть http://127.0.0.1:8091/

Меню сначала берётся из API Flavor Tree; если API не ответил, страница показывает снимок из `pilot/alberto-menu.json`.

## QR-код для столиков

- `qr.png` / `qr.svg` — QR на гостевое меню, `qr.html` — печатная карточка с брендингом Alberto.
- По умолчанию QR ведёт на `https://alberto-qr.vercel.app`. После деплоя на Vercel проверьте реальный адрес и при необходимости перегенерируйте:

```
python3 make_qr.py https://<ваш-адрес>.vercel.app
```
