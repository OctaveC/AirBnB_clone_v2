# AirBnB_clone v1 - File storage / Console

The purpose of this project is to recreate the AirBnB site, from the back-end data management to the front-end user interface.

This repo contains the first part of the project which consists in :

*    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
*    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
*    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
*    create the first abstracted storage engine of the project: File storage
*    create all unittests to validate all our classes and storage engine

![Alt text](https://imagizer.imageshack.com/v2/1257x669q90/924/Aebfet.png "The part of this project: v1")

# Command interpreter

We have created a command line that allows us to manage objects that store data.

### Mandatory part

The console supports the following commands :

*   Create an object of the class name:

        (hbnb) create class_name

*   Display object information if it exists:

        (hbnb) show class_name id

*   Delete the object if its exists:

        (hbnb) destroy class_name id

*   Display all instances, or only instances of the specified objects:

        (hbnb) all / (hbnb) all class_name

*   Update an instance attribute of a previously declared object:

        (hbnb) update class_name id attribute_name attribute_value

### Advanced part

Additionally, you can use the following command formats :

*   Display the number of instances of the specified class:

        (hbnb) class_name.count()

*   Display object information if it exists:

        (hbnb) class_name.show(id)

*   Delete the object if its exists:

        (hbnb) class_name.destroy(id)

*   Display all instances of the specified objects:

        (hbnb) class_name.all()

## Installation

Clone this repositary:

    $ git clone https://github.com/hollaze/AirBnB_clone.git 

Access the folder:

    $ cd AirBnB_clone

## How to use it

You can access the console via two modes.

Interactive mode:

    $ ./console.py

Non-interactive mode:

    $ echo "<command>" | ./console.py

## Examples

Standard commands:

        (hbnb)create User
        993e570d-9b4e-449c-84b3-085ab454d3ce
        (hbnb)

Create an instance of BaseModel and show the info:

        (hbnb)create BaseModel
        d711be23-73d9-4fbd-92f5-fe9ec7044d6d
        (hbnb)show BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
        [BaseModel] (d711be23-73d9-4fbd-92f5-fe9ec7044d6d) {'id': 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d', 'created_at': '2019-07-04T02:20:53.149558', 'updated_at': '2019-07-04T02:20:53.149791'}
        (hbnb)

Delete the instance using the id:

        (hbnb)destroy BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
        ['BaseModel', 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d']
        (hbnb)

Helper function:

        (hbnb) help create

                Create a new instance of a class, saves
                it to a JSON file and prints the id

                Usage:
                create <class name>
                
        (hbnb) 

### Advanced commands:

        (hbnb) Amenity.all()
        ["[Amenity] (ad91a8b5-8487-4e17-8bf6-51eda726704b) {'id': 'ad91a8b5-8487-4e17-8bf6-51eda726704b', 'created_at': datetime.datetime(2021, 7, 2, 13, 4, 27, 605079), 'updated_at': datetime.datetime(2021, 7, 2, 13, 4, 27, 605104)}"]
        (hbnb)

        (hbnb) Amenity.show("ad91a8b5-8487-4e17-8bf6-51eda726704b")
        Amenity
        ad91a8b5-8487-4e17-8bf6-51eda726704b
        [Amenity] (ad91a8b5-8487-4e17-8bf6-51eda726704b) {'id': 'ad91a8b5-8487-4e17-8bf6-51eda726704b', 'created_at': datetime.datetime(2021, 7, 2, 13, 4, 27, 605079), 'updated_at': datetime.datetime(2021, 7, 2, 13, 4, 27, 605104)}
        (hbnb)

Destroy the instance:

        (hbnb) Amenity.destroy("ad91a8b5-8487-4e17-8bf6-51eda726704b")
        (hbnb)

Count the instances of the specified class:

        (hbnb) User.count()
        7
        (hbnb) 

### Authors

*   [Etienne Brun](https://github.com/EtienneBrJ)

*   [Alrick Deperiers](https://github.com/hollaze)
