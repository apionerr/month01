'''
    Fun with list and functions and error handeling
    ---Not Completed, active doc--- 2/9/2014
    Objective: Work through the various methods of list
'''

first_names = ["Drew", "Jeremy", "Landon", "Danny"]

last_names = []
def append_name(l):
    def ifappended(n=""):
        for name in first_names:
                if len(l) == 0:
                    continue
                else:
                    last_names.append("{} Prescott".format(name))
        if n != "":
            last_names.append("{} Prescott".format(n))
            return last_names
        else:
            return last_names
    return ifappended

drew = append_name(last_names)

try:
    drew().remove("Drew Pres")
except ValueError:
    drew("Peter")
    print "List has been append"

print drew()
