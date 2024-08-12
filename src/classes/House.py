class House():
    def __init__(self):
        # TODO: Initialize the house object, this should have the following properties: id, neighborhood, house_style, overall_condition, year_built, roof_type,
        # roof_material, foundation_material, heating, central_air, electrical, fireplace_num, garage_area, date_sold 
        pass

    def update_house(self, updated_data):
        # TODO: Update the house by id
        # Example: id = 1 and updated_data = { "neighborhood": "Gilbert"}
        # This should update the neighborhood of the house with id 1 to Gilbert
        pass

    def delete_house(self):
        # TODO: Delete the house by id
        pass

    @classmethod
    def get_houses_by_filters(self, house_data, filters):
        # TODO: Get the house by filters
        # Example: filters = { "id": 1, "neighborhood": "Gilbert" }
        # This should return the house with id 1 in the neighborhood Gilbert
        pass