# Seguimiento de actividades

Este documento tiene como finalidad registrar el avance de las actividades correspondientes a la construcción del Sistema de Finanzas Personales. El seguimiento se realizará de acuerdo con la planeación establecida previamente y se actualizará conforme avance el desarrollo del proyecto.

## Estados

- ⬜ Pendiente
- 🟡 En proceso
- ✅ Terminada

## Seguimiento general

| #  | Actividad                                                       | Fecha de inicio | Fecha de término | Responsable       | Estado       |
| -- | --------------------------------------------------------------- | --------------- | ----------------- | ----------------- | ------------ |
| 1  | Revisar el documento de requisitos y las funciones principales  | 20 sep. 2026    | 22 sep. 2026      | Ana Laura y Edson | ✅ Terminada |
| 2  | Definir el alcance y organizar el plan de trabajo               | 23 sep. 2026    | 26 sep. 2026      | Ana Laura y Edson | ✅ Terminada |
| 3  | Diseñar la estructura general del archivo de Excel             | 27 sep. 2026    | 3 oct. 2026       | Ana Laura         | ✅ Terminada |
| 4  | Crear el catálogo de categorías financieras                   | 27 sep. 2026    | 2 oct. 2026       | Edson             | ✅ Terminada |
| 5  | Desarrollar el registro de ingresos y gastos                    | 4 oct. 2026     | 10 oct. 2026      | Ana Laura y Edson | ✅ Terminada |
| 6  | Desarrollar la sección de presupuestos                         | 11 oct. 2026    | 17 oct. 2026      | Ana Laura         | ✅ Terminada |
| 7  | Desarrollar la sección de obligaciones y pagos                 | 11 oct. 2026    | 17 oct. 2026      | Edson             | ✅ Terminada |
| 8  | Capturar datos de prueba y revisar la estructura                | 18 oct. 2026    | 21 oct. 2026      | Ana Laura y Edson | ✅ Terminada |
| 9  | Configurar importación, validación y limpieza con Power Query | 22 oct. 2026    | 28 oct. 2026      | Edson             | ✅ Terminada |
| 10 | Crear el modelo de datos y relaciones en Power BI               | 29 oct. 2026    | 4 nov. 2026       | Ana Laura         | ✅ Terminada |
| 11 | Crear indicadores, gráficas y dashboard en Power BI            | 5 nov. 2026     | 11 nov. 2026      | Ana Laura         | ⬜ Pendiente |
| 12 | Desarrollar análisis complementario con Python/Pandas          | 5 nov. 2026     | 11 nov. 2026      | Edson             | ⬜ Pendiente |
| 13 | Integrar los componentes desarrollados                          | 12 nov. 2026    | 14 nov. 2026      | Ana Laura y Edson | ⬜ Pendiente |
| 14 | Realizar pruebas funcionales                                    | 15 nov. 2026    | 18 nov. 2026      | Ana Laura y Edson | ⬜ Pendiente |
| 15 | Elaborar manual y recopilar evidencias                          | 15 nov. 2026    | 21 nov. 2026      | Ana Laura         | ⬜ Pendiente |
| 16 | Corregir errores encontrados durante las pruebas                | 19 nov. 2026    | 21 nov. 2026      | Ana Laura y Edson | ⬜ Pendiente |
| 17 | Realizar revisión final, respaldo y preparación de la entrega | 22 nov. 2026    | 23 nov. 2026      | Ana Laura y Edson | ⬜ Pendiente |

## Registro de avances

### Actividad 1. Revisión de requisitos y funciones principales

**Estado:** ✅ Terminada
**Periodo:** 20 al 22 de septiembre de 2026
**Responsables:** Ana Laura y Edson

Se revisó el documento de requerimientos del Sistema de Finanzas Personales con el propósito de verificar las funciones principales que deberán desarrollarse. Se identificaron los requerimientos relacionados con movimientos financieros, categorías, presupuestos, obligaciones, consultas, procesamiento de datos, indicadores y almacenamiento de información.

La revisión realizada fue documentada y publicada en el repositorio del proyecto.

---

### Actividad 2. Definición del alcance y organización del plan de trabajo

**Estado:** ✅ Terminada
**Periodo:** 23 al 26 de septiembre de 2026
**Responsables:** Ana Laura y Edson

Se definió el alcance de la primera versión del Sistema de Finanzas Personales, estableciendo las funciones que se desarrollarán y los límites del proyecto. También se determinaron los principales entregables correspondientes a Excel, Power Query, Power BI y Python/Pandas, de acuerdo con las etapas previstas para la construcción del sistema.

Además, se distribuyeron las responsabilidades entre los integrantes del equipo y se definió la estructura de carpetas y archivos que se utilizará en el repositorio de GitHub. Con esto se estableció una organización clara para continuar con las siguientes actividades de construcción y mantener un seguimiento ordenado de los avances del proyecto.

---

### Actividad 3. Diseño de la estructura general del archivo de Excel

**Estado:** ✅ Terminada
**Periodo:** 27 de septiembre al 3 de octubre de 2026
**Responsable:** Ana Laura

Se diseñó la estructura general del archivo principal del Sistema de Finanzas Personales en Excel. Se crearon las hojas Inicio, Movimientos, Categorías, Presupuestos, Obligaciones y Resumen, de acuerdo con los principales módulos definidos para el sistema.

Se establecieron las columnas necesarias para el registro y organización de la información de cada módulo. Asimismo, se preparó la hoja Resumen con los principales indicadores y espacios de análisis que serán desarrollados en etapas posteriores.

Como resultado de esta actividad se obtuvo la estructura base del archivo `Sistema_Finanzas_Personales.xlsx`, sobre la cual se desarrollarán las siguientes funciones del sistema.

---

### Actividad 4. Creación del catálogo de categorías financieras

**Estado:** ✅ Terminada
**Periodo:** 27 de septiembre al 2 de octubre de 2026
**Responsable:** Edson

Se creó el catálogo de categorías financieras dentro del archivo principal del Sistema de Finanzas Personales. Se definieron categorías para ingresos y gastos, asignando a cada una un identificador único, nombre, tipo, descripción y estado.

El catálogo incluye categorías de ingreso como sueldo, ingresos extra y ventas, así como categorías de gasto relacionadas con alimentación, transporte, vivienda, servicios, educación, salud, entretenimiento, compras personales, suscripciones, deudas y ahorro, entre otras.

Como resultado de esta actividad, la hoja `Categorías` quedó preparada para ser utilizada posteriormente en el registro y clasificación de los movimientos financieros del sistema.

---

### Actividad 5. Desarrollo del registro de ingresos y gastos

**Estado:** ✅ Terminada
**Periodo programado:** 4 al 10 de octubre de 2026
**Responsables:** Ana Laura y Edson

Se desarrolló el registro de ingresos y gastos dentro de la hoja `Movimientos` del archivo principal del Sistema de Finanzas Personales.

Se configuraron listas desplegables para seleccionar el tipo de movimiento, la categoría y el método de pago. También se establecieron validaciones para las fechas y los montos, así como el formato de moneda y la estructura de los identificadores.

Para comprobar su funcionamiento, se capturaron cinco movimientos ficticios correspondientes a ingresos y gastos. Se verificó que los datos pudieran registrarse correctamente y que los filtros permitieran consultar los movimientos según su tipo.

Como resultado, el módulo de registro de ingresos y gastos quedó preparado para utilizarse en las siguientes actividades del proyecto.

---

### Actividad 6. Desarrollo del módulo de presupuestos

**Estado:** ✅ Terminada
**Periodo programado:** 11 al 17 de octubre de 2026
**Responsable:** Ana Laura

Se desarrolló el módulo de presupuestos dentro de la hoja Presupuestos del archivo principal del Sistema de Finanzas Personales.

Se configuraron listas desplegables para seleccionar las categorías financieras y validaciones para evitar el registro de montos presupuestados incorrectos.

También se implementaron fórmulas que permiten calcular automáticamente el monto gastado por categoría y periodo, utilizando la información registrada en la hoja Movimientos. A partir de estos datos, el sistema calcula el presupuesto disponible y determina su estado como Disponible, Agotado o Excedido.

Para comprobar su funcionamiento, se registraron tres presupuestos ficticios correspondientes a octubre de 2026. Se realizaron pruebas modificando temporalmente los montos y periodos, verificando que los resultados se actualizaran correctamente.

Como resultado, el módulo de presupuestos quedó funcional y preparado para integrarse con los demás componentes del sistema.

---

### Actividad 7. Desarrollo del módulo de obligaciones y pagos

**Estado:** ✅ Terminada
**Periodo programado:** 11 al 17 de octubre de 2026
**Responsable:** Edson

Se desarrolló el módulo de obligaciones y pagos dentro de la hoja Obligaciones del archivo principal del Sistema de Finanzas Personales.

Se configuraron listas desplegables para seleccionar las categorías financieras, así como validaciones para los montos y las fechas de las obligaciones.

También se implementaron fórmulas que permiten identificar automáticamente el estado de cada obligación como Pendiente, Pagado o Vencido, considerando su fecha límite y la fecha de pago registrada.

Para comprobar su funcionamiento, se capturaron cuatro obligaciones ficticias correspondientes a servicios, suscripciones y deudas. Se realizaron pruebas registrando y eliminando temporalmente fechas de pago, verificando que los estados se actualizaran correctamente.

Además, se comprobó el funcionamiento de los filtros para consultar las obligaciones según su estado.

Como resultado, el módulo de obligaciones y pagos quedó funcional a nivel de prototipo en Excel y preparado para las siguientes etapas del desarrollo del sistema.

---

### Actividad 8. Captura de datos de prueba y revisión de la estructura

**Estado:** ✅ Terminada
**Periodo programado:** 18 al 21 de octubre de 2026
**Responsables:** Ana Laura y Edson

Se realizó una revisión del prototipo del Sistema de Finanzas Personales desarrollado en Excel, utilizando los datos ficticios registrados durante las actividades anteriores.

Se llevaron a cabo tres pruebas funcionales para comprobar la actualización de los movimientos financieros, los cálculos automáticos de los presupuestos y los estados de las obligaciones.

Las tres pruebas fueron exitosas. Se verificó que los cambios realizados en los movimientos se reflejaran en los presupuestos, que los estados de los presupuestos se actualizaran correctamente y que las obligaciones cambiaran de estado según sus fechas de pago.

Después de las pruebas, se restauraron los valores originales. También se guardaron capturas de pantalla como evidencia de los resultados obtenidos.

Los resultados se documentaron en el archivo `pruebas/pruebas-funcionales.md` y las capturas se almacenaron en `documentacion/evidencias`.

Como resultado, se comprobó el funcionamiento de las características evaluadas del prototipo en Excel, quedando preparado para continuar con la etapa de integración de Power Query.

---

### Actividad 9. Importación, validación y limpieza de datos con Power Query

**Estado:** ✅ Terminada
**Periodo programado:** 22 al 28 de octubre de 2026
**Responsable:** Edson

Se realizó la importación y preparación de los datos del prototipo del Sistema de Finanzas Personales desarrollado en Excel, utilizando la herramienta Power Query.

Se crearon cuatro consultas correspondientes a las tablas Movimientos, Categorías, Presupuestos y Obligaciones. En cada una se configuraron los tipos de datos, se filtraron los registros vacíos y se aplicaron herramientas para eliminar identificadores duplicados, espacios y caracteres innecesarios.

También se revisaron los campos de fechas, montos y estados para comprobar que la información se importara correctamente, manteniendo los datos originales del prototipo sin modificaciones.

Una vez finalizada la limpieza, las cuatro consultas se guardaron como conexiones dentro del archivo Excel. Posteriormente, se realizó una prueba mediante la opción Refresh All, comprobando que las consultas se actualizaran sin presentar errores.

El procedimiento se documentó en el archivo `documentacion/procesamiento-datos/power-query.md` y se guardó una captura de pantalla como evidencia en `documentacion/evidencias/power-query-consultas.png`.

Adicionalmente, se realizaron cuatro pruebas funcionales para verificar el funcionamiento de las transformaciones implementadas en Power Query. Estas pruebas incluyeron el filtrado de registros vacíos, la limpieza de espacios adicionales en los textos, la eliminación de identificadores duplicados y la actualización de consultas mediante Refresh All.

Las cuatro pruebas fueron exitosas. Se comprobó que Power Query excluyera los registros sin identificador, limpiara correctamente los textos, conservara registros con identificadores únicos e incorporara nuevos movimientos al actualizar las consultas.

Al finalizar, se eliminaron los registros temporales utilizados durante las pruebas y se restauraron los datos originales del prototipo.

Los procedimientos, resultados y capturas de pantalla se documentaron en el archivo `pruebas/pruebas-power-query.md`, y las evidencias se almacenaron en `documentacion/evidencias`.

Como resultado, se completó la etapa de importación, validación y limpieza de datos, dejando configuradas las consultas de Power Query para facilitar futuras actualizaciones y continuar con la preparación de la información para su análisis en Power BI.

---

### Actividad 10. Creación del modelo de datos y relaciones en Power BI

**Estado:** ✅ Terminada
**Periodo programado:** 29 de octubre al 4 de noviembre de 2026
**Responsable:** Ana Laura

Se realizó la importación de las tablas Movimientos, Categorías, Presupuestos y Obligaciones del prototipo del Sistema de Finanzas Personales desarrollado en Excel hacia Microsoft Power BI Desktop.

Se revisaron y configuraron los tipos de datos de las columnas, se excluyeron los registros vacíos y se aplicaron transformaciones de limpieza de texto y eliminación de identificadores duplicados mediante Power Query.

Posteriormente, se creó el modelo de datos utilizando la tabla Categorías como referencia principal. Se establecieron tres relaciones de uno a muchos entre Categorías y las tablas Movimientos, Presupuestos y Obligaciones, con dirección de filtrado única.

Para comprobar su funcionamiento, se realizaron cuatro pruebas relacionadas con la configuración del modelo y el filtrado de movimientos, presupuestos y obligaciones por categoría.

Las cuatro pruebas fueron exitosas. Durante la revisión se identificó una diferencia entre el periodo de un presupuesto y la fecha de un movimiento. Después de ajustar el periodo en Excel y actualizar Power BI, se comprobó que los importes coincidieran correctamente.

Los procedimientos y resultados de las pruebas se documentaron en pruebas/pruebas-power-bi-modelo.md, mientras que las capturas de pantalla se almacenaron en documentacion/evidencias.

El modelo desarrollado se guardó en el archivo power-bi/Sistema_Finanzas_Personales.pbix.

Como resultado, se completó la estructura inicial del modelo de datos en Power BI y se verificó el funcionamiento de las relaciones entre las cuatro tablas, quedando preparado para continuar con la creación de indicadores y visualizaciones financieras.