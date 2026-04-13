print("Hello from W1D2")

source_system = "crm_database"
row_limit = 5000
success_threshold = 0.95
is_dry_run = False

print(source_system)
print(row_limit)
print(success_threshold)
print(is_dry_run)

print(type(source_system))
print(type(row_limit))
print(type(success_threshold))
print(type(is_dry_run))

export_year = 2026
export_month = 2
source_name = "crm"

#Build a file path string from typed values
filename = source_name + "_" + str(export_year) + "_" + str(export_month) + ".csv"

print(filename)
print(type(filename))
print(type(str(export_year)))
print(type(export_year))


# Create a variable first_name with a string value and print it.
first_name = "Cristian"
print(first_name)

#Create a variable age with an int value and print it

age = 30
print(age)

#Create a variable pi_estimate with a float value and print it

pi_estimate = 3.14
print(pi_estimate)

# Create a variable is_student with a bool value and print it.
is_student = False

print(is_student)