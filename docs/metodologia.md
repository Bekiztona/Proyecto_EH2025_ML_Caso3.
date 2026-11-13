# Metodología y cautelas

## Universo analítico
El módulo de discriminación registra una persona seleccionada por hogar mediante tabla Kish para la sección de discriminación y seguridad. La EH2025 tiene cobertura nacional urbana y rural, pero las desagregaciones deben respetar el diseño muestral y los errores de muestreo.

## Unión de módulos
Se vinculan `EH2025_Discriminacion.sav` y `EH2025_Persona.sav` con `folio` + `nro`, mediante DuckDB. Se verifica que el JOIN no multiplique ni elimine filas.

## Variables objetivo
- Discriminación: al menos un sí en `s09a_01a`–`s09a_01l`; negativo si todas las respuestas están clasificadas como 1/2 y no existe positivo.
- Victimización provisional: SAV etiqueta códigos 1–7 como delitos y 8 como “Ninguno”. La documentación PDF revisada no coincide con estas etiquetas. La variable se considera provisional hasta validación con INE.

## Diseño muestral
Se utiliza `ponderador` para indicadores departamentales descriptivos. Los modelos predictivos y sus intervalos/valores p son exploratorios y no incorporan completamente estratos, UPM y ponderación de diseño. No presentar sus errores estándar como inferencia oficial.

## Clustering
K-Means se aplica a nueve observaciones departamentales con dos indicadores ponderados: inseguridad percibida (muy inseguro + inseguro) y victimización. Se estandarizan ambas variables y se comparan k=2,3,4 con Silhouette. El resultado es exploratorio.

## Reproducibilidad
Semilla aleatoria: 42. Ejecutar notebook en orden. Dependencias en `requirements.txt`.
