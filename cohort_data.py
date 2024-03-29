"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    data = open(filename).read().split('\n')
    houses_lst = []
    for i in data:
        try:
            if(i.split('|')[2]):
                houses_lst.append(i.split('|')[2])

        except IndexError:
            pass

    houses = set(houses_lst)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    data = open(filename).read().split('\n')
    students = []
    try:
        if cohort == 'All':
            for i in data:
                students.append(i.split('|')[0] + ' ' + i.split('|')[1])
        for i in data:
            if(cohort == i.split('|')[4]):
                students.append(i.split('|')[0] + ' ' + i.split('|')[1])
    except IndexError:
        pass

    students = sorted(students)
    return students


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    data = open(filename).read().split('\n')
    for i in data:
        try:
            if i.split('|')[2] == "Dumbledore's Army":
                dumbledores_army.append(
                    i.split('|')[0] + ' ' + i.split('|')[1])
            if i.split('|')[2] == "Gryffindor":
                gryffindor.append(i.split('|')[0] + ' ' + i.split('|')[1])
            if i.split('|')[2] == 'Hufflepuff':
                hufflepuff.append(i.split('|')[0] + ' ' + i.split('|')[1])
            if i.split('|')[2] == 'Ravenclaw':
                ravenclaw.append(i.split('|')[0] + ' ' + i.split('|')[1])
            if i.split('|')[2] == 'Slytherin':
                slytherin.append(i.split('|')[0] + ' ' + i.split('|')[1])
            if i.split('|')[4] == 'G':
                ghosts.append(i.split('|')[0] + ' ' + i.split('|')[1])
            if i.split('|')[2] == 'I':
                instructors.append(i.split('|')[0] + ' ' + i.split('|')[1])
        except IndexError:
            pass

    dumbledores_army = sorted(dumbledores_army)
    gryffindor = sorted(gryffindor)
    hufflepuff = sorted(hufflepuff)
    ravenclaw = sorted(ravenclaw)
    slytherin = sorted(slytherin)
    ghosts = sorted(ghosts)
    instructors = sorted(instructors)

    return [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []
    # TODO: replace this with your code
    data = open(filename).read().split('\n')
    for i in data:
        student = tuple(i.split('|'))
        all_data.append(student)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    data = open(filename).read().split('\n')
    for i in data:
        if name == i.split('|')[0] + ' ' + i.split('|')[1]:
            return i.split('|')[4]


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    data = open(filename).read().split('\n')
    lastnames = []
    try:
        for i in data:
            lastnames.append(i.split('|')[1])
    except IndexError:
        pass

    uniq = set([x for x in lastnames if lastnames.count(x) > 1])
    return sorted(uniq)


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code
    data = open(filename).read().split('\n')
    housemates = []
    for i in data:
        try:
            if name == i.split('|')[0] + ' ' + i.split('|')[1]:
                house = i.split('|')[2]
        except IndexError:
            pass
    for i in data:
        try:
            if i.split('|')[2] == house:
                housemates.append(i.split('|')[0] + ' ' + i.split('|')[1])
        except IndexError:
            pass

    return housemates


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
