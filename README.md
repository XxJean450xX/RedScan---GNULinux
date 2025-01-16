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

## Guia de Uso

Sigue estos pasos para utilizar el script de manera segura y eficiente. Recuerda que este proyecto es **exclusivamente educativo** y debe usarse con los permisos adecuados.


1.  Ejecuta el script con permisos de administrador en tu terminal:  
    ```bash
    sudo ./RedScan.py
    ```
    


2.  El script te guiará por los siguientes pasos:
    - **Seleccionar la tarjeta de red**: Verás las tarjetas disponibles y deberás elegir la que desees usar.
    - **Escanear redes WiFi**: Se abrirán ventanas mostrando las redes disponibles.
    - **Elegir la red objetivo**: Introduce el **BSSID** y el **canal (CH)** de la red que deseas auditar.
    - **Monitorear dispositivos conectados**: Identifica los dispositivos en la red.
    - **Desautenticar dispositivos**: Envía solicitudes de desautenticación (pings) a un dispositivo específico.
    


3.  Detener el Envío de Pings:

    Mientras se envían pings para desautenticar un dispositivo, el proceso continuará hasta que lo detengas manualmente.  
    Para detenerlo, presiona **CTRL + C** en la ventana correspondiente. Esto finalizará el proceso de desautenticación.


4.  Reactivar tu Conexión a Internet
    Durante el uso del programa, tu conexión a Internet será deshabilitada.  
    Para restaurarla al finalizar el script (o en caso de error), ejecuta:  
    ```bash
    airmon-ng stop {tarjeta_red}
    ```
    Reemplaza **`{tarjeta_red}`** con el nombre de la tarjeta que seleccionaste al inicio (por ejemplo: `wlan0`, `wlo1`, etc.).

    **Nota**: El nombre de la tarjeta es el mismo que elegiste en el primer paso.


## Ejemplo de salida:
1. 
    ```bash
    === Script de Auditoría de Redes WiFi ===
    Nota: Este script es exclusivamente para fines educativos. Asegúrate de tener los permisos adecuados.
    Asegúrate de ejecutarlo como administrador.

    Verificando tarjetas de red disponibles...
    lo        no wireless extensions.

    wlan0     IEEE 802.11  ESSID:"Mi_Red"
            Mode:Managed  Frequency:2.437 GHz  Access Point: 00:1A:2B:3C:4D:5E   
            Bit Rate=144.4 Mb/s   Tx-Power=20 dBm   
            Retry short limit:7   RTS thr:off   Fragment thr:off
            Power Management:off

    Introduce el nombre de la tarjeta de red (ejemplo: wlan0): wlan0

    Cambiando la tarjeta de red al modo monitor...
    PHY Interface   Driver      Chipset
    phy0 wlan0      ath9k       Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter

    (mac80211 monitor mode vif enabled for [phy0] on [wlan0mon])
    (mac80211 station mode vif disabled for [phy0] on [wlan0])

    Abriendo escáner de redes en una nueva ventana...
    --> Se han abierto ventanas separadas para escanear redes en 2.4 GHz y 5 GHz.
    Observa la ventana del escáner. Cuando tengas el BSSID y el canal de la red (CH) objetivo, vuelve aquí y presiona Enter para continuar.

    Introduce el BSSID de la red objetivo: 00:1A:2B:3C:4D:5E
    Introduce el canal (CH) de la red objetivo: 6

    Abriendo monitoreo de la red 00:1A:2B:3C:4D:5E en una nueva ventana...
    --> Realiza prueba y error con los siguientes dispositivos hasta encontrar el deseado.
    Observa la ventana del monitoreo. Cuando identifiques el dispositivo objetivo anota el STATION, vuelve aquí y presiona Enter para continuar.

    Introduce el STATION (dispositivo objetivo): 00:5F:6G:7H:8I:9J

    Enviando desautenticación al dispositivo 00:5F:6G:7H:8I:9J...
    ```

## Contribución

Las contribuciones son bienvenidas. Si encuentras un error o tienes mejoras que sugerir, no dudes en abrir un issue o enviar un pull request.

# Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

