# Proyecto_EH2025_ML_Caso3
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![INE](https://img.shields.io/badge/Fuente-INE%20Bolivia-green)](https://anda.ine.gob.bo/index.php/catalog/256)
[![Uso](https://img.shields.io/badge/Uso-académico-orange)](#ética-y-privacidad)

**Caso 3: Análisis de la discriminación y la seguridad ciudadana en Bolivia.**

Pregunta: ¿Qué factores sociodemográficos y geográficos están asociados con una mayor percepción de discriminación y victimización en Bolivia?

## Fuente y citación
Fuente: Instituto Nacional de Estadística, Encuesta de Hogares 2025 (EH2025), catálogo ANDA:
http://anda.ine.gob.bo/index.php/catalog/256

Citación obligatoria para el informe y el repositorio:
> Fuente: Instituto Nacional de Estadística, Encuesta de Hogares 2025 - http://anda.ine.gob.bo/index.php/catalog/256. Fecha de acceso: **12/11/2026 (verificar y sustituir por la fecha real de descarga, si corresponde).**

La EH2025 es una encuesta por muestreo nacional, con cobertura urbana y rural de los nueve departamentos. Consultar la documentación oficial sobre diseño muestral, factores de expansión y niveles de desagregación antes de producir estimaciones oficiales.

## Estructura
```text
Proyecto_EH2025_ML_Caso3/
├── data/                  # No publicar microdatos originales
│   ├── raw/               # Colocar aquí los .sav descargados
│   └── processed/
├── notebooks/             # Notebook reproducible
├── src/                   # Funciones modulares
├── outputs/               # Reportes EDA, figuras, dashboard y modelos
├── docs/                  # Informe ejecutivo PDF y recursos visuales
├── .gitignore
├── requirements.txt
└── README.md
```

## Datos requeridos
Colocar localmente (no subir a GitHub):
- `data/raw/EH2025_Discriminacion.sav`
- `data/raw/EH2025_Persona.sav`

Los datos se descargan desde ANDA-INE. Este repositorio no distribuye microdatos.

## Ejecución
1. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copiar los dos archivos SAV a `data/raw/`.
3. Abrir `notebooks/01_analisis_completo_caso3.ipynb` en Jupyter o Google Colab y ejecutar las celdas en orden.
4. Los reportes y visualizaciones se guardan en `outputs/`.

## Componentes implementados en el notebook
- Lectura de SPSS/SAV con `pyreadstat`.
- Cruce `folio` + `nro` mediante DuckDB.
- Perfil exploratorio HTML con YData-Profiling (Sweetviz como alternativa).
- Variables binarias de discriminación y victimización.
- Cuatro visualizaciones interactivas Plotly y mapa Folium (el mapa requiere GeoJSON compatible).
- Validación cruzada estratificada y comparación de Random Forest, ExtraTrees y XGBoost opcional.
- Importancia por permutación y SHAP opcional.
- K-Means departamental exploratorio con indicadores ponderados.

## Resultados preliminares documentados
Los resultados ya observados en la sesión de análisis:
- Discriminación: 1.825 positivos (14,77%), 10.130 negativos clasificables (81,97%) y 403 no clasificados (3,26%).
- Victimización según etiquetas de valores recuperadas del SAV: 1.638 positivos (13,25%) y 10.720 negativos (86,75%).
- Clustering departamental: dos grupos, Silhouette 0,3589.
- Cluster 0: Beni, Cochabamba, La Paz, Pando y Santa Cruz.
- Cluster 1: Chuquisaca, Oruro, Potosí y Tarija.

**Advertencia crítica:** el catálogo PDF consultado presenta una codificación de `s09b_02a`/`s09b_02b` diferente de las etiquetas de valores leídas desde el SAV. Este proyecto deja constancia de la discrepancia y utiliza provisionalmente las etiquetas del SAV (código 8 = “Ninguno”; códigos 1–7 = categorías de hechos delictivos). Confirmar con INE antes de presentar esta variable como definitiva.

## Ética y privacidad
- No intentar reidentificar personas u hogares.
- No publicar microdatos crudos ni datos individuales procesados.
- No subir credenciales, tokens, claves API ni archivos pesados.
- Publicar únicamente código, documentación y resultados agregados compatibles con las condiciones de uso.
- Los resultados observacionales no implican causalidad.
- Los modelos de esta versión son exploratorios: los errores estándar y la validación ML no incorporan plenamente el diseño complejo de la encuesta.

## Dependencias y reproducibilidad
Ver `requirements.txt`. Para obtener resultados reproducibles, conservar semillas aleatorias y documentar las versiones instaladas.
