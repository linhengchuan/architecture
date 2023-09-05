# (D)ependency inversion principle(DIP)

- High level modules should not depend on low level modules. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.

### High level vs low level module

- Whether a module is high or low level is relative, it can be both high and low. High level modules usually command low level modules to do tasks.

### Achieving DIP will inverse the relations of the low module to depend on abstraction instead of being depended on by higher level modules.

# Dependency injection(another principle)

- Required dependency is injected to the module so that the module doesnt have to worry about create the dependency just strict focus on its functions.
- This helps to prevent tight coupling and also the module from having to go find its dependency instances.

# Inversion of control(IOC)

- To keep all injections in a seperate thread so that main control flow/thread is kept isolated from injections.
