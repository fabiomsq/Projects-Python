import random

def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.

    t: list

    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()


    d = []

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            d.append(s[i])
            #return True
    return d


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    #s = [][]
    for i in range(num_simulations):
        t = random_bdays(num_students)
        d = has_duplicates(t)
        l = len(d)
        if (l > 0):
            #s.append(i,d)
            print ('The iteration %d' % i, 'has', l, 'duplications:', 'values', d)
            #print (d)
    #         print ('The iteration' i 'has duplicates)
    #         count += 1
    #return s


def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 25
    num_simulations = 1000


    print ('****** SUMMARY ******')

    print('-> with %d students' % num_students)
    print('-> After %d iterations' % num_simulations)
    count_matches(num_students, num_simulations)


    #print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()
