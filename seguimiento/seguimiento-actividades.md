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
| 5  | Desarrollar el registro de ingresos y gastos                    | 4 oct. 2026     | 10 oct. 2026      | Ana Laura y Edson | ⬜ Pendiente |
| 6  | Desarrollar la sección de presupuestos                         | 11 oct. 2026    | 17 oct. 2026      | Ana Laura         | ⬜ Pendiente |
| 7  | Desarrollar la sección de obligaciones y pagos                 | 11 oct. 2026    | 17 oct. 2026      | Edson             | ⬜ Pendiente |
| 8  | Capturar datos de prueba y revisar la estructura                | 18 oct. 2026    | 21 oct. 2026      | Ana Laura y Edson | ⬜ Pendiente |
| 9  | Configurar importación, validación y limpieza con Power Query | 22 oct. 2026    | 28 oct. 2026      | Edson             | ⬜ Pendiente |
| 10 | Crear el modelo de datos y relaciones en Power BI               | 29 oct. 2026    | 4 nov. 2026       | Ana Laura         | ⬜ Pendiente |
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