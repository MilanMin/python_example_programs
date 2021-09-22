"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc=False):
    """ Return the largest element of a sequence a.
    """

    if(loc):
        return (max(a), a.index(max(a)))
    return max(a)


if __name__ == "__main__":

    a = [1,2,3,2,1]
    print("Largest element is {:}".format(largest_element(a)))
