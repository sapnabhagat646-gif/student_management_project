from pydantic import BaseModel, EmailStr, Field, model_validator
from datetime import date
from typing import Optional


class StudentBaseSchemas(BaseModel):
    student_name: str = Field(min_length=2, max_length=100)
    student_dob: date
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=7, max_length=15)
    student_class: Optional[str] = None
    student_section: Optional[str] = None

    @model_validator(mode="after")
    def check_contact(self):
        if not self.email and not self.phone:
            raise ValueError("Enter an email address or phone number")
        if self.student_dob >= date.today():
            raise ValueError("Date of birth must be in the past")
        return self


class StudentCreate(StudentBaseSchemas):
    pass


class StudentUpdate(BaseModel):
    student_name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    student_dob: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=7, max_length=15)
    student_class: Optional[str] = None
    student_section: Optional[str] = None


class StudentResponse(StudentBaseSchemas):
    id: int

    class Config:
        from_attributes = True
