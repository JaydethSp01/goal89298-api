from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/alertas", tags=["alertas"])

@router.post("/", response_model=schemas.Alerta)
def create_alerta(alerta: schemas.AlertaCreate, db: Session = Depends(get_db)):
    return crud.create_alerta(db=db, alerta=alerta)

@router.get("/", response_model=list[schemas.Alerta])
def read_alertas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    alertas = crud.get_alertas(db, skip=skip, limit=limit)
    return alertas

@router.get("/{alerta_id}", response_model=schemas.Alerta)
def read_alerta(alerta_id: int, db: Session = Depends(get_db)):
    db_alerta = crud.get_alerta(db, alerta_id=alerta_id)
    if db_alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    return db_alerta

@router.put("/{alerta_id}", response_model=schemas.Alerta)
def update_alerta(alerta_id: int, alerta: schemas.AlertaUpdate, db: Session = Depends(get_db)):
    db_alerta = crud.get_alerta(db, alerta_id=alerta_id)
    if db_alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    return crud.update_alerta(db=db, alerta_id=alerta_id, alerta=alerta)

@router.delete("/{alerta_id}", response_model=schemas.Alerta)
def delete_alerta(alerta_id: int, db: Session = Depends(get_db)):
    db_alerta = crud.get_alerta(db, alerta_id=alerta_id)
    if db_alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    return crud.delete_alerta(db=db, alerta_id=alerta_id)