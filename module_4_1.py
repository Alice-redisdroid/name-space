def test_function():
    def inner_function():
        return "Я в области видимости функции test_function"
    print(inner_function())

test_function()
# print(inner_function()) - функция не сработает, так как существует только внутри
# пространства функции tedt_function