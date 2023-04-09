def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:str tipidagi o'zgaruvchi berilgan. U faqat harflardan iborat ekanligini tekshiring.
        s: str
    Returns:
        bool: answer
    """
    
    return str(s).isalpha()
print(main('kjjhbhjbHBHBJHBH'))