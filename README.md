# MailSenderAPI

## Descripción del Proyecto
**MailSenderAPI** es un servidor de prueba desarrollado con Flask en Python que permite el envío de correos electrónicos. Este proyecto está diseñado principalmente para fines de desarrollo y pruebas, y no se recomienda su uso en producción.

## Características
- **Servidor de Prueba**: Ideal para experimentar con el envío de correos electrónicos sin comprometer un entorno de producción.
- **Plantillas Personalizables**: Incluye plantillas específicas para mis proyectos, pero puedes agregar tus propias plantillas en la carpeta `templates`.
- **Selección de Plantillas**: Modificando la función `select_template` en el archivo principal, puedes decidir qué plantilla utilizar para enviar correos.

## Instalación

Para instalar y ejecutar el proyecto, sigue estos pasos:

1. Clona el Repositorio:

    ```bash
    git clone https://github.com/TheZombie272/MailSenderAPI
    cd MailSenderAPI

2. Instala las Dependencias:
Asegúrate de tener Flask y otras dependencias necesarias instaladas. Puedes hacerlo ejecutando:

    ```bash
    pip install -r requirements.txt
    
3. Ejecuta el Servidor:
Inicia el servidor Flask con python.

## Uso
Para enviar correos electrónicos, puedes hacer solicitudes a las rutas definidas en el servidor. Asegúrate de modificar la función select_template para elegir la plantilla que deseas utilizar.

### Ejemplo de Uso
Aquí hay un ejemplo básico de cómo enviar un correo electrónico utilizando la API:

    ```http
    {
    "reciepient":[
        {
            "name": "Jon Doe",
            "email": "Jon.Doe@ucaldas.edu.co"
        }
    ],
    "subject": "this is the subject",
    "content": "content",
    "template": "2-fa"
}

""Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, no dudes en abrir un issue o enviar un pull request.

