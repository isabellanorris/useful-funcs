from datetime import date, datetime
from uuid import UUID, uuid4


def generate_uuid():
    return uuid4()


def is_valid_uuid(uuid_to_test, version=4):
    if isinstance(uuid_to_test, UUID) and uuid_to_test.version == version:
        return True
    try:
        UUID(uuid_to_test, version=version)
        return True
    except ValueError:
        return False


def stringify_uuid_keys(d):
    if isinstance(d, dict):
        o = {}
        for k, v in d.items():
            if isinstance(k, UUID):
                o[str(k)] = stringify_uuid_keys(v)
            else:
                o[k] = stringify_uuid_keys(v)
        return o
    else:
        return d


def jsonify_data(data, format_date=False):
    for key, value in data.dict().items():
        if type(value) == dict:
            for key2, value2 in value.items():
                if type(value2) not in [list, float, int, bool] and value2 is not None:
                    value[key2] = str(value2)
            setattr(data, key, value)
        elif type(value) in [list, float, int, bool]:
            setattr(data, key, value)
        elif value is None:
            data.dict().pop(key)
        elif format_date:
            if type(value) == date:
                setattr(data, key, value.strftime("%d/%m/%Y"))
            elif type(value) == datetime:
                setattr(data, key, value.strftime("%d-%m-%Y, %H:%M"))
        else:
            try:
                setattr(data, key, value.value)  # this is a catch for enums
            except AttributeError:
                setattr(data, key, str(value))

    return data.dict()


def snake_case_to_display(text):
    if text:
        return " ".join([split_words.capitalize() for split_words in text.split("_")])


def name_list(people):
    if len(people) == 0:
        return "No people"
    elif len(people) == 1:
        return people[0]
    else:
        names = [person for person in people]
        return (",").join(names[:-1]) + " and " + names[-1]


def full_name_as_string(title, first_name, last_name):
    if None not in [title, first_name, last_name]:
        return " ".join([title, first_name, last_name])


def decrease_colour_opacity(colour):
    return colour.replace("1)", "0.2)")
