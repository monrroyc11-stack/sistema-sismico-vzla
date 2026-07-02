async function verificarSeguridad() {
    const response = await fetch('/api/sismos');
    const { data } = await response.json();
    
    navigator.geolocation.getCurrentPosition(pos => {
        const { latitude, longitude } = pos.coords;
        
        data.forEach(sismo => {
            const dist = calcularDistancia(latitude, longitude, sismo.lat, sismo.lon);
            if (dist < 50) {
                alert("¡ALERTA! Sismo detectado a menos de 50km. Busque zona segura.");
            }
        });
    });
}

function calcularDistancia(lat1, lon1, lat2, lon2) {
    // Fórmula de Haversine simplificada
    const R = 6371; // Radio tierra
    // ... lógica matemática de distancia
    return dist;
}
