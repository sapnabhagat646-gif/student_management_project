from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student
from app.schemas import StudentResponse, StudentUpdate

router = APIRouter(prefix="/students", tags=["Students"])


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    data = student_data.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(student, key, value)

    if not student.email and not student.phone:
        raise HTTPException(
            status_code=422,
            detail="Student must have an email address or phone number",
        )

    try:
        db.commit()
        db.refresh(student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email or phone number already exists",
        )

    return student
