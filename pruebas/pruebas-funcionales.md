# Pruebas funcionales del prototipo

### Actividad 8. Captura de datos de prueba y revisión de la estructura

**Proyecto:** Sistema de Finanzas Personales
**Periodo programado:** 18 al 21 de octubre de 2026
**Responsables:** Ana Laura y Edson
**Estado:** Pruebas realizadas satisfactoriamente

* **Objetivo**

Comprobar el funcionamiento de los módulos desarrollados en Excel mediante la captura y modificación temporal de datos ficticios, verificando que las fórmulas, los cálculos y los estados automáticos respondan correctamente.


* **Pruebas realizadas**

Prueba 1. Actualización de movimientos

Se modificó temporalmente el monto de un gasto registrado en la categoría Alimentación, asignándole un valor de $1,000.00.

Resultado esperado: El monto gastado en la hoja Presupuestos debía actualizarse automáticamente, modificando también el dinero disponible.

Resultado obtenido: Los cálculos se actualizaron correctamente de acuerdo con el nuevo monto registrado.

Estado: Exitosa.


Prueba 2. Actualización del estado de presupuestos

Se modificó temporalmente el monto presupuestado para la categoría Alimentación, estableciendo un valor inferior a los gastos registrados.

Resultado esperado: El dinero disponible debía mostrar un valor negativo y el estado del presupuesto debía cambiar a Excedido.

Resultado obtenido: El sistema calculó correctamente la diferencia y actualizó el estado a Excedido. También se comprobó que los cálculos consideran el periodo seleccionado, evitando mezclar gastos de diferentes meses.

Estado: Exitosa.


Prueba 3. Actualización del estado de obligaciones

Se modificó temporalmente la fecha de pago de una obligación vencida para comprobar la actualización automática de su estado.

Resultado esperado: Al registrar una fecha de pago, la obligación debía cambiar a Pagado. Al eliminarla, debía regresar a Vencido si la fecha límite ya había pasado.

Resultado obtenido: El estado se actualizó correctamente en ambos casos.

Estado: Exitosa.


* **Resultados generales**

Se realizaron tres pruebas funcionales sobre los módulos de movimientos, presupuestos y obligaciones. Todas obtuvieron los resultados esperados.

Después de realizar las comprobaciones, se restauraron los valores originales para conservar la información de prueba.

No se identificaron errores en las funcionalidades evaluadas durante estas pruebas.


* **Conclusión**

Las pruebas realizadas permitieron comprobar que los módulos desarrollados en Excel funcionan correctamente en los casos evaluados. Se verificó la actualización automática de los presupuestos, el cálculo del dinero disponible y la identificación de los estados de las obligaciones.

Estos resultados permiten continuar con las siguientes actividades del proyecto. Sin embargo, las pruebas corresponden únicamente al prototipo desarrollado en Excel y no representan una validación del sistema completo, ya que todavía falta integrar Power Query, Power BI y Python.
