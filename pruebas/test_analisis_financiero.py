
from pathlib import Path
import pandas as pd

# Localizar el archivo Excel del proyecto
ruta_proyecto = Path(__file__).resolve().parent.parent
ruta_excel = ruta_proyecto / "excel" / "Sistema_Finanzas_Personales.xlsx"

# Cargar los movimientos financieros
movimientos = pd.read_excel(
    ruta_excel,
    sheet_name="Movimientos"
)

movimientos = movimientos.dropna(subset=["ID"])

# Prueba 1: verificar la cantidad de movimientos
def test_cantidad_movimientos():
    assert len(movimientos) == 5


# Convertir los montos a valores numéricos
movimientos["Monto"] = pd.to_numeric(
    movimientos["Monto"],
    errors="coerce"
)

# Prueba 2: verificar los ingresos totales
def test_ingresos_totales():
    ingresos = movimientos.loc[
        movimientos["Tipo"] == "Ingreso", "Monto"
    ].sum()

    assert ingresos == 9700


# Prueba 3: verificar los gastos totales
def test_gastos_totales():
    gastos = movimientos.loc[
        movimientos["Tipo"] == "Gasto", "Monto"
    ].sum()

    assert gastos == 1700


# Prueba 4: verificar el balance financiero
def test_balance_financiero():
    ingresos = movimientos.loc[
        movimientos["Tipo"] == "Ingreso", "Monto"
    ].sum()

    gastos = movimientos.loc[
        movimientos["Tipo"] == "Gasto", "Monto"
    ].sum()

    balance = ingresos - gastos

    assert balance == 8000


# Prueba 5: verificar gastos por categoría
def test_gastos_por_categoria():
    gastos = movimientos[
        movimientos["Tipo"] == "Gasto"
    ]

    gastos_categoria = gastos.groupby("Categoría")["Monto"].sum()

    assert gastos_categoria["Alimentación"] == 750
    assert gastos_categoria["Transporte"] == 500
    assert gastos_categoria["Servicios"] == 450


# Prueba 6: verificar el resumen mensual
def test_resumen_mensual():
    datos = movimientos.copy()

    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    datos["Periodo"] = datos["Fecha"].dt.to_period("M")

    resumen = datos.pivot_table(
        index="Periodo",
        columns="Tipo",
        values="Monto",
        aggfunc="sum",
        fill_value=0
    )

    periodo = pd.Period("2026-10", freq="M")

    assert resumen.loc[periodo, "Ingreso"] == 9700
    assert resumen.loc[periodo, "Gasto"] == 1700
    assert (
        resumen.loc[periodo, "Ingreso"]
        - resumen.loc[periodo, "Gasto"]
    ) == 8000
