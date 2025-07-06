# HubServer 🔧🖥️

**HubServer** es una aplicación web para visualizar, administrar y documentar múltiples servidores locales o remotos, junto con sus servicios asociados. Diseñada para entornos técnicos como laboratorios caseros, redes de desarrollo, servidores Docker, Proxmox, Kubernetes, NAS y más.

Su diseño está inspirado en herramientas como Portainer, con una estética profesional, soporte para imágenes, CRUD completo y generación de códigos QR para acceder rápidamente desde el móvil.

---

## 🧩 ¿Qué puedo hacer con HubServer?

- Registrar **múltiples servidores** en red con nombre, IP principal e imagen personalizada.
- Asociar a cada servidor uno o más **servicios** (por ejemplo: interfaces web, APIs, paneles, etc.).
- Subir imágenes opcionales para representar cada **servicio**.
- Acceder a cada servicio desde un **link clickeable** (IP:puerto).
- **Editar o eliminar** servicios directamente desde una interfaz amigable.
- Generar **códigos QR** por servidor para acceder rápidamente desde un smartphone.
- Todo esto, **sin necesidad de base de datos**, solo con `data.json`.

---

## 🖼️ Capturas de Pantalla

### Vista principal: listado de servidores
![Home](docs/img/home.png)

### Agregar servidor
![Agregar Servidor](docs/img/add_server.png)

### Vista de un servidor y sus servicios
![Detalle Servidor](docs/img/server_detail.png)

### Modal de edición de servicios
![Editar Servicio](docs/img/edit_service.png)

---

## ⚙️ Tecnologías Utilizadas

- **Python 3.11**
- **Flask** como framework web
- **Bootstrap 5.3** para diseño moderno y responsive
- **Docker** y **Docker Compose** para despliegue fácil
- **QRCode** (librería `qrcode`) para generación de códigos QR
- Almacenamiento en archivo JSON (sin base de datos)

---

## 🚀 Instalación rápida con Docker Compose

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/HubServer.git
cd HubServer
