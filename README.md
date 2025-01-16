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
3. **IMPORTANTE**
    -Cuando se este desautenticando el dispositivo, enviandole ping durara todo lo que usted lo permita, si quiere parar el envio de ping oprima CTRL + C. Esto acabara la ejecucion.

4. Reactivar tu Red internet
    -Al usar el programa se deshabilitara tu internet, para recuperar la conexion al finalizar el programa o por cualquier otro error ingrese:
    ```bash  
    #Este es un bloque de codigo en bash

    airmon-ng stop {tarjeta_red}
    ```
    Donde dice tarjeta_red ingrese el nombre de su tarjeta (wlo1, wla0, NIC...)
    NOTA: Es el mismo nombre que ingreso de primeras.

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

