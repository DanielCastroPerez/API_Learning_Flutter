## Aqui se crean las tablas desde Python 1
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import base

class Widget_class(base):
    """
    Clase que representa la tabla "Widget_tab" en la base de datos.
    """
    __tablename__ = "Widget_tab"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    descripcion = Column(Text, nullable=False)
    cuando_no_usar = Column(Text, nullable=False)
    codigo = Column(Text, nullable=False)
    imagen = Column(Text, nullable=False) # se modifica para tomar la url de firabase
    ruta = Column(String(60), nullable=False)

    # Relación uno-a-muchos con PropiedadDetallada (un widget tiene muchas propiedades)
    propiedades_detalladas = relationship(
        "PropiedadDetallada",          # la tabla a la que hace relacion   
        back_populates="widget",      
        cascade="all, delete-orphan"   # Elimina propiedades si el widget es eliminado
    )

    usos_comunes = relationship(
        "UsoComun",
        back_populates="widget",
        cascade="all, delete-orphan"
    )

    constructores_comunes = relationship(
        "ConstructorComun",
        back_populates="widget",
        cascade="all, delete-orphan"
    )

    widgets_relacionados = relationship(
        "WidgetRelacionado",
        back_populates="widget",
        cascade="all, delete-orphan"
    )

class PropiedadDetallada(base):## LISTO ##
    """
    Clase que representa la tabla "Propiedad_detallada" en la base de datos.
    """
    __tablename__ = "Propiedad_detallada"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), nullable=False) 
    tipo = Column(String(30), nullable=False)
    descripcion_extendida = Column(Text, nullable=False)
    ejemplo_propiedad = Column(Text, nullable=False)
    widget_id = Column(Integer, ForeignKey("Widget_tab.id"), nullable=False)  # Clave foránea que conecta con el id de la tabla Widget_tab

    # Relación muchos-a-uno con Widget_class (muchas propiedades pertenecen a un solo widget)
    widget = relationship(
        "Widget_class",               # Modelo padre al que esta propiedad pertenece
        back_populates="propiedades_detalladas"  # Atributo inverso en el modelo padre
    )

class UsoComun(base):## LISTO ##
    """
    Clase que representa la tabla "Uso_comun" en la base de datos.
    """
    __tablename__ = "uso_comun"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    descripcion = Column(Text, nullable=False)## LISTO ##
    widget_id = Column(Integer, ForeignKey("Widget_tab.id", ondelete="CASCADE"), nullable=False)  # Conecta con el id de la tabla Widget_tab
    widget = relationship("Widget_class", back_populates="usos_comunes") 

class ConstructorComun(base): ## LISTO ##
    """
    Clase que representa la tabla "constructor_comun" en la base de datos.
    """
    __tablename__ = "constructor_comun"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    firma = Column(Text, nullable=False)
    widget_id = Column(Integer, ForeignKey("Widget_tab.id", ondelete="CASCADE"), nullable=False)  # Conecta con el id de la tabla Widget_tab
    widget = relationship("Widget_class", back_populates="constructores_comunes")

class WidgetRelacionado(base):
    """
    Clase que representa la tabla "widget_relacionado" en la base de datos.
    """
    __tablename__ = "widget_relacionado"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(Text, nullable=False)
    widget_id = Column(Integer, ForeignKey("Widget_tab.id", ondelete="CASCADE"), nullable=False)  # Conecta con el id de la tabla Widget_tab
    widget = relationship("Widget_class", back_populates="widgets_relacionados")

##########################################################################################################
# Explicacion de como se hizo el modelo despues esto se conecta con schemas.py
# bd C:\xampp\mysql\bin>mysql -u root -p  jejeje porque se me olvida 
##########################################################################################################
# Se crea una tabla independiente para cada lsta como propiedades_detalladas, usos_comunes, constructores_comunes, widgets_relacionados.
# En  propiedades_detalladas cada elemnto se crea como un reguistro en la bd seguido de su llave forena **widget_id**

# En caso de usos_comunes, constructores_comunes, widgets_relacionados cada elemento de la lista  se crea un reguistro en la bd y se relaciona con ua llave primaria que es widget_id
# Ejemplo en la JSON LA la lista de widgets_relacionados tiene tres elementos , esos elementos se encuentran en la tabla widget_relacionado y se identifican por su llave foranea (widget_id)
# SELECT * FROM widget_relacionado WHERE widget_id=11;
# +----+------------------------------------------------------------------+-----------+
# | id | nombre                                                           | widget_id |
# +----+------------------------------------------------------------------+-----------+
# | 44 | SizedBox                                                         |        11 |
# | 45 | Container                                                        |        11 |
# | 46 | Margin (aunque `Container` con `margin` es el equivalente común) |        11 |
# +----+------------------------------------------------------------------+-----------+
    """{
    "nombre": "Padding",
    "descripcion": "Un widget fundamental en Flutter que inserta espacio vacío alrededor de su 'child' (hijo). Permite controlar el espaciado interno de un widget, empujando su contenido lejos de sus bordes.",
    "propiedades_detalladas": [
      {
        "nombre": "padding",
        "tipo": "EdgeInsetsGeometry",
        "descripcion_extendida": "Define la cantidad de espacio vacío que se debe aplicar alrededor del 'child'. Puedes especificar un valor uniforme, solo para ciertos lados, o para lados horizontales/verticales.",
        "ejemplo_propiedad": "Padding(\n  padding: const EdgeInsets.all(16.0), // Padding uniforme de 16px\n  child: Text('Con padding de 16'),\n)\n\nPadding(\n  padding: const EdgeInsets.only(left: 8.0, top: 4.0), // Padding solo a la izquierda y arriba\n  child: Text('Con padding específico'),\n)\n\nPadding(\n  padding: const EdgeInsets.symmetric(horizontal: 20.0), // Padding horizontal\n  child: Text('Con padding horizontal'),\n)"
      },
      {
        "nombre": "child",
        "tipo": "Widget",
        "descripcion_extendida": "El widget al que se le aplicará el padding. El espacio definido por `padding` se agregará alrededor de este widget.",
        "ejemplo_propiedad": "Padding(\n  padding: const EdgeInsets.all(8.0),\n  child: Container(\n    color: Colors.blue,\n    width: 100,\n    height: 100,\n  ),\n)"
      }
    ],
    "usos_comunes": [
      "Crear espacio entre widgets en un `Column`, `Row` o `Stack`.",
      "Ajustar la separación de un widget respecto a los bordes de la pantalla o de su contenedor padre.",
      "Mejorar la legibilidad y la estética de la interfaz de usuario."
    ],
    "constructores_comunes": [
      "Padding({Key? key, required EdgeInsetsGeometry padding, Widget? child})"
    ],
    "widgets_relacionados": [
      "SizedBox",
      "Container",
      "Margin (aunque `Container` con `margin` es el equivalente común)"
    ],
    "cuando_no_usar": "No uses `Padding` si el espaciado es parte inherente del diseño de un widget personalizado (donde podrías dibujar el padding directamente). Para espaciados simples entre elementos en un `Row` o `Column`, a veces `SizedBox` con `width` o `height` puede ser una alternativa más explícita.",
    "codigo": "Padding(\n  padding: const EdgeInsets.all(12.0),\n  child: Text(\n    'Este texto tiene padding por todos lados.',\n    style: TextStyle(fontSize: 18),\n  ),\n);",
    "imagen": "assets/Padding.jpg",
    "ruta": "/Page_Padding"
  },
    """