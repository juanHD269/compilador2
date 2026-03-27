#!/bin/bash
echo "========== UPDATE =========="
echo "Nodo: $(hostname)"
echo "Iniciando actualización del sistema..."
sudo apt-get update -y
echo "Instalando actualizaciones disponibles..."
sudo apt-get upgrade -y
echo "Actualización completada exitosamente."
