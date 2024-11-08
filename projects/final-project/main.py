'''
# **Cataloger of Household Objects 🏡**

This project is to develop a household object cataloger, 
a tool that helps users catalog and manage objects in their homes.   
The cataloger will use recursion to explore home environments in depth, gathering information about objects, 
such as name, location, and category.   
It will also provide functionality to search, add, edit, and delete objects from the catalog, 
simplifying home inventory management.


## **Objective 🎯**
The goal of the project is to provide users with a practical tool for cataloging and keeping
track of objects in their home.   
Using variables, strings, mathematical calculations, conditional operators, loops, functions, arrays, JSON objects, 
and recursive functions, the cataloger will enable users to effectively organize their household objects 
and obtain detailed information about them.

## **Recursive exploration of home environments 🔁**

- Using a recursive function, explore home environments, such as rooms and closets, to identify the objects present.  
- Gather information about objects, such as name, location, and category.
- Use an appropriate data structure, such as an array of JSON objects, to store object information.

## **Adding new objects ➕**

- Using a function, allow the user to add new objects to the catalog.
- Capture the object's information, such as name, location, and category, and create a new JSON object with that information.
- Add the object to the home object catalog.

## **Modify existing objects ✍️**

- Using a recursive function, allow the user to search and edit existing objects in the catalog.
- Allow the user to edit the object's information, such as name, location, or category.
- Update the corresponding JSON object in the catalog with the new information.


## **Object deletion ➖**

- Using a recursive function, allow the user to search for and delete existing objects in the catalog.
- Remove the corresponding JSON object from the home object catalog.

## **Limitations ✋**

- The project focuses on cataloging and management of household objects, without including features such as object 
  quantity management or integration with more complex inventory systems.
- Interactions with external databases or other sources of additional information are not considered.

## **Project Duration ⏲️**

Considering the functionality required and the use of the specified constructs, 
the project is expected to take about 1 to 2 days to complete.
'''

def check_environment(catalog):
    room = input("Please input which room do you want to explore: ")
    for object in catalog:
        if object["location"] == room:
            print(object)

def add_object(catalog):
    name = input("Please input the name of the object: ")
    location = input("Please input the position of the object: ")
    category = input("Please input the category of the object: ")
    object = name, location, category
    catalog.append(object)
    print("Object added correctly!")

def change_object(catalog):
    name = input("Please input the name of which object you would like to modify?\n", catalog)
    for object in catalog:
        if object["name"] == name: 
            object["location"] = input("Please input new location: ")
            object["category"] = input("Please input new category: ")
            print("Object modified correctly")
            return
    print("Object not found\n", catalog)

def delete_object(catalog):
    name = input("Please input the name of which object you would like to delete?\n", catalog)
    for object in catalog:
        if object["name"] == name: 
            catalog.remove(object)
            print("Object removed correctly")
            return
    print("Object not found\n", catalog)

def main():
    catalog = []
    userchoice = input("Please choose one of the following options\n 1. Search\n 2. Add\n 3. Edit\n 4. Delete")
    if userchoice == "1":
        check_environment(catalog)
    elif userchoice == "2":
        add_object(catalog)
    elif userchoice == "3":
        change_object(catalog)
    elif userchoice == "4":
        delete_object(catalog)

if __name__ == '__main__':
    main()