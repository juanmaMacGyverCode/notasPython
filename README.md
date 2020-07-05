# Programa para gestionar notas

Es un programa sin interfaz gráfica en la cual puedes registrarte como usuario y realizar login para así poder crear, borrar o consultar las notas que hayas creado.

## Comenzando 🚀

Es muy sencillo de configurar, te lo detallo por aquí.

### Pre-requisitos 📋

* Tener configurada la máquina de **PYTHON**
* Disponer de una base de datos MySQL o MariaDB (XAMPP)
* Para los test, yo uso PyTest

_Para instalar PyTest abre tu CMD (por si acaso en donde se ubique el proyecto) y escribe lo siguiente:_

```
pip install pytest
```

No es necesario realizar más operaciones.

En caso de que el código de la base de datos no funcione, dispone del código en un bloc de notas.

### Problemas 🔧

Es posible que puedas no poder conectarte a la base de datos. Hay dos soluciones.

La primera es instalando el conector de **MariaDB** usando **CMD** (en caso de usar MariaDB):

```
pip3 install pytest
```
Una vez hecho esto cambia el conector en el fichero **funcionesSQL.py**:

```
import metodosComunes
import mariadb
import clases

def crearConector():
    database = mariadb.connect(
        host="localhost",
        user="root",
        passwd="",
        database="programaNotas"
    )
    return database
```

Si esto no funciona, puede ser que tu intérprete de python esté mal instalada. Para arreglarlo desinstalelo e instalelo de nuevo y sigue los pasos anteriores.

## Ejecutando las pruebas ⚙️

Para ejecutar las pruebas debes ir a la dirección donde se encuentre tu fichero y escribir la siguiente orden en **CMD**:

```
pytest test.py
```
