
# Actividad 9. Importación, validación y limpieza de datos con Power Query

## Objetivo

Importar y preparar los datos del prototipo del Sistema de Finanzas Personales mediante Power Query, con la finalidad de mejorar su organización y facilitar su posterior análisis.

## Herramienta utilizada

Se utilizó Microsoft Excel con Power Query para realizar la importación, revisión y limpieza de los datos registrados en el prototipo.

## Tablas procesadas

Se crearon cuatro consultas:

- `pq_Movimientos`
- `pq_Categorias`
- `pq_Presupuestos`
- `pq_Obligaciones`

## Procedimiento realizado

1. Se importaron las tablas de Excel a Power Query.
2. Se configuraron los tipos de datos correspondientes a cada columna.
3. Se filtraron los registros sin identificador para excluir las filas vacías.
4. Se aplicó la eliminación de identificadores duplicados.
5. Se utilizaron las herramientas Trim y Clean para limpiar los campos de texto.
6. Se revisaron los datos de fechas, montos y estados.
7. Se guardaron las consultas como conexiones dentro del archivo Excel.
8. Se ejecutó Refresh All para comprobar su actualización.

## Resultados

Se configuraron correctamente las cuatro consultas y se realizó una prueba de actualización sin errores reportados.

Las tablas originales se conservaron sin modificaciones y las filas vacías preparadas para futuros registros fueron excluidas de las consultas mediante filtros.

## Pruebas realizadas

Para comprobar el funcionamiento de las transformaciones configuradas en Power Query, se realizaron cuatro pruebas funcionales sobre la consulta `pq_Movimientos`.

1. **PQ-01. Filtrado de registros vacíos:** Se comprobó que los registros con identificador nulo fueran excluidos de la consulta.
2. **PQ-02. Limpieza de textos:** Se verificó que la transformación Trim eliminara los espacios adicionales de un concepto.
3. **PQ-03. Eliminación de duplicados:** Se agregó temporalmente un movimiento con identificador repetido y se comprobó que Power Query conservara cinco registros únicos.
4. **PQ-04. Actualización de datos:** Se agregó un nuevo movimiento y se verificó que apareciera en la consulta después de ejecutar Refresh All.

Las cuatro pruebas fueron exitosas. Al finalizar, se restauraron los datos originales del prototipo y se actualizaron nuevamente las consultas.

Los procedimientos, resultados y evidencias se documentaron en `pruebas/pruebas-power-query.md`.

## Evidencia

La captura de las consultas se encuentra en:

`documentacion/evidencias/power-query-consultas.png`

## Conclusión

El uso de Power Query permitió preparar y organizar los datos del prototipo de manera más eficiente. Las transformaciones quedaron guardadas para facilitar futuras actualizaciones y servirán como base para continuar con el análisis de información financiera.
