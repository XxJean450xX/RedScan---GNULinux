# RedScan-GNULinux

## Descripción  
**RedScan** es una herramienta educativa desarrollada en Python que permite a los usuarios explorar redes locales e interactuar con dispositivos conectados. Este proyecto tiene como propósito enseñar los fundamentos del análisis de redes y la comunicación básica entre dispositivos utilizando el protocolo ICMP (ping).  

⚠️ **Nota:** Este software está diseñado exclusivamente para fines educativos y de aprendizaje. El uso de esta herramienta en redes ajenas sin autorización podría violar leyes y regulaciones locales.  

## Características  
- **Escaneo de redes locales**: Detecta dispositivos conectados a la red.  
- **Envío de pings**: Permite probar la conectividad con dispositivos específicos.  
- **Interfaz simple y funcional**: Diseño intuitivo para facilitar el aprendizaje.  

## Requisitos del Sistema  
- **Sistema operativo**: Linux  
- **Python**: Versión 3.6 o superior  
- **Permisos de administrador**: Se requiere ejecutar con permisos de `sudo` para ciertas operaciones relacionadas con redes.  

- **IMPORTANTE:** Asegúrate de tener Python 3 y las dependencias necesarias instaladas.
## Instalación  
1. Clona este repositorio:  
    ```bash  
    #Este es un bloque de codigo en bash

    git clone https://github.com/tu-usuario/redscan.git  
    cd redscan  
    ```
2. Instala las herramientas de auditoría de red:
    ```bash
    #Este es un bloque de codigo en bash

    sudo apt update
    sudo apt install xterm
    sudo apt-get install aircrack-ng
    ```
3. Haz el script ejectuable
    ```bash
    #Este es un bloque de codigo en bash

    chmod +x RedScan.py
    ```

## Uso

1. Ejecuta el script con permisos de administrador (sudo):  
    ```bash  
    #Este es un bloque de codigo en bash

    sudo ./RedScan.py
    ```
2. Sigue las instrucciones en pantalla para:
    - Seleccionar tu tarjeta de red.
    - Escanear redes disponibles.
    - Introducir el BSSID y Canal de la red a auditar.
    - Identificar y desautenticar dispositivos conectados a la red.
3. Ejemplo de salida:
    ```bash

    #Verificando tarjetas de red disponibles...
    #Introduce el nombre de la tarjeta de red (ejemplo: wlan0): wlan0

    #Cambiando la tarjeta de red al modo monitor...
    #Escaneando redes WiFi disponibles en la banda 'a'...
    #Presiona CTRL+C cuando encuentres la red que deseas auditar.

    #Introduce el BSSID de la red objetivo: 00:11:22:33:44:55
    #Introduce el canal (CH) de la red objetivo: 6

    #Monitoreando la red 00:11:22:33:44:55 en el canal 6...
    #Presiona CTRL+C cuando encuentres los dispositivos conectados.

    #Introduce el STATION (dispositivo objetivo): 00:11:22:33:44:66

    #Enviando desautenticación al dispositivo 00:11:22:33:44:66...

    ```

## Contribución

Las contribuciones son bienvenidas. Si encuentras un error o tienes mejoras que sugerir, no dudes en abrir un issue o enviar un pull request.

# Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

