# The SOLID Principles of Object-Oriented Design

Once you understand the four pillars of Object-Oriented Programming (OOP), the next step is learning how to structure your objects effectively. Without design rules, it is easy to write fragile, rigid, and unmaintainable objects.

The industry standard for solving this is **The SOLID Principles of Object-Oriented Design**. 

Introduced by Robert C. Martin (often called "Uncle Bob"), SOLID is an acronym representing five architectural rules. Adhering to these principles prevents your classes from becoming massive, tangled, or easily broken when you add new features.

---

## 1. Single Responsibility Principle (SRP)
**"A class should have one, and only one, reason to change."**

Every class or module should focus entirely on a single task or piece of functionality. If a class is doing too many things, it becomes heavily coupled, meaning a change in one feature might accidentally break another.

*   **The Problem:** You have a `User` class that holds user data, validates email formats, and also handles saving the user to the database.
*   **The Solution:** Split it up. Have a `User` class for data, an `EmailValidator` class for checking formatting, and a `UserRepository` class for database interactions. 

## 2. Open/Closed Principle (OCP)
**"Software entities should be open for extension, but closed for modification."**

You should be able to add new functionality to a system without altering existing, tested code. Modifying working code introduces the risk of new bugs.

*   **The Problem:** You have a `DiscountCalculator` with a massive `if/else` block checking if a customer is "VIP", "Regular", or "New" to apply different discounts. If you add a "Holiday" tier, you have to modify this core class.
*   **The Solution:** Use Polymorphism. Create a `DiscountStrategy` interface. Create separate classes for `VipDiscount`, `RegularDiscount`, etc. When a new tier is needed, you simply write a *new* class that implements the interface, leaving the original calculator untouched.

## 3. Liskov Substitution Principle (LSP)
**"Objects of a superclass shall be replaceable with objects of its subclasses without breaking the application."**

If Class B inherits from Class A, you should be able to drop Class B into any function that expects Class A, and it should work perfectly. Subclasses must behave in expected ways without throwing unexpected errors or changing the core logic.

*   **The Problem:** The classic "Square vs. Rectangle" problem. If `Square` inherits from `Rectangle`, but overriding `setWidth()` on a square forces the height to change too, any function expecting a standard rectangle will suddenly break.
*   **The Solution:** Rethink the inheritance hierarchy. A Square is mathematically a Rectangle, but behaviorally in software, they are different. They should perhaps both implement a `Shape` interface instead of inheriting one from the other.

## 4. Interface Segregation Principle (ISP)
**"No client should be forced to depend on methods it does not use."**

It is better to have many small, specific interfaces than one massive, general-purpose interface. 

*   **The Problem:** You have a `Machine` interface with `print()`, `scan()`, and `fax()` methods. You create a `BasicPrinter` class that implements this interface. Because it's just a basic printer, it has to implement `scan()` and `fax()` by throwing errors or leaving them blank.
*   **The Solution:** Break it into `Printer`, `Scanner`, and `Fax` interfaces. The `BasicPrinter` only implements `Printer`, while an `AdvancedCopier` class can implement all three.

## 5. Dependency Inversion Principle (DIP)
**"Depend upon abstractions, not concretions."**

High-level modules (the core logic of your app) should not depend on low-level modules (like specific databases or APIs). Both should depend on abstractions (interfaces). 

*   **The Problem:** Your `Store` class directly creates and uses a `MySQLDatabase` object to save orders. If you ever switch to a cloud database, you have to rewrite the `Store` class.
*   **The Solution:** The `Store` class should require a generic `Database` interface. You can then inject the `MySQLDatabase` into it. If you switch to MongoDB, you write a new class that obeys the `Database` interface and plug it in. The `Store` class never knows the difference.
