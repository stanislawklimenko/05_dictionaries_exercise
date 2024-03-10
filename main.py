# 1 Populating a dictionary
first_name = "John"
last_name = "Doe"
favorite_hobby = "Python"
sports_hobby = "gym"
age = 82
# Your implementation
my_dict = {"name": first_name + ' ' + last_name, "age": age, "hobbies": [favorite_hobby, sports_hobby]}
assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}

# 2 Accessing and merging dictionaries
dict1 = dict(key1="This is not that hard", key2="Python is still cool")
dict2 = {"key1": 123, "special_key": "secret"}
# This is also a away to initialize a dict (list of tuples)
dict3 = dict([("key2", 456), ("keyX", "X")])
# 'Your impelementation'
my_dict = {"key1": dict2["key1"], "key2": dict3["key2"], "keyX": dict3["keyX"]}
special_value = dict2["special_key"]
assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
assert special_value == "secret"

# Let's check that the originals are untouched
assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
assert dict2 == {"key1": 123, "special_key": "secret"}
assert dict3 == {"key2": 456, "keyX": "X"}