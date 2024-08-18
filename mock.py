class MockSomeClass:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        return self.__dict__.get(name, None)


mock_instance = MockSomeClass(attr1='value1', attr2='value2')
mock_instance.attr3 = 'value3'
mock_obj = MockSomeClass()

def some_function_to_test(mock_object):
    return mock_object.greet()

setattr(mock_obj, 'greet', lambda: "Hello, Quera!")
result = some_function_to_test(mock_obj)
print(mock_instance.attr1)
print(mock_instance.attr2)
print(mock_instance.attr3)
print(result)
