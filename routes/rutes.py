from typing import List
from config.db import get_db
from models.tablas_flutter import *
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schemas.model_flutter import *

routes = APIRouter()


# WIDGET_CLASS ENDPOINTS

@routes.get("/get_widgets", response_model=List[WidgetResponse], tags=["widgets"])
def get_all_widgets(db: Session = Depends(get_db)):
    consulta = db.query(Widget_class)
    print(str(consulta.statement))  
    widgets = consulta.all()
    if not widgets:
        raise HTTPException(status_code=404, detail="No hay widgets para mostrar")
    return widgets

@routes.get("/widget_by_id/{id}", response_model=WidgetResponse , tags=["widgets"])
def get_widget_by_id(id: int, db: Session = Depends(get_db)):
    widget = db.query(Widget_class).filter(Widget_class.id == id).first()
    if not widget:
        raise HTTPException(status_code=404, detail="Widget no encontrado")
    return widget

@routes.post("/create_widget", response_model=WidgetResponse , tags=["widgets"])
def create_widget(data: WidgetCreate, db: Session = Depends(get_db)):
    nuevo_widget = Widget_class(**data.dict())
    db.add(nuevo_widget)
    db.commit()
    db.refresh(nuevo_widget)
    return nuevo_widget

@routes.put("/update_widget/{id}", response_model=WidgetResponse , tags=["widgets"])
def update_widget(id: int, data: WidgetCreate, db: Session = Depends(get_db)):
    widget = db.query(Widget_class).filter(Widget_class.id == id).first()
    if not widget:
        raise HTTPException(status_code=404, detail="Widget no encontrado")
    for key, value in data.dict().items():
        setattr(widget, key, value)
    db.commit()
    db.refresh(widget)
    return widget

@routes.delete("/delete_widget/{id}", tags=["widgets"])
def delete_widget(id: int, db: Session = Depends(get_db)):
    widget = db.query(Widget_class).filter(Widget_class.id == id).first()
    if not widget:
        raise HTTPException(status_code=404, detail="Widget no encontrado")
    db.delete(widget)
    db.commit()
    return {"message": "Widget eliminado"}



# PROPIEDAD DETALLADA ENDPOINTS

@routes.get("/get_propiedades", response_model=List[PropiedadDetalladaResponse], tags=["propiedades"])
def get_all_propiedades(db: Session = Depends(get_db)):
    propiedades = db.query(PropiedadDetallada).all()
    return propiedades

@routes.get("/get_propiedad/{id}", response_model=PropiedadDetalladaResponse, tags=["propiedades"])
def get_propiedad(id: int, db: Session = Depends(get_db)):
    propiedad = db.query(PropiedadDetallada).filter(PropiedadDetallada.id == id).first()
    if not propiedad:
        raise HTTPException(status_code=404, detail="Propiedad no encontrada")
    return propiedad

@routes.post("/create_propiedad", response_model=PropiedadDetalladaResponse, tags=["propiedades"])
def create_propiedad(data: PropiedadDetalladaCreate, db: Session = Depends(get_db)):
    new_propiedad = PropiedadDetallada(**data.dict())
    db.add(new_propiedad)
    db.commit()
    db.refresh(new_propiedad)
    return new_propiedad

@routes.put("/update_propiedad/{id}", response_model=PropiedadDetalladaResponse, tags=["propiedades"])
def update_propiedad(id: int, data: PropiedadDetalladaCreate, db: Session = Depends(get_db)):
    propiedad = db.query(PropiedadDetallada).filter(PropiedadDetallada.id == id).first()
    if not propiedad:
        raise HTTPException(status_code=404, detail="Propiedad no encontrada")
    for field, value in data.dict().items():
        setattr(propiedad, field, value)
    db.commit()
    db.refresh(propiedad)
    return propiedad

@routes.delete("/delete_propiedad/{id}",tags=["propiedades"])
def delete_propiedad(id: int, db: Session = Depends(get_db)):
    propiedad = db.query(PropiedadDetallada).filter(PropiedadDetallada.id == id).first()
    if not propiedad:
        raise HTTPException(status_code=404, detail="Propiedad no encontrada")
    db.delete(propiedad)
    db.commit()
    return {"message": "Propiedad eliminada"}



# USO COMUN ENDPOINTS

@routes.get("/get_usos", response_model=List[UsoComunResponse], tags=["usos"])
def get_all_usos(db: Session = Depends(get_db)):
    usos = db.query(UsoComun).all()
    return usos

@routes.get("/get_UsoComun_by_id/{id}", response_model=UsoComunResponse, tags=["usos"])
def get_UsoComun_by_id(id: int, db: Session = Depends(get_db)):
    uso = db.query(UsoComun).filter(UsoComun.id == id).first()
    if not uso:
        raise HTTPException(status_code=404, detail="Uso común no encontrado")
    return uso

@routes.post("/create_uso", response_model=UsoComunResponse, tags=["usos"])
def create_uso(data: UsoComunCreate, db: Session = Depends(get_db)):
    nuevo_uso = UsoComun(**data.dict())
    db.add(nuevo_uso)
    db.commit()
    db.refresh(nuevo_uso)
    return nuevo_uso



# CONSTRUCTOR COMUN ENDPOINTS

@routes.get("/get_constructores", response_model=List[ConstructorComunResponse], tags=["constructores"])
def get_all_constructores(db: Session = Depends(get_db)):
    constructores = db.query(ConstructorComun).all()
    return constructores

@routes.get("/get_ConstructorComun_by_id/{id}", response_model=ConstructorComunResponse, tags=["constructores"])
def get_ConstructorComun_by_id(id: int, db: Session = Depends(get_db)):
    constructor = db.query(ConstructorComun).filter(ConstructorComun.id == id).first()
    if not constructor:
        raise HTTPException(status_code=404, detail="Constructor común no encontrado")
    return constructor

@routes.post("/create_constructor", response_model=ConstructorComunResponse, tags=["constructores"])
def create_constructor(data: ConstructorComunCreate, db: Session = Depends(get_db)):
    nuevo_constructor = ConstructorComun(**data.dict())
    db.add(nuevo_constructor)
    db.commit()
    db.refresh(nuevo_constructor)
    return nuevo_constructor



# WIDGET RELACIONADO ENDPOINTS

@routes.get("/get_relacionados", response_model=List[WidgetRelacionadoResponse], tags=["relacionados"] )
def get_all_widgets_relacionados(db: Session = Depends(get_db)):
    relacionados = db.query(WidgetRelacionado).all()
    return relacionados

@routes.get("/get_WidgetRelacionado_by_id/{id}", response_model=WidgetRelacionadoResponse, tags=["relacionados"] )
def get_WidgetRelacionado_by_id(id: int, db: Session = Depends(get_db)):
    relacionado = db.query(WidgetRelacionado).filter(WidgetRelacionado.id == id).first()
    if not relacionado:
        raise HTTPException(status_code=404, detail="Widget relacionado no encontrado")
    return relacionado

@routes.post("/create_widget_relacionado", response_model=WidgetRelacionadoResponse, tags=["relacionados"] )
def create_widget_relacionado(data: WidgetRelacionadoCreate, db: Session = Depends(get_db)):
    nuevo_widget = WidgetRelacionado(**data.dict())
    db.add(nuevo_widget)
    db.commit()
    db.refresh(nuevo_widget)
    return nuevo_widget
