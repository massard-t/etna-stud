# coding: utf-8
"""
Quick and dirty script allowing to get ranking per promotion
"""
import os
import operator
import statistics as s
import etnawrapper as etna


ANAME = 'activity_name'
MARK = 'student_mark'


def get_notes(notes):
    """Returns filtered student grades"""
    return [ewrp[MARK] for ewrp in notes if 'jour' not in ewrp[ANAME].lower()]


def get_b_login(final, **kwargs):
    """Prints student stats"""
    should_check = kwargs.get('check')
    login = kwargs.get('login')
    for idx, stud in enumerate(reversed(final)):
        if should_check and stud['login'] != login:
            continue
        print(idx + 1, stud['login'], stud['mean'])


def main():
    """Main function"""
    login = os.environ.get('ETNAUSER')
    password = os.environ.get('ETNAPASS')
    promotion = os.environ.get('PROMOTION', 205)

    ewrp = etna.EtnaWrapper(
        login=login,
        password=password
    )

    resp = ewrp.get_students(promotion=promotion)
    students = resp['students']
    logins = [ewrp['login'] for ewrp in students]

    tots = []
    for stud in logins:
        student_grades = ewrp.get_grades(login=stud)
        grades = get_notes(student_grades)
        stud_mean = s.mean(grades)
        tots.append({
            'login': stud,
            'mean': stud_mean
        })

    final = sorted(tots, key=operator.itemgetter('mean'))
    get_b_login(final, login='login')

if __name__ == '__main__':
    main()
