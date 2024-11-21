class Palindrom:
    def find_palindrome(self, arg: str) -> bool:
        chistka = ''.join(arg.split()).lower()
        
        if not chistka:
            return False
            
        return chistka == chistka[::-1]