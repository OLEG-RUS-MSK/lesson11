def test_function():
    def  inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_function() - NameError (вне функции test_function(), не существует)
test_function()