# 0x0C. Python - Almost a circle

## Learning Objectives

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Tasks

_**0. If it's not tested it doesn't work**_  
All your files, classes and methods must be unit tested and be PEP 8 validated.  

_**1. Base class**_  
Write the first class `Base`.  

_**2. First Rectangle**_  
Write the class `Rectangle` that inherits from `Base`.  

_**3. Validate attributes**_  
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded).  

_**4. Area first**_  
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.  

_**5. Display #0**_  
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.  

_**6. __str__**_  
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`  

_**7. Display #1**_  
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`.  

_**8. Update #0**_  
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute.  

_**9. Update #1**_  
Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes.  

_**10. And now, the Square!**_  
Write the class `Square` that inherits from `Rectangle`.  

_**11. Square size**_  
Update the class `Square` by adding the public getter and setter `size`.  

_**12. Square update**_  
Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes.  

_**13. Rectangle instance to dictionary representation**_  
Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`.  

_**14. Square instance to dictionary representation**_  
Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.  

_**15. Dictionary to JSON string**_  
JSON is one of the standard formats for sharing data representation.  

Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`.  

_**16. JSON string to file**_  
Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file.  

_**17. JSON string to dictionary**_  
Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`.  

_**18. Dictionary to Instance**_  
Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set.  

_**19. File to instances**_  
Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances.  
