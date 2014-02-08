#-- Naming with closure nested function V.01 - Drew Prescott
def names(u):
    name = []
    for i in range(1, int(u)):
        name.append(raw_input("name:"))

    return name

nameing = names(7)                                                              #How many names do you want to cycle through

def name_list():                                                                #List of names to itterate through
    namecheck = ["Drew", "Mallory", "Landon", "Jeremy"]                         #Approved first names
    def find(n):                                                                #Inside Function - takes iteration of names pass from line 26
        i = 0
        while i <= len(namecheck) - 1:                                          #go through name check so many times
            if namecheck[i] == n:                                               #if the i name check is equal to the name passed through
                return namecheck[i]                                             #If it's approved give it back
            i += 1
    return find                                                                 #Return the value namecheck from name_list

find_name = name_list()                                                         #find_name is find(n)

def assing_last(name_arr):                                                      #Append all names if they are prescott
    approved = []                                                               #Create a list for the data
    for name in name_arr:                                                       #If the passed through name is in name_arr
        if name == find_name(name):                                                 #if that name, passed through the findname function, is a prescott
            approved.append(name + " Prescott")                                     #append the list
        else:
            approved.append(name + " is not Prescott")                              #append the list with the not a prescott verbiage
    return approved                                                                 #return the list



hey = assing_last(nameing)

print "\n".join(hey)

