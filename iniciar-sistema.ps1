# Detectar la carpeta donde está guardado el proyecto
$RutaProyecto = $PSScriptRoot

# Construir las rutas de los archivos
$RutaExcel = Join-Path $RutaProyecto "excel\Sistema_Finanzas_Personales.xlsx"
$RutaPowerBI = Join-Path $RutaProyecto "powerbi\Sistema_Finanzas_Personales.pbix"

Write-Host "Sistema de Finanzas Personales"
Write-Host "--------------------------------"

# Verificar que los archivos existan
if (-not (Test-Path $RutaExcel)) {
    Write-Host "ERROR: No se encontro el archivo Excel."
    exit 1
}

if (-not (Test-Path $RutaPowerBI)) {
    Write-Host "ERROR: No se encontro el archivo Power BI."
    exit 1
}

Write-Host "Carpeta del proyecto: $RutaProyecto"
Write-Host "Excel encontrado correctamente."
Write-Host "Power BI encontrado correctamente."
Write-Host "Ruta de Excel: $RutaExcel"
Write-Host "Verificacion de rutas completada."
