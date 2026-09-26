# Alcance y organización del plan de trabajo

## 1. Alcance definitivo del proyecto

El proyecto consiste en desarrollar un Sistema de Finanzas Personales que permita registrar, organizar, procesar y analizar información financiera personal. El sistema estará orientado principalmente al control de ingresos, gastos, presupuestos y obligaciones de pago, proporcionando información que facilite la consulta y análisis de la situación financiera del usuario.

Para esta versión del proyecto se desarrollarán las siguientes funciones:

- Registro de ingresos y gastos, incluyendo información como fecha, concepto, cantidad y categoría.
- Creación y administración de un catálogo de categorías para clasificar los movimientos financieros.
- Registro y seguimiento de presupuestos, permitiendo comparar los montos establecidos con los gastos registrados.
- Registro de obligaciones y pagos pendientes para mantener un control de los compromisos financieros.
- Consulta y filtrado de los movimientos registrados.
- Validación, limpieza y transformación de los datos mediante Power Query.
- Generación de indicadores y visualizaciones financieras mediante Power BI.
- Utilización de Python y Pandas como apoyo para realizar procesamiento o análisis complementarios.
- Almacenamiento organizado de la información para permitir su consulta y actualización.

### Límites del alcance

Esta versión del sistema no realizará operaciones bancarias reales ni pagos directamente desde la aplicación. El proyecto estará enfocado en el registro, procesamiento, consulta y análisis de la información financiera proporcionada por el usuario.

La primera versión funcionará principalmente de manera local y utilizará las herramientas definidas para cada etapa del desarrollo. La estructura se mantendrá organizada de forma que posteriormente puedan incorporarse nuevas funciones o tecnologías sin modificar completamente el sistema.

---

## 2. Entregables del sistema

La construcción del Sistema de Finanzas Personales se realizará de manera progresiva. Los principales entregables serán los siguientes:

### Archivo principal de Excel

Será la base inicial para organizar y registrar la información financiera. Contendrá las estructuras necesarias para el registro de ingresos y gastos, catálogo de categorías, presupuestos y obligaciones de pago.

### Procesamiento mediante Power Query

Se desarrollarán consultas para importar, validar, limpiar y transformar la información proveniente de los registros financieros. Su finalidad será preparar los datos para las etapas posteriores de análisis.

### Modelo y reporte en Power BI

Se elaborará un modelo de datos que permita generar indicadores y visualizaciones financieras. El reporte mostrará información relacionada con ingresos, gastos, presupuestos y otros datos relevantes para conocer la situación financiera del usuario.

### Procesamiento complementario con Python y Pandas

Se desarrollará al menos un componente de procesamiento o análisis complementario utilizando Python y Pandas, con la finalidad de apoyar el análisis de los datos cuando resulte conveniente utilizar programación.

### Repositorio del proyecto

Se utilizará Git para mantener el control de versiones del proyecto y GitHub como plataforma para alojar el repositorio y facilitar el trabajo colaborativo. El repositorio permitirá conservar los archivos generados y mantener un historial de los cambios realizados durante la construcción.

### Documentación

Se conservará la documentación desarrollada durante el proyecto, incluyendo requerimientos, planeación, seguimiento de actividades, evidencias, pruebas y documentación necesaria para explicar el desarrollo y funcionamiento del sistema.

---

## 3. Distribución del trabajo

Las actividades se distribuirán entre los dos integrantes del equipo. Algunas serán realizadas individualmente y aquellas relacionadas con decisiones generales, integración y pruebas serán desarrolladas en conjunto.

| # | Actividad | Responsable |
|---|-----------|-------------|
| 1 | Revisar el documento de requisitos y las funciones principales | Ana Laura y Edson |
| 2 | Definir el alcance y organizar el plan de trabajo | Ana Laura y Edson |
| 3 | Diseñar la estructura general del archivo de Excel | Ana Laura |
| 4 | Crear el catálogo de categorías financieras | Edson |
| 5 | Desarrollar el registro de ingresos y gastos | Ana Laura y Edson |
| 6 | Desarrollar la sección de presupuestos | Ana Laura |
| 7 | Desarrollar la sección de obligaciones y pagos | Edson |
| 8 | Capturar datos de prueba y revisar la estructura | Ana Laura y Edson |
| 9 | Configurar importación, validación y limpieza con Power Query | Edson |
| 10 | Crear el modelo de datos y relaciones en Power BI | Ana Laura |
| 11 | Crear indicadores, gráficas y dashboard en Power BI | Ana Laura |
| 12 | Desarrollar análisis complementario con Python/Pandas | Edson |
| 13 | Integrar los componentes desarrollados | Ana Laura y Edson |
| 14 | Realizar pruebas funcionales | Ana Laura y Edson |
| 15 | Elaborar manual y recopilar evidencias | Ana Laura |
| 16 | Corregir errores encontrados durante las pruebas | Ana Laura y Edson |
| 17 | Realizar revisión final, respaldo y preparación de la entrega | Ana Laura y Edson |

Aunque se establezca un responsable principal para determinadas actividades, ambos integrantes podrán colaborar cuando sea necesario para mantener la continuidad y correcta integración del proyecto.

---

## 4. Organización del repositorio

El repositorio se organizará mediante carpetas que permitan identificar los diferentes componentes generados durante la construcción del sistema.

La estructura general será:

    Sistema-Finanzas-Personales/
    │
    ├── README.md
    │
    ├── documentacion/
    │   ├── requerimientos/
    │   │   └── revision-requisitos.md
    │   ├── planeacion/
    │   │   └── alcance-plan-trabajo.md
    │   └── evidencias/
    │
    ├── seguimiento/
    │   └── seguimiento-actividades.md
    │
    ├── excel/
    │
    ├── datos/
    │   └── datos-prueba/
    │
    ├── power-bi/
    │
    ├── python/
    │
    └── pruebas/

La carpeta `documentacion` almacenará los documentos relacionados con los requerimientos, planeación y evidencias del proyecto.

La carpeta `seguimiento` contendrá el registro general de las actividades y se actualizará conforme avance la construcción.

La carpeta `excel` contendrá el archivo principal utilizado para registrar y organizar la información financiera.

La carpeta `datos` se utilizará para almacenar los datos de prueba empleados durante el desarrollo.

La carpeta `power-bi` almacenará los archivos correspondientes al modelo, indicadores y visualizaciones desarrollados en Power BI.

La carpeta `python` contendrá los archivos utilizados para el procesamiento y análisis complementario mediante Python y Pandas.

Finalmente, la carpeta `pruebas` se utilizará para conservar los resultados y evidencias de las pruebas realizadas durante la etapa de integración.

---

## 5. Resultado de la actividad

Como resultado de esta actividad se definió el alcance de la primera versión del Sistema de Finanzas Personales, los principales entregables que deberán obtenerse durante su construcción, la distribución de responsabilidades entre los integrantes y la estructura que se utilizará para organizar los archivos del repositorio.

Esta organización servirá como base para continuar con las siguientes actividades del proyecto y permitirá mantener un desarrollo ordenado de acuerdo con la planeación establecida.