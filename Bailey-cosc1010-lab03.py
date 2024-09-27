# Mackenzie Bailey
# UWYO COSC 1010
# 26 September, 2024
# Lab 03 
# Lab Section: 13
# Sources, people worked with, help given to: 
## Used to figure out the reverse method: 
    # w3schools.com/python/ref_list_reverse.asp



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list

states = ['Wyoming', 'Colorado', 'Montana']

#print the entire list

print(states)

#now print the first element in the list

## Lists start at zero on the count!
print(states[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)

print(states[-1])


#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

## {} lets you add things in an f-string
print(f"{states[1].upper()} is south of {states[0].upper()}")


print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list

## sadly, .append() only takes one argument
states.append('Washington')
states.append('Oregon')
states.append('California')
print(states)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 

## -2 is used to guarrentee that it will always be the second to last element
states[-2] = "Maine"
print(states)

#Insert the state Texas to be the third element in the list, again printing your list

## as someone from Texas, no Texas should not be added, thanks.
## third element must be 2, since lists state indexing at 0 (0, 1, 2)
states.insert(2, 'Texas')
print(states)


#Using the `del` statement remove the fourth item from the list, print your list 

## fourth item (3) is currently Montana
del states[3]
print(states)


#Remove Texas using its value, print the list

## oh good, I get to remove it!
## Value = 'Texas'
## Index = 2
states.remove('Texas')
print(states)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 

print(sorted(states))
print(states)


#Permanently sort your list in reverse order, printing it out

## .sort() is permanent
## sorted() is temporary
states.sort(reverse = True)
print(states)


#Using the reverse method reverse the list and print it

states.reverse()
print(states)