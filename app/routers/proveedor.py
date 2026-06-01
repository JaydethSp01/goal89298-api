from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/proveedores", tags=["proveedores"])

@router.post("/", response_model=schemas.Proveedor)
def create_proveedor(proveedor: schemas.ProveedorCreate, db: Session = Depends(get_db)):
    return crud.create_proveedor(db=db, proveedor=proveedor)

@router.get("/", response_model=list[schemas.Proveedor])
def read_proveedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    proveedores = crud.get_proveedores(db, skip=skip, limit=limit)
    return proveedores

@router.get("/{proveedor_id}", response_model=schemas.Proveedor)
def read_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return db_proveedor

@router.put("/{proveedor_id}", response_model=schemas.Proveedor)
def update_proveedor(proveedor_id: int, proveedor: schemas.ProveedorUpdate, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return crud.update_proveedor(db=db, proveedor_id=proveedor_id, proveedor=proveedor)

@router.delete("/{proveedor_id}", response_model=schemas.Proveedor)
def delete_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return crud.delete_proveedor(db=db, proveedor_id=proveedor_id)