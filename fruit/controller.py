import json
from ninja import NinjaAPI, Router
from fruit.schemas.fruits_schema import FruitSchema
from fruit.schemas.general_schema import MessageOut

api_controller = NinjaAPI()


# load data from json file
def load_fruit():
    with open('fruit/fruit_data.json', 'r') as f:
        return json.load(f)


# write data into json file considering the emoji and indent (new line)
def write_fruit(fruit):
    with open('fruit/fruit_data.json', 'w') as write_json:
        json.dump(fruit, write_json, ensure_ascii=False, indent=2)


# get all fruits
@api_controller.get('/fruits', response={200: list[FruitSchema], 404: MessageOut})
def list_fruits(request):
    all_fruits = load_fruit()
    if not all_fruits:
        return 404, {'msg': 'There are no fruits to display'}
    return 200, all_fruits


# get single fruit by id
@api_controller.get('/fruit/{id}', response={200: FruitSchema, 404: MessageOut})
def list_fruit_by_id(request, id: int):
    all_fruits = load_fruit()
    for fruit in all_fruits:
        if fruit['id'] == id:
            return 200, fruit
    return 404, {'msg': 'Fruit with that id was not found'}


# create new fruit, considering to check if id exists
@api_controller.post('/fruit', response={201: MessageOut, 404: MessageOut})
def post_fruit(request, payload: FruitSchema):
    # check to see if id exist
    all_fruits = load_fruit()
    for fruit in all_fruits:
        if fruit['id'] == payload.id:
            return 404, {'msg': 'This id is already exist'}
    # convert payload Fruit schema into dictionary
    new_dic = {
        'id': payload.id,
        'name': payload.name,
        'description': payload.description
    }
    # add the new dict into all json data and then write into json file
    all_fruits.append(new_dic)
    write_fruit(all_fruits)
    return 201, {'msg': 'added successfully'}


# delete fruit by Id
@api_controller.delete('/fruit/{id}', response={202: MessageOut, 404: MessageOut})
def delete_fruit(request, id: int):
    all_fruits = load_fruit()
    for fruit in all_fruits:
        if fruit['id'] == id:
            # delete the object if exist then write into json file
            all_fruits.remove(fruit)
            print(all_fruits)
            write_fruit(all_fruits)
            return 202, {'msg': 'Deleted successfully'}
    return 404, {'msg': 'This id is not exist'}
