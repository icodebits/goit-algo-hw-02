from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо рядок в нижній регістр
    s = ''.join(s.split()).lower()
    
    # Створюємо двосторонню чергу (deque) та додаємо всі символи рядка до неї
    char_queue = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False  # Якщо хоча б одна пара символів не рівна, рядок не є паліндромом
    
    return True  # Якщо всі пари символів рівні, рядок є паліндромом

input_str = "A man a plan a canal Panama"
result = is_palindrome(input_str)
print(f'Is "{input_str}" a palindrome? {result}')
