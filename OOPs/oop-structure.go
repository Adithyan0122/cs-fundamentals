package main

import "fmt"

// 1. ABSTRACTION & POLYMORPHISM: The Interface
// Any struct that possesses these two methods is automatically considered an "Employee".
type Employee interface {
	GetID() string
	CalculateSalary() float64
}

// 2. COMPOSITION BASE: Instead of a parent class, we make a base struct to embed later.
type BaseEmployee struct {
	Name string
	id   string // ENCAPSULATION: Lowercase 'i' makes this private to the package.
}

// Method attached to BaseEmployee (Receiver function)
func (b BaseEmployee) GetID() string {
	return b.id
}

// 3. COMPOSITION (Go's alternative to Inheritance)
type FullTimeEmployee struct {
	BaseEmployee // Embedding the base struct gives FullTimeEmployee Name and id.
	AnnualSalary float64
}

func (f FullTimeEmployee) CalculateSalary() float64 {
	return f.AnnualSalary / 12
}

// COMPOSITION: Another distinct struct
type Contractor struct {
	BaseEmployee
	HourlyRate  float64
	HoursWorked float64
}

func (c Contractor) CalculateSalary() float64 {
	return c.HourlyRate * c.HoursWorked
}

// --- Execution ---

// POLYMORPHISM: This function accepts our interface.
// It doesn't care what the underlying structs are, as long as they satisfy the interface.
func ProcessPayroll(staff []Employee) {
	for _, person := range staff {
		fmt.Printf("Payroll for ID %s: $%.2f\n", person.GetID(), person.CalculateSalary())
	}
}

func main() {
	alice := FullTimeEmployee{
		BaseEmployee: BaseEmployee{Name: "Alice Smith", id: "FT-001"},
		AnnualSalary: 120000,
	}

	bob := Contractor{
		BaseEmployee: BaseEmployee{Name: "Bob Jones", id: "CT-999"},
		HourlyRate:   50,
		HoursWorked:  160,
	}

	// Grouping our different structs into a slice of the 'Employee' interface
	companyStaff := []Employee{alice, bob}

	ProcessPayroll(companyStaff)
}
