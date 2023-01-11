from ninja import Schema


class FruitSchema(Schema):
    id: int
    name: str
    description: str
