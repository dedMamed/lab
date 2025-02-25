def main():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    
    # Проверка, является ли возраст числом
    if age.isdigit():
        print(f"Привет, {name}! Вам {age} лет.")
    else:
        print("Пожалуйста, введите корректный возраст.")


if __name__ == "__main__":
    main()
