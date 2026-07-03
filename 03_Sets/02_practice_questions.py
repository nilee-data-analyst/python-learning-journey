
# Remove Duplicate Customer IDs from a list/tuple
customer_ids = [101, 102, 103, 102, 104, 101, 105]

unique_ids = set(customer_ids) # convert a list to set as a set does not allow duplicates
print(unique_ids)

# check an item in a set
products = {"Laptop", "Phone", "Keyboard", "Mouse"}

if "Phone" in products:
    print("Available")
else:
    print("Not Available")

# Customers Who Bought Both Products
product_A = {"John", "Alice", "Bob", "Emma"}
product_B = {"Alice", "Emma", "David", "Mike"}

print(product_A.intersection(product_B))

# find Employees Only in HR
HR = {"John", "Alice", "Bob", "Emma"}
Finance = {"John", "Emma", "David"}

print(HR.difference(Finance))

# Are Two Sets Equal?
# note: sets are unordered
dept1 = {101, 102, 103, 104}
dept2 = {103,101,104,102}

if dept1 == dept2:
    print("Both departments have same employees records")
else:
    print("Employee records are different")

# Check whether all the candidate's skills are included in the company's skill list
company_skills = {"sql", "python", "excel", "power BI", "tableau"}
candidate_skills = {"python", "excel", "power BI"}

if candidate_skills.issubset(company_skills):
    print("Candidate skills are a subset of company skills.")
else:
    print("Candidate has skills outside the company list.")

# Compare Employees from Two Years
employees_2025 = {"John", "Emma", "David", "Mike", "Alice"}
employees_2026 = {"Emma", "David", "Mike", "Sophia", "James"}

new_employees = employees_2026.difference(employees_2025)
employees_left = employees_2025.difference(employees_2026)
common_employees = employees_2025.intersection(employees_2026)

print("New Employees:", new_employees)
print("Employees Left:", employees_left)
print("Common Employees:", common_employees)