#!/bin/bash
echo "========== BACKUP =========="
echo "Nodo: $(hostname)"
echo "Iniciando proceso de backup..."

ITEMS=("base_datos" "configuraciones" "archivos_estaticos" "logs")

for ITEM in "${ITEMS[@]}"; do
    echo -n "Resguardando $ITEM..."
    # Simulación de progreso
    for i in {1..3}; do
        echo -n "."
        sleep 0.5
    done
    echo " [OK]"
done

if [ $? -eq 0 ]; then
    echo "Backup finalizado exitosamente en $(date)"
else
    echo "Error durante el proceso de backup."
    exit 1
fi
