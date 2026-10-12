from typing import Optional

def find_vehicle_by_plate(plate_num : str , vehicles : list[dict]) -> Optional[dict]:
    for car in vehicles:
        if car.get("plate") == plate_num:
            return car
    return None    

kilo_fleet = [
    {"plate": "R123", "brand": "Hyundai", "type": "SUV"},
    {"plate": "M332", "brand": "BMW", "type": "sedan"}
]                          

result = find_vehicle_by_plate("R123", kilo_fleet)
print(result)