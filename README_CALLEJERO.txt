MI ESCAPADA POR GRAN CANARIA · CALLEJERO REAL SIN CONEXIÓN
=========================================================

¿QUÉ INCLUYE?
- 22 planes, fichas, precios orientativos, distancias, autobuses, precauciones y favoritos.
- Mapa geográfico y marcadores con posición del hotel destacada.
- Callejero REAL: calles, carreteras, senderos y nombres de vías de OpenStreetMap.
- Zoom, desplazamiento con dedo/ratón, detalle de cada destino.
- La web funciona sin datos móviles después de una primera visita con internet.

POR QUÉ ESTA VERSIÓN NECESITA GENERARSE EN GITHUB
El archivo roads.js dentro del ZIP es un marcador vacío hasta que GitHub Actions
obtiene las calles auténticas a partir del extracto oficial de Geofabrik.
No se inventan calles, ni se copian ilegalmente los mosaicos de Google Maps.
La compilación ocurre UNA VEZ al publicar y la web aloja el callejero en su
mismo dominio: no solicita mapas externos al consultarse en móvil.

PUBLICACIÓN EN GITHUB
1) Crea un repositorio público en GitHub, p.ej. `gran-canaria-planes`.
2) Ve a Settings → Pages → Build and deployment → Source: GitHub Actions.
3) Sube el contenido extraído del ZIP conservando la carpeta oculta
   `.github/workflows/deploy.yml` tal cual y el archivo `build_roads.py`.
   Recomendado: GitHub Desktop (arrastrar carpeta al repositorio y hacer Push)
   o por terminal:
      git init
      git add .
      git commit -m "Mapa de Gran Canaria offline"
      git branch -M main
      git remote add origin https://github.com/TU_USUARIO/gran-canaria-planes.git
      git push -u origin main
   En la web de GitHub: si la subida no conserva la carpeta `.github`, crea
   el archivo `.github/workflows/deploy.yml` con la opción Add file → Create new file.
4) En Actions revisa el flujo “Publicar mapa offline de Gran Canaria”.
   Debe terminar en verde. Si se publicó antes de habilitar Pages,
   pulsa Run workflow para ejecutarlo otra vez.
5) El enlace será https://TU_USUARIO.github.io/gran-canaria-planes/.
6) Abre el enlace UNA VEZ con internet y deja que se cargue completamente.
   Comprueba que aparece "✓ Callejero real de OpenStreetMap" en verde.
   En iPhone/iPad: Safari → Compartir → Añadir a pantalla de inicio.
   Desde ese momento, la app puede reabrirse SIN DATOS (almacenamiento del sitio).

IMPORTANTE
- Al abrir index.html directamente antes del proceso de Actions, solo se
  muestra el mapa geográfico básico (sin calles): roads.js aún está vacío.
- El mapa offline incluye carreteras y senderos pero NO calcula rutas ni hace
  navegación GPS paso a paso. Google Maps e información de horarios actualizada
  sí requieren conexión a Internet.
- El servicio offline depende de que el navegador conserve los datos del sitio.
  No borres los datos de Safari/Chrome si vas a usarla durante el viaje.
- Si el sitio es público, las fechas y dirección de alojamiento también lo son.
  Evita compartir el enlace públicamente si te preocupa la privacidad.
- Se trata de un visor de mapas, no de información de seguridad de senderos.

CARTOGRAFÍA Y ATRIBUCIÓN
Fuente: © OpenStreetMap contributors (ODbL)
https://www.openstreetmap.org/copyright
Extracto: Geofabrik, https://download.geofabrik.de/africa/canary-islands.html
La base de datos derivada roads.js se distribuye de acuerdo con la licencia ODbL.
