# Secure Password Generator

Generador de contraseñas en Python, con interfaz tkinter. Se elige la longitud y qué
tipos de caracteres entran: letras, números, símbolos, alfabetos no latinos y símbolos
Unicode.

Las contraseñas se generan con `secrets.choice`, no con `random`.

## Uso

Hace falta Python 3. En Windows, tkinter viene con el instalador; en Linux puede haber
que instalar `python3-tk`.

1. Descarga `passwords.py` o clona el repositorio.
2. Ejecuta `python passwords.py`.
3. Escribe la longitud, marca los tipos de caracteres y pulsa *Generate Password*.
4. Haz clic en la contraseña y elige *Copy* en el menú para copiarla.

## English

Run `python passwords.py` with Python 3. Choose the length, tick the character sets and
press *Generate Password*. Click the result and choose *Copy* to put it in the
clipboard.

The character sets are ASCII letters and digits, punctuation, a few Asian and Arabic
alphabets, accented Latin characters and a handful of Unicode symbols.

## License

GPL-3.0. See [LICENSE](LICENSE).
