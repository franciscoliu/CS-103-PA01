'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
# import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
start time (filter by start time of the course)
independent stutdy (filter by the independent study course with the provided subjects)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    # pylint:disable=too-many-branches
    # pylint:disable=no-else-return
    # pylint:disable=global-statement
    # pylint:disable=invalid-name
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['i','instructor']:
            instructor = input("enter a instructor:")
            schedule = schedule.lastname(instructor)
        elif command in ['t','title']:
            title = input("enter a title:")
            schedule = schedule.title(title)
        elif command in ['d','description']:
            temp = input("enter a description:")
            schedule = schedule.description(temp)
        elif command in ['st','start time']:
            time = input("enter a start time:")
            schedule = schedule.start_time(int(time))
        elif command in ['in', 'independent study']:
            subject = input("enter a subject (eg: MATH, BIO):")
            schedule = schedule.independent_study(subject)
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])
    # This line is for tesing

if __name__ == '__main__':
    topmenu()
