from fastapi import FastAPI
import schedule, time, threading
from database import sismos_db, limpiar_base_datos

app = FastAPI()

# Tarea 24/7: Limpieza automática
def tarea_programada():
    while True:
        limpiar_base_datos()
        time.sleep(3600) # Se limpia cada hora

threading.Thread(target=tarea_programada, daemon=True).start()

@app.get("/api/sismos")
def obtener_sismos():
    return {"sismos": sismos_db}
