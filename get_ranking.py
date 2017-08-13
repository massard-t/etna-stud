# coding: utf-8
"""
Quick and dirty script allowing to get ranking per promotion
"""
import os
import operator
import statistics as s
import etnawrapper as etna

e = etna.EtnaWrapper(login='massar_t', password=os.environ.get('ETNAPASS'))

e.get_students(promotion=205)
resp = e.get_students(promotion=205)
students = resp['students']
logins = [e['login'] for e in students]

def get_notes(notes):
    return [e['student_mark'] for e in notes if not "jour" in e['activity_name'].lower()]

tots = []
for stud in logins:
    s_g = e.get_grades(login=stud)
    g = get_notes(s_g)
    tots.append({"login":stud, "mean":s.mean(g)})

final = sorted(tots, key=operator.itemgetter('mean'))

def get_b_login(log):
    for idx, st in enumerate(reversed(final)):
        #if st['login'] == log:
        print(idx+1, st['login'], st['mean'])

get_b_login('chaho_l')
