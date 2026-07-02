import time

# Usamos una lista en memoria por ahora, pero se puede conectar a SQLite o Firebase
sismos_db = []

def limpiar_base_datos():
    """Borra sismos con más de 24 horas de antigüedad."""
    ahora = time.time()
    # 86400 segundos = 24 horas
    global sismos_db
    sismos_db = [s for s in sismos_db if (ahora - s['timestamp']) < 86400]
    print("Limpieza de registros ejecutada.")

def guardar_sismo(lat, lon, mag, lugar):
    sismos_db.append({
        "lat": lat, "lon": lon, "mag": mag, "lugar": lugar,
        "timestamp": time.time()
    })
