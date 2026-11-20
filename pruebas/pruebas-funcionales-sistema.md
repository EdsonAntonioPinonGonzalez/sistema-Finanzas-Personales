
# Pruebas funcionales del Sistema de Finanzas Personales

## 1. Objetivo

Verificar el funcionamiento de los componentes del Sistema de Finanzas Personales mediante pruebas funcionales que permitan comprobar el registro, validación, procesamiento y visualización de la información financiera.

Las pruebas se realizaron utilizando Microsoft Excel, Power Query, Python y Power BI, con el propósito de identificar posibles errores y comprobar la consistencia de los datos.

## 2. Alcance

Las pruebas comprenden las siguientes funcionalidades:

- Registro y almacenamiento de movimientos financieros.
- Validación de datos ingresados.
- Cálculo y actualización de presupuestos.
- Seguimiento de obligaciones financieras.
- Transformación de datos mediante Power Query.
- Procesamiento de información con Python.
- Visualización y filtrado de datos en Power BI.
- Consistencia de resultados entre los componentes.

## 3. Casos de prueba

### PF-01. Registro de movimientos financieros

**Objetivo:** Verificar que Excel permita registrar y conservar nuevos movimientos.

**Procedimiento:** Se agregó temporalmente el movimiento MOV006 con un gasto de $100 en la categoría Alimentación. Posteriormente, se guardó y volvió a abrir el archivo.

**Resultado esperado:** El movimiento permanece registrado después de guardar y abrir nuevamente el archivo.

**Resultado obtenido:** El registro se conservó correctamente.

**Estado:** Aprobada.

**Evidencia:** `documentacion/evidencias/prueba-funcional-pf01.png`

### PF-02. Validación de datos

**Objetivo:** Comprobar que el sistema impida registrar valores no válidos.

**Procedimiento:** Se intentó introducir un monto negativo y un tipo de movimiento no permitido.

**Resultado esperado:** Excel rechaza los valores incorrectos mediante sus reglas de validación.

**Resultado obtenido:** El sistema mostró mensajes de validación y rechazó los datos incorrectos.

**Estado:** Aprobada.

**Evidencias:**
- `documentacion/evidencias/prueba-funcional-pf02-monto.png`
- `documentacion/evidencias/prueba-funcional-pf02-tipo.png`

### PF-03. Actualización de presupuestos

**Objetivo:** Verificar que los presupuestos se actualicen al modificar los movimientos financieros.

**Procedimiento:** Se cambió temporalmente la fecha de MOV006 a octubre de 2026, incorporando su gasto de $100 al presupuesto de Alimentación.

**Resultado esperado:** El monto gastado aumenta de $750 a $850 y el disponible disminuye de $1,750 a $1,650.

**Resultado obtenido:** Los valores se actualizaron correctamente. Después se eliminó el movimiento temporal.

**Estado:** Aprobada.

**Evidencias:**
- `documentacion/evidencias/prueba-funcional-pf03-presupuestos.png`
- `documentacion/evidencias/prueba-funcional-pf03-actualizacion.png`

### PF-04. Seguimiento de obligaciones financieras

**Objetivo:** Comprobar la actualización del estado de las obligaciones.

**Procedimiento:** Se agregó temporalmente una fecha de pago a la obligación correspondiente a Netflix.

**Resultado esperado:** El estado cambia de Vencido a Pagado.

**Resultado obtenido:** El estado se actualizó correctamente. Posteriormente, se eliminó la fecha de pago utilizada para la prueba.

**Estado:** Aprobada.

**Evidencias:**
- `documentacion/evidencias/prueba-funcional-pf04-obligaciones.png`
- `documentacion/evidencias/prueba-funcional-pf04-actualizacion.png`

### PF-05. Procesamiento con Power Query

**Objetivo:** Comprobar que Power Query importe y transforme correctamente los datos del archivo Excel.

**Procedimiento:** Se actualizaron las consultas de Movimientos, Categorías, Presupuestos y Obligaciones.

**Resultado esperado:** Las consultas se actualizan sin errores y conservan la estructura esperada.

**Resultado obtenido:** Las cuatro consultas se actualizaron correctamente.

**Estado:** Aprobada.

**Evidencia:** `documentacion/evidencias/prueba-funcional-pf05-power-query.png`

### PF-06. Procesamiento con Python y actualización de Power BI

**Objetivo:** Verificar que Python procese los registros financieros y que Power BI muestre los resultados esperados.

**Procedimiento:** Se ejecutó el archivo `analisis_financiero.py` y se actualizó el dashboard de Power BI.

**Resultado esperado:**
- Ingresos: $9,700.
- Gastos: $1,700.
- Saldo: $8,000.
- Total de movimientos: 5.

**Resultado obtenido:** Python generó correctamente el resumen financiero y Power BI presentó los mismos indicadores.

**Estado:** Aprobada.

**Evidencias:**
- `documentacion/evidencias/prueba-funcional-pf06-python.png`
- `documentacion/evidencias/prueba-funcional-pf06-power-bi.png`

### PF-07. Filtros y visualizaciones de Power BI

**Objetivo:** Verificar que las visualizaciones respondan correctamente a los filtros por categoría.

**Procedimiento:** Se seleccionaron las categorías Alimentación y Transporte en el filtro del dashboard.

**Resultado esperado:** Las visualizaciones muestran únicamente la información correspondiente a la categoría seleccionada.

**Resultado obtenido:**
- Alimentación mostró gastos por $750.
- Transporte mostró gastos por $500.
- Las gráficas y los presupuestos respondieron correctamente.

**Estado:** Aprobada.

**Evidencias:**
- `documentacion/evidencias/prueba-funcional-pf07-alimentacion.png`
- `documentacion/evidencias/prueba-funcional-pf07-transporte.png`

### PF-08. Consistencia de información entre componentes

**Objetivo:** Comprobar que Excel, Python y Power BI utilicen información financiera consistente.

**Procedimiento:** Se verificaron los cinco movimientos originales en Excel y se compararon los resultados obtenidos en Python y Power BI.

**Resultado esperado:**
- Ingresos: $9,700.
- Gastos: $1,700.
- Saldo: $8,000.
- Alimentación: $750.
- Transporte: $500.
- Servicios: $450.

**Resultado obtenido:** Los resultados coincidieron entre los componentes evaluados.

**Estado:** Aprobada.

**Evidencia:** `documentacion/evidencias/prueba-funcional-pf08-consistencia.png`

## 4. Limitaciones técnicas identificadas

Durante las pruebas se identificó una limitación de portabilidad en Power BI Desktop, debido a que las rutas de los archivos locales pueden cambiar al descargar el repositorio en otra computadora.

Para reducir este inconveniente se implementó el parámetro `RutaExcel`, utilizado por las cuatro consultas de Power Query en Power BI.

Como solución provisional, cada usuario deberá establecer la ubicación de su archivo Excel en el parámetro al utilizar el proyecto desde una computadora diferente.

También se desarrolló el script `iniciar-sistema.ps1`, que identifica automáticamente la carpeta del repositorio y verifica la existencia de los archivos Excel y Power BI. Sin embargo, este script no modifica las conexiones internas del archivo `.pbix`.

La automatización completa de las rutas queda propuesta como una mejora futura.

## 5. Resultados generales

Se ejecutaron ocho casos de prueba funcional, todos con resultados satisfactorios.

Las pruebas permitieron verificar el registro y la validación de movimientos, la actualización de presupuestos y obligaciones, el procesamiento de datos y la generación de visualizaciones.

También se comprobó la consistencia de los indicadores financieros entre Excel, Python y Power BI.

## 6. Conclusiones

Los resultados obtenidos permiten concluir que las funcionalidades evaluadas del Sistema de Finanzas Personales cumplen con los comportamientos esperados para esta etapa del desarrollo.

Las pruebas confirmaron la correcta integración de los componentes y permitieron identificar una limitación de portabilidad que fue documentada junto con una solución provisional.

Como siguiente etapa se recomienda continuar con la revisión del sistema, atender las mejoras identificadas y mantener actualizada la documentación técnica.
