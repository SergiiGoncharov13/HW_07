from sqlalchemy import func, desc, select, and_

from pprint import pprint
from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session

"""
1 Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2 Знайти студента із найвищим середнім балом з певного предмета.
3 Знайти середній бал у групах з певного предмета.
4 Знайти середній бал на потоці (по всій таблиці оцінок).
5 Знайти які курси читає певний викладач.
6 Знайти список студентів у певній групі.
7 Знайти оцінки студентів у окремій групі з певного предмета.
8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
9 Знайти список курсів, які відвідує певний студент.
10 Список курсів, які певному студенту читає певний викладач.
"""


def select_1():
    result_1 = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result_1


def select_2(discipline_id):
    result_2 = session.query(Discipline.name,
                             Student.fullname,
                             func.round(func.avg(Grade.grade), 2).label('avg_grade')
                             ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return result_2


def select_3():
    result_3 = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label('avg_score')) \
        .select_from(Grade).join(Student, isouter=True).join(Discipline, isouter=True).join(Group, isouter=True) \
        .where(Grade.discipline_id == 1) \
        .group_by(Group.id, Discipline.id) \
        .order_by(desc('avg_score')) \
        .all()
    return result_3


def select_4():
    result_4 = session.query(func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade) \
        .all()
    return result_4


def select_5():
    result_5 = session.query(Teacher.fullname, Discipline.name) \
        .select_from(Discipline).join(Teacher) \
        .where(Teacher.id == 3) \
        .all()
    return result_5


def select_6():
    result_6 = session.query(Group.name, Student.fullname) \
        .select_from(Group).join(Student) \
        .where(Group.id == 2) \
        .all()
    return result_6


def select_7():
    result_7 = session.query(Group.name, Discipline.name, Student.fullname, Grade.grade) \
        .select_from(Grade).join(Student, isouter=True).join(Discipline, isouter=True).join(Group, isouter=True) \
        .where(Grade.discipline_id == 1) \
        .where(Group.id == 1) \
        .order_by(desc(Grade.grade)) \
        .all()
    return result_7


def select_8():
    result_8 = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade).join(Discipline, isouter=True).join(Teacher, isouter=True) \
        .where(Teacher.id == 3) \
        .group_by(Discipline.id, Teacher.fullname) \
        .all()
    return result_8


def select_9():
    result_9 = session.query(Student.fullname, Discipline.name) \
        .select_from(Grade).join(Discipline, isouter=True).join(Student, isouter=True) \
        .where(Student.id == 13) \
        .group_by(Discipline.id, Student.fullname) \
        .all()
    return result_9


def select_10():
    result_10 = session.query(Student.fullname, Discipline.name, Teacher.fullname) \
        .select_from(Grade).join(Discipline).join(Student).join(Teacher) \
        .where(Teacher.id == 3) \
        .where(Student.id == 13) \
        .group_by(Discipline.id, Student.id, Teacher.id) \
        .all()
    return result_10


if __name__ == "__main__":
    # pprint(select_1())
    # pprint(select_2(2))
    # pprint(select_3())
    # pprint(select_4())
    # pprint(select_5())
    # pprint(select_6())
    # pprint(select_7())
    # pprint(select_8())
    # pprint(select_9())
    pprint(select_10())
