import json
from sqlalchemy.orm import Session
from config.db import SessionLocal
from models.tablas_flutter import (
    Widget_class,
    PropiedadDetallada,
    UsoComun,
    ConstructorComun,
    WidgetRelacionado
)

# Cargar el JSON
with open("widgets_avanzado.json", "r", encoding="utf-8") as file:
    widgets_data = json.load(file)

# Iniciar sesión con la base de datos
db: Session = SessionLocal()

try:
    for widget in widgets_data:
        nuevo_widget = Widget_class(
            nombre=widget["nombre"],
            descripcion=widget["descripcion"],
            cuando_no_usar=widget["cuando_no_usar"],
            codigo=widget["codigo"],
            imagen=widget["imagen"],
            ruta=widget["ruta"]
        )
        db.add(nuevo_widget)
        db.flush()  # Para obtener el ID del widget antes de commit

        # Propiedades detalladas
        for prop in widget.get("propiedades_detalladas", []):
            propiedad = PropiedadDetallada(
                nombre=prop["nombre"],
                tipo=prop["tipo"],
                descripcion_extendida=prop["descripcion_extendida"],
                ejemplo_propiedad=prop["ejemplo_propiedad"],
                widget_id=nuevo_widget.id
            )
            db.add(propiedad)

        # Usos comunes
        for uso in widget.get("usos_comunes", []):
            uso_comun = UsoComun(
                descripcion=uso,
                widget_id=nuevo_widget.id
            )
            db.add(uso_comun)

        # Constructores comunes
        for constructor in widget.get("constructores_comunes", []):
            constructor_comun = ConstructorComun(
                firma=constructor,
                widget_id=nuevo_widget.id
            )
            db.add(constructor_comun)

        # Widgets relacionados
        for relacionado in widget.get("widgets_relacionados", []):
            relacionado_comun = WidgetRelacionado(
                nombre=relacionado,
                widget_id=nuevo_widget.id
            )
            db.add(relacionado_comun)

    db.commit()
    print("✅ Datos migrados correctamente desde widgets_avanzado.json")

except Exception as e:
    db.rollback()
    print(f"❌ Error durante la migración: {e}")

finally:
    db.close()
    