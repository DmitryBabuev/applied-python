# -*- encoding: utf-8 -*-


def process(data, events, car):
    try:
        for ev in events:
            drift_ev = ev
            if drift_ev["type"] == "switch":
                car_index = drift_ev.get("cars") - 1
                train_from = drift_ev.get("train_from")
                train_to = drift_ev.get("train_to")
                condition = False
                while condition != True:
                    for drift_train in data:
                        if drift_train["name"] == train_from:
                            drift_cars = drift_train["cars"]
                            buffer_car = drift_cars[car_index]
                            del drift_cars[car_index]
                    for drift_train in data:
                        if drift_train["name"] == train_to:
                            drift_cars = drift_train["cars"]
                            drift_cars.append(buffer_car)
                            condition = True
            elif drift_ev["type"] == "walk":
                passenger = drift_ev.get("passenger")
                distance = drift_ev.get("distance")
                for drift_train in data:
                    drift_car = drift_train["cars"]
                    for ix, drift_car_param in enumerate(drift_car):
                        drift_person = drift_car_param["people"]
                        for ixx, name in enumerate(drift_person):
                            if name == passenger:
                                buffer_person = name
                                person_car = ix
                                del drift_person[ixx]
                    for ix1, drift_car_param1 in enumerate(drift_car):
                        if ix1 == (person_car + distance):
                            drift_person = drift_car_param1["people"]
                            drift_person.append(buffer_person)
        for drift_trainresult in data:
            drift_carresult = drift_trainresult["cars"]
            for drift_car_paramresult in drift_carresult:
                if drift_car_paramresult["name"] == car:
                    blalala = drift_car_paramresult["people"]
                    return len(blalala)
    except Exception:
        return -1
