
# %%
import numpy as py
# %%
type(bmi) # specific type of variable
#float, loating point: a number that has both an integer and fractional part, separated by a point.
#int -  integer: a number without a fractional part.
#str - A string is Python's way to represent text
# Bool -  boolean: a type to represent logical values. Can only be True or False (the capitalization is important!).

######### 1.CREATING LIST python list
#Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
## area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)Print areas with the print() function.


######## 2. Create list with different types
 #Finish the code that creates the areas list. 
 # Build the list so that the list first contains
 # the name of each room as a string and then its area. 
 # In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, 
        "kitchen", kit, 
        "living room", liv, 
        "bedroom", bed, 
        "bathroom", bath]

# Print areas
print(areas)
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

######### Subsetting List ###############
#%%
fam2= [["a", 1.73],
        ["b", 1.68],
        ["e", 1.72], 
        ["w", 1.89]]
fam2[3] #selecting list 
fam2[-3] #selects the height



# %%
########## LISTS ####################
#Select the valid list, 
#Can you tell which ones of the following lines of Python code are valid ways to build a list?
[1, 3, 4, 2] 
[[1, 2, 3], [4, 5, 7]] 
[1 + 2, "a" * 5, 3] 
# all are lists
# area variables (in square meters)
        ########### List of Lists  ##########
#Instead of creating a flat list containing strings and floats, 
# representing the names and areas of the rooms in your house, you can create a list of lists. 
# The script in the editor can already give you an idea.
        #Instructions
#Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
#Print out house; does this way of structuring your data make more sense?
#Print out the type of house. Are you still dealing with a list?
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
#Don't get confused here: "hallway" is a string, while hall is a variable that represents the float 11.25 you specified earlier.


#############  SUBSET AND CONQUER  ###########
#%%
#Take the code sample below, which creates a list x and then selects "b" from it. Remember that this is the second element, 
# so it has index 1. You can also use negative indexing.
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!

#ex 1. 
#1. Print out the second element from the areas list (it has the value 11.25).
#2. Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
#3. Select the number representing the area of the living room (20.0) and print it out.
# Create the areas list
areas = ["hallway", 11.25, 
"kitchen", 18.0, 
"living room", 20.0, 
"bedroom", 10.75, 
"bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

#ex.2 
#Take this example, where the second and fourth element of a list x are extracted. 
# The strings that result are pasted together using the + operator:
x = ["a", "b", "c", "d"]
print(x[1] + x[3])

#1. Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
#2. Print the new variable eat_sleep_area.
#3. Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
#eat_sleep_area = [areas[3] +areas[-3]]
eat_sleep_area = (18.0 + 10.75)

########### SLICING AND DICING #########
#It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:
my_list[start:end]
#The start index will be included, while the end index is not.

#The code sample below shows an example. A list with "b" and "c", corresponding to indexes 1 and 2, are selected from a list x:
x = ["a", "b", "c", "d"]
x[1:3]
#The elements with index 1 and 2 are included, while the element with index 3 is not.
 #%%
#ex1. 
#1. Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
#2. Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
#3. Print both downstairs and upstairs using print().
# Create the areas list
areas = ["hallway", 11.25,
 "kitchen", 18.0, 
 "living room", 20.0, 
 "bedroom", 10.75, 
 "bathroom", 9.50]
#%%
# Use slicing to create downstairs
downstairs = areas[0:6]
# Use slicing to create upstairs
upstairs = areas[6:10]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
# %%
 ######## Slicing and dicing #2 ########
 #ex. 1
 #However, it's also possible not to specify these indexes. If you don't specify the begin index, 
 # Python figures out that you want to start your slice at the beginning of your list. If you don't specify the end index, 
 # the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:
x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]
#Create downstairs again, as the first 6 elements of areas. This time, simplify the slicing by omitting the begin index.
downstairs = areas[:6]
#Create upstairs again, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
upstairs = areas[6:]

#%%
########## Subsetting lists of lists ###########
#To subset lists of lists, you can use the same technique as before: square brackets. Try out the commands in the following 
# code sample in the IPython Shell:
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
#['g', 'h']

#x[2] results in a list, that you can subset again by adding additional square brackets.
#What will house[-1][1] return? house, the list of lists that you created before, is already defined for you in the workspace. 
        #A float: the bathroom area
# %%

