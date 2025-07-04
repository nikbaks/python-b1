import string

import string

text = input("ведіть текст: ")
sentences = [s for s in text.split('.') if s.strip()]
print("Кількість речень:", len(sentences))








reserved = {"if", "else", "while", "for", "return"}  
text = input("Вkдіть текст: ")

words = text.split()
result = [word.upper() if word.lower() in reserved else word for word in words]
print("Змінений текст:", ' '.join(result))





reserved = {"if", "else", "while", "for", "return"}  
text = input("ведіть текст: ")

words = text.split()
result = [word.upper() if word.lower() in reserved else word for word in words]
print("Змінений текст:", ' '.join(result))










text = input("Введіть рядок: ")
sym1 = input("Перший символ: ")
sym2 = input("Другий символ: ")

start = text.find(sym1)
end = text.find(sym2, start + 1)

if start != -1 and end != -1:
    new_text = text[:start] + text[end + 1:]
    print("Результат:", new_text)
else:
    print("Один або обидва символи не знайдено.")




      


      
