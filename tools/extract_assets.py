"""Build web assets (renders + boards) from the portfolio PDFs.

Usage: python3 tools/extract_assets.py <workdir> assets/img
<workdir> must contain src/Portfolio archi Katarzyna Socha/{inz,centrum,jp2,wyspa}.pdf
and emb/ (output of `pdfimages -png -p <pdf> emb/<name>` for each PDF)."""
import json, subprocess, sys
from pathlib import Path
from PIL import Image
import numpy as np

Image.MAX_IMAGE_PIXELS = None
S = Path(sys.argv[1]); OUT = Path(sys.argv[2])
SRC = S / "src/Portfolio archi Katarzyna Socha"; EMB = S / "emb"; TMP = S / "pages"; TMP.mkdir(exist_ok=True)

P = {  # slug: (renders [(embedded-name | (pdf,page,box), caption)], boards (pdf, pages))
 "centrum-sztuki-i-sceny": ([("centrum-003-1202","Wizualizacja zewnętrzna"),("centrum-002-1196","Foyer"),("centrum-002-1194","Sala widowiskowa"),("centrum-002-1198","Sala konferencyjna"),("centrum-002-1200@0.945","Restauracja"),("centrum-003-3512","Aksonometria"),("centrum-001-1189","Rozwinięcie urbanistyczne ulicy Piłsudskiego")],("centrum",[1,2,3])),
 "zespol-wielofunkcyjny-plac-jana-pawla-ii": ([("jp2-005-182","Widok z lotu ptaka"),("jp2-003-122","Bryła w kontekście kwartału"),("jp2-004-173","Arkady parteru"),("jp2-003-124","Fasada — detal"),("jp2-003-126","Elewacja"),("jp2-003-123","Subtrakcja bryły — wejście do wnętrza kwartału"),("jp2-002-038","Rysunek koncepcyjny"),("jp2-002-033","Model roboczy"),("jp2-002-040","Szkic koncepcji")],("jp2",[1,2,3,4,5])),
 "wyspa-opatowicka": ([("wyspa-004-180","Pomost — aktywna rekreacja"),("wyspa-002-025","Wieża widokowa w koronach drzew"),("wyspa-002-033","Pawilon na wyniesionej ścieżce"),("wyspa-002-032","Ścieżka nad lustrem wody"),("wyspa-003-064","Pawilony nad nabrzeżem"),("wyspa-003-065","Wyspa Miłości — pergola"),("wyspa-003-152","Przystań"),("wyspa-004-174","Amfiteatr"),("wyspa-004-212","Kawiarnia — wnętrza")],("wyspa",[1,2,3,4])),
 "eco-cohousing": ([("inz-004-018","Widok osiedla z lotu ptaka"),("inz-003-016","Budynek wspólny"),("inz-005-037","Dom mieszkalny"),("inz-005-038","Dom mieszkalny — widok od ścieżki"),("inz-003-015","Budynek wspólny — perspektywa"),("inz-003-010","Aksonometria budynku wspólnego"),("inz-002-002","Projekt zagospodarowania terenu")],("inz",[2,3,4,5])),
 "hala-sportowa-opole": ([(("inz",9,(0.405,0.535,0.735,0.772)),"Wizualizacja wnętrza")],("inz",[9,10])),
 "obiekt-przemyslowy-nysa": ([(("inz",14,(0.062,0.535,0.768,0.842)),"Wizualizacja — strefa biurowa"),(("inz",17,(0.062,0.602,0.772,0.842)),"Wizualizacja — hala produkcyjna")],("inz",[14,15,16,17])),
 "budynek-wielorodzinny": ([("inz-012-089","Widok od ulicy"),("inz-012-088","Perspektywa narożnika"),("inz-012-094","Perspektywa"),("inz-012-087","Projekt zagospodarowania terenu")],("inz",[11,12,13])),
 "silownia-opole": ([("inz-007-047","Widok z lotu ptaka"),("inz-007-044","Widok od ulicy"),("inz-007-045","Widok od strony zieleni"),("inz-007-046","Perspektywa"),("inz-006-042","Plan zagospodarowania terenu")],("inz",[6,7,8])),
 "osiedle-nad-jeziorem-nysa": ([("inz-024-184","Projekt zagospodarowania terenu"),("inz-025-196","Fragment założenia"),("inz-025-186","Schemat zabudowy")],("inz",[24,25])),
 "dom-z-biblioteka": ([("inz-021-164","Widok od ogrodu"),("inz-021-163","Bryła"),("inz-021-165","Widok z lotu ptaka"),("inz-021-162","Biblioteka — klatka schodowa")],("inz",[18,19,20,21])),
 "domek-letniskowy-skorochow": ([("inz-023-174","Wnętrze — strefa dzienna"),("inz-023-173","Wnętrze — sypialnia"),("inz-023-172","Łazienka")],("inz",[22,23])),
 "zespol-domow-letniskowych-skorochow": ([("inz-026-200","Domy nad stawem"),("inz-026-199","Widok z lotu ptaka"),("inz-026-198","Promenada")],("inz",[26,27])),
 "pierzeja-muzealna-opole": ([("inz-029-248","Elewacja uzupełnienia pierzei"),("inz-028-228","Analiza kwartału"),("inz-029-252","Szkic")],("inz",[28,29])),
 "maly-rynek-opole": ([("inz-030-259","Model — widok z góry"),("inz-030-258","Model — pierzeja"),("inz-030-260","Model — perspektywa")],("inz",[30,31])),
 "round-harmony": ([("inz-032-272","Koncepcja na ortofotomapie"),("inz-032-267","Rzut założenia")],("inz",[32])),
}
DPI = {"inz": 200, "centrum": 90, "jp2": 90, "wyspa": 90}

def page(pdf, n):
    f = TMP / f"{pdf}-{n}.png"
    if not f.exists():
        subprocess.run(["pdftoppm","-f",str(n),"-l",str(n),"-r",str(DPI[pdf]),"-png","-singlefile",str(SRC/f"{pdf}.pdf"),str(f)[:-4]],check=True,stderr=subprocess.DEVNULL)
    return Image.open(f).convert("RGB")

def strip_titleblock(im):
    """A3 boards: crop to the drawing field, dropping the frame and the application title block."""
    g = np.asarray(im.convert("L")) < 110
    h, w = g.shape
    cols = np.where(g.sum(0) > 0.55*h)[0]; rows = np.where(g.sum(1) > 0.55*w)[0]
    l, r, t, b = cols.min(), cols.max(), rows.min(), rows.max()
    inner = [c for c in cols if l + 0.5*(r-l) < c < r - 10]
    tb = min(inner) if inner else r
    return im.crop((l+6, t+6, tb-6, b-6))

def save(im, base, sizes=(1400, 2600), q=80):
    base.parent.mkdir(parents=True, exist_ok=True)
    out = []
    for s in sizes:
        c = im.copy()
        if c.width > s: c.thumbnail((s, s*10), Image.LANCZOS)
        p = base.with_name(f"{base.name}-{s}.webp"); c.save(p, "WEBP", quality=q, method=6); out.append((s, c.width, c.height))
    return out

manifest = {}
for slug, (renders, (pdf, pages)) in P.items():
    m = {"images": [], "boards": []}
    for i, (src, cap) in enumerate(renders, 1):
        if isinstance(src, tuple):
            pdfn, pn, (x0,y0,x1,y1) = src; pg = page(pdfn, pn)
            im = pg.crop((int(x0*pg.width), int(y0*pg.height), int(x1*pg.width), int(y1*pg.height)))
        else:
            name, _, keep = src.partition("@")  # "@0.945" keeps the top 94.5% (drops a watermark)
            im = Image.open(EMB/f"{name}.png").convert("RGB")
            if keep: im = im.crop((0, 0, im.width, int(im.height*float(keep))))
        r = save(im, OUT/slug/f"r{i:02d}")
        m["images"].append({"src": f"r{i:02d}", "w": im.width, "h": im.height, "caption": cap})
    for j, pn in enumerate(pages, 1):
        im = page(pdf, pn)
        if pdf == "inz": im = strip_titleblock(im)
        save(im, OUT/slug/f"b{j:02d}", sizes=(1400, 3200), q=78)
        m["boards"].append({"src": f"b{j:02d}", "w": im.width, "h": im.height})
    manifest[slug] = m
    print(slug, len(m["images"]), len(m["boards"]), flush=True)
(OUT/"manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
