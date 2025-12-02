def calculate(expression):
    """
    Calculates the result of a mathematical expression.

    NOTE: This function uses eval() which is not safe for production use
    as it can execute arbitrary code. This is a simplified implementation
    for demonstration purposes.
    """
    try:
        # Sanitize the expression to only allow numbers and basic operators
        allowed_chars = "0123456789+-*/. ()"
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Invalid characters in expression")
            
        result = eval(expression)
        return result
    except (SyntaxError, ZeroDivisionError):
        raise ValueError("Invalid mathematical expression")
