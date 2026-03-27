#!/bin/bash
echo "========== UPDATE =========="
echo "Nodo: $(hostname)"

MAX_RETRIES=3
RETRY_COUNT=0
SUCCESS=false

while [ $RETRY_COUNT -lt $MAX_RETRIES ] && [ "$SUCCESS" = false ]; do
    echo "Conectando al repositorio de actualizaciones (Intento $((RETRY_COUNT + 1)))..."
    sleep 1
    
    # Simulación de conexión inestable
    if [ $(( $RANDOM % 5 )) -ne 0 ]; then
        echo "Conexión establecida correctamente."
        SUCCESS=true
    else
        echo "[ERROR] Fallo en la conexión. Reintentando en 2 segundos..."
        RETRY_COUNT=$((RETRY_COUNT + 1))
        sleep 2
    fi
done

if [ "$SUCCESS" = true ]; then
    PACKAGES=("kernel" "security-patch" "runtime-env")
    for PKG in "${PACKAGES[@]}"; do
        echo "Actualizando: $PKG..."
        sleep 0.5
    done
    echo "Actualización del sistema completada exitosamente."
else
    echo "FATAL: No se pudo conectar al repositorio tras $MAX_RETRIES intentos."
    exit 1
fi
