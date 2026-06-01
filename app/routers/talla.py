from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/tallas", tags=["tallas"])

@router.post("/", response_model=schemas.Talla)
def create_talla(talla: schemas.TallaCreate, db: Session = Depends(get_db)):
    return crud.create_talla(db=db, talla=talla)

@router.get("/", response_model=list[schemas.Talla])
def read_tallas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tallas = crud.get_tallas(db, skip=skip, limit=limit)
    return tallas

@router.get("/{talla_id}", response_model=schemas.Talla)
def read_talla(talla_id: int, db: Session = Depends(get_db)):
    db_talla = crud.get_talla(db, talla_id=talla_id)
    if db_talla is None:
        raise HTTPException(status_code=404, detail="Talla not found")
    return db_talla

@router.put("/{talla_id}", response_model=schemas.Talla)
def update_talla(talla_id: int, talla: schemas.TallaUpdate, db: Session = Depends(get_db)):
    db_talla = crud.get_talla(db, talla_id=talla_id)
    if db_talla is None:
        raise HTTPException(status_code=404, detail="Talla not found")
    return crud.update_talla(db=db, talla_id=talla_id, talla=talla)

@router.delete("/{talla_id}", response_model=schemas.Talla)
def delete_talla(talla_id: int, db: Session = Depends(get_db)):
    db_talla = crud.get_talla(db, talla_id=talla_id)
    if db_talla is None:
        raise HTTPException(status_code=404, detail="Talla not found")
    return crud.delete_talla(db=db, talla_id=talla_id)