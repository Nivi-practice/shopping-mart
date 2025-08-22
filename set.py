
subjects = ["Math", "Science", "English", "History", "Math", "Science"]
unique_subjects = set(subjects)
print("Total number of unique subjects:", len(unique_subjects))

print("\n" + "-"*30 + "\n")


studentA_hobbies = {"reading", "swimming", "painting", "cycling"}
studentB_hobbies = {"swimming", "cycling", "dancing", "gaming"}

common_hobbies = studentA_hobbies.intersection(studentB_hobbies)
unique_to_A = studentA_hobbies.difference(studentB_hobbies)
all_hobbies = studentA_hobbies.union(studentB_hobbies)

print("Common hobbies:", common_hobbies)
print("Hobbies unique to Student A:", unique_to_A)
print("All hobbies:", all_hobbies)

print("\n" + "-"*30 + "\n")


fruits = {"apple", "banana", "mango", "orange", "grape"}
user_fruit = input("Enter a fruit name: ").strip().lower()

if user_fruit in fruits:
    print(f"Yes, {user_fruit} is present in the set.")
else:
    print(f"No, {user_fruit} is not present in the set.")
