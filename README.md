Sistema de Gestión de Asistencia

Este es un sistema de gestión de asistencia basado en Python que permite registrar entradas y salidas, generar reportes individuales y visualizar estadísticas.

Requisitos

Para ejecutar el sistema, asegúrate de tener Python instalado y todas las dependencias requeridas. Puedes instalarlas con:

pip install -r requirements.txt

Archivos del Proyecto

main.py: Código principal del sistema.

estudiantes_promedios.xlsx: Archivo donde se almacena la información de los promedios de los estudiantes.

requirements.txt: Lista de dependencias necesarias.

Uso

Ejecuta el script principal con:

python main.py

Se mostrará un menú interactivo con las siguientes opciones:

estudiantes: Solicita nombres y notas de los estudiantes.

nombre: Permite ingresar el nombre del estudiante.

nota: Permite ingresar la nota del estudiante.

promedios: Calcula el promedio de las notas de cada estudiante.

wb-ws: Crea un nuevo libro de Excel.

fila: Escribe los nombres en la columna A y los promedios en la columna B

promedio_general: Escribe el promedio general en la celda B1

wb.save: Guarda el archivo

Estructura del Archivo de estudiantes_promedios

El archivo estudiantes_promedios.xlsx tiene la siguiente estructura:

nombre Andres Buritica promedio 5.0

Funcionalidades Adicionales

Creación automática del archivo de asistencia si no existe.

Cálculo automático de promedio basado en las notas.

Notas

Asegúrate de que estudiantes_promedios.xlsx no esté abierto en otro programa antes de ejecutar el script.

El sistema no admite múltiples registros de entrada y salida en un mismo día para el mismo usuario.

Licencia

Este proyecto es de código abierto y puedes modificarlo según tus necesidades.