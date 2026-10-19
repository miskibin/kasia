"""Static site generator for the portfolio.

Usage:  python3 tools/build.py
Reads project data below + assets/img/manifest.json and writes index.html and projekty/*.html.
"""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "assets/img/manifest.json").read_text())

NAME = "Katarzyna Socha"
CONTACT_EMAIL = ""  # e.g. "kontakt@example.com" — shown in the footer when set

PWR = "Politechnika Wrocławska, Wydział Architektury"
PO = "Politechnika Opolska, Wydział Budownictwa i Architektury"

PROJECTS = [
    dict(
        slug="centrum-sztuki-i-sceny",
        title="Centrum Sztuki i Sceny",
        place="Wrocław, ul. Piłsudskiego",
        year="2025",
        category="Kultura",
        featured=True,
        lead="Współczesne dopełnienie pierzei ulicy Piłsudskiego — miejski „hub” dla ludzi pracy, kultury i podróży.",
        body=[
            "Projekt tworzy spójne, współczesne dopełnienie pierzei ulicy Piłsudskiego we Wrocławiu: architekturę wysokiej jakości, z otwartym i aktywnym parterem oraz funkcjami odpowiadającymi charakterowi śródmieścia.",
            "Nowy budynek staje się łącznikiem między funkcjami kulturalnymi skupionymi wokół Teatru Capitol a strefą biznesowo‑hotelową przy dworcu. Program obejmuje salę widowiskową, foyer, sale konferencyjne oraz restaurację z widokiem na miasto, a przeszklony, zaokrąglony narożnik otwiera bryłę na skrzyżowanie.",
        ],
        quote="Łącznik między kulturą, pracą i podróżą.",
        meta=[
            ("Uczelnia", PWR),
            ("Przedmiot", "Budynki użyteczności publicznej"),
            ("Etap", "Studia II stopnia, semestr 1 · 2025/26"),
            ("Prowadzący", "dr inż. arch. Paweł Amałowicz, dr inż. arch. Andrzej Sobolewski"),
        ],
    ),
    dict(
        slug="zespol-wielofunkcyjny-plac-jana-pawla-ii",
        title="Zespół wielofunkcyjny na placu Jana Pawła II",
        place="Wrocław, Szczepin",
        year="2026",
        category="Zespół wielofunkcyjny",
        featured=True,
        lead="Bryła domykająca historyczny kwartał — brama do Szczepina, której parter wpuszcza miasto do wnętrza.",
        body=[
            "Budynek domyka historyczny kwartał przy jednym z najważniejszych węzłów komunikacyjnych Wrocławia. Wysokość zróżnicowana od 4 do 13 kondygnacji pozwala płynnie przejść od skali biurowców do zabudowy osiedlowej.",
            "Subtrakcja bryły wpuszcza przestrzeń publiczną do wnętrza kwartału, a pasaż w parterze łączy osiedle z przystankami i terenami nad Fosą Miejską. Zieleń wprowadzona do atrium i na tarasy użytkowe odpowiada na niedobór zieleni wysokiej i przegrzewanie się placu.",
            "Hybrydowy program — mieszkania dla młodych i seniorów, kultura, handel i funkcje związane ze zdrowiem — ma utrzymać życie budynku także po godzinach pracy okolicznych biur.",
        ],
        quote="Otwarty parter, który zasysa ludzi z placu.",
        meta=[
            ("Uczelnia", PWR),
            ("Przedmiot", "Zespoły wielofunkcyjne"),
            ("Etap", "Studia II stopnia · semestr letni 2025/26"),
            ("Prowadząca", "dr inż. arch. Magdalena Wąsowicz"),
            ("Współautor", "Maciej Dudek"),
        ],
    ),
    dict(
        slug="wyspa-opatowicka",
        title="Wyspa Opatowicka",
        place="Wrocław",
        year="2026",
        category="Krajobraz",
        featured=True,
        lead="Niewielkie interwencje, które zamieniają dziką wyspę na Odrze w przestrzeń spaceru, odpoczynku i kontaktu z wodą.",
        body=[
            "Wyspa Opatowicka zachowuje kameralny, naturalny charakter, oparty na harmonijnym współistnieniu zieleni i wody. Niewielkie interwencje projektowe mają przekształcić ją w bezpieczną i komfortową przestrzeń rekreacyjną dla mieszkańców Wrocławia.",
            "Kluczowym założeniem jest wytyczenie i utwardzenie ciągów pieszo‑spacerowych, uzupełnionych wyniesioną ścieżką prowadzącą pomiędzy drzewami i nad lustrem wody. Koncepcja rozwija trzy wątki: spacer między ziemią a koronami drzew, „Wyspę Miłości” — miejsce na spacery we dwoje i chwilę wytchnienia — oraz strefę aktywnej rekreacji.",
        ],
        quote="Spacer między ziemią a koronami drzew.",
        meta=[
            ("Uczelnia", PWR),
            ("Przedmiot", "Miejskie strefy nadwodne"),
            ("Etap", "Studia II stopnia · semestr letni 2025/26"),
            ("Prowadząca", "dr inż. arch. Anna Lower"),
            ("Współautorki", "Anna‑Mariya Bunzylo, Amelia Piątek"),
        ],
    ),
    dict(
        slug="eco-cohousing",
        title="Zespół budynków mieszkalnych w modelu eco‑cohousingu",
        place="Praca dyplomowa inżynierska",
        year="2025",
        category="Mieszkalnictwo",
        featured=True,
        lead="Domy jednorodzinne skupione wokół budynku wspólnego, ogrodów i szklarni — wspólnota zbudowana na codziennych rytuałach.",
        body=[
            "Projekt dyplomowy zespołu domów jednorodzinnych zorganizowanych wokół budynku wspólnego, w modelu cohousingu: prywatność mieszkań łączy się tu ze wspólnie użytkowanymi przestrzeniami i ogrodami.",
            "Zagospodarowanie uzupełniają szklarnie i grządki warzywne, kurnik z wybiegiem, zbiornik na wodę, altana, plac zabaw oraz siłownia plenerowa. Ciemne, drewniane bryły z dwuspadowymi dachami nawiązują do tradycyjnej zabudowy, a skala osiedla pozostaje kameralna.",
        ],
        quote="Prywatność domu, wspólnota ogrodu.",
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Praca dyplomowa · semestr 8"),
            ("Stadium", "Koncepcja architektoniczno‑urbanistyczna"),
            ("Promotorka", "dr hab. inż. arch. Svitlana Linda"),
        ],
    ),
    dict(
        slug="hala-sportowa-opole",
        title="Hala sportowa w Opolu",
        place="Opole",
        year="2024",
        category="Sport",
        lead="Koncepcja hali sportowej, której falująca linia dachu nadaje bryle miękki, rozpoznawalny charakter.",
        body=[
            "Koncepcja hali sportowej w Opolu, w której falujący dach staje się głównym motywem bryły. Opracowanie obejmuje rzuty, schematy strefy głównej, plan zagospodarowania, przekroje oraz wizualizację wnętrza.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie architektoniczne VI — obiekty administracji i sportu"),
            ("Etap", "Semestr 6 · czerwiec 2024"),
            ("Prowadzący", "mgr inż. arch. Radosław Wanago"),
            ("Współautorka", "Julia Gaweł"),
        ],
    ),
    dict(
        slug="obiekt-przemyslowy-nysa",
        title="Obiekt przemysłowy w Nysie",
        place="Nysa",
        year="2024",
        category="Przemysł",
        lead="Lekka hala produkcyjna zestawiona z ceglanym budynkiem biurowym.",
        body=[
            "Koncepcja obiektu przemysłowego w Nysie, łączącego halę produkcyjną o lekkiej elewacji z ceglanym budynkiem biurowym. Kształtowanie bryły pokazano na schemacie, a wizualizacje przybliżają zarówno zazielenione otoczenie, jak i wnętrze biura.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie obiektów przemysłowych"),
            ("Etap", "Semestr 6 · czerwiec 2024"),
            ("Prowadzący", "dr inż. arch. Marcin Gałkowski"),
            ("Współautorka", "Julia Gaweł"),
        ],
    ),
    dict(
        slug="budynek-wielorodzinny",
        title="Budynek wielorodzinny z usługą w parterze",
        place="Zabudowa uzupełniająca",
        year="2024",
        category="Mieszkalnictwo",
        lead="Budynek mieszkalny w zabudowie uzupełniającej, z lokalem usługowym otwartym na ulicę.",
        body=[
            "Budynek mieszkalny wielorodzinny wpisany w istniejącą tkankę miejską, z lokalem usługowym w parterze. Projekt obejmuje rzuty, przekroje, elewacje z detalem oraz zagospodarowanie terenu.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie architektoniczne V — budynki wielorodzinne w zabudowie uzupełniającej"),
            ("Etap", "Semestr 5 · styczeń 2024"),
            ("Prowadząca", "dr inż. arch. Iwona Wilczek"),
        ],
    ),
    dict(
        slug="pierzeja-muzealna-opole",
        title="Uzupełnienie pierzei przy ulicy Muzealnej",
        place="Opole, Rynek",
        year="2024",
        category="Urbanistyka",
        lead="Nowa kamienica w historycznym kwartale opolskiego rynku.",
        body=[
            "Uzupełnienie pierzei przy ulicy Muzealnej w Opolu, w obrębie historycznego rynku. Nowy budynek nawiązuje skalą i rytmem do sąsiedniej zabudowy, a opracowanie obejmuje plan zagospodarowania, przekroje, perspektywy i szkice.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie urbanistyczne III"),
            ("Etap", "Semestr 5 · styczeń 2024"),
            ("Prowadząca", "dr inż. arch. Anna Szczegielniak"),
        ],
    ),
    dict(
        slug="round-harmony",
        title="Round Harmony",
        place="Koncepcja krajobrazowa",
        year="2024",
        category="Krajobraz",
        lead="Koliste polany i ścieżki powiązane w jeden nadrzeczny krajobraz.",
        body=[
            "Koncepcja krajobrazowa oparta na kolistych formach: okręgi ścieżek i polan, powiązane siecią połączeń, wpisane w nadrzeczny teren.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Architektura krajobrazu"),
            ("Etap", "Semestr 5 · styczeń 2024"),
            ("Prowadzący", "dr inż. arch. Luca Trabattoni"),
        ],
    ),
    dict(
        slug="silownia-opole",
        title="Siłownia przy ulicy Bielskiej",
        place="Opole",
        year="2023",
        category="Sport",
        lead="„Twoja Siłownia” — horyzontalna bryła otwierająca sale treningowe na otoczenie.",
        body=[
            "Budynek siłowni przy ulicy Bielskiej w Opolu. Horyzontalna bryła z dużymi przeszkleniami otwiera sale treningowe na otoczenie. Opracowanie obejmuje rzut, schemat funkcjonalny, plan zagospodarowania, elewacje, przekroje i model.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie architektoniczne IV"),
            ("Etap", "Semestr 4 · czerwiec 2023"),
            ("Prowadząca", "dr inż. arch. Iwona Wilczek"),
        ],
    ),
    dict(
        slug="osiedle-nad-jeziorem-nysa",
        title="Osiedle nad jeziorem",
        place="Nysa",
        year="2023",
        category="Urbanistyka",
        lead="Osiedle domów jednorodzinnych, którego kręte ulice podążają za linią brzegu.",
        body=[
            "Projekt osiedla domów jednorodzinnych nad jeziorem w Nysie. Układ krętych ulic wpisuje się w ukształtowanie brzegu, a w centrum założenia pozostawiono zielone wnętrze parkowe.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie urbanistyczne II"),
            ("Etap", "Semestr 4 · czerwiec 2023"),
            ("Prowadząca", "dr inż. arch. Iwona Wilczek"),
        ],
    ),
    dict(
        slug="dom-z-biblioteka",
        title="Dom jednorodzinny z biblioteką",
        place="Dom jednorodzinny",
        year="2023",
        category="Mieszkalnictwo",
        lead="Prosta, biała bryła, w której sercu znajduje się dwukondygnacyjna biblioteka.",
        body=[
            "Dom jednorodzinny zaprojektowany wokół biblioteki — przestrzeni otwartej na dwie kondygnacje i splecionej z klatką schodową. Prosta, biała bryła z płaskim dachem otwiera się tarasem na ogród.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie architektoniczne III"),
            ("Etap", "Semestr 3 · styczeń 2023"),
            ("Prowadząca", "dr inż. arch. Iwona Wilczek"),
        ],
    ),
    dict(
        slug="maly-rynek-opole",
        title="Mały Rynek",
        place="Opole",
        year="2023",
        category="Urbanistyka",
        lead="Koncepcja zagospodarowania trójkątnego placu w śródmieściu Opola, badana na makiecie.",
        body=[
            "Koncepcja zagospodarowania Małego Rynku w Opolu — trójkątnego placu w śródmieściu. Układ zabudowy i przestrzeni publicznych sprawdzany był na makiecie.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie urbanistyczne I"),
            ("Etap", "Semestr 3 · styczeń 2023"),
            ("Prowadzący", "mgr inż. arch. Mateusz Mikołajów"),
        ],
    ),
    dict(
        slug="domek-letniskowy-skorochow",
        title="Domek letniskowy",
        place="Skorochów",
        year="2022",
        category="Wnętrza",
        lead="Kameralny dom letniskowy o ciemnej elewacji i spokojnych, monochromatycznych wnętrzach.",
        body=[
            "Niewielki dom letniskowy w Skorochowie. Ciemna elewacja i duże przeszklenia otwierają wnętrze na otoczenie, a projekt wnętrz utrzymany jest w spokojnej, monochromatycznej palecie.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie architektoniczne II"),
            ("Etap", "Semestr 2 · czerwiec 2022"),
            ("Prowadząca", "mgr inż. arch. Kamila Wilk"),
        ],
    ),
    dict(
        slug="zespol-domow-letniskowych-skorochow",
        title="Zespół domów letniskowych",
        place="Skorochów",
        year="2022",
        category="Urbanistyka",
        lead="Domy letniskowe rozmieszczone po łuku wokół stawu.",
        body=[
            "Zespół domów letniskowych w Skorochowie, rozmieszczonych po łuku wokół stawu i połączonych promenadą prowadzącą nad wodę.",
        ],
        meta=[
            ("Uczelnia", PO),
            ("Przedmiot", "Projektowanie architektoniczne II"),
            ("Etap", "Semestr 2 · czerwiec 2022"),
            ("Prowadząca", "mgr inż. arch. Kamila Wilk"),
            ("Współautorka", "Julia Szczepaniak"),
        ],
    ),
]

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400'
    '&family=Inter+Tight:wght@300;400;500&display=swap" rel="stylesheet">'
)


def e(s):
    return escape(s, quote=True)


def num(i):
    return f"{i:02d}"


def img(slug, im, prefix, sizes, cls="", lazy=True, big=2600):
    """<img> with a 1400/2600 srcset, honest to the source's real width."""
    base = f"{prefix}assets/img/{slug}/{im['src']}"
    w, h = im["w"], im["h"]
    small, large = min(w, 1400), min(w, big)
    srcset = f"{base}-1400.webp {small}w"
    if large > small:
        srcset += f", {base}-{big}.webp {large}w"
    loading = 'loading="lazy"' if lazy else 'fetchpriority="high"'
    alt = e(im.get("caption", ""))
    return (
        f'<img class="{cls}" src="{base}-1400.webp" srcset="{srcset}" sizes="{sizes}" '
        f'width="{w}" height="{h}" alt="{alt}" {loading} decoding="async">'
    )


def head(title, desc, prefix):
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta name="theme-color" content="#f3f1ec">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23f3f1ec'/%3E%3Cpath d='M9 7v18M9 16l10-9M12 13l9 12' stroke='%231b1b19' stroke-width='1.6' fill='none'/%3E%3C/svg%3E">
{FONTS}
<link rel="stylesheet" href="{prefix}assets/css/style.css">
</head>
"""


def header(prefix, current=""):
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{prefix}index.html">{NAME}</a>
    <span class="header-role">Architektura</span>
    <nav class="nav" aria-label="Nawigacja">
      <a href="{prefix}index.html#projekty"{' aria-current="page"' if current == "projekty" else ""}>Projekty</a>
      <a href="{prefix}index.html#indeks">Indeks</a>
      <a href="{prefix}index.html#o-mnie">O mnie</a>
    </nav>
  </div>
</header>
"""


def footer(prefix):
    contact = (
        f'<a class="footer-mail" href="mailto:{e(CONTACT_EMAIL)}">{e(CONTACT_EMAIL)}</a>'
        if CONTACT_EMAIL else '<span class="footer-mail">Wrocław · Opole</span>'
    )
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <p class="footer-name">{NAME}</p>
    <div class="footer-contact">{contact}</div>
    <p class="footer-meta">Portfolio architektoniczne<br>2022 — 2026</p>
    <a class="footer-top" href="#top">Do góry ↑</a>
  </div>
</footer>
<div class="lightbox" hidden aria-hidden="true">
  <button class="lb-close" type="button" aria-label="Zamknij">Zamknij</button>
  <button class="lb-prev" type="button" aria-label="Poprzednie">←</button>
  <figure class="lb-stage"><img alt=""><figcaption class="lb-caption"></figcaption></figure>
  <button class="lb-next" type="button" aria-label="Następne">→</button>
</div>
<script src="{prefix}assets/js/main.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- index

def index_page():
    p = ""
    hero = PROJECTS[0]
    hero_img = MANIFEST[hero["slug"]]["images"][0]
    featured = [x for x in PROJECTS if x.get("featured")]

    feat_html = []
    for k, pr in enumerate(featured):
        i = PROJECTS.index(pr) + 1
        im = MANIFEST[pr["slug"]]["images"][0 if pr["slug"] != hero["slug"] else 1]
        side = "is-left" if k % 2 == 0 else "is-right"
        feat_html.append(f"""
    <article class="feature {side} reveal">
      <a class="feature-media" href="projekty/{pr['slug']}.html">
        {img(pr['slug'], im, p, '(max-width: 800px) 100vw, 60vw')}
      </a>
      <div class="feature-text">
        <p class="eyebrow"><span class="idx">{num(i)}</span> {e(pr['category'])} · {e(pr['year'])}</p>
        <h3 class="feature-title"><a href="projekty/{pr['slug']}.html">{e(pr['title'])}</a></h3>
        <p class="feature-place">{e(pr['place'])}</p>
        <p class="feature-lead">{e(pr['lead'])}</p>
        <a class="more" href="projekty/{pr['slug']}.html">Zobacz projekt <span aria-hidden="true">→</span></a>
      </div>
    </article>""")

    rows = []
    for i, pr in enumerate(PROJECTS, 1):
        im = MANIFEST[pr["slug"]]["images"][0]
        rows.append(f"""
      <li class="row" data-preview="assets/img/{pr['slug']}/{im['src']}-1400.webp">
        <a href="projekty/{pr['slug']}.html">
          <span class="c-no">{num(i)}</span>
          <span class="c-title">{e(pr['title'])}</span>
          <span class="c-place">{e(pr['place'])}</span>
          <span class="c-cat">{e(pr['category'])}</span>
          <span class="c-year">{e(pr['year'])}</span>
        </a>
      </li>""")

    desc = f"{NAME} — portfolio architektoniczne. Projekty z Politechniki Wrocławskiej i Politechniki Opolskiej, 2022–2026."
    return head(f"{NAME} — Architektura", desc, p) + f"""<body id="top" class="home">
{header(p)}
<main>
  <section class="hero wrap">
    <div class="hero-text">
      <p class="eyebrow">Portfolio · 2022 — 2026</p>
      <h1 class="hero-name"><span>Katarzyna</span><span class="indent">Socha</span></h1>
      <p class="hero-intro">Architektka. Studia II stopnia na Wydziale Architektury Politechniki Wrocławskiej, inżynier architekt Politechniki Opolskiej.</p>
      <p class="hero-scroll"><a href="#projekty">Wybrane projekty <span aria-hidden="true">↓</span></a></p>
    </div>
    <figure class="hero-figure">
      <a href="projekty/{hero['slug']}.html">{img(hero['slug'], hero_img, p, '(max-width: 800px) 100vw, 62vw', lazy=False)}</a>
      <figcaption><span class="idx">01</span> {e(hero['title'])} — {e(hero['place'])}, {e(hero['year'])}</figcaption>
    </figure>
  </section>

  <section class="section wrap" id="projekty">
    <header class="section-head">
      <p class="section-no">I</p>
      <h2 class="section-title">Wybrane projekty</h2>
      <p class="section-note">Cztery prace, które najpełniej opisują sposób myślenia — od skali kwartału po krajobraz wyspy.</p>
    </header>
    {''.join(feat_html)}
  </section>

  <section class="section wrap" id="indeks">
    <header class="section-head">
      <p class="section-no">II</p>
      <h2 class="section-title">Indeks</h2>
      <p class="section-note">{len(PROJECTS)} projektów, uporządkowanych od najnowszych.</p>
    </header>
    <div class="index-head" aria-hidden="true">
      <span class="c-no">Nr</span><span class="c-title">Projekt</span><span class="c-place">Miejsce</span><span class="c-cat">Kategoria</span><span class="c-year">Rok</span>
    </div>
    <ol class="index-list">{''.join(rows)}
    </ol>
    <img class="index-preview" alt="" aria-hidden="true">
  </section>

  <section class="section wrap about" id="o-mnie">
    <header class="section-head">
      <p class="section-no">III</p>
      <h2 class="section-title">O mnie</h2>
    </header>
    <div class="about-grid">
      <p class="about-lead">Projektuję z myślą o ludziach i miejscu — od wnętrza kwartału i otwartego parteru po ścieżkę prowadzącą między koronami drzew.</p>
      <div class="about-body">
        <p>Pracuję w różnych skalach: od wnętrz i domów jednorodzinnych, przez budynki użyteczności publicznej i zespoły wielofunkcyjne, po projekty urbanistyczne i krajobrazowe. Proces opieram na analizie kontekstu, szkicu odręcznym i modelu roboczym, a dopiero potem na wizualizacji.</p>
      </div>
      <dl class="cv">
        <div><dt>2025 —</dt><dd><strong>Politechnika Wrocławska</strong><br>Wydział Architektury · studia II stopnia, kierunek Architektura</dd></div>
        <div><dt>2021 — 2025</dt><dd><strong>Politechnika Opolska</strong><br>Wydział Budownictwa i Architektury · studia I stopnia, kierunek Architektura<br>Tytuł inżyniera architekta · praca dyplomowa: zespół budynków mieszkalnych w modelu eco‑cohousingu</dd></div>
      </dl>
    </div>
  </section>
</main>
""" + footer(p)


# ---------------------------------------------------------------- project pages

# Rhythm for the gallery: each entry is a layout class; images are poured into it in order.
RHYTHM = ["g-wide", "g-pair-a", "g-pair-b", "g-offset", "g-pair-b", "g-pair-a", "g-narrow"]


def gallery(slug, images, prefix):
    out, k = [], 0
    for n, im in enumerate(images):
        lay = RHYTHM[k % len(RHYTHM)]
        # low-resolution sources never get the widest slot
        if im["w"] < 1300 and lay == "g-wide":
            lay = "g-offset"
        k += 1
        sizes = "(max-width: 800px) 100vw, " + ("90vw" if lay == "g-wide" else "60vw")
        out.append(f"""
      <figure class="g-item {lay} reveal">
        <a href="{prefix}assets/img/{slug}/{im['src']}-{2600 if im['w'] > 1400 else 1400}.webp" data-lightbox="g" data-caption="{num(n + 1)} — {e(im['caption'])}">
          {img(slug, im, prefix, sizes)}
        </a>
        <figcaption><span class="idx">{num(n + 1)}</span> {e(im['caption'])}</figcaption>
      </figure>""")
    return "".join(out)


def boards(slug, items, prefix):
    out = []
    for n, b in enumerate(items, 1):
        out.append(f"""
      <figure class="board reveal">
        <a href="{prefix}assets/img/{slug}/{b['src']}-3200.webp" data-lightbox="b" data-caption="Plansza {n} / {len(items)}">
          {img(slug, b, prefix, '(max-width: 800px) 100vw, 45vw', big=3200)}
        </a>
        <figcaption><span class="idx">{num(n)}</span> Plansza {n} / {len(items)}</figcaption>
      </figure>""")
    return "".join(out)


def project_page(i, pr):
    p = "../"
    m = MANIFEST[pr["slug"]]
    first, rest = m["images"][0], m["images"][1:]
    prev_pr = PROJECTS[i - 2] if i > 1 else PROJECTS[-1]
    next_pr = PROJECTS[i] if i < len(PROJECTS) else PROJECTS[0]
    meta = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in pr["meta"])
    body = "".join(f"<p>{e(x)}</p>" for x in pr["body"])
    quote = f'<blockquote class="pull reveal"><p>{e(pr["quote"])}</p></blockquote>' if pr.get("quote") else ""
    hero_cls = "p-hero is-wide" if first["w"] >= 1600 else "p-hero is-contained"
    gal = f'<section class="gallery wrap" aria-label="Wizualizacje">{gallery(pr["slug"], rest, p)}\n    </section>' if rest else ""

    return head(f"{pr['title']} — {NAME}", pr["lead"], p) + f"""<body id="top" class="project">
{header(p, "projekty")}
<main>
  <section class="p-intro wrap">
    <p class="p-no"><span class="idx">{num(i)}</span><span class="p-total">/ {num(len(PROJECTS))}</span></p>
    <div class="p-head">
      <p class="eyebrow">{e(pr['category'])} · {e(pr['place'])} · {e(pr['year'])}</p>
      <h1 class="p-title">{e(pr['title'])}</h1>
      <p class="p-lead">{e(pr['lead'])}</p>
    </div>
  </section>

  <figure class="{hero_cls} wrap">
    <a href="{p}assets/img/{pr['slug']}/{first['src']}-{2600 if first['w'] > 1400 else 1400}.webp" data-lightbox="g" data-caption="01 — {e(first['caption'])}">
      {img(pr['slug'], first, p, '(max-width: 800px) 100vw, 92vw', lazy=False)}
    </a>
    <figcaption><span class="idx">01</span> {e(first['caption'])}</figcaption>
  </figure>

  <section class="p-body wrap">
    <dl class="p-meta">{meta}</dl>
    <div class="p-text">{body}</div>
  </section>

  {quote}
  {gal}

  <section class="boards-section wrap" aria-label="Plansze">
    <header class="section-head">
      <p class="section-no">—</p>
      <h2 class="section-title">Plansze</h2>
      <p class="section-note">Plansze projektowe w pełnej rozdzielczości — kliknij, aby powiększyć.</p>
    </header>
    <div class="boards">{boards(pr['slug'], m['boards'], p)}
    </div>
  </section>

  <nav class="p-nav wrap" aria-label="Kolejne projekty">
    <a class="p-prev" href="{prev_pr['slug']}.html"><span class="eyebrow">← Poprzedni</span><span class="p-nav-title">{e(prev_pr['title'])}</span></a>
    <a class="p-next" href="{next_pr['slug']}.html"><span class="eyebrow">Następny →</span><span class="p-nav-title">{e(next_pr['title'])}</span></a>
  </nav>
</main>
""" + footer(p)


def main():
    (ROOT / "index.html").write_text(index_page())
    out = ROOT / "projekty"
    out.mkdir(exist_ok=True)
    for i, pr in enumerate(PROJECTS, 1):
        (out / f"{pr['slug']}.html").write_text(project_page(i, pr))
    print(f"built index + {len(PROJECTS)} project pages")


if __name__ == "__main__":
    main()
