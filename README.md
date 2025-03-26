# Store Management System using Python OOPs

A Python-based store inventory management system built using Object-Oriented Programming principles. This was a guided project by [JimShapedCoding](https://www.youtube.com/watch?v=Ej_02ICOIgs&t=5367s) uploaded on the FreeCodeCamp YouTube channel.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OOP](https://img.shields.io/badge/Object_Oriented-Yes-green)

### Note:
```text
I am adding new comments for the new changes made and removing the old comments with every commit, and have added information in
some pull requests so that it will be easier for me to revisit the individual concepts again when I want to revise OOPs.
```

## Features
- 📦 Item management (create/update/delete).
- 💰 Pricing methods with discount system.
- 📊 Instantiation from CSV files.
- 🔒 Encapsulation of attributes with getters/setters.
- 📱 Inheritance (Item → Phone/Keyboard).

## 🧠 Key Concepts Summary:
### Core Principles
- **Encapsulation** 🛡️  
  *Bundling data + methods together while controlling access via private attributes/properties.*
  
- **Abstraction** ✨  
  *Hiding complex logic behind simplified interfaces.*

- **Inheritance** 🧬  
  *Deriving new classes (children) from existing ones (parents).*

- **Polymorphism** 🎭  
  *Different classes responding uniquely to the same method call.*

### Advanced Techniques
- **Constructors** (`__init__`) 🏗️  
  *Special method for initializing new objects.*

- **Class Methods** (`@classmethod`) 🏛️  
  *Methods bound to the class (not instance), often used as alternate constructors.*

- **Static Methods** (`@staticmethod`) �  
  *Utility functions that don't access instance/class state.*

- **Property Decorators** (`@property`) 🎀  
  *Enables attribute-like access to methods with validation logic.*

- **Method Overriding** ♻️  
  *Child classes redefining parent class methods.*

- **`super()`** 🔝  
  *Accessing parent class methods from child classes.*

## 📁 Project Structure
```text
fcc-oops-python/
├── README.md            # Project documentation (you are here)
├── item.py              # Base Item class (parent)
├── items.csv            # Inventory data in CSV
├── keyboard.py          # Keyboard subclass
├── main.py              # Program entry point
├── phone.py             # Phone subclass
└── project_notes.docx   # Development notes
```
# Credits:
- Tutorial by [JimShapedCoding](https://www.youtube.com/@jimshapedcoding).
- Uploaded on the [FreeCodeCamp](https://www.youtube.com/@freecodecamp) Youtube channel.
