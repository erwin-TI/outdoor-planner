# Planificador de Rutas Outdoor

def calcular_tiempo_marcha(distancia, desnivel_positivo, desnivel_negativo):
    tiempo_distancia = distance = distancia / 4
    tiempo_subida = desnivel_positivo / 400
    tiempo_bajada = desnivel_negativo / 800
    return tiempo_distancia + tiempo_subida + tiempo_bajada


# Módulo de Seguridad
EQUIPO_POR_ACTIVIDAD = {
    "1": {
        "nombre": "Trekking por el día",
        "elementos": ["Zapatos de trekking", "Mochila 20-30L", "Ración de marcha", "1.5L de Agua mín.", "Cortaviento", "Botiquín básico"]
    },
    "2": {
        "nombre": "Trail running",
        "elementos": ["Zapatillas de trail", "Chaleco de hidratación", "Manta térmica de emergencia", "Geles/Barras energéticas", "Cortaviento ultra liviano"]
    },
    "3": {
        "nombre": "Montañismo invernal",
        "elementos": ["Botas de alta montaña", "Crampones", "Arnés", "Piolet", "Casco", "Ropa sistema 3 capas", "Termo con agua caliente", "Botiquín básico", "Lentes de sol Categoría 4"]
    },
    "4": {
        "nombre": "Snowboard de montaña / Splitboard",
        "elementos": ["Tabla/Splitboard", "ARVA (DVA)", "Pala de nieve", "Sonda", "Casco y antiparras", "Pieles de ascensión", "Herramienta multiuso"]
    }
}

print("=== BIENVENIDO AL PLANIFICADOR DE RUTAS OUTDOOR ===\n")

print("Selecciona tu actividad:")
for clave, info in EQUIPO_POR_ACTIVIDAD.items():
    print(f"{clave}. {info['nombre']}")

opcion = input("\nElige el número de tu actividad: ")

if opcion in EQUIPO_POR_ACTIVIDAD:
    actividad_seleccionada = EQUIPO_POR_ACTIVIDAD[opcion]["nombre"]
    checklist = EQUIPO_POR_ACTIVIDAD[opcion]["elementos"]
else:
    print("Opción no válida. Se asignará checklist genérico.")
    actividad_seleccionada = "Salida general"
    checklist = ["Agua", "Ración de marcha", "Botiquín", "Linterna"]

print(f"\n--- Configurando ruta para: {actividad_seleccionada} ---\n")

# Pide un nombre a la ruta para usarlo como nombre del archivo
nombre_ruta = input("Nombre de la ruta (ej: Volcan_Villarrica): ")
distancia = float(input("Distancia total (en km): "))
desnivel_pos = float(input("Desnivel positivo (metros de subida): "))
desnivel_neg_input = input(
    "Desnivel negativo (metros de bajada) [Enter si es igual a la subida]: ")

if desnivel_neg_input == "":
    desnivel_neg = desnivel_pos
else:
    desnivel_neg = float(desnivel_neg_input)

tiempo_estimado = calcular_tiempo_marcha(distancia, desnivel_pos, desnivel_neg)

# --- CREACIÓN DEL TEXTO PARA EL REPORTE ---
reporte = f"""=======================================
        RESUMEN DE TU PLANIFICACIÓN    
=======================================
Ruta: {nombre_ruta}
Actividad: {actividad_seleccionada}
Tiempo estimado de marcha: {tiempo_estimado:.2f} horas.
---------------------------------------
 CHECKLIST DE SEGURIDAD RECOMENDADO:
"""
for item in checklist:
    reporte += f" [ ] {item}\n"
reporte += "=======================================\n¡Disfruta la ruta y vuelve seguro!"

# Mostramos en pantalla
print("\n" + reporte)

# --- MÓDULO DE PERSISTENCIA (GUARDADO) ---
nombre_archivo = f"plan_{nombre_ruta.lower().replace(' ', '_')}.txt"

try:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(reporte)
    print(f"\n✔ ¡Planificación guardada con éxito en: '{nombre_archivo}'!")
except Exception as e:
    print(f"\n❌ Hubo un problema al guardar el archivo: {e}")
