from pydantic import BaseModel
from typing import List


# Esquemas para PropiedadDetallada (tabla Propiedad_detallada)

class PropiedadDetalladaBase(BaseModel):
    """
    Representa los atributos de la tabla Propiedad_detallada.
    Este esquema base se usa para crear o devolver propiedades detalladas
    asociadas a un Widget_class.
    """
    nombre: str
    tipo: str
    descripcion_extendida: str
    ejemplo_propiedad: str

class PropiedadDetalladaCreate(PropiedadDetalladaBase):
    """
    Esquema usado al crear una nueva PropiedadDetallada.
    Se agrega el campo widget_id que indica a qué widget pertenece.
    """
    widget_id: int

class PropiedadDetalladaResponse(PropiedadDetalladaBase):
    """
    Esquema de respuesta que incluye el campo id.
    orm_mode = True permite que se puedan usar instancias ORM directamente.
    """
    id: int

    class Config:
        orm_mode = True


# Esquemas para UsoComun (tabla uso_comun)

class UsoComunBase(BaseModel):
    """
    Atributos compartidos para la tabla uso_comun.
    Describe un uso común de un widget.
    """
    descripcion: str

class UsoComunCreate(UsoComunBase):
    """
    Esquema para crear un nuevo UsoComun.
    Se requiere el widget_id que lo asocia a un widget.
    """
    widget_id: int

class UsoComunResponse(UsoComunBase):
    """
    Esquema de respuesta que incluye el id del uso común registrado.
    """
    id: int

    class Config:
        orm_mode = True


# Esquemas para ConstructorComun (constructor_comun)

class ConstructorComunBase(BaseModel):
    """
    Atributos base de ConstructorComun, como la firma del constructor.
    """
    firma: str

class ConstructorComunCreate(ConstructorComunBase):
    """
    Esquema para crear un ConstructorComun asociado a un widget.
    """
    widget_id: int

class ConstructorComunResponse(ConstructorComunBase):
    """
    Respuesta con id del constructor común creado.
    """
    id: int

    class Config:
        orm_mode = True


# Esquemas para WidgetRelacionado (widget_relacionado)

class WidgetRelacionadoBase(BaseModel):
    """
    Atributos del widget relacionado.
    """
    nombre: str

class WidgetRelacionadoCreate(WidgetRelacionadoBase):## foranea
    """
    Esquema para crear un widget relacionado, indicando widget_id padre.
    """
    widget_id: int

class WidgetRelacionadoResponse(WidgetRelacionadoBase):## incremental
    """
    Esquema de respuesta que incluye id del widget relacionado.
    """
    id: int

    class Config:
        orm_mode = True


# Esquemas para Widget_class

class WidgetBase(BaseModel):
    """
    Representa los atributos de entrada de un Widget.
    Este esquema se usa para crear widgets.
    """
    nombre: str
    descripcion: str
    cuando_no_usar: str
    codigo: str
    imagen: str
    ruta: str

class WidgetCreate(WidgetBase):
    """
    No añade campos nuevos, pero sirve para separar el propósito de creación.
    """
    pass

class WidgetResponse(WidgetBase):
    """
    Esquema completo de respuesta del widget, con:
    - id del widget
    - listas anidadas con las propiedades, usos, constructores y relacionados
    """
    id: int
    propiedades_detalladas: List[PropiedadDetalladaResponse] = []
    usos_comunes: List[UsoComunResponse] = []
    constructores_comunes: List[ConstructorComunResponse] = []
    widgets_relacionados: List[WidgetRelacionadoResponse] = []

    class Config:
        orm_mode = True




##########################################################################################################
##########################################################################################################
##########################################################################################################

# RESUMEN PARA RECORDAR 

"""
- Los esquemas BaseModel definen los atributos que ingresan o salen en una API.
- Los que terminan en Base contienen lo que el usuario puede llenar.
- Los que terminan en Create añaden claves foráneas para insertar relaciones.
- Los que terminan en Response agregan el campo id y devuelven relaciones anidadas.
- orm_mode permite devolver directamente datos desde los modelos ORM.
"""


# RESUMEN EXPLICACION DE LA CLASE 

# ############   TABLA Propiedad_detallada ############
"""
Este es un esquema que hace referencia a la clase PropiedadDetallada,
de la tabla Propiedad_detallada del archivo tablas_flutter.py
"""

"""
Este esquema hereda los atributos de la clase PropiedadDetalladaBase.
widget_id es el campo que hace referencia como llave foránea
al campo id de la tabla Widget_tab (clase Widget_class).
"""

"""
Este esquema hereda los atributos de la clase PropiedadDetalladaBase.
El campo id es el valor incremental de la tabla Propiedad_detallada.
"""

# ############   TABLA Uso_comun ############
"""
Hace referencia a la clase UsoComun de la tabla uso_comun.
UsoComunBase tiene el campo descripcion, que describe un uso del widget.
UsoComunCreate hereda descripcion y agrega widget_id como llave foránea.
UsoComunResponse añade el id para respuestas y usa orm_mode.
"""

# ############   TABLA Constructor_comun ############
"""
Hace referencia a la clase ConstructorComun de la tabla constructor_comun.
ConstructorComunBase tiene el campo firma.
ConstructorComunCreate hereda firma y agrega widget_id como llave foránea.
ConstructorComunResponse añade id para respuestas y activa orm_mode.
"""

# ############   TABLA Widget_relacionado ############
"""
Hace referencia a la clase WidgetRelacionado de la tabla widget_relacionado.
WidgetRelacionadoBase contiene el campo nombre.
WidgetRelacionadoCreate agrega widget_id como llave foránea.
WidgetRelacionadoResponse añade el campo id y habilita orm_mode.
"""

# ############   TABLA Widget_class ############
"""
WidgetBase representa los atributos de un widget (nombre, descripción, código, etc.).
WidgetCreate no cambia nada pero separa la intención de crear.
WidgetResponse hereda todo y agrega:
- id del widget
- listas anidadas: propiedades, usos, constructores y widgets relacionados.
"""
