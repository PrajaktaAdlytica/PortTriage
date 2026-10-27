from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from xml.sax.saxutils import escape
import zipfile,shutil
out=Path('public/brand')
font=TTFont('node_modules/@fontsource/newsreader/files/newsreader-latin-500-normal.woff')
glyphs=font.getGlyphSet(); cmap=font.getBestCmap(); units=font['head'].unitsPerEm
scale=70/units; x=0; paths=[]
for c in 'PortTriage':
 name=cmap[ord(c)]; pen=SVGPathPen(glyphs); glyphs[name].draw(pen)
 paths.append(f'<path transform="translate({x*scale:.3f} 0)" d="{pen.getCommands()}"/>')
 x+=font['hmtx'][name][0]-units*.018
width=x*scale
# Three nested routes form a P; the rose waypoint identifies the handoff.
def symbol(navy,blue,pink):
 return f'<path d="M16 88V32C16 20 24 12 36 12H59C78 12 90 24 90 42S78 72 59 72H35" fill="none" stroke="{navy}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 88V35C30 29 34 26 40 26H58C69 26 76 32 76 42S69 58 58 58H30" fill="none" stroke="{blue}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="58" r="6" fill="{pink}"/>'
def svg(content,w,h,title):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{content}</svg>'
variants={'primary':('#0F2C44','#5FADDD','#EC6E93'),'reverse':('#F3FAFF','#5FADDD','#EC6E93'),'navy':('#0F2C44',)*3,'white':('#FFFFFF',)*3}
for key,(ink,blue,pink) in variants.items():
 out.joinpath(f'porttriage-symbol-{key}.svg').write_text(svg(symbol(ink,blue,pink),104,104,'PortTriage symbol'))
 # Glyph outlines make the wordmark independent of installed fonts.
 lettering=''.join(paths)
 word=f'<g transform="translate(124 77)" fill="{ink}"><g transform="scale(1 -1)"><g transform="scale({scale})">'
 # Path translations were in screen units; place each glyph independently instead.
 wordpaths=[]; cursor=0
 for c in 'PortTriage':
  name=cmap[ord(c)]; pen=SVGPathPen(glyphs);glyphs[name].draw(pen)
  wordpaths.append(f'<path transform="translate({cursor*scale:.3f} 0) scale({scale} {-scale})" d="{pen.getCommands()}"/>');cursor+=font['hmtx'][name][0]-units*.018
 word=f'<g transform="translate(124 77)" fill="{ink}">'+''.join(wordpaths)+f'<circle cx="{width+7:.2f}" cy="-4" r="4" fill="{pink}"/></g>'
 out.joinpath(f'porttriage-logo-{key}.svg').write_text(svg(symbol(ink,blue,pink)+word,round(144+width),104,'PortTriage'))
for size in [16,32,48]:
 out.joinpath(f'favicon-{size}.svg').write_text(svg(symbol('#0F2C44','#5FADDD','#EC6E93'),104,104,'PortTriage favicon').replace('viewBox=',f'width="{size}" height="{size}" viewBox='))
adaptive='<style>.outer{stroke:#0F2C44}@media(prefers-color-scheme:dark){.outer{stroke:#F3FAFF}}</style>'+symbol('#0F2C44','#5FADDD','#EC6E93').replace('stroke="#0F2C44"','class="outer"')
out.joinpath('favicon.svg').write_text(svg(adaptive,104,104,'PortTriage favicon'))
shutil.copy('node_modules/@fontsource/newsreader/LICENSE',out/'Newsreader-OFL.txt')
out.joinpath('README.txt').write_text('PORTTRIAGE / VECTOR IDENTITY\n\nOriginal route-and-waypoint P symbol. Full logos use outlined Newsreader Medium lettering, licensed under the included SIL Open Font License. All SVGs are pure vector paths; no embedded raster assets or external fonts.\n\nprimary: light surfaces. reverse: navy surfaces. navy/white: single-color use. favicon.svg adapts its outer route for light/dark browser chrome. Numbered favicons include explicit pixel dimensions.\n\nKeep clear space of at least one waypoint diameter. Use the symbol for small applications; full logo recommended at 160px width or larger. Do not stretch. Brand colors: Navy #0F2C44, Sky #5FADDD, Rose #EC6E93.\n\nThis artwork does not represent trademark clearance.\n')
cards=''.join(f'<figure class="{ "dark" if key in ["reverse","white"] else ""}"><img src="porttriage-logo-{key}.svg" alt="{key} full logo"><figcaption>{key.upper()} / OUTLINED VECTOR</figcaption><img class="symbol" src="porttriage-symbol-{key}.svg" alt="{key} symbol"></figure>' for key in variants)
out.joinpath('index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PortTriage · Vector identity</title><style>body{margin:0;background:#eef6fb;color:#0f2c44;font:14px system-ui;padding:48px}h1{font:48px Georgia;margin:12px 0}p{line-height:1.6}main{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:32px}figure{margin:0;padding:40px;background:white;border-radius:12px}figure.dark{background:#0f2c44;color:white}img{width:100%;height:100px;object-fit:contain;object-position:left}figcaption{font-size:10px;letter-spacing:2px;margin:30px 0}.symbol{width:72px;height:72px}.fav img{width:32px;height:32px;margin:20px}a{color:inherit}@media(max-width:650px){body{padding:24px}main{grid-template-columns:1fr}figure{padding:24px}}</style><p>PORTTRIAGE / BRAND ASSETS</p><h1>A clear signal. At every scale.</h1><p>Route geometry, a named waypoint, and an editorial wordmark.<br>True vector SVGs with outlined lettering.</p><main>'+cards+'</main><section class="fav"><h2>Favicon family</h2><img src="favicon-16.svg" style="width:16px;height:16px"><img src="favicon-32.svg"><img src="favicon-48.svg" style="width:48px;height:48px"><p><a href="porttriage-svg-set.zip">Download the SVG set</a></p></section></html>')
with zipfile.ZipFile(out/'porttriage-svg-set.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(out.iterdir()):
  if p.suffix in ['.svg','.txt','.html']:z.write(p,p.name)
print('Created 12 SVGs, preview, license and ZIP.')
