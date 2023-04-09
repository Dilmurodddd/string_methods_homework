def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:str tipidagi o'zgaruvchi berilgan. U faqat raqamlardan iborat ekanligini tekshiring.
        s: str
    Returns:
        bool: answer
    """
    
    return str(s).isdigit()
print(main('65466465'))