from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Nissan Motor Co."},
        {"name": "Mercedes", "description": "Mercedes-Benz Group"},
        {"name": "Audi", "description": "Audi AG"},
        {"name": "Kia", "description": "Kia Corporation"},
        {"name": "Toyota", "description": "Toyota Motor Corporation"},
    ]
    car_make_instances = []
    for make in car_make_data:
        car_make_instances.append(
            CarMake.objects.get_or_create(
                name=make["name"],
                defaults={"description": make["description"]}
            )[0]
        )
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SEDAN", "year": 2023,
         "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SEDAN", "year": 2023,
         "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SEDAN", "year": 2023,
         "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[2]},
        {"name": "Sorento", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "SEDAN", "year": 2023,
         "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023,
         "car_make": car_make_instances[4]},
    ]
    for model in car_model_data:
        CarModel.objects.get_or_create(
            name=model["name"],
            defaults={
                "type": model["type"],
                "year": model["year"],
                "car_make": model["car_make"],
            }
        )
