
from pathlib import Path
import pandas as pd

# Ubicación del archivo Excel
ruta_proyecto = Path(__file__).resolve().parent.parent
ruta_excel = ruta_proyecto / "excel" / "Sistema_Finanzas_Personales.xlsx"

# Importar los movimientos financieros
movimientos = pd.read_excel(
    ruta_excel,
    sheet_name="Movimientos"
)

# Eliminar filas sin identificador
movimientos = movimientos.dropna(subset=["ID"])

# Mostrar los datos importados
print("MOVIMIENTOS FINANCIEROS")
print(movimientos.to_string(index=False))

print("\nTotal de movimientos:", len(movimientos))


# Convertir los montos a valores numéricos
movimientos["Monto"] = pd.to_numeric(
    movimientos["Monto"],
    errors="coerce"
)

# Calcular ingresos y gastos
ingresos = movimientos.loc[
    movimientos["Tipo"] == "Ingreso", "Monto"
].sum()

gastos = movimientos.loc[
    movimientos["Tipo"] == "Gasto", "Monto"
].sum()

# Calcular el balance financiero
balance = ingresos - gastos

# Mostrar los resultados
print("\nRESUMEN FINANCIERO")
print(f"Ingresos totales: ${ingresos:,.2f}")
print(f"Gastos totales: ${gastos:,.2f}")
print(f"Balance financiero: ${balance:,.2f}")

# Filtrar únicamente los gastos
movimientos_gastos = movimientos[
    movimientos["Tipo"] == "Gasto"
]

# Agrupar los gastos por categoría
gastos_categoria = (
    movimientos_gastos
    .groupby("Categoría")["Monto"]
    .sum()
    .sort_values(ascending=False)
)

# Mostrar resultados
print("\nGASTOS POR CATEGORÍA")
for categoria, monto in gastos_categoria.items():
    print(f"{categoria}: ${monto:,.2f}")


# Convertir las fechas al formato de fecha
movimientos["Fecha"] = pd.to_datetime(
    movimientos["Fecha"],
    errors="coerce"
)

# Obtener el periodo de cada movimiento
movimientos["Periodo"] = movimientos["Fecha"].dt.to_period("M")

# Agrupar ingresos y gastos por mes
resumen_mensual = movimientos.pivot_table(
    index="Periodo",
    columns="Tipo",
    values="Monto",
    aggfunc="sum",
    fill_value=0
)

# Asegurar que existan ambas columnas
resumen_mensual = resumen_mensual.reindex(
    columns=["Ingreso", "Gasto"],
    fill_value=0
)

# Calcular balance mensual
resumen_mensual["Balance"] = (
    resumen_mensual["Ingreso"] - resumen_mensual["Gasto"]
)

# Mostrar resultados
print("\nRESUMEN MENSUAL")
print(resumen_mensual.to_string())
