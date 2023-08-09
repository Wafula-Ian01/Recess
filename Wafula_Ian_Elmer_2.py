#Recess Day 2: Session 1

#Control flow
x=input("How old are you? \n")
x=int(x)

#Using ifs
if(x<18):
    print("You are a minor.")

elif(x>=18 and x<65):
    print("You are an adult.")

else:
    print("You are a senoir citizen.")
    

#For Loops

cars=["Audi", "Toyota", "Honda", "Mercedes", "BMW"]

for car in cars:
    print(f"{car} is a car type." )


fruits=["Guava", "Mango", "Pineapple", "Guava"]

while(len(fruits)>0):
    print(f"{fruits[0]} is a fruit.")
    fruits.pop(0)
    
    
#Break and Continue
numbers=[1,3,45,3,5,2,31,5,46]
count=0

while count<len(numbers):
    if count==4:
        count+=1
        continue
    elif count==6:
        break
    print(numbers[count])
    count+=1
    
#Catching Exceptions
try:
    print(numbers[12])
    
except Exception as Error:
    print("Error: Index out of bound item cannot be printed.")
    
finally:
    print("Please enter value within bound.")
    
    
try:
    x=(input("How old are you?"))

except Exception as e:
    print("Error:f{e.__class__.__name__} has occurred")
    
finally:
    print ("Expression has been assessed.")    
    
    


#Dictionaries
#Assignment: Write a program toask a student about their mental health.
State={
    1:"Please go for immediate help!",
    2:"Talk to a person it could seem helpful",
    3:"You need to free up a little",
    4:"Take a break from work",
    5:"Take a deep breath",
    6:"Just do not over flex it will wear you out",
    7:"You are currently doing well.",
    8:"With this vibe you will be unstoppable",
    9:"Chances are high success is guaranteed",
    10:"Perfect, excellent.",
}

state=int(input("On a scale of 1 to 10 could you please tell me your level of satisfaction, \n"))
#state=int(state)
if state<=10:
    print(State[state])
    
else:
    print("Sorry, I'm unable to understand your current situation.")
    
    
    
#Sets
student_Numbers={12,44, 344, 2334, 32}
names={"Wafula", "Ian", "Elmer", "Philly"}

print("ID No:",student_Numbers)
print(type(student_Numbers))

#empty_set=set()
print(names)
names.add("Simon")#adding an item to a set
print(names)
names.add("Jack")#adding an item to a set
print(names)

mixed=student_Numbers.union(names)
#Alt
mixed= student_Numbers|names
print(mixed) #Combines two sets to make one

for mix in mixed:
    print (mix)



print(len(student_Numbers))

#updating a set
languages=["Python", "R", 'Java']


#Day 2: Session 2
#EXE 1

val= "Hello World"
print(len(val))     #length of a string
for letter in val:     #Looping through a string
    print(letter)
    
    
#Dictionary

dict={
    "name":"Samsung",
    "model":"Galaxy  S22 Ultra",
    "mfg date":  "2022"
}

#Exe 2
values= dict.values()
print(list(values)) #Lists values of a dictionary

keys= dict.keys()
print(list(keys))#Lists keys of the dictionary

if "name" in dict.keys():
    print("Available")

#updating a value in the dictionary
dict["model"]= "iPhone"
print(dict)

#removing a key value pair from the dictionary 
dict.pop("mfg date")

print(dict)

#iterating through the dictionary
for key, value in dict.items():
    print(f"{key}:{value} ") #prints the key pair values in the dictionary
    
#Nesting a dictionary
dictionary_nested={"First":{1:"Date",3:"Month",43:"year",6:"Time"}, "Second":{23:"Weather",67:"Climate",12:"Rainfall",56:"Season"}}

print(dictionary_nested["First"][1])
print(dictionary_nested["Second"][67])