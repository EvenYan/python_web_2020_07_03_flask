# a = 10
# print(a)
string_a = "Hello"
print(type(string_a))

num_list = [1, 3, 5, "Hello ", ["Python", "Java"]]

print(num_list[-1][0])

num_tuple = (1, 4, 7, "Hello")
print(num_tuple)

people_dict = {"name": "Alice", "age": 70}
print(people_dict.items())

for k, v in people_dict.items():
    if k=="age" and v > 60:
        print("老年人")

