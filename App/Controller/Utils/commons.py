from functools import wraps

from flask import session, redirect, url_for


class Carousel:
    def __init__(self, items, max_rows=10, items_per_row=3):
        self.items = items
        self.max_rows = max_rows
        self.items_per_row = items_per_row

    def rows(self):
        rows = [self.items[i:i + self.items_per_row] for i in range(0, len(self.items), self.items_per_row)]
        return rows[0:self.max_rows]


class DataIndex:
    def __init__(self, items, bucket_key_attribute='title'):
        self.bucket_key_attribute = bucket_key_attribute
        self.buckets = {}
        for item in items:
            key_attribute = item[bucket_key_attribute]
            key = str(key_attribute)[0]
            if key not in self.buckets.keys():
                self.buckets[key] = []
            self.buckets[key].append(item)

    def indices(self):
        return sorted(self.buckets.keys())

    def entries(self, key):
        if key not in self.buckets.keys():
            return []
        else:
            result = self.buckets[key]
            result.sort(key=lambda entry: entry[self.bucket_key_attribute])
            return result


def authenticated(fail_route='index'):
    def decorator(route):
        @wraps(route)
        def wrapper(*args, **kwargs):
            if is_authenticated():
                return route(*args, **kwargs)
            return redirect(url_for(fail_route))

        return wrapper

    return decorator


def is_authenticated():
    return 'username' in session
