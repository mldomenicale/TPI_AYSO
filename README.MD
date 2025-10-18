# 🖥️ Trabajo Integrador: Virtualización

## 📚 Arquitectura y Sistemas Operativos

**Tecnicatura Universitaria en Programación – Universidad Tecnológica Nacional**
**Comisión 4 – Año 2025**

---

## 👩‍💻 Integrantes

- **Maria Luz Domenicale Doré** – [maria.domenicale@tupad.utn.edu.ar](mailto:maria.domenicale@tupad.utn.edu.ar)
- **Magaly Egea Ruiz** – [magaly.egea@tupad.utn.edu.ar](mailto:magaly.egea@tupad.utn.edu.ar)

**Docente Titular:** Prof. Ariel Enferrel
**Docente Tutor:** Nicolás Carcaño

📅 _22 de octubre de 2025_

🎥 **Video de presentación:** [Ver en YouTube](https://youtu.be/krjGht0kt4s?si=5K-yCkXTgBUrtHVb)

---

## 🧩 Descripción del Proyecto

Este trabajo integrador tiene como objetivo aplicar los conceptos teóricos de **virtualización** mediante la creación de una máquina virtual con **Ubuntu Server**, la instalación de **Python**, y la ejecución de un programa dentro de un entorno aislado y seguro.

Se utilizó **VirtualBox** como hipervisor de tipo 2, por su carácter libre, multiplataforma y educativo.
El entorno permitió experimentar con la instalación de herramientas como **nginx**, **postgresql**, **glances** y **nextcloud**, validando la funcionalidad de un servidor virtual operativo.

---

## ⚙️ Tecnologías y Herramientas Utilizadas

- **VirtualBox** (Hipervisor Tipo 2)
- **Ubuntu Server 22.04.3 LTS**
- **Python 3**
- **Snapd** (Gestor de paquetes)
- **Glances** – Monitoreo de sistema
- **Nextcloud** – Nube privada
- **Nginx** – Servidor web
- **PostgreSQL** – Base de datos
- **Curtin Installer** – Instalación automatizada
- **Copilot & ChatGPT** – Soporte técnico y acompañamiento en redacción

---

## 🧠 Objetivos

1. Comprender el funcionamiento de la **virtualización** desde un enfoque teórico y práctico.
2. Crear un entorno virtual funcional utilizando **VirtualBox**.
3. Instalar y configurar un **servidor Ubuntu** dentro de una VM.
4. Implementar herramientas Snap y validar su ejecución.
5. Ejecutar un script en Python en el entorno virtualizado.

---

## 🧪 Caso Práctico

1. **Creación del entorno virtual**

   - Instalación de VirtualBox
   - Configuración de la VM (memoria, disco, red)
   - Instalación de Ubuntu Server con _curtin installer_

2. **Instalación de herramientas**

   ```bash
   sudo apt update && sudo apt upgrade
   sudo snap install glances
   sudo snap install nextcloud
   sudo snap install postgresql
   ```

3. **Verificación del entorno**

   ```bash
   df -h
   ip a
   systemctl status snapd
   snap list
   ```

4. **Instalación y ejecución de Python**
   Se implementó un script para registrar nombres y notas de alumnos, calculando el promedio de cada uno.

---

## 🐍 Código Fuente en Python

```python
# Actividad: ingresar los nombres de 3 alumnos y calcular su promedio de notas.

def probar_numero(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def calcular_promedio(lista):
    return sum(lista) / len(lista)

lista_completa_notas = {}
promedios = {}

for i in range(3):
    nombre = input("Nombre del estudiante: ").strip().title()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Intenta nuevamente: ").strip().title()

    notas = []
    for j in range(1, 4):
        nota = -1
        while nota < 1 or nota > 10:
            nota_txt = input(f"Nota {j} de {nombre}: ")
            while not probar_numero(nota_txt):
                nota_txt = input("Debes ingresar un número. Intenta nuevamente: ")
            nota = float(nota_txt)
        notas.append(nota)

    lista_completa_notas[nombre] = tuple(notas)
    promedio = calcular_promedio(notas)
    promedios[nombre] = round(promedio, 2)
    print(f"Promedio de {nombre}: {promedio:.2f}\n")

print("\nResultados:")
for alumno, media in promedios.items():
    print(f"{alumno}: {media}")
```

---

## 📊 Resultados

- Se logró implementar y validar un entorno virtual **totalmente funcional**.
- El servidor virtual respondió correctamente a todas las pruebas de instalación y ejecución.
- Se documentó cada fase con capturas y comprobaciones.
- Se verificó el correcto desempeño de los servicios Snap y del sistema base.
- La experiencia fortaleció los conocimientos sobre **sistemas operativos, virtualización y administración de entornos Linux**.

---

## 🧩 Conclusiones

El proyecto permitió:

- Comprender la **virtualización** como una herramienta esencial en la arquitectura moderna.
- Aplicar conceptos de **sistemas operativos**, gestión de recursos y aislamiento.
- Trabajar de forma colaborativa y reflexiva con un enfoque técnico y ético.
- Aprovechar tecnologías libres y accesibles para el aprendizaje práctico.

---

## 📚 Bibliografía

- Universidad Tecnológica Nacional (2025). _Material de estudio: Virtualización._
- Canonical Ltd. (2024). [Ubuntu Server Documentation](https://ubuntu.com/server/docs)
- Oracle Corporation (2024). [VirtualBox User Manual](https://www.virtualbox.org/manual/UserManual.html)
- GitHub (2025). [Copilot](https://github.com/features/copilot)
- OpenAI (2025). [ChatGPT](https://chat.openai.com)

---

> ✨ _“La virtualización no solo permite experimentar sin miedo, sino aprender desde la práctica, entendiendo que cada error es una oportunidad para crecer.”_
