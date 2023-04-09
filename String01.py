def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:Bir nechta so'zlardan iborat str berilgan. Barcha harflar kichik. Har bir so'zning birinchi harfi bosh harf bilan yozilganligiga ishonch hosil qiling.
        s: str
    Returns:
        str: answer
    """
    
    return str(s).title()
print(main('abcd dcba'))