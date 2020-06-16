def change_keys(dictionary: dict, **kwargs: dict) -> dict:
    for (old_key, new_key) in kwargs.items():
        if old_key in dictionary:
            dictionary[new_key] = dictionary[old_key]
            del dictionary[old_key]

    return dictionary
