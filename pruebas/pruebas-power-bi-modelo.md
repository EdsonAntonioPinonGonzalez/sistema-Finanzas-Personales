# Pruebas del modelo de datos en Power BI

## 1. Objetivo

Verificar el funcionamiento del modelo de datos desarrollado en Power BI para el prototipo del Sistema de Finanzas Personales, comprobando la configuración de las relaciones entre tablas y el filtrado de la información financiera por categoría.

## 2. Entorno de pruebas

- Herramienta: Microsoft Power BI Desktop.
- Archivo: `Sistema_Finanzas_Personales.pbix`.
- Fuente de datos: `Sistema_Finanzas_Personales.xlsx`.
- Tablas evaluadas: Categorías, Movimientos, Presupuestos y Obligaciones.
- Tipo de pruebas: Funcionales y de integración de datos.
- Datos utilizados: Registros ficticios del prototipo en Excel.

Las pruebas se realizaron sobre el modelo de datos desarrollado en Power BI y no representan una validación del sistema final.

## 3. Pruebas realizadas

### PBI-01. Verificación de relaciones

**Objetivo:** Comprobar que las relaciones del modelo estén configuradas correctamente.

**Procedimiento:**

1. Se abrió la vista Model view de Power BI.
2. Se revisaron las relaciones entre Categorías y las tablas Movimientos, Presupuestos y Obligaciones.
3. Se comprobó que las tres relaciones estuvieran activas.
4. Se verificó que la cardinalidad fuera de uno a muchos (1:*) y la dirección de filtrado fuera única (Single).

**Resultado esperado:** Contar con tres relaciones activas de uno a muchos, utilizando la tabla Categorías como referencia.

**Resultado obtenido:** Se configuraron correctamente las tres relaciones entre Categorías y las demás tablas del modelo.

**Estado:** Exitosa.

**Evidencia:** `documentacion/evidencias/prueba-pbi-relaciones.png`

### PBI-02. Filtrado de movimientos por categoría

**Objetivo:** Verificar que la relación entre Categorías y Movimientos permita filtrar correctamente los registros financieros.

**Procedimiento:**

1. Se creó una página llamada "Pruebas del modelo".
2. Se agregó un segmentador (Slicer) utilizando el campo Nombre de la tabla Categorías.
3. Se creó una tabla visual con los campos ID, Categoría, Concepto y Monto de Movimientos.
4. Se seleccionó la categoría Alimentación.

**Resultado esperado:** Mostrar únicamente los movimientos correspondientes a Alimentación.

**Resultado obtenido:** Power BI mostró únicamente el movimiento MOV002, correspondiente a una compra de supermercado por $750.

**Estado:** Exitosa.

**Evidencia:** `documentacion/evidencias/prueba-pbi-filtrado.png`

### PBI-03. Filtrado de presupuestos por categoría

**Objetivo:** Comprobar que la relación entre Categorías y Presupuestos permita visualizar los presupuestos correspondientes a la categoría seleccionada.

**Procedimiento:**

1. Se agregó una tabla visual con los campos Categoría, Monto presupuestado, Monto gastado, Disponible y Estado.
2. Se seleccionó Alimentación en el segmentador.
3. Se revisaron los importes y el periodo del presupuesto.
4. Se identificó que inicialmente el presupuesto correspondía a noviembre de 2026, mientras que el movimiento registrado era de octubre.
5. Se ajustó el periodo del presupuesto en Excel a octubre de 2026 y se actualizaron los datos en Power BI.

**Resultado esperado:** Mostrar el presupuesto de Alimentación correspondiente a octubre de 2026, con los importes coincidentes con Excel.

**Resultado obtenido:** Se visualizó un presupuesto de $2,500, un gasto de $750 y un disponible de $1,750, con estado Disponible.

**Estado:** Exitosa.

**Evidencia:** `documentacion/evidencias/prueba-pbi-presupuestos.png`

### PBI-04. Filtrado de obligaciones por categoría

**Objetivo:** Verificar que la relación entre Categorías y Obligaciones permita mostrar únicamente las obligaciones correspondientes a la categoría seleccionada.

**Procedimiento:**

1. Se agregó una tabla visual con los campos ID Obligación, Concepto, Categoría, Monto y Estado.
2. Se seleccionó la categoría Servicios en el segmentador.
3. Se revisaron los registros mostrados.

**Resultado esperado:** Mostrar únicamente las obligaciones registradas en la categoría Servicios.

**Resultado obtenido:** Se mostraron las obligaciones OBL001 (Pago de internet, $450, Pagado) y OBL004 (Pago de electricidad, $680, Vencido).

**Estado:** Exitosa.

**Evidencia:** `documentacion/evidencias/prueba-pbi-obligaciones.png`

## 4. Resumen de resultados

| Prueba                              | Resultado |
| ----------------------------------- | --------- |
| PBI-01. Verificación de relaciones | Exitosa   |
| PBI-02. Filtrado de movimientos     | Exitosa   |
| PBI-03. Filtrado de presupuestos    | Exitosa   |
| PBI-04. Filtrado de obligaciones    | Exitosa   |

**Total de pruebas realizadas:** 4
**Pruebas exitosas:** 4
**Pruebas fallidas:** 0

## 5. Observaciones

Durante las pruebas se identificó una diferencia entre el periodo del presupuesto de Alimentación y la fecha del movimiento registrado.

Se comprobó que el presupuesto correspondía inicialmente a noviembre de 2026, mientras que el gasto se había realizado en octubre. Después de ajustar el periodo en Excel y actualizar Power BI, los importes coincidieron correctamente.

Esta situación permitió comprobar la importancia de mantener consistentes los periodos de los registros financieros.

## 6. Conclusión

Las cuatro pruebas realizadas fueron exitosas y permitieron comprobar el funcionamiento de las relaciones configuradas en el modelo de datos de Power BI.

Se verificó que la tabla Categorías permite filtrar correctamente los movimientos, presupuestos y obligaciones, mostrando únicamente los registros correspondientes a cada categoría seleccionada.

Los resultados obtenidos respaldan el desarrollo de la Actividad 10 y permiten continuar con la creación de indicadores y visualizaciones financieras en Power BI.
