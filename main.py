# json1.py
import json


def load_fruit():
    with open('fruit/fruit_data.json', 'r') as f:
        return json.load(f)

# my_list = ["this", "is", "a", "simple", "list", 35]
my_json_object = json.dumps(load_fruit())
print(my_json_object)

my_second_list = json.loads(my_json_object)
print(my_second_list)

# # Python program to update
# # JSON
#
#
# import json
#
# # JSON data:
# x = '{ "organization":"GeeksForGeeks","city":"Noida","country":"India"}'
#
# # python object to be appended
# y = {"pin": 22222222}
#
# # parsing JSON string:
# z = json.loads(x)
#
# # appending the data
# z.update(y)
#
# # the result is a JSON string:
# print(json.dumps(z))
# # ---------------------
