# Escapada por Gran Canaria — web sin conexión

## Publicar en GitHub Pages

1. En GitHub crea un repositorio nuevo, por ejemplo `gran-canaria-planes` (público).
2. Sube a la **raíz del repositorio** estos cinco archivos extraídos del ZIP: `index.html`, `sw.js`, `manifest.webmanifest`, `icon-192.png` e `icon-512.png`.
3. En **Settings → Pages → Build and deployment**, selecciona **Deploy from a branch**, rama **main** y carpeta **/(root)**, y pulsa **Save**.
4. El enlace tendrá la forma: `https://TU_USUARIO.github.io/gran-canaria-planes/`.
5. Abre el enlace una primera vez **con internet** para que se descarguen los archivos y se instale el almacenamiento sin conexión. Después se puede volver a abrir desde el mismo dispositivo sin internet. En iPad/iPhone, Safari → Compartir → Añadir a pantalla de inicio.

## Modo totalmente local
El archivo `index.html` (o la copia `Gran_Canaria_OFFLINE.html`) contiene mapa y actividades incrustados; también puede abrirse desde la app Archivos de iOS o un ordenador SIN internet, sin usar el service worker. En iOS algunos visores de archivos restringen JavaScript; si ocurre, utiliza Safari con la web instalada.

## Limitaciones
- El mapa offline es geográfico, con costa trazada cartográficamente y ubicaciones estimadas, **no** un callejero para orientarse por calles, ni proporciona navegación GPS.
- Los enlaces a Google Maps y los horarios oficiales sí requieren datos móviles o wifi cuando se abren. El contenido textual de horarios en las fichas ya está guardado.
- Los favoritos se guardan por navegador y dispositivo. No se sincronizan entre dispositivos.
- En caso de duda de seguridad, prioriza volver con luz de día y revisa la línea de autobús elegida.
