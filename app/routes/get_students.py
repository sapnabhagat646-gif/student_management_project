from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student
from app.schemas import StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[StudentResponse])
def get_students(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    search: Optional[str] = None,
    student_class: Optional[str] = None,
    student_section: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Student)

    if search:
        query = query.filter(Student.student_name.ilike(f"%{search}%"))
    if student_class:
        query = query.filter(Student.student_class == student_class)
    if student_section:
        query = query.filter(Student.student_section == student_section)

    return query.order_by(Student.id).offset(skip).limit(limit).all()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
