
# Pruebas de Power Query

## 1. Objetivo

Verificar el funcionamiento de las transformaciones de importación, validación y limpieza de datos implementadas mediante Power Query en el prototipo del Sistema de Finanzas Personales.

## 2. Entorno de pruebas

- Herramienta: Microsoft Excel y Power Query.
- Archivo: `Sistema_Finanzas_Personales.xlsx`.
- Consulta evaluada: `pq_Movimientos`.
- Tipo de pruebas: Funcionales.
- Datos utilizados: Registros ficticios y temporales.

Las pruebas se realizaron sobre el prototipo desarrollado en Excel y no representan una validación del sistema final.

## 3. Pruebas realizadas

### PQ-01. Filtrado de registros vacíos

**Objetivo:** Comprobar que Power Query excluya los registros cuyo identificador sea nulo.

**Procedimiento:**
1. Se abrió la consulta `pq_Movimientos`.
2. Se revisó el filtro aplicado sobre la columna ID.
3. Se verificó que únicamente aparecieran los registros con identificador.

**Resultado esperado:** Mostrar los cinco movimientos registrados, excluyendo las filas sin identificador.

**Resultado obtenido:** Se visualizaron los cinco movimientos originales, de MOV001 a MOV005, sin registros con ID nulo.

**Estado:** Exitosa.

**Evidencia:** `documentacion/evidencias/prueba-pq-filtrado.png`

### PQ-02. Limpieza de textos

**Objetivo:** Comprobar que la transformación Trim elimine espacios innecesarios al inicio y al final de los textos.

**Procedimiento:**
1. Se modificó temporalmente el concepto del movimiento MOV005, agregando espacios antes y después del texto.
2. Se guardaron los cambios y se actualizaron las consultas.
3. Se revisó el resultado en Power Query.

**Resultado esperado:** Mostrar el concepto "Pago de internet" sin espacios adicionales.

**Resultado obtenido:** Power Query mostró el concepto sin los espacios agregados, aplicando las transformaciones de limpieza configuradas.

**Estado:** Exitosa.

**Evidencias:**
- `documentacion/evidencias/prueba-pq-trim-antes.png`
- `documentacion/evidencias/prueba-pq-trim-despues.png`

### PQ-03. Eliminación de registros duplicados

**Objetivo:** Verificar que Power Query elimine registros con identificadores repetidos.

**Procedimiento:**
1. Se duplicó temporalmente el movimiento MOV005 en la tabla original.
2. Se comprobó que Excel contenía seis movimientos, de los cuales dos tenían el mismo ID.
3. Se actualizaron las consultas.
4. Se revisó el paso Removed Duplicates en Power Query.

**Resultado esperado:** Conservar cinco registros con identificadores únicos.

**Resultado obtenido:** Power Query mostró cinco movimientos, conservando un solo registro con ID MOV005.

**Estado:** Exitosa.

**Evidencias:**
- `documentacion/evidencias/prueba-pq-duplicados-antes.png`
- `documentacion/evidencias/prueba-pq-duplicados-despues.png`

### PQ-04. Actualización de datos

**Objetivo:** Comprobar que Power Query incorpore nuevos registros mediante la actualización de consultas.

**Procedimiento:**
1. Se agregó temporalmente el movimiento MOV006 con un gasto de $150 en la categoría Alimentación.
2. Se guardaron los cambios en Excel.
3. Se ejecutó la opción Refresh All.
4. Se revisaron los registros de la consulta `pq_Movimientos`.

**Resultado esperado:** Incorporar el movimiento MOV006 y mostrar seis registros.

**Resultado obtenido:** Power Query incorporó correctamente MOV006, mostrando seis movimientos con los datos correspondientes.

**Estado:** Exitosa.

**Evidencias:**
- `documentacion/evidencias/prueba-pq-actualizacion-antes.png`
- `documentacion/evidencias/prueba-pq-actualizacion-despues.png`

## 4. Resumen de resultados

| Prueba | Resultado |
|---|---|
| PQ-01. Filtrado de registros vacíos | Exitosa |
| PQ-02. Limpieza de textos | Exitosa |
| PQ-03. Eliminación de duplicados | Exitosa |
| PQ-04. Actualización de datos | Exitosa |

**Total de pruebas realizadas:** 4  
**Pruebas exitosas:** 4  
**Pruebas fallidas:** 0

## 5. Restauración de los datos

Al finalizar las pruebas se eliminaron los registros temporales y se restauraron los valores originales de la tabla Movimientos.

Posteriormente, se actualizaron las consultas para comprobar que el prototipo conservara los cinco movimientos iniciales.

## 6. Conclusión

Las cuatro pruebas realizadas fueron exitosas y permitieron comprobar el funcionamiento de las transformaciones evaluadas en Power Query.

Se verificó el filtrado de registros con identificadores nulos, la limpieza de espacios adicionales, la eliminación de identificadores duplicados y la incorporación de nuevos movimientos mediante la actualización de consultas.

Estos resultados respaldan el avance de la Actividad 9 y permiten continuar con las siguientes etapas del proyecto. Las pruebas realizadas se limitaron a las funcionalidades y datos evaluados en el prototipo.
