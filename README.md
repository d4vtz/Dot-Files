<p align="center">
  <b>Una tarde de olas</b>
</p>




### ¡Gracias por venir!


Estos son mis archivos de configuración de mi entorno de trabajo, actualmente estoy usando Arch Linux con BSPWM... Porque amo los Tiling Window Manager!!


Aquí dejo algunos detalles sobre mi configuración:

+ **OS**: [Arch Linux](https://www.archlinux.org/)
+ **WM**: [BSPWM](https://github.com/baskerville/bspwm)
+ **Hotkey Daemon**: [Sxhkd](https://github.com/baskerville/sxhkd)
+ **Compositor**: [Picom-ibhagwan](https://github.com/ibhagwan/picom)
+ **Shell**: [zsh](https://wiki.archlinux.org/index.php/Zsh)
+ **Terminal**: [Termite](https://github.com/thestinger/termite)
+ **Editor**: [Vim](https://www.vim.org/)
+ **File Manager**: [Thunar](https://git.xfce.org/xfce/thunar/)
+ **Launcher**: [rofi](https://github.com/davatorium/rofi/)
+ **Status Bar**: [Polybar](https://github.com/polybar/polybar)
+ **Dock**: [Dockbarx](https://github.com/M7S/dockbarx)
+ **Browser**: [Google Chrome](https://aur.archlinux.org/packages/google-chrome/)

## Novedades

- **Selector de temas**: Ajusta los temas tanto gtk2 y gtk3 como de Termite de acuerdo a el wallpaper seleccionado con ayuda de pywal.

- Código más limpio


## Setup

Aquí dejo las instrucciones que debe seguir para obtener mi configuración.

1. Instalar [BSPWM](https://github.com/baskerville/bspwm) y [SXHKD](https://github.com/baskerville/sxhkd).


   **Para usuarios de Arch**  pueden usar los paquetes de AUR [bspwm-git](https://aur.archlinux.org/packages/bspwm-git/) y [sxhkd-git](https://aur.archlinux.org/packages/sxhkd-git/) por medio de un ayudante de paquetes como yay.

   ```shell
   yay -S bspwm-git sxhkd-git
   ```

   **Para otras distribuciónes**, pueden construir los paquete siguiendo las instrucciones de compilación [aquí](https://github.com/baskerville/bspwm/wiki).



2. Dependencias:

      Esta es una lista de las dependencias necesarias para que mi configuración de BSPWM funcione correctamente. Si los instala todos, tendrá una experiencia (en su      mayoría) sin complicaciones.

      | Dependencia | Descripción | ¿Porque se necesita? |
      | --- | --- | --- |
      | `termite` | Terminal | ¡Hay que dejar de tenerle miedo! |
      | `zsh` | Interprete de Shell | Una shell con elegancia |
      | `zsh-autosuggestions,  zsh-completions, zsh-syntax-highlighting` | Plugins de zsh | Facilita mucho el uso de la terminal |
      | `picom-ibhagwan` | Compositor | Habilita la transparencia de las ventanas y las esquinas redondiadas |
      | `rofi` | Lanzador de aplicaciones | Se explica solo |
      | `mpd` | Demonio del servidor para reproducir música | Widgets de música |
      | `ncmpcpp` | Reproductor de música para la terminal| Widgets de música |
      | `mpv` | Reproductor multimedia  | Se explica solo |
      | `ranger, thunar` | Administrador de archivos | Se explica  solo |
      | `dunst` | Demonio de notificaciones | Se explica solo |
      | `polybar` | Barra de estado | Permite configurar modulos como mostrar los espacios de trabajo, volumen, etc. |
      | `dockbarx` | Dock | Se explica solo |
      | `vim` | Editor de texto de consola | Se explica solo |
      | `spicetify-cli, spicetify-themes-git` | Herramienta de línea de comandos para personalizar el cliente de Spotify  | Mejorar estetica de Spotify |
      | `redshift` | Control de temperatura de Pantalla | Uso del modo nocturno |
      | `feh` | Visualizador de imágenes  | Se explica solo |
      | `python-wal` | Generador de esquemas de colores basado en una imagen | Fijar wallpaper y temas de polybar, rofi, etc |
      | `lsd` | ls con esteroides | Colorear la salida del comando ls con su respectivos iconos |
      | `bat` | cat con resaltado de syntaxis | Se explica solo |
      | `scrot` | Aplicación de linea de comandos para tomar screnshots | Se explica solo |



    - **Arch Linux** (y todas las ditros basadas en Arch)

        ```shell
       yay -S termite zsh zsh-autosuggestions zsh-completions zsh-syntax-highlighting rofi mpd mpv ncmpcpp ranger dunst polybar dockbarx vim thunar spicetify-cli spicetify-themes-git redshift feh python-pywal lsd bat scrot
       ```
      Para instalar [picom-ibhagwan](https://www.reddit.com/r/unixporn/comments/fs8trg/oc_comptonpicom_fork_with_both_tryone144s_dual/) el cual es un fork de picom, tenemos que construirlo siguiendo las instrucciones de compilación o bien en Arch ejecutamos:

      ```shell
      git clone https://github.com/ibhagwan/picom-ibhagwan-git
       makepkg -si
      ```

    - **Para otras distribuciones**

      Pueden buscar los paquetes en el repositorio de su distro (pueden cambiar los nombres), o bien buscar el código fuente de los paquetes y compilarlos usted mismo.


3. Instalar fuentes necesarias:

   Necesita instalar algunas fuentes de texto para poder visualizar correctamente algunos iconos de polybar y de la terminal.
   Estas fuentes se encuentran en mis dotfiles.

   Fuentes:
   + **Iosevka Nerd Font**
   + **Comfortaa Regular**
   + **Hack Regular Nerd Font**

   Fuentes Opcionales:
   + **San Francisco Display**

   Para instalarlas solo basta con moverlas a `~/.fonts` o `~/.local/share/fonts`.
   - Debera crear el directorio en caso de no existir.

   Finalmente, ejecute el siguente comando para que su sistema detecte las fuentes instaladas.
   ```shell
   fc-cache -v
   ```

4. Instalar mi configuración de BSPWM.

   ```shell
   git clone https://github.com/medicendav/Dotfiles.git
   cd Dotfiles
   chmod +x INSTALL
   ./INSTALL
   ```

5. Configurar Archivos.

   La configuración de archivos básicos para mi entorno son:

   + **Configurar BSPWM**

      El archivo de configuraciones de BSPWM se encuentra como `~/.config/bspwm/bspwmrc`.

      En este archivo se encuentran todas losa configuraciones sobre el comportamiento de las ventanas, apicaciones de inicio, espacios de trabajo, etc



   + **Configurar SXHKD**

      El archivo de configuraciones de SXHKD se encuentra como  `~/.config/sxhkd/sxhkdrc`. Dentro de este archivo van todos los shortcuts configurados, como el lanzador de rofi, la terminal, portapapeles, cerrar sesión, etc. Ver [Shortcuts](#Shortcuts) para más detalles.



   + **Configurar PICOM**

      El archivo de configuraciones de PICOM se encuentra como  `~/.config/picom/picom.conf`. En este archivo van todas las configuraciones del compositor, como la transparencia, el desenfoque, esquinas redondeadas, sombras, etc.

   + **Configurar POLYBAR**

      Las configuraciones de polybar se encuentran dentro del directorio `~/.config/polybar`, En este directorio se encuentra en script de inicio de polybar `launch.sh`, el cual manda a llamar a las barras `top.ini`, `down-left.ini` y `down-right.ini`.

      Además estos archivos mandan a llamar la los módulos que que requieran dentro de la carpeta `~/.config/polybar/modulos`, sientese libre de modificarlos a su gusto.

   + *Y muchos más...*



6. Tema visual

   **Esquema de colores y wallpaper**

   + (Opcional) Fijar el wallpaper, puedes configurar tu wallpaper con ayuda de `feh`, ejecutando el siguiente comando,

      ```shell
      feh --bg-fill /path/to/your/wallpaper
      ```

   + (Opcional) Cargar esquemas de colores,


      ```shell
      xrdb -merge /path/to/colorscheme
      ```

      Observaciones:

      - Todos mi temas de mi BSPWM toman los colores de `xrdb`. Esto va bien con el uso de  [pywal](https://github.com/dylanaraps/pywal).

      Yo utilizo `pywal` para generar mis esquemas de colores de acuerdo a mi wallpaper, por lo cual solo se necesita ejecutar el siguente comando para generar los esquemas de colores y fija el wallpaper.

      ```shell
      wal -i "path/to/img"
      ```

   **Temas de iconos y ventanas**

      Iconos:
      + **[Tela](https://github.com/vinceliuice/Tela-icon-theme)** (Tela Manjaro)
      + **[Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)** (ePapirus)

      Temas:
      + **[Tarde de olas](https://github.com/medicendav/Dotfiles/tree/master/.themes/tarde-de-olas)** (Tema creado con Oomox)
      + **[Adapta](https://github.com/adapta-project/adapta-gtk-theme)** (Adapta-Nokto)


7. Inicie sesión con BSPWM.

En hora buena, en este punto ya debería estar listo para cerrar sesión en su escritorio actual y utilizar BSPWM.

Pruébalo, juega con él, disfrútalo.



## Shortcuts

Yo uso <kbd>super</kbd> (tecla Windows) como mi tecla principal.

| Shortcuts | Acción |
| --- | --- |
| <kbd>super + enter</kbd> | Abrir terminal (Termite)|
| <kbd>super + shift + enter</kbd> | Lanzar rofi |
| <kbd>super + q</kbd> | Cerrar ventana |
| <kbd>super + shitf + r </kbd> | Recargar configuración de bspwm |
| <kbd>super + alt + r </kbd> | Recargar configuración de sxhkd |
| <kbd>alt + w</kbd> | Abrir navegador (Google-Chrome) |
| <kbd>super + f</kbd> | Abrir administrador de archivos (Thunar) |
| <kbd>super + End</kbd> | Menu para cerrar, bloquear, reiniciar y apagar |
| <kbd>super + shift + p </kbd> | Cambiar a ventana a modo fullscreen |
| <kbd>super + shitf + o </kbd> | Cambiar a ventana a modo flotante |
  <kbd>super + shift + i </kbd> | Cambiar a ventana a modo tiling |
  <kbd>super + shift + f </kbd> | Cambiar a ventana a modo monoculo |
| <kbd>alt + [Flechas]</kbd> | Alternar entre nodos |
| <kbd>super + [Prior,Next] </kbd> | Cambiar entre workspaces |
| <kbd>super + [Letf,Right]</kbd> | Cambiar entre workspace ocupados |
| <kbd>super + [h,w,c,p,m,v,t,s]</kbd> | Moverse a un workspace especifico |
| <kbd>super + shift + [h,w,c,p,m,v,t,s]</kbd> | Enviar un nodo a un workspace especifico |
| <kbd>ctrl + [Flechas]</kbd> | Mover ventanas flotantes |
| <kbd>super + z : [Flechas]</kbd> | Cambiar de tamaño las ventanas |
| <kbd>super + shift + [Prior, Next]</kbd> | Rotar arbol de ventanas |
|
Y mucho más, ver archivo `~/.config/sxhkd/sxhkdrc`.*



### Disfruta en mundo de los Tiling Window Manager
Si disfrutas mis temas y te gustaría mostrar tu agradecimiento, puedesinvitarme un cafe.

¡Gracias desde el fondo de mi corazón!
- [**PayPal**](paypal.me/medicenDav)
