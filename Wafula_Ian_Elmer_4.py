#Exercise # -*- coding: latin-1 -*-
#1
names= ["Wafula", "Ian", "Elmer", "Paul","Joseph"]

print(names[1])

#2
names[0]="Vincent"
print(names)

#3
names.append("Benon")
print(names)

#4
names[2]="Bathel"
print(names)

#5
del names[3]
print(names)

#6
print(names[-1])

#7
my_list=[12, 44, 35, 82, 86, 56, 67]
print(my_list[2:5])

#8
countries=["Uganda", "Kenya", "Tanzania", "Rwanda", "South Africa"]

my_countries= countries.copy()
print(my_countries)

#9
for country in countries:
    print (country)
    
#10
animals=["lion", "cheetah", "leopard", "panther", "lynx"]
#descending
animals.sort()
print(animals)

#ascending
animals.sort(reverse=1)
print(animals)

#11
for animal in animals:
    if 'a' in animal:
        print(animal)
        
#12
firstnames=["John", "Bruce", "Clark", "Tony"]
lastnames=["Constantine", "Wayne", "Kent", "Stark"]

allnames= firstnames + lastnames

#Exercise 2
#1
x=("samsung", "iphone", "tecno", "redmi")

for phone in x:
    if phone=="iphone":
        print(phone)
        
#2
print(x[-3])

#3
y= list(x)
y[1]= "itel"

x= tuple(y)
print(x)

#4
h=list(x)
h.append("hauwei")

x= tuple(h)
print(x)

#5
for phone in x:
    print (phone)

#6
a=list(x)
del a[0]
print(a)
x= tuple(a)
print(x)

#7
t=["Kampala", "Jinja", "Wakiso", "Gulu", "Fort_Portal"]
Tuple= tuple(t)
print(Tuple)

#8
(Capital, East, Central, North, West)= Tuple

print(Capital)
print(East)
print(Central)
print(North)
print(West)

#9
print(Tuple[1:4])

#10
firstnames=("John", "Bruce", "Clark", "Tony")
lastnames=("Constantine", "Wayne", "Kent", "Stark")

Combined= firstnames + lastnames
print(Combined)

#11
colors=("black", "yellow", "red", "green", "orange", "purple")
multi= colors*3
print(multi)

#12
thistuple=(1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))


#Exercise 3
#1
beverages= set(("stoney","apple cidar","orange"))
print(beverages)

#2
beverages.add("pineapple")
beverages.add("passion")
print(beverages)

#3
mySet={"oven", "kettle", "microwave", "refrigerator"}

if "refrigerator" in mySet:
    print("Refrigirator is in", mySet)
    
    
#4
if "kettle" in mySet:
    mySet.remove("kettle")
    print(mySet)
    
#5
mySet={"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)
    
#6
MySet={"Uganda", "Kenya", "Tanzania", "Rwanda"}
MyList=["Kampala", "Nairobi"]

Set=set().union(MyList)
print(Set)
uniSet= MySet.union(Set)
print(uniSet)

#7
names={"Wafula", "Ian", "Elmer"}
ages={6, 3, 5}

combo=names.union(ages)
print(combo)

#Exercis 4
#1
Integer= 23
String= " Wafula"
Strint=str(Integer) + String
print(Strint)

#2
txt="   Hello,    Uganda!   "
String= txt.strip(" ").replace(" ", "")
print(String)

#3
S= txt.upper()
print(S)

#4
print(S.replace('U', 'V'))

#5
y="I am proudly Ugandan"
x=[*y]
print(x[1:4])

 
#6
x="All\"Data Scientists\" are cool"


#Exercise 5
#1
Shoes={
    "brand":"Nick",
    "color":"black",
    "size":40
}

print("The shoe size is",Shoes["size"])

#2
Shoes["brand"]= "Adidas"
print(Shoes)

#3
Shoes["type"]= "sneakers"
print(Shoes)


#4
keys=Shoes.keys()
print(list(keys))

#5
values=Shoes.values()
print(list(values))

#6
if "size" in Shoes.items():
    print("It is existent")
    
else: print("Its non existent")

#7
for key, value in Shoes.items():
    print(f"{key}:{value}")
    
    
#8
Shoes.pop("color")
print(Shoes)

#9
Shoes.clear()
print(Shoes)


#10
names={"first":"Wafula", "second": "Ian", "third": "Elmer"}
amanya= names.copy()
print(amanya)

#11
dictionary_nested={"First":{1:"Date",3:"Month",43:"year",6:"Time"}, "Second":{23:"Weather",67:"Climate",12:"Rainfall",56:"Season"}}
#accessing items in a nested dictionary
print(dictionary_nested["First"][1])
print(dictionary_nested["Second"][67])