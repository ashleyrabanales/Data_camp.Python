
# %%
import numpy as py
# %%
type(bmi) # specific type of variable
#float, loating point: a number that has both an integer and fractional part, separated by a point.
#int -  integer: a number without a fractional part.
#str - A string is Python's way to represent text
# Bool -  boolean: a type to represent logical values. Can only be True or False (the capitalization is important!).

#python list
fam = [1.73, 1.68, 1.72, 1.89]

#adding strings to name
fam2= [["a", 1.73],
        ["b", 1.68],
        ["e", 1.72], 
        ["w", 1.89]]
print(fam2)

#or
#%%
a = 1.73,
b = 1.68
e = 1.72,
w = 1.89
#%%
fam4 = ["ash", a,
        "bob", b,
        "ellie", e,
        "will", w]

# %%
########## LISTS ####################
#Select the valid list, 
#Can you tell which ones of the following lines of Python code are valid ways to build a list?
[1, 3, 4, 2] 
[[1, 2, 3], [4, 5, 7]] 
[1 + 2, "a" * 5, 3] 
# all are lists
# area variables (in square meters)
#%%
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

#%%
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
#%%
# Print out the type of house
print(type(house))
#%%

######### Subsetting List ###############
#%%
fam2= [["a", 1.73],
        ["b", 1.68],
        ["e", 1.72], 
        ["w", 1.89]]
fam2[3] #selecting list 
fam2[-3] #selects the height




############## List Slicing #############
#example
fam2[3:5]
#print , [ start (inclusive) : end (exclusive)]
#syntax: the index you specify before the colon, 
# so where the slice starts, is included, while the index 
# you specify after the colon, where the slice ends, is not

fam2 [:4]#star from 0 till 4th

fam2[5:]
#If you leave out the index where the slice should end, 
# you include all elements up to and including the last element in the list, like here
#%%
#Practice
# Create the areas list
areas = 
["hallway", 11.25, 
"kitchen", 18.0, 
"living room", 20.0, 
"bedroom", 10.75, 
"bathroom", 9.50]
#%%
# Print out second element from areas list (it has the value 11.25).
print(areas[1])
#%%
# Print out last element from areas,  being 9.50. Using a negative index makes sense here!
print(areas[-1])
#%%
# Print out the area of the living room,the living room (20.0) and print it out.
print(areas[5])
#%%
# Create the areas list
areas = 
["hallway", 11.25, 
"kitchen", 18.0, 
"living room", 20.0, 
"bedroom", 10.75, 
"bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
#eat_sleep_area = [areas[3] +areas[-3]]
eat_sleep_area = (18.0 + 10.75)


# Print the variable eat_sleep_area
print(eat_sleep_area)
#%%
