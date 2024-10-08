import json

def persist_to_file(file_name):

    def decorator(original_func):

        try:
            cache = json.load(open(file_name, 'r'))
        except (IOError, ValueError):
            cache = {}

        def new_func(*param):
            if (tuple(param)) not in cache:
                cache[(tuple(param))] = original_func(*param)
                json.dump(cache, open(file_name, 'w'))
            return cache[(tuple(param))]

        return new_func

    return decorator