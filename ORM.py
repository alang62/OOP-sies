from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///employeetype.db', echo=False)


Base = declarative_base()


class PartTimeEmployee(Base):
    __tablename__ = 'part_time_employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    wage = Column(Float)

    def __repr__(self):
        return f'<PartTimeEmployee(id={self.id}, name={self.first_name} {self.last_name}, wage={self.wage})>'


class FullTimeEmployee(Base):
    __tablename__ = 'full_time_employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    salary = Column(Float)

    def __repr__(self):
        return f'<FullTimeEmployee(id={self.id}, name={self.first_name} {self.last_name}, salary={self.salary})>'


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


pte = PartTimeEmployee(first_name='Joe', last_name='Schmoe', wage=18.00)


session.add(pte)
session.commit()


part_time_employees = session.query(PartTimeEmployee).all()


for employee in part_time_employees:
    print(employee)

fte = FullTimeEmployee(first_name='Jim', last_name='Jefferson', salary=50000.00)


session.add(pte)
session.add(fte)
session.commit()


employees = session.query(PartTimeEmployee, FullTimeEmployee).all()


for part_time_employee, full_time_employee in employees:
    print(part_time_employee)
    print(full_time_employee)
    