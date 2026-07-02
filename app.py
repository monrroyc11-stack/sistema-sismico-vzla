from fastapi import FastAPI
import schedule, time, threading
from database import obtener_sismos_recientes, limpiar_base_datos

app = FastAPI()

# Tarea 24/7: Limpieza y actualización
def tarea_programada():
    while True:
        limpiar_base_datos()
        # Aquí llamarías a tu función que consulta el USGS/API
        time.sleep(3600) # Se ejecuta cada hora

threading.Thread(target=tarea_programada, daemon=True).start()

@app.get("/api/sismos")
def get_sismos():
    return {"data": obtener_sismos_recientes()}
