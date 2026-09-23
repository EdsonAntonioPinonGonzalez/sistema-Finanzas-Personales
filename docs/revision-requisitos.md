# Revisión de requisitos del Sistema de Finanzas Personales

## 1. Objetivo

Revisar el Documento de Requerimientos del Sistema (DRS) con el propósito de identificar las funciones principales, la estructura del sistema y las tecnologías consideradas para su construcción.

Esta revisión servirá como base para las siguientes actividades del proyecto y permitirá mantener correspondencia entre los requisitos definidos y la implementación del Sistema de Finanzas Personales.

## 2. Descripción general del sistema

El Sistema de Finanzas Personales estará orientado al registro, organización, consulta y análisis de información financiera personal.

El sistema contempla la gestión de ingresos, gastos, categorías, presupuestos y obligaciones financieras. A partir de esta información será posible realizar procesos de validación y transformación, generar resúmenes financieros y presentar indicadores y visualizaciones para facilitar el análisis de las finanzas del usuario.

El sistema no contempla inicialmente servicios bancarios, transacciones monetarias reales, acceso directo a cuentas bancarias ni procesamiento de pagos.

## 3. Requisitos funcionales identificados

| ID | Requisito | Descripción |
|---|---|---|
| RF-01 | Registrar ingresos | Registrar ingresos indicando fecha, monto, descripción y categoría. |
| RF-02 | Registrar gastos | Registrar gastos indicando fecha, monto, descripción y categoría. |
| RF-03 | Editar y eliminar movimientos | Modificar o eliminar movimientos financieros registrados. |
| RF-04 | Gestionar categorías | Crear, consultar y administrar las categorías utilizadas para clasificar movimientos. |
| RF-05 | Consultar y filtrar movimientos | Consultar movimientos aplicando filtros como fecha, tipo, categoría o monto. |
| RF-06 | Gestionar presupuestos | Establecer y consultar presupuestos asociados a categorías o periodos. |
| RF-07 | Gestionar obligaciones financieras | Registrar y dar seguimiento a obligaciones financieras, pagos y saldos. |
| RF-08 | Generar resúmenes financieros | Generar información resumida de ingresos, gastos, presupuestos y obligaciones. |
| RF-09 | Generar indicadores y visualizaciones | Generar indicadores y representaciones visuales del comportamiento financiero. |
| RF-10 | Importar información financiera | Incorporar información proveniente de archivos o fuentes externas compatibles. |
| RF-11 | Validar y transformar información | Validar, limpiar y transformar los datos antes de almacenarlos o analizarlos. |
| RF-12 | Almacenar y recuperar información | Conservar la información financiera y recuperarla cuando sea requerida. |

## 4. Módulos principales identificados

De acuerdo con el DRS, el sistema se divide en los siguientes módulos:

- Gestión de movimientos.
- Gestión de categorías.
- Gestión de presupuestos.
- Gestión de obligaciones.
- Procesamiento y transformación.
- Análisis financiero.
- Indicadores y visualización.
- Persistencia de datos.

## 5. Flujo funcional general

El flujo principal identificado para el funcionamiento del sistema es:

**Registro o importación de información → Validación → Transformación → Almacenamiento → Análisis → Generación de indicadores y visualizaciones.**

Este flujo establece el orden general mediante el cual la información financiera será capturada, procesada, almacenada y posteriormente utilizada para generar resultados.

## 6. Requisitos no funcionales identificados

Durante la revisión también se identificaron los siguientes aspectos no funcionales:

- Rendimiento.
- Seguridad.
- Fiabilidad.
- Disponibilidad.
- Mantenibilidad.
- Portabilidad.

Estos requisitos deberán considerarse durante la construcción y las pruebas del sistema.

## 7. Tecnologías contempladas

El DRS establece las siguientes herramientas para el desarrollo del proyecto:

| Herramienta | Uso previsto |
|---|---|
| Microsoft Excel | Registro y organización inicial de la información financiera. |
| Power Query | Importación, limpieza, transformación y preparación de datos. |
| Power BI | Generación de indicadores, reportes y visualizaciones financieras. |
| Python | Procesamiento y análisis complementario de datos. |
| Pandas | Manipulación y análisis de estructuras de datos tabulares mediante Python. |
| Visual Studio Code | Edición de código, archivos de configuración y documentación técnica. |
| PlantUML | Elaboración de diagramas UML. |

## 8. Resultado de la revisión

La revisión permitió identificar las funciones, módulos, requisitos no funcionales y tecnologías contempladas para la construcción del Sistema de Finanzas Personales.

Los requisitos establecidos en el DRS proporcionan la base para continuar con la planeación y construcción progresiva del sistema. La siguiente actividad del proyecto consistirá en delimitar el alcance de la implementación y organizar el plan de trabajo de acuerdo con el tiempo disponible.