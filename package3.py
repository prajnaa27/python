import traceback

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        traceback.print_exc()  # Print the exception and stack trace
    return result

divide(10, 0)
