# Gran Canaria · callejero real y planes (offline)

**Entregado con mapas geográficos reales:** `atlas.js` (~8 MB) contiene carreteras, senderos, polígonos de costa y playas, parques y edificios extraídos del archivo Shapefile proporcionado. NO hay descargas de otros servidores, ni placeholders, ni procesos de conversión pendientes.

## Publicación en GitHub Pages (sin GitHub Actions)

1. Crea un repositorio **público** en GitHub, por ejemplo `gran-canaria`.
2. Sube **los siguientes archivos al directorio raíz** (no metas una carpeta contenedora extra): `index.html`, `atlas.js`, `sw.js`, `manifest.webmanifest`, `icon-192.png`, `icon-512.png`, `.nojekyll` y `LICENCIA-Y-FUENTE.txt`.
3. Ve a **Settings → Pages → Build and deployment** → **Deploy from a branch** → `main` / `/(root)` → **Save**.
4. Abre la URL `https://TU_USUARIO.github.io/gran-canaria/`. Con internet, espera que carguen por completo las calles una vez. Para comprobar modo offline, vuelve a abrir con modo avión.
5. En Safari iOS/iPadOS: Compartir → Añadir a pantalla de inicio. En Android Chrome: instalar o añadir a pantalla de inicio.

## HTML completamente autónomo

`Gran_Canaria_MAPA_REAL_SIN_INTERNET.html` contiene **también los datos del atlas** dentro del propio archivo. Puedes compartirlo y abrirlo localmente **sin internet desde la primera apertura** en un navegador que permita abrir archivos HTML. En algunos iPhone, conviene moverlo a Archivos y compartirlo con Safari; el visor de previsualización del mensajero podría no ejecutar JavaScript.

## Nota práctica

- Las coordenadas de hoteles y la mayoría de los destinos se cotejaron con mapas/datos públicos; los miradores sin nombre y ciertos paseos generales se señalan como **puntos orientativos**, no como acceso verificado.
- Autobuses, costos, distancias y tiempos son estimaciones. Google Maps y horarios de Global necesitan conexión; el mapa de la página NO.
- GitHub Pages es público: la página incluye la dirección del alojamiento y fechas del viaje.
- No distribuir Shapefiles de toda Canarias innecesariamente: el atlas optimizado ya contiene las capas necesarias del norte de Gran Canaria.
- Atribución visible en el mapa, documentación y `LICENCIA-Y-FUENTE.txt`. Datos cartográficos bajo ODbL 1.0.
