# C1-GarbageCollection

## PythonGC
PythonGC is a simple Python code which containts a class called CustomGarbageCollector. This class allows simple manual garbage collection. It can be used to manage when objects are to be deallocated by tracking their reference count.

## Features
- Manual garbage collection of objects
- Tracking of object reference counts

### Prerequisites
- Python V3.11.5

## Usage
```python
from PythonGC import CustomGarbageCollector, ExampleClass

#Create an instance of the custom garbage collector
custom_gc = CustomGarbageCollector()

#Create and add objects to the garbage collector
obj1 = ExampleClass([1, 2, 3])
obj2 = ExampleClass("Hello")

custom_gc.add_object(obj1)
custom_gc.add_object(obj2)

#Call for manual garbage collection
custom_collector.collect()
