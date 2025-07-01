from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import manager
from app.models.organization import Organization
from app.models.securitymanger import SecurityManager
from app.utils import auth

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
def signup(data: manager.ManagerSignup, db: Session = Depends(get_db)):
    org = db.query(Organization).filter_by(name=data.organization_name).first()
    if not org:
        org = Organization(name=data.organization_name)
        db.add(org)
        db.commit()
        db.refresh(org)

    if db.query(SecurityManager).filter_by(email=data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = auth.hash_password(data.password)
    manager = SecurityManager(
        name=data.name,
        email=data.email,
        password=hashed_pw,
        phone=data.phone,
        organization_id=org.organization_id
    )
    db.add(manager)
    db.commit()
    db.refresh(manager)
    return {"message": "Signup successful", "manager_id": manager.manager_id}


@router.post("/login")
def login(data: manager.ManagerLogin, db: Session = Depends(get_db)):
    manager = db.query(SecurityManager).filter_by(email=data.email).first()
    if not manager or not auth.verify_password(data.password, manager.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "manager_id": manager.manager_id}
