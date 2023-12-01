const prompt = require('prompt-sync')({sigint: true});

// Main functions
function createHouseholdCatalog(house) {
    if (!Array.isArray(house)) throw new TypeError("Please pass only array to the function");
    // Base case, if no element in [] so exit
    if (!house[0]) return "";
    // clone the house structure into another []
    const householdCatalog = [];
    householdCatalog.push(house[0]); // push the first room(in the house list) data structure

    return [...householdCatalog, ...createHouseholdCatalog(house.slice(1))];
}
function catalogAdd(item, room, category) {
    // check if the specifed room exist in the house structure
    if (householdCatalog.every( rooms => !Object.hasOwn(rooms, room))) {
        return console.error("No such room in the house!");
    }
    
    let roomItems; // declaring the variable that hoisting the items in the room
    householdCatalog.find( roomObject => { 
        if (roomObject[room]) {
            return roomItems = roomObject[room]; // when find a match exit
        } // return an array of objects(items in the room)
    })
    
    roomItems.push({name : item, location : room, category : category}); // add the new item to the item list

    return householdCatalog;
}
function catalogEdit(item, catalog, room = undefined) { // room parameter it's optional
    const [roomsObject] = catalog;
    // if no room parameter is entred
    if (!room) {
        const sameTypeRooms = Object.keys(roomsObject); // supposing there are more rooms of the same category e.g. (bathroom1, bathroom2)

        let flagEdit = false; // a marker for the editing event (aka: when the item is inside the current searching room, the edit can be done)
        for ( let sameTypeRoom of sameTypeRooms) {
            const itemsCollection = roomsObject[sameTypeRoom]; // here I am on the item list in the room

            itemsCollection.find( singleItem => {
                if (singleItem.name === item) {

                    const name = prompt(`${yellow}Enter new item name or press only Enter to continue: `);
                    const location = prompt(`${yellow}Enter new item location or press only Enter to continue: `);
                    const category = prompt(`${yellow}Enter new item category or press only Enter to continue: `);
                    // edit the property of the item via reference
                    singleItem.name = name ? name : singleItem.name; // if no new value was entered, I use previous
                    singleItem.location = location ? location : singleItem.location;
                    singleItem.category = category ? category : singleItem.category;

                    return flagEdit = true; // switch the value to true let me exit the recursion
                }
            });
        }
        // Base case
        if (flagEdit) return householdCatalog;

        const reduceCatalog = catalog.slice(1); // create a shallow copy of the catalog? ask Mentor!
    
        catalogEdit(item, reduceCatalog);
    }
    else { // if room parameter is entred

        if (!roomsObject[room]) { // if the item is not inside the current room, remove the room from the list
            const reduceCatalog = catalog.slice(1); // create a shallow copy of the catalog? ask Mentor!
    
            catalogEdit(item, reduceCatalog, room);
        }

        const itemsCollection = roomsObject[room]; // here I am on the item list in the room

        itemsCollection.find( singleItem => {
            if (singleItem.name === item) { // searching the target item

                const name = prompt(`${yellow}Enter new item name or press only Enter to continue: `);
                const location = prompt(`${yellow}Enter new item location or press only Enter to continue: `);
                const category = prompt(`${yellow}Enter new item category or press only Enter to continue: `);
            
                singleItem.name = name ? name : singleItem.name;
                singleItem.location = location ? location : singleItem.location;
                singleItem.category = category ? category : singleItem.category;

                return householdCatalog;
            }
        })
    }

}
function catalogDelete(item, catalog, room = undefined) {
    // room parameter is entered
    if (room) {
        const itemsCollection = catalog[0][room];
        
        if(!itemsCollection) catalogDelete(item, householdCatalog.slice(1), room);

        itemsCollection.find( (singleItem, index) => {
            if (singleItem.name === item) {
                return delete itemsCollection[index];
            }
        })
    }
    // room parameter in not entered
    else { 
        const roomObject = catalog[0];

        if(!roomObject.length) return householdCatalog;

        const roomsCollection = Object.keys(roomObject);
        
        let editFlag = false;
        for (let singleRoom of roomsCollection) {
            const itemsCollection = roomObject[singleRoom];
    
            itemsCollection.find( (singleItem, index) => {
                if (singleItem.name === item) {
                    editFlag = true;
                    return delete itemsCollection[index];
                }
            })
        }
        
        if(editFlag) return householdCatalog;

        catalogDelete(item, catalog.slice(1), room);
    }
 
}
// Program module function, to manage the user interaction with the program 
function addingProtocol() {
    let switcher;
    do {
        const adding = prompt(`${yellow}Do you want to add ${(!switcher) ? "an" : "another"} item? [yes/no] `).toLowerCase();
    
        if (!(adding === "yes" || adding === "no")) {
            console.log("Error! Please type correctly"); 
            continue; 
        }
    
        if (adding === "no") {
            console.log(`\n${yellow}This is your${(!switcher) ? "" : " NEW"} Catalog: ${cyan}${JSON.stringify(householdCatalog)}${reset}\n`)
            break;
        }
    
        const item = prompt(`${yellow}Enter item name: `).toLowerCase();
        const room = prompt(`${yellow}Enter item located room: `).toLowerCase();
        const category = prompt(`${yellow}Enter item category(e.g. 'personal care'): `).toLowerCase();
    
        catalogAdd(item, room, category);
        switcher = "on";
    
    } while(true);
}
function editingProtocol() {
    let switcher;
    do {
        const editing = prompt(`${yellow}Do you want to edit ${(!switcher) ? "an" : "another"} item? [yes/no] `).toLowerCase();
    
        if (!(editing === "yes" || editing === "no")) {
            console.log("Error! Please type correctly"); 
            continue; 
        }
    
        if (editing === "no") {
            console.log(`\n${yellow}This is your${(!switcher) ? "" : " NEW"} Catalog: ${cyan}${JSON.stringify(householdCatalog)}\n`)
            break;
        }
    
        const item = prompt(`${yellow}Enter item name: `).toLowerCase();
        const room = prompt(`${yellow}Enter item located room(leave empty if you don't remember the exact room): `).toLowerCase();
    
        catalogEdit(item, householdCatalog, room);
        switcher = "on";
        
    } while(true);
}
function deletingProtocol() {
    let switcher;
    do {
        const deleting = prompt(`${yellow}Do you want to delete ${(!switcher) ? "an" : "another"} item? [yes/no] `).toLowerCase();
    
        if (!(deleting === "yes" || deleting === "no")) {
            console.log("Error! Please type correctly"); 
            continue; 
        }
    
        if (deleting === "no") {
            console.log(`\n${yellow}This is your${(!switcher) ? "" : " NEW"} Catalog: ${cyan}${JSON.stringify(householdCatalog)}\n`)
            break;
        }
    
        const item = prompt(`${yellow}Enter item name: `).toLowerCase();
        const room = prompt(`${yellow}Enter item located room(leave empty if you don't remember the exact room): `).toLowerCase();
    
        catalogDelete(item, householdCatalog, room);
        switcher = "on";
        
    } while(true);   
}

// console text color
const cyan = "\x1b[36m";
const yellow = "\x1b[33m";
const reset = "\x1b[0m";

// create my home data structure
const home = [
    {bathroom : [
        {
            name : "soap",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "toothpaste",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "toothbrush",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "mouthwash",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "towel",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "washing machine",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "detergent",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "mirror",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "laundry basket",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "bathrobe",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "hair dryer",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "electric razor",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "cotton wool",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "toilet paper",
            location : "bathroom",
            category : "intimate hygiene"
        },
        {
            name : "moisturizer",
            location : "bathroom",
            category : "cosmetics"
        },
        {
            name : "shampoo",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "bubble bath",
            location : "bathroom",
            category : "personal care"
        },
        {
            name : "makeup",
            location : "bathroom",
            category : "cosmetics"
        }
    ]
    },
    {kitchen : [  
        {
            name : "table",
            location : "kitchen",
            category : "furniture"
        },
        {
            name : "chairs",
            location : "kitchen",
            category : "furniture"
        },
        {
            name : "refrigerator",
            location : "kitchen",
            category : "appliances"
        },
        {
            name : "microwave",
            location : "kitchen",
            category : "appliances"
        },
        {
            name : "coffee maker",
            location : "kitchen",
            category : "appliances"
        },
        {
            name : "television",
            location : "kitchen",
            category : "appliances"
        },
        {
            name : "oven",
            location : "kitchen",
            category : "appliances"
        },
        {
            name : "fruit",
            location : "kitchen",
            category : "food"
        },
        {
            name : "bread box",
            location : "kitchen",
            category : "furniture"
        },
        {
            name : "stove",
            location : "kitchen",
            category : "appliances"
        },
        {
            name : "sink",
            location : "kitchen",
            category : "utensils"
        },
        {
            name : "glasses",
            location : "kitchen",
            category : "utensils"
        },
        {
            name : "napkins",
            location : "kitchen",
            category : "utensils"
        },
        {
            name : "salt",
            location : "kitchen",
            category : "food"
        },
    ]
    }, 
    {livingroom : []}, 
    {bedroom : []}, 
    {storageroom : []}
];
// init catalog
const householdCatalog = createHouseholdCatalog(home);

// -------- START ----------
// ask for username and display a default home catalog
const username = prompt("Enter your name: ");

console.log(`\n${cyan}HELLO ${username.toUpperCase()}!
\n${yellow}This is your Household Catalog:
${cyan}${JSON.stringify(householdCatalog)}${reset}\n`);

// call the actual user's avaiable features, each feature can be managed in a separate space
// adding process
addingProtocol();
// editing process
editingProtocol();
// deleting process
deletingProtocol();
// RICORDATI DI AGGIUNGER UN CONTROL PANEL PER CON UN PROMPT IN ATTESA, PER NON LANCIARE IN AUTOMATICO LE RICHIESTE DI AZIONI SUL CATALOGO
// --------- END ----------