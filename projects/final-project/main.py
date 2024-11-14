'''
# **Cataloger of Household elements 🏡**

This project is to develop a household element cataloger, 
a tool that helps users catalog and manage elements in their homes.   
The cataloger will use recursion to explore home environments in depth, gathering information about elements, 
such as name, location, and category.   
It will also provide functionality to search, add, edit, and delete elements from the catalog, 
simplifying home inventory management.


## **elementive 🎯**
The goal of the project is to provide users with a practical tool for cataloging and keeping
track of elements in their home.   
Using variables, strings, mathematical calculations, conditional operators, loops, functions, arrays, JSON elements, 
and recursive functions, the cataloger will enable users to effectively organize their household elements 
and obtain detailed information about them.

## **Recursive exploration of home environments 🔁**

- Using a recursive function, explore home environments, such as rooms and closets, to identify the elements present.  
- Gather information about elements, such as name, location, and category.
- Use an appropriate data structure, such as an array of JSON elements, to store element information.

## **Adding new elements ➕**

- Using a function, allow the user to add new elements to the catalog.
- Capture the element's information, such as name, location, and category, and create a new JSON element with that information.
- Add the element to the home element catalog.

## **Modify existing elements ✍️**

- Using a recursive function, allow the user to search and edit existing elements in the catalog.
- Allow the user to edit the element's information, such as name, location, or category.
- Update the corresponding JSON element in the catalog with the new information.


## **element deletion ➖**

- Using a recursive function, allow the user to search for and delete existing elements in the catalog.
- Remove the corresponding JSON element from the home element catalog.

## **Limitations ✋**

- The project focuses on cataloging and management of household elements, without including features such as element 
  quantity management or integration with more complex inventory systems.
- Interactions with external databases or other sources of additional information are not considered.

## **Project Duration ⏲️**

Considering the functionality required and the use of the specified constructs, 
the project is expected to take about 1 to 2 days to complete.
'''

def check_environment(catalog, index = 0, room = ""):
    if catalog:
        if index == 0:
            room = input("Please input which room do you want to explore: ")
        if catalog[index]["location"] == room:
            print(catalog[index])
            return catalog
        index += 1
        return check_environment(catalog, index, room)
    return catalog

def add_element(catalog):
    name = input("Please input the name of the element: ")
    location = input("Please input the position of the element: ")
    category = input("Please input the category of the element: ")
    element = {"name": name,"location": location,"category": category}
    catalog.append(element)
    print("element added correctly!")

def change_element(catalog, name):
    if catalog:
        if catalog[0]["name"] == name:
            catalog[0]["name"] = input("Please input new name: ")
            catalog[0]["location"] = input("Please input new location: ")
            catalog[0]["category"] = input("Please input new category: ")
            print("Element modified correctly")
            return catalog
        return change_element(catalog[1:], name)
    print("Element not found\n", catalog)
    return catalog

def delete_element(catalog, name, index = 0):
    if catalog:
        if catalog[index]["name"] == name:
            del catalog[index]
            print("Element deleted correctly")
            return catalog
        index += 1
        return delete_element(catalog, name, index)
    print("element not found\n", catalog)
    return catalog

def main():
    catalog = [{"name": "Fra", "location": "Living", "category": "Computer"}, 
                {"name": "Mattia", "location": "Kitchen", "category": "Box"}, 
                {"name": "Simone", "location": "Bathroom", "category": "Soap"}]
    userchoice = input("Please choose one of the following options\n 1. Search\n 2. Add\n 3. Edit\n 4. Delete\n")
    while userchoice != "":
        if userchoice == "1":
            check_environment(catalog)
        elif userchoice == "2":
            add_element(catalog)
        elif userchoice == "3":
            name = input("Please input the name of which element you would like to modify?\n")
            change_element(catalog, name)
        elif userchoice == "4":
            name = input("Please input the name of which element you would like to delete?\n")
            delete_element(catalog, name, index = 0)
        userchoice = input("Please choose one of the following options\n 1. Search\n 2. Add\n 3. Edit\n 4. Delete\n")

if __name__ == '__main__':
    main()