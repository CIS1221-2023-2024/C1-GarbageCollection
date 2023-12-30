# C1-GarbageCollection
----------------------------------------------------------------------------
# PythonGC
PythonGC is a simple Python code which containts a class called CustomGarbageCollector. This class allows simple manual garbage collection. It can be used to manage when objects are to be deallocated by tracking their reference count.
This code is meant to show the basic concept of how a garbage collector works.

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
```
----------------------------------------------------------------------------
----------------------------------------------------------------------------
# PythonDGC
PythonDGC is a more detailed Python code, inspired and based on another garbage collection GitHub project (link for project below) than the previously mentioned PythonGC. It containts a class called GarbageCollector. This class provides basic functionality to allocate objects on a heap, process pointers, and perform garbage collection. The aim of this code is understanding and experimenting with garbage collection concept in a simple manner.

## Features
- Manual Garbage Collection: Provides control over the removal of objects, allowing efficient memory management.
- Reference count tracking: Tracks reference counts of objects for better understanding and management of their lifecycles.
- Object allocation simulation: Simulates object allocation on the heap, helping the understanding memory allocation dynamics.
- Pointer Processing simulation: Simulates the processing of pointers, visualising how references are updated.
- GC simulation: Simulates the garbage collection process, creating a new heap and updating roots.
- Status printing: Prints the heap status, moved roots, and mapping table for debugging and monitoring.

### Prerequisites
- Python V3.11.5

## Usage
```python
#Creating a GarbageCollector with a heap size of 20
gc = GarbageCollector(20)

#Printing the initial status
gc.print_status("Initial")

#Simulating allocation. (Adding objects to the heap)
obj_a_index = gc.allocate_object("Object A")
obj_b_index = gc.allocate_object("Object B")

#Printing the status after allocation
gc.print_status("After Allocation")

#Simulating garbage collection with roots at indices of allocated objects
gc.collect_garbage([obj_a_index, obj_b_index])

#Printing the final status after garbage collection
gc.print_status("After Garbage Collection")
```

[Link for GitHub project on which PythonDGC.py is based](https://github.com/marijanedjalkova/Garbage-Collector)
----------------------------------------------------------------------------
# Java Garbage Collector
## Garbage Collector V1
### Features
- Manually-executable automatic garbage collection
- Use of JVM built-in features

### Prerequisites
- Java 11+ JDK

### Description
- This Java program begins by creating a test object and linking it with a PhantomReference
that is being queued into a ReferenceQueue. In order for the garbage collection to be possible 
we set obj to null. The program pauses for three seconds giving the program some time to run.
After this, we give a suggestion to the system to execute garbage collection using the 
System.gc() command. The program then enters a loop checking the ReferenceQueue for any 
enqueued PhantomReference objects. If a reference is found, it implies that the object has been
garbage collected, followed with a confirming message.
----------------------------------------------------------------------------
## Garbage Collector V2
### Features
- Complete manual & custom garbage collection
- Object allocation and disposal

### Prerequisites
- Java 11+ JDK

### Description
- Different to version one of the garbage collector, this version is a more detailed
and fully manual version. This is unlike version one, where the program still used
JVM's built in features. Instead, this program is more custom-built it defines a
CustomGarbageCollector class that maintains a list of allocated objects, the 
collectGarbage method iterates through the list and disposes of objects based on
a simulated condition, which in this case is a random mathematical number. However,
this condition is only a test and can be switched for any given condition of my 
choice.
----------------------------------------------------------------------------

# Comparison between V1 and V2

## V1
- Version 1 demonstrates the use of Java's built-in mechanisms (PhantomReference and ReferenceQueue) 
for handling actions after an object is garbage collected.

- Version 1 leverages Java's automatic garbage collection but provides a mechanism (phantom references)
 to perform additional actions after an object is collected.

- Version 1 aligns more closely with Java best practices, 
utilizing built-in features for managing resources associated with objects.

## V2
- Version 2 simulates a custom garbage collector with manual disposal of objects based on a condition.
- Version 2 takes a manual approach to memory management, which is not typical in Java, where automatic garbage collection is the norm.
- Version 2 is a simple example of a custom garbage collector and not suitable for practical use in real-world applications.
