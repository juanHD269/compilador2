#!/bin/bash
echo "========== DEPLOY =========="
echo "Nodo: $(hostname)"

ENV="PROD"

if [ "$ENV" == "PROD" ]; then
    echo "Desplegando en ambiente de PRODUCCIÓN..."
else
    echo "Desplegando en ambiente de DESARROLLO..."
fi

COMPONENTS=("frontend" "backend" "api" "database-migrations")

for COMP in "${COMPONENTS[@]}"; do
    echo "Preparando despliegue de: $COMP..."
    sleep 1
    echo "Instalando $COMP..."
    # Simular una verificación aleatoria de éxito
    if [ $(( $RANDOM % 10 )) -gt 1 ]; then
        echo "$COMP desplegado correctamente."
    else
        echo "[ADVERTENCIA] Reintentando despliegue de $COMP..."
        sleep 2
        echo "$COMP desplegado tras reintento."
    fi
done

echo "Despliegue completado exitosamente."
