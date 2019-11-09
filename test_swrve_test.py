      
def assert_equal(first, second):
    message = "Expected {0} and {1} to be the same"
    message = message.format(first, second)
    assert first == second, message        
        
