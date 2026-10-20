# Guía de instalación de Vainilla

Vainilla no está en la tienda de extensiones de VS Code: se instala desde su archivo `.vsix`. Son tres
pasos: descargarlo, instalarlo y activarlo.

## 1. Descargar el tema

Descarga **[vainilla-0.4.1.vsix](https://github.com/sryena/tema-vainilla/raw/main/releases/vainilla-0.4.1.vsix)**
y déjalo en una carpeta que encuentres fácil, por ejemplo **Descargas**.

## 2. Instalarlo

Elige una de las dos formas. Las dos hacen lo mismo.

### Opción A: desde VS Code, sin terminal

1. Abre VS Code.
2. Abre la vista de extensiones: `Ctrl+Shift+X` (en Mac, `Cmd+Shift+X`).
3. Arriba a la derecha de esa vista, pulsa los tres puntos **`···`**.
4. Elige **Instalar desde VSIX…** (en inglés, *Install from VSIX…*).
5. Busca el archivo `vainilla-0.4.1.vsix` que descargaste y pulsa **Instalar**.

### Opción B: desde la terminal

Abre una terminal en la carpeta donde está el archivo y escribe:

```bash
code --install-extension vainilla-0.4.1.vsix
```

En **Windows**, desde PowerShell, si lo tienes en Descargas:

```powershell
code --install-extension "$HOME\Downloads\vainilla-0.4.1.vsix"
```

Si sale **«Extension 'vainilla-0.4.1.vsix' was successfully installed»**, ya está.

## 3. Activarlo

1. En VS Code pulsa `Ctrl+K` y, sin soltar `Ctrl`, `T` (en Mac, `Cmd+K` y `Cmd+T`).
2. En la lista de temas elige **Vainilla**.

También puedes ponerlo a mano en tu `settings.json`:

```json
"workbench.colorTheme": "Vainilla"
```

## Actualizar a una versión nueva

Descarga el `.vsix` nuevo de la carpeta [`releases/`](releases/) e instálalo encima. Con la terminal,
añade `--force` para que sustituya a la versión anterior:

```bash
code --install-extension vainilla-0.4.1.vsix --force
```

Después, recarga la ventana: `Ctrl+Shift+P` → **Developer: Reload Window**.

Para ver qué versión tienes:

```bash
code --list-extensions --show-versions | grep vainilla
```

## Desinstalar

Desde la vista de extensiones (`Ctrl+Shift+X`), busca **Vainilla** y pulsa **Desinstalar**, o en la
terminal:

```bash
code --uninstall-extension sryena.vainilla
```

## Problemas frecuentes

| Qué pasa | Qué hacer |
|---|---|
| `code: command not found` (Linux o Mac) | En Mac: en VS Code, `Cmd+Shift+P` → **Shell Command: Install 'code' command in PATH**. En Linux, usa la opción A o reinstala VS Code desde el paquete oficial. |
| `code` no se reconoce (Windows) | Reinstala VS Code marcando **Agregar a PATH**, o usa la opción A. |
| VS Code instalado con Flatpak | `flatpak run com.visualstudio.code --install-extension vainilla-0.4.1.vsix` |
| Lo instalé y no lo veo en la lista de temas | Recarga la ventana (`Ctrl+Shift+P` → **Developer: Reload Window**) y vuelve a `Ctrl+K Ctrl+T`. |
| Algunos colores no cambian | Otra extensión o tu `settings.json` puede estar pisándolos: revisa si tienes `workbench.colorCustomizations` o `editor.tokenColorCustomizations`. |

¿Algo más? Abre una *issue* en [GitHub](https://github.com/sryena/tema-vainilla/issues).
