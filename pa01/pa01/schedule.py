'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    # pylint:disable=pointless-string-statement
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        # pylint:disable=line-too-long
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        # pylint:disable=missing-function-docstring
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        print("can't sort by "+str(field)+" yet")
        return self

    def title(self, phrase):
        ''' title filters the courses by phrases in the course names'''
        return Schedule([c for c in self.courses if phrase in c['name']])

    def description(self, phrase):
        ''' description filters the courses by phrase in the descriptions '''
        return Schedule([course for course in self.courses if phrase in course['description']])

    '''
        create our own filters
    '''
    def start_time(self, start_time):
        ''' startTime filters the courses by the given start time'''
        # pylint:disable=line-too-long
        return Schedule([course for course in self.courses if len(course['times']) != 0 and course['times'][0]['start'] == start_time])

    def list_courses(self):
        ''' listCourses prints the first ten courses of self.courses'''
        # pylint:disable=consider-using-enumerate
        for i in range(len(self.courses)):
            print(self.courses[i], '\n')

    def independent_study(self, subject):
        '''List independent course of under a specific subject '''
        # pylint:disable=line-too-long
        return Schedule([course for course in self.courses if course['subject'] == str(subject) and course['independent_study']])
# if __name__ == "__main__":
#     test = Schedule()
#     test.load_courses()
#     test = test.enrolled(range(5,1000))
#     test = test.lastname("Thomas")
#     test = test.independent_study('MATH')
#     test = test.start_time(570)
#     test.list_courses()
    