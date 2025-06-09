class Solution:
    def sort_map_in_revers_order(self, value_freq_map :dict):

        sorted_dict = dict(sorted(value_freq_map.items(), key = lambda x:x[0], reverse=True))
        sorted_by_values =  dict(sorted(value_freq_map.items(), key=lambda x : x[1], reverse=True))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        # Define comparison for sorting (e.g., by age)
        return self.age < other.age

    def __str__(self):
        return f"{self.name} ({self.age})"

# Create Person objects
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p3 = Person("Charlie", 35)

# Dictionary with Person objects as keys
hashmap = {p1: 1, p2: 2, p3: 3}

# Sort by Person's age in reverse order
sorted_by_keys = dict(sorted(hashmap.items(), key=lambda x: x[0].age, reverse=True))

# Print result
print("Sorted by keys (age, reverse):")
for person, value in sorted_by_keys.items():
    print(f"{person}: {value}")