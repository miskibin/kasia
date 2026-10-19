# Katarzyna Socha — portfolio architektoniczne

Statyczna strona portfolio (GitHub Pages).

- `index.html`, `projekty/*.html` — strony generowane przez `tools/build.py` (dane projektów są w tym pliku).
- `assets/css`, `assets/js` — styl i interakcje (lightbox, podgląd w indeksie).
- `assets/img/<projekt>/` — rendery (`rNN`) i plansze (`bNN`) w WebP, wygenerowane z PDF-ów przez `tools/extract_assets.py`.

Po zmianie danych: `python3 tools/build.py`.
Adres e-mail w stopce: ustaw `CONTACT_EMAIL` w `tools/build.py` i przebuduj.
