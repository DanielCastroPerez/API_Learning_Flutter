from typing import List
from config.db import get_db
from models.tablas_flutter import *
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schemas.model_flutter import *

routes = APIRouter()


# WIDGET_CLASS ENDPOINTS

@routes.get("/get_widgets", response_model=List[WidgetResponse])
def get_all_widgets(db: Session = Depends(get_db)):
    widgets = db.query(Widget_class).all()
    return widgets

@routes.get("/widget_by_id/{id}", response_model=WidgetResponse)
def get_widget_by_id(id: int, db: Session = Depends(get_db)):
    widget = db.query(Widget_class).filter(Widget_class.id == id).first()
    if not widget:
        raise HTTPException(status_code=404, detail="Widget no encontrado")
    return widget

@routes.post("/create_widget", response_model=WidgetResponse)
def create_widget(data: WidgetCreate, db: Session = Depends(get_db)):
    nuevo_widget = Widget_class(**data.dict())
    db.add(nuevo_widget)
    db.commit()
    db.refresh(nuevo_widget)
    return nuevo_widget

@routes.put("/update_widget/{id}", response_model=WidgetResponse)
def update_widget(id: int, data: WidgetCreate, db: Session = Depends(get_db)):
    widget = db.query(Widget_class).filter(Widget_class.id == id).first()
    if not widget:
        raise HTTPException(status_code=404, detail="Widget no encontrado")
    for key, value in data.dict().items():
        setattr(widget, key, value)
    db.commit()
    db.refresh(widget)
    return widget

@routes.delete("/delete_widget/{id}")
def delete_widget(id: int, db: Session = Depends(get_db)):
    widget = db.query(Widget_class).filter(Widget_class.id == id).first()
    if not widget:
        raise HTTPException(status_code=404, detail="Widget no encontrado")
    db.delete(widget)
    db.commit()
    return {"message": "Widget eliminado"}



# PROPIEDAD DETALLADA ENDPOINTS

@routes.get("/get_propiedades", response_model=List[PropiedadDetalladaResponse])
def get_all_propiedades(db: Session = Depends(get_db)):
    propiedades = db.query(PropiedadDetallada).all()
    return propiedades

@routes.get("/get_propiedad/{id}", response_model=PropiedadDetalladaResponse)
def get_propiedad(id: int, db: Session = Depends(get_db)):
    propiedad = db.query(PropiedadDetallada).filter(PropiedadDetallada.id == id).first()
    if not propiedad:
        raise HTTPException(status_code=404, detail="Propiedad no encontrada")
    return propiedad

@routes.post("/create_propiedad", response_model=PropiedadDetalladaResponse)
def create_propiedad(data: PropiedadDetalladaCreate, db: Session = Depends(get_db)):
    new_propiedad = PropiedadDetallada(**data.dict())
    db.add(new_propiedad)
    db.commit()
    db.refresh(new_propiedad)
    return new_propiedad

@routes.put("/update_propiedad/{id}", response_model=PropiedadDetalladaResponse)
def update_propiedad(id: int, data: PropiedadDetalladaCreate, db: Session = Depends(get_db)):
    propiedad = db.query(PropiedadDetallada).filter(PropiedadDetallada.id == id).first()
    if not propiedad:
        raise HTTPException(status_code=404, detail="Propiedad no encontrada")
    for field, value in data.dict().items():
        setattr(propiedad, field, value)
    db.commit()
    db.refresh(propiedad)
    return propiedad

@routes.delete("/delete_propiedad/{id}")
def delete_propiedad(id: int, db: Session = Depends(get_db)):
    propiedad = db.query(PropiedadDetallada).filter(PropiedadDetallada.id == id).first()
    if not propiedad:
        raise HTTPException(status_code=404, detail="Propiedad no encontrada")
    db.delete(propiedad)
    db.commit()
    return {"message": "Propiedad eliminada"}



# USO COMUN ENDPOINTS

@routes.get("/get_usos", response_model=List[UsoComunResponse])
def get_all_usos(db: Session = Depends(get_db)):
    usos = db.query(UsoComun).all()
    return usos

@routes.post("/create_uso", response_model=UsoComunResponse)
def create_uso(data: UsoComunCreate, db: Session = Depends(get_db)):
    nuevo_uso = UsoComun(**data.dict())
    db.add(nuevo_uso)
    db.commit()
    db.refresh(nuevo_uso)
    return nuevo_uso



# CONSTRUCTOR COMUN ENDPOINTS

@routes.get("/get_constructores", response_model=List[ConstructorComunResponse])
def get_all_constructores(db: Session = Depends(get_db)):
    constructores = db.query(ConstructorComun).all()
    return constructores

@routes.post("/create_constructor", response_model=ConstructorComunResponse)
def create_constructor(data: ConstructorComunCreate, db: Session = Depends(get_db)):
    nuevo_constructor = ConstructorComun(**data.dict())
    db.add(nuevo_constructor)
    db.commit()
    db.refresh(nuevo_constructor)
    return nuevo_constructor



# WIDGET RELACIONADO ENDPOINTS

@routes.get("/get_relacionados", response_model=List[WidgetRelacionadoResponse])
def get_all_widgets_relacionados(db: Session = Depends(get_db)):
    relacionados = db.query(WidgetRelacionado).all()
    return relacionados

@routes.post("/create_widget_relacionado", response_model=WidgetRelacionadoResponse)
def create_widget_relacionado(data: WidgetRelacionadoCreate, db: Session = Depends(get_db)):
    nuevo_widget = WidgetRelacionado(**data.dict())
    db.add(nuevo_widget)
    db.commit()
    db.refresh(nuevo_widget)
    return nuevo_widget
