# Automatización de correo

Script en Python para enviar un mismo correo a múltiples destinatarios obtenidos desde un archivo CSV. Su objetivo es automatizar el envío de comunicados, avisos o notificaciones, reduciendo el tiempo necesario para enviar cada correo manualmente.

## Caracteristicas

- Lee los destinatarios desde un archivo CSV.
- Detecta automáticamente la columna que contiene los correos electrónicos mediante su encabezado.
- Reconoce encabezados comunes como:
  - `correo`
  - `email`
  - `mail`
  - `e-mail`
  - `correo electronico`
  - `correo electrónico`
- Si no encuentra un encabezado válido, permite seleccionar manualmente la columna.
- Utiliza SMTP de Gmail mediante una contraseña de aplicación.
- Las credenciales se almacenan en un archivo `.env`, evitando escribir datos sensibles directamente en el código.
- Envía el mismo mensaje a todos los destinatarios encontrados.

## Requisitos previos

- Python 3.10 o superior.
- Una cuenta de Gmail.
- Tener habilitada la verificación en dos pasos en la cuenta de Google.
- Crear una contraseña de aplicación para Gmail.
- Instalar las dependencias necesarias.

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/
cd repositorio
```

2. Crear un entorno virtual (opcional pero recomendado).

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias.

```bash
pip install python-dotenv
```

## Configuración

### 1. Crear el archivo `.env`

En la carpeta del proyecto cree un archivo llamado `.env`.

```env
REMITENTE=micorreo@ejemplo.com
GOOGLE_PASS=xxxx xxxx xxxx xxxx
```

Donde:

- **REMITENTE:** dirección de correo desde la que se enviarán los mensajes.
- **GOOGLE_PASS:** contraseña de aplicación generada por Google, no la contraseña normal de la cuenta.

### 2. Crear el archivo CSV

El programa busca un archivo llamado:

```
CorreosPrueba.csv
```

Debe contener una fila de encabezados y una columna con los correos electrónicos.

Ejemplo:

| Nombre | Correo | Empresa |
| ------- | ------- | ------- |
| Juan | juan@email.com | Empresa A |
| Ana | ana@email.com | Empresa B |
| Luis | luis@email.com | Empresa C |

Si el encabezado de la columna no coincide con alguno de los nombres reconocidos, el programa solicitará indicar el número de la columna.

## Uso

Ejecute el programa desde la terminal.

```bash
python Automatizacion_de_correo.py
```

Durante la ejecución:

1. Se cargan las variables de entorno.
2. Se abre el archivo CSV.
3. Se identifica automáticamente la columna de correos.
4. Si no puede identificarla, solicitará el número de la columna.
5. Se establece la conexión segura con Gmail mediante SMTP SSL.
6. Se envía el correo a todos los destinatarios.
7. Al finalizar se mostrará:

```
Correo enviado con éxito
```

## Decisiones de diseño

- Se utiliza un archivo `.env` para mantener las credenciales fuera del código fuente.
- Se emplea `SMTP_SSL` en el puerto 465 para establecer una conexión cifrada con Gmail.
- La detección automática del encabezado evita depender de una posición fija de la columna de correos.
- Se implementa manejo de excepciones para errores comunes como:
  - Archivo CSV inexistente.
  - Credenciales inválidas.
  - Destinatarios rechazados.
  - Errores durante el envío.
- Se utiliza la biblioteca `csv` incluida en Python para garantizar compatibilidad con archivos CSV estándar.
- Cada correo se envía individualmente, permitiendo identificar errores específicos por destinatario en futuras mejoras.

## Dependencias

- Python Standard Library
  - `smtplib`
  - `csv`
  - `os`
  - `email.mime.text`
  - `sys`

- Librerías externas

```text
python-dotenv
```

## Mejoras futuras

- Personalización del asunto y cuerpo mediante plantillas.
- Adjuntar archivos.
- Registro de correos enviados en un archivo de log.
- Envío de correos en formato HTML.
- Validación del formato de las direcciones de correo.
- Soporte para otros proveedores SMTP como Outlook o Yahoo. 
