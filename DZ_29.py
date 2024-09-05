# Задание 1
# Создайте класс Обувь. Необходимо хранить следующую информацию:
# ■ тип обуви;
# ✓мужская,
# ✓женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Обувь и код для
# использования модели, контроллера и представления.
class Shoes:
    def __init__(self, shoe_type, style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.style = style
        self.color = color
        self.price = int(price)
        self.manufacturer = manufacturer
        self.size = int(size)

    def show_shoe(self):
        print(f'Тип обуви: {self.shoe_type}')
        print(f'Вид обуви: {self.style}')
        print(f'Цвет: {self.color}')
        print(f'Цена: {self.price}')
        print(f'Производитель: {self.manufacturer}')
        print(f'Размер: {self.size}')


# Задание 2
# Создайте класс Рецепт. Необходимо хранить следующую информацию:
# ■ название рецепта;
# ■ автор рецепта;
# ■ тип рецепта (первое, второе блюдо и т.д.);
# ■ текстовое описание рецепта;
# ■ ссылка на видео с рецептом;
# ■ список ингредиентов;
# ■ название кухни (итальянская, французская, украинская и т.д.).
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Рецепт и код для
# использования модели, контроллера и представления.
class Recipe:
    def __init__(self, name, author, recipe_type, description, link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.link = link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def show_recipe(self):
        print(f'Название рецепта: {self.name}')
        print(f'Автор рецепта: {self.author}')
        print(f'Тип рецепта: {self.recipe_type}')
        print(f'Текстовое описание рецепта: {self.description}')
        print(f'Ссылка на видео с рецептом: {self.link}')
        print(f'Список ингредиентов: {self.ingredients}')
        print(f'Название кухни: {self.cuisine}')


class Controller:
    def request(self, req):
        if req.lower() == 'обувь':
            s = Shoes('женская', 'кроссовки', 'черный', 1200, 'Спорт', 37)
            return s.show_shoe()
        elif req.lower() == 'рецепты':
            r = Recipe('Борщ украинский', 'FoodTV', 'Первое',
                       'https://www.russianfood.com/recipes/recipe.php?rid=126240',
                       'https://youtu.be/UeSp67Uif1k', 'Продукты', 'Украинская')
            return r.show_recipe()
        else:
            return 'Неверный запрос!'


class View:
    def __init__(self, service):
        self.service = service

    def run(self):
        print('Обувь или Рецепты? ')
        r = input()
        print(self.service.request(r))


if __name__ == '__main__':
    service = Controller()
    view = View(service)
    view.run()
