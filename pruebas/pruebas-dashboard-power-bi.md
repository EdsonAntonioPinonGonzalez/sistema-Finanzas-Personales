
# Pruebas funcionales del dashboard financiero en Power BI

### Objetivo

Verificar el funcionamiento de los indicadores y visualizaciones desarrollados en Power BI para el prototipo del Sistema de Finanzas Personales, comprobando que los resultados correspondan con los datos registrados en Excel y que los filtros funcionen correctamente.


### Entorno de pruebas

**Proyecto:** Sistema de Finanzas Personales.

**Herramienta:** Microsoft Power BI Desktop.

**Origen de datos:** Archivo Excel Sistema_Finanzas_Personales.xlsx.

**Tablas utilizadas:** Movimientos, Categorías, Presupuestos y Obligaciones.

**Tipo de pruebas:** Pruebas funcionales del prototipo.

**Fecha de ejecución:** 6 de noviembre de 2026.


### Pruebas realizadas

##### DASH-01. Filtrado por categoría

**Objetivo:** Verificar que el segmentador de categorías actualice correctamente los indicadores y visualizaciones del dashboard.

**Procedimiento:**

Abrir la página Dashboard financiero.

Seleccionar la categoría Alimentación en el segmentador.

Observar los cambios en las tarjetas, gráficos y tabla de obligaciones.

Resultado esperado: Mostrar gastos por $750, únicamente la categoría Alimentación en el gráfico de dona y su presupuesto correspondiente. Los indicadores y visualizaciones sin registros relacionados deben reflejar la ausencia de datos.

**Resultado obtenido:** El dashboard mostró gastos por $750, ingresos sin datos, saldo de -$750 y únicamente la categoría Alimentación. La tabla de obligaciones no mostró registros.

**Estado:** Exitosa.

**Evidencia:** documentacion/evidencias/prueba-dashboard-filtrado.png


##### DASH-02. Verificación de indicadores financieros

**Objetivo:** Comprobar los cálculos de ingresos totales, gastos totales y saldo disponible mediante medidas DAX.

**Procedimiento:**

Quitar los filtros del dashboard.

Revisar los importes de las tres tarjetas.

Comparar los resultados con las operaciones realizadas sobre los datos de prueba.

**Resultado esperado:**

Ingresos Totales: $9,700.

Gastos Totales: $1,700.

Saldo Disponible: $8,000.

**Resultado obtenido:** Los tres indicadores mostraron los importes esperados.

**Estado:** Exitosa.

**Evidencia:** documentacion/evidencias/prueba-dashboard-indicadores.png


##### DASH-03. Distribución de gastos por categoría

**Objetivo:** Verificar que el gráfico de dona represente correctamente los gastos agrupados por categoría.

**Procedimiento:**

Visualizar el gráfico de dona sin filtros.

Revisar los importes y porcentajes de cada categoría.

Comparar la distribución con los movimientos registrados.

**Resultado esperado:**

Alimentación: $750 (44.12 %).

Transporte: $500 (29.41 %).

Servicios: $450 (26.47 %).

Total: $1,700.

**Resultado obtenido:** El gráfico mostró correctamente las tres categorías, sus importes y porcentajes.

**Estado:** Exitosa.

**Evidencia:** documentacion/evidencias/prueba-dashboard-distribucion-gastos.png


##### DASH-04. Comparación de presupuestos

**Objetivo:** Verificar que el gráfico de barras compare correctamente los montos presupuestados y gastados por categoría.

**Procedimiento:**

Visualizar el gráfico de presupuestos sin filtros.

Colocar el cursor sobre las barras para consultar los importes exactos.

Comparar los valores mostrados con los registros de prueba.

**Resultado esperado:**

| Categoría    | Presupuestado | Gastado |
| ------------- | ------------- | ------- |
| Alimentación | $2,500        | $750    |
| Transporte    | $500          | $500    |
| Servicios     | $200          | $450    |

**Resultado obtenido:** Los seis importes coincidieron con los valores esperados. El gráfico permitió identificar las categorías con presupuesto disponible, agotado y excedido.

**Estado:** Exitosa.

**Evidencia:** documentacion/evidencias/prueba-dashboard-presupuestos.png


##### DASH-05. Seguimiento de obligaciones

**Objetivo:** Verificar que la tabla de obligaciones presente correctamente los conceptos, categorías, montos, fechas límite y estados importados desde Excel.

**Procedimiento:**

Revisar los cuatro registros mostrados en la tabla del dashboard.

Abrir la hoja Obligaciones del archivo Excel original.

Comparar los datos entre ambas herramientas.

**Resultado esperado:** Los cuatro registros deben coincidir con la información de Excel, incluyendo sus estados.

**Resultado obtenido:** Se confirmó que los conceptos, montos, fechas límite y estados de las cuatro obligaciones coincidían con Excel. Se visualizaron tres obligaciones vencidas y una pagada.

**Estado:** Exitosa.

**Evidencia:** documentacion/evidencias/prueba-dashboard-obligaciones.png


### Resumen de resultados

|   ID   | Prueba                       | Estado     |
| :-----: | ---------------------------- | ---------- |
| DASH-01 | Filtrado por categoría      | ✅ Exitosa |
| DASH-02 | Indicadores financieros      | ✅ Exitosa |
| DASH-03 | Distribución de gastos      | ✅ Exitosa |
| DASH-04 | Comparación de presupuestos | ✅ Exitosa |
| DASH-05 | Seguimiento de obligaciones  | ✅ Exitosa |

Total: 5 pruebas realizadas, 5 exitosas y 0 fallidas.


### Conclusión

Las pruebas realizadas permitieron comprobar que los indicadores y visualizaciones del dashboard financiero funcionan correctamente con los datos de prueba utilizados. Los cálculos de ingresos, gastos y saldo disponible coincidieron con los resultados esperados, mientras que los gráficos mostraron adecuadamente la distribución de gastos y la comparación de presupuestos.

También se verificó que el segmentador actualiza las visualizaciones según la categoría seleccionada y que la información de obligaciones coincide con los registros de Excel.

Por lo tanto, se considera que el dashboard cumple con las funcionalidades evaluadas en esta etapa del prototipo. Estos resultados no representan una validación completa del sistema terminado, ya que todavía quedan actividades de integración y pruebas posteriores.
